# FreePBX 17 Warm Spare Setup (GUI Method)

## Overview

This guide will walk you through setting up a **warm spare** for FreePBX 17 using the **Backup & Restore module** in the FreePBX GUI. The warm spare will mirror your primary FreePBX system so you can quickly switch in case of a failure, minimizing downtime.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Architecture Overview](#architecture-overview)
3. [Step 1: Prepare Both Servers](#step-1-prepare-both-servers)
4. [Step 2: Configure Passwordless SSH for Transfers](#step-2-configure-passwordless-ssh-for-transfers)
5. [Step 3: Configure Backups on the Primary PBX (GUI)](#step-3-configure-backups-on-the-primary-pbx-gui)
6. [Step 4: Monitor and Test Restores on the Spare PBX](#step-4-monitor-and-test-restores-on-the-spare-pbx)
7. [Step 5: Failover Procedures](#step-5-failover-procedures)
8. [Notes and Best Practices](#notes-and-best-practices)
9. [References](#references)

---

## Requirements

- Two servers with FreePBX 17 installed and network access to each other:
  - **Primary PBX:** The in-use/active server.
  - **Spare PBX:** The backup server, typically idle.

- Both should have:
  - Matching **FreePBX/Asterisk/OS versions**
  - Similar or identical configuration (network, trunk, etc)
  - Static IP addresses or reserved DHCP

- **Admin/root access** (SSH and GUI)
- Sufficient **disk space** for full configuration and voicemails

---

## Architecture Overview

![Warm Spare Diagram](https://wiki.freepbx.org/download/attachments/21891595/warm-spare-overview.png)

- The **Primary** PBX runs production workloads.
- Regularly, the **Backup & Restore module** exports configuration from the Primary and pushes it via SSH to the Spare.
- The **Spare** PBX remains in standby, powered on but with PBX services stopped. In case of primary failure, services on the Spare are started and it assumes the production role.

---

## Step 1: Prepare Both Servers

1. **Install FreePBX 17**  
   Make sure both servers run an identical version.

2. **Configure Basic Settings**
   - Set up the same timezone and locale.
   - Assign static IPs.
   - (Optional) Synchronize hostnames or note which is Primary/Spare.

3. **Register modules and apply latest security updates** via the GUI or SSH.

---

## Step 2: Configure Passwordless SSH for Transfers

1. **On the Primary PBX (as `root` or admin user):**

   ```bash
   ssh-keygen -t rsa
   ```

   Press ENTER to accept defaults if prompted.

2. **Copy the public key to the Spare PBX:**

   ```bash
   ssh-copy-id root@spare-pbx-ip
   ```

   Replace `spare-pbx-ip` with the actual IP of the Spare PBX.

3. **Test the connection:**

   ```bash
   ssh root@spare-pbx-ip
   ```

   - You should log in without entering a password.

4. **Copy your FreePBX admin SSH user key as well if you do not use root.**

---

## Step 3: Configure Backups on the Primary PBX (GUI)

1. **Log into the FreePBX GUI on the Primary PBX.**

2. Navigate to:  
   **Admin → Backup & Restore**

3. **Create a New Backup Job:**
   - Click **Add Backup**.
   - Name your backup (e.g., `Warm Spare Sync`).

4. **Select Items to Include:**
   - **Configuration Files:** All modules, system recordings, voicemails, fax, etc.
   - Optionally, include voicemail, CDRs, system audio, and custom files if desired.

5. **Schedule the Backup:**
   - Schedule (cron) the backup (e.g., daily at 02:00).
   - Example: `0 2 * * *`

6. **Set Up Warm Spare Restore:**
   - Locate the **Remote Server** or **Warm Spare** option (bottom of the backup config).
   - **Enable "Restore to Remote Server"**.
   - Enter the following:
     - **Server:** IP address of the Spare PBX
     - **SSH User:** `root` (or equivalent user)
     - **SSH Port:** `22` (unless changed)
     - **Restore Path:** `/`
     - **Remote Restore:** Enable **Automatically Restore Backup**
     - (Optional) Enable reboot after restore if needed.

7. **Save** the new backup job.

8. **Test the backup job** immediately by running it once from the GUI, and verify there are no errors.

---

## Step 4: Monitor and Test Restores on the Spare PBX

1. **On the Spare PBX:**
   - The backup/restore module will receive the backup and auto-restore it.
   - You can check **Admin → Backup & Restore → Restore** for restore logs.

2. Optionally, check logs via SSH:

   ```bash
   tail -f /var/log/asterisk/backup.log
   ```

3. **Confirm:**
   - Configuration and settings on the Spare PBX reflect the latest backup.
   - Voicemail and system recordings, if included, are present.

4. **Prevent Accidental Conflict:**
   - Keep Asterisk/FreePBX services stopped on the Spare to avoid registration or trunk conflicts:

     ```bash
     fwconsole stop
     systemctl disable asterisk
     ```

   - Only start these during failover.

---

## Step 5: Failover Procedures

1. **When Primary PBX Fails:**
   - Assign the Primary's IP/DNS to the Spare PBX, if required (or use DNS to re-point phones/trunks).
   - Start Asterisk/FreePBX services on the Spare:

     ```bash
     fwconsole start
     ```

   - Verify endpoints and SIP trunks register.
   - Conduct test calls to ensure PBX services are working.

2. **Communicate with your users** about the switch-over.

3. **Once the primary is restored,** reverse the process and update the restored primary with the latest data from the spare if needed.

---

## Notes and Best Practices

- **Test regularly:** Run failover drills and test restores at least quarterly.
- Do **not** run both PBXs live on the same network (causes endpoint and trunk registration problems).
- Regularly **check disk space** on both servers.
- Update backup selection if you modify system modules or add features.
- If you use TLS/SRTP, add key/certificate directories to your backup sources.

---

## References

- [Official FreePBX Warm Spare Wiki](https://wiki.freepbx.org/display/FOP/How+to+Setup+FreePBX+Warm+Spare)
- [FreePBX Backup & Restore Module](https://wiki.freepbx.org/display/FPG/Backup+Module)
- [FreePBX Forum on Warm Spares](https://community.freepbx.org/search?q=warm%20spare)

---

**Created by:**  
Shane Daley M0VUB  
Date: 06-12-2025
