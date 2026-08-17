# Integration

Connect the SIP-DMR portal to your existing systems.

| Guide | Description |
|-------|-------------|
| [FreePBX / Asterisk](freepbx.md) | Trunk, IVR dialplan, access control, Custom Destination |
| [Everywhere phonebook](phonebook.md) | Optional live status tab on FreeSTAR Everywhere |

## Generic pattern

1. **Feature code** → IVR collects talkgroup
2. **Dial** `PJSIP/${TG}@your-trunk-name` with pre-dial headers
3. **Trunk** points at exchange public IP:5060
4. **Access control** — restrict who may dial the feature code (see FreePBX Misc Applications)

Other PBX platforms follow the same SIP and dialplan pattern; FreePBX is the reference implementation used by FreeSTAR.
