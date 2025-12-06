# FreePBX 17 Warm Spare Setup (CLI Method)

## Overview

This guide describes how to set up a **warm spare** for FreePBX 17 using command-line tools and scripts. The spare server will mirror your primary FreePBX system through scheduled backups, manual or automated file and database transfer, and basic networking techniques. This setup minimizes downtime and preserves call flow in the event of primary server failure.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Architecture](#architecture)
3. [Step 1: Prepare Both Servers](#step-1-prepare-both-servers)
4. [Step 2: Set Up Passwordless SSH](#step-2-set-up-passwordless-ssh)
5. [Step 3: Create Scheduled Backups](#step-3-create-scheduled-backups)
6. [Step 4: Transfer Backups to Warm Spare](#step-4-transfer-backups-to-warm-spare)
7. [Step 5: Restore Backups on the Spare](#step-5-restore-backups-on-the-spare)
8. [Step 6: Prevent Split-Brain](#step-6-prevent-split-brain)
9. [Step 7: Failover Procedure](#step-7-failover-procedure)
10. [Automation Example (Bash Scripts)](#automation-example-bash-scripts)
11. [Best Practices and Notes](#best-practices-and-notes)
12. [References](#references)

---

## Requirements

- Two servers running FreePBX 17 with the same Asterisk and OS versions.
- Root/admin shell access to both servers.
- Both servers networked together (LAN, VPN, or public but firewalled).
- Sufficient disk space on both.
- Outbound SSH from primary to spare server.

---

## Architecture

1. **Primary PBX:** Active, in-use server.
2. **Warm Spare PBX:** Standby, kept in sync via backups; outbound services (Asterisk) stopped.
3. **Synchronization:** Performed via scheduled scripts using `fwconsole backup`, `rsync`, and `mysqldump`.

---

## Step 1: Prepare Both Servers

```bash
# On both systems:
hostnamectl set-hostname freepbx-primary     # or freepbx-spare
timedatectl set-timezone <Your/Timezone>
yum update -y  # or dnf/apt as appropriate
```

Set static IPs, ensure matching versions of FreePBX, Asterisk, and modules.

---

## Step 2: Set Up Passwordless SSH

On the **primary PBX**:

```bash
ssh-keygen -t rsa  # Accept the defaults
ssh-copy-id root@spare-pbx-ip
```
- Test:
```bash
ssh root@spare-pbx-ip
```
You should login without a password.

---

## Step 3: Create Scheduled Backups

Use FreePBX's CLI backup tools or manually backup configs and MySQL.

### A. Using fwconsole backup (Recommended)
```bash
# List Backup jobs (if any)
fwconsole backup --list

# Create a manual backup profile or use
# GUI to create one, then schedule with cron

# Create a backup from CLI:
fwconsole backup --backup='FullBackup'
```

### B. Manual Backup Method

#### Backup config files:
```bash
tar czf /tmp/freepbx-config-$(date +%F).tar.gz \
  /etc/asterisk \
  /var/spool/asterisk \
  /var/lib/asterisk \
  /var/www/html \
  /var/lib/mysql/asterisk
```

#### Database only:
```bash
mysqldump -u root -p'YOURMYSQLPASS' asterisk > /tmp/asterisk-db-$(date +%F).sql
```

---

## Step 4: Transfer Backups to Warm Spare

Transfer backups to the spare using `scp` or `rsync`.

```bash
# If using fwconsole backup file, look in /var/spool/asterisk/backup/...

scp /path/to/backupfile root@spare-pbx-ip:/tmp/

# Or using rsync for directories
rsync -avz -e ssh /etc/asterisk/ root@spare-pbx-ip:/etc/asterisk/
rsync -avz -e ssh /var/www/html/ root@spare-pbx-ip:/var/www/html/
# Add other needed directories
```

You may automate this in a shell script and schedule it with `cron`.

---

## Step 5: Restore Backups on the Spare

### A. Using fwconsole restore

On the **spare PBX**:
```bash
fwconsole stop          # Ensure not running
fwconsole restore /tmp/your-backup-file.tar.gz
```

### B. Manual Restore

**CAUTION:** Overwrite only if you are certain.
```bash
tar xzf /tmp/freepbx-config-YYYY-MM-DD.tar.gz -C /
mysql -u root -p'YOURMYSQLPASS' asterisk < /tmp/asterisk-db-YYYY-MM-DD.sql
```

---

## Step 6: Prevent Split-Brain

Ensure you do **NOT** run both PBX servers Asterisk/FreePBX services live at the same time.

On the **spare**:
```bash
fwconsole stop
systemctl disable asterisk
```

Only start these during a failover.

---

## Step 7: Failover Procedure

1. **Stop Services on the Primary.**
2. **Update DNS/IP:** Point phones/trunks to the spare PBX's IP or assign the failed PBX's IP to the spare.
3. **On the spare**, start services:
    ```bash
    fwconsole start
    ```
4. **Verify:** Phones and trunks register, calls flow normally.
5. **Communicate:** Inform users about the failover.

Reverse after the primary is restored and updated with the latest data from the spare, if necessary.

---

## Automation Example (Bash Scripts)

### **Primary PBX: Nightly Backup & Sync Script**
```bash
#!/bin/bash

# 1. Create backup file
fwconsole backup --backup='FullBackup'

# 2. Find latest backup
BACKUP_FILE=$(ls -t /var/spool/asterisk/backup/FullBackup/*.tgz | head -1)

# 3. Transfer backup
scp "$BACKUP_FILE" root@spare-pbx-ip:/tmp/

# Optional: Notify on error or success
```

### **Spare PBX: Restore Script (Triggered via SSH, in cron, or manually)**
```bash
#!/bin/bash

fwconsole stop
LATEST_BACKUP=$(ls -t /tmp/FullBackup*.tgz | head -1)
[ -f "$LATEST_BACKUP" ] && fwconsole restore "$LATEST_BACKUP"
```

---

## Best Practices and Notes

- **Test regularly!** Perform restores and failovers during maintenance windows.
- **Keep the spare system up-to-date** with OS and FreePBX updates.
- **Disk space monitoring** is crucial.
- **TLS/SRTP:** Add `/etc/asterisk/keys/` to your sync if you use encrypted signaling/audio.
- **Don’t schedule overlapping sync and restore jobs.**
- Backups may briefly lock database tables; schedule accordingly.

---

## References

- [FreePBX Warm Spare: Official Documentation](https://wiki.freepbx.org/display/FOP/How+to+Setup+FreePBX+Warm+Spare)
- [fwconsole backup/restore CLI Docs](https://wiki.freepbx.org/display/FPG/Backup+Module#BackupModule-CommandLine)
- [Secure Shell (SSH) Keys Guide](https://wiki.archlinux.org/title/SSH_keys)
- [Community Thread on Warm Spares](https://community.freepbx.org/search?q=warm%20spare)

---

**Created by:**  
Shane DALEY **M0VUB**  
Date: 06-12-2025 
