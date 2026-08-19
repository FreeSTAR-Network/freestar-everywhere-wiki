# PBX Admin Guide: Connecting to a Remote RF-Link Node (IAX Extension, FreePBX 17)

This guide explains how to create an IAX2 extension in FreePBX 17 so your PBX can connect to a remote RF-Link node (where the node acts as the Asterisk server).

---

## 1. Gather Required Information from RF-Link Applicant

Ensure you have the following details from the RF-Link node owner:

- **Callsign:** The callsign of the individual or club applying for the RF-link.
- **Extension Name:** The RF-Link display name (phonebook)
- **Licence Document:** Copy of the license document for callsign or club.
- **IAX Dial String:** The complete connection dial string in the format `IAX2/USERNAME:PASSWORD@NODE-HOSTNAME:PORT/NODE`. Direct the applicant to [IAX2 String Generator](https://freestareverywhere.com/apps/iax2string-generator/). Dial string must be obtained from RF-Link applicant to complete the setup of the extension.

Once extension is set up, supply RF-Link owner with extension number (8000-8999)

---

## 2. Understand the Dial String Format

The RF-Link owner will provide a dial string in the following format:

```text
IAX2/USERNAME:PASSWORD@NODE-HOSTNAME:PORT/NODE
```

**Example:**

```text
IAX2/freestar:passw0rd@40071.nodes.allstarlink.org:4569/40071
```

**Components:**

- `freestar` = Username (normally callsign of node owner or club call)
- `passw0rd` = Password/secret
- `40071.nodes.allstarlink.org` = Node's public DNS or IP address
- `4569` = IAX port (default is 4569)
- `/40071` = Desired AllStar Node number

---

## 3. Create and Configure the IAX2 Extension

1. Go to **Applications > Extensions**
2. Click **Add Extension** > **Add IAX2 Extension**

### General Tab Configuration

- **User Extension:** Enter a unique extension number (e.g., `8001`)
- **Display Name:** Enter a descriptive name (e.g., `RF-Link Node`)
- **Secret:** Enter the password provided by the RF-Link owner
- **Outbound CallerID:** Leave blank or set as desired

### Advanced Tab Configuration

1. Click on the **Advanced** tab
2. Configure the following settings:

    - **Transfer:** `no`
    - **Host:** Enter the node's hostname (e.g., `40071.nodes.allstarlink.org`) or IP address
    - **Port:** Enter the IAX port (e.g., `4569`, or custom port specified by the RF-Link owner)
    - **Qualify:** `yes`
    - **Disallow:** `all`
    - **Allow:** `ulaw`
    - **Dial:** `IAX2/USERNAME:PASSWORD@NODE-HOSTNAME:PORT/NODE`

3. Click **Submit** and then **Apply Config**

### Firewall Considerations

If your PBX is behind NAT/firewall, ensure outbound UDP traffic to the node's IP and IAX port is permitted.

---

## 4. Test the Connection

1. Use the Asterisk CLI to verify the connection:

   ```bash
   asterisk -rx "iax2 show peers"
   ```

   - Look for your new RF-Link extension in the list
   - Status should show "OK" if the node is reachable (BLF will be green)
   - If the node is "UNKNOWN" or "OFFLINE", the BLF will be grey

2. Test calling the extension:
   - Dial the extension from a SIP phone or another extension
   - The call should route to the RF-Link node and trigger its dialplan

---

## 5. Troubleshooting

- **Connection Issues:**
  - Double-check username, password, port, hostname, and extension match the node configuration
  - Ensure your PBX can reach the RF-Link node's public IP/DNS (check firewall/NAT rules)
  
- **Authentication Errors:**
  - If you see "no authority" or "authentication failed," verify credentials are correctly entered
  
- **Debugging:**
  - Use Asterisk logs for detailed information:

    ```bash
    asterisk -rvv
    ```

---

## 6. Support

For further help, contact: M0VUB
