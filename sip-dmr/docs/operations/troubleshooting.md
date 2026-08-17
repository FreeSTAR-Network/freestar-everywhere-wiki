# Troubleshooting

## Exchange / SIP

| Symptom | Checks |
|---------|--------|
| **403 Forbidden** on INVITE | `X-Auth-Token` mismatch; compare PBX dialplan vs exchange `SIP_AUTH_TOKEN` |
| **503** after talkgroup entered | `MAX_ACTIVE_CALLS` reached; scale VM or raise cap |
| No audio | B2BUA path; verify bridge healthy (`docker ps`, bridge logs) |
| Long ring before answer | Bridge cold start 5–15 s; normal until healthy |
| INVITE never arrives | Firewall UDP 5060; trunk host/IP; `tcpdump -n udp port 5060` |

```bash
# On portal host
docker compose logs -f
curl -sS http://127.0.0.1:8080/bridges
asterisk -rx "pjsip show endpoints"   # if testing from PBX side
```

## Bridge containers

| Symptom | Checks |
|---------|--------|
| Container exits immediately | `docker logs <container>`; MMDVM auth, port bind |
| Orphan containers after deploy | `docker ps -a` vs `/bridges`; manual cleanup |
| MMDVM packet loss | DMR server load; too many concurrent logins from one IP |

## FreePBX GUI

| Symptom | Fix |
|---------|-----|
| **Bad Dest: dmr-portal,234,1** | Add **Custom Destination** → `dmr-portal,234,1` (Admin → Custom Destinations) |
| User cannot dial feature code | Missing Misc Application for `234/_EXTNUM` |
| Everyone can dial feature code | Remove global `exten => 234` from `from-internal-custom` |

## Phonebook

| Symptom | Checks |
|---------|--------|
| DMR tab unreachable | HTTPS from PBX to portal `/bridges`; URL in `config.php` |
| IVR row missing | AMI Read `call` permission; IVR context detection |
| Bridge row missing | `/bridges` empty; talkgroup join logic |
| Wrong capacity display | `DMR_PORTAL_MAX_ACTIVE_CALLS` vs exchange `.env` |

```bash
# From PBX host
curl -sS https://your-portal.example.com/bridges
asterisk -rx "core show channels concise" | grep -E "234|sip-dmr|dmr-portal"
```

## Build issues

| Symptom | Checks |
|---------|--------|
| PJSIP compile hours on small VM | Use thin rebuild; build on larger CI runner |
| Bridge build fails | Docker disk space; sip-usrp-bridge access |

## Getting help

- FreeSTAR operators: contact via [freestar.network](https://freestar.network)
- Code issues: GitHub issues on the relevant repo (when you have access)
