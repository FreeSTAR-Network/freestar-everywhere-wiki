# Everywhere phonebook integration

Optional integration with [freestar-everywhere-phonebook](https://github.com/FreeSTAR-Network/freestar-everywhere-phonebook) on the same PBX host.

## Purpose

Show **who is using the DMR portal** in the Everywhere phonebook UI. Feature code **234 is not a directory contact** — status appears as:

- **DMR Portal** navigation tab (live sessions, capacity, host stats)
- **Stats** page DMR cards and Live Activity
- **User BLF tooltips:** `In DMR IVR` or `On DMR Portal (TG …)`

## Enable

In `/var/www/html/apps/phonebook/config.php`:

```php
define('DMR_PORTAL_ENABLED', true);
define('DMR_PORTAL_BRIDGES_URL', 'https://your-portal.example.com/bridges');
define('DMR_PORTAL_STATS_URL', 'https://your-portal.example.com/stats');
define('DMR_PORTAL_MAX_ACTIVE_CALLS', 2);   // match exchange MAX_ACTIVE_CALLS
define('DMR_PORTAL_HTTP_TIMEOUT', 2.0);
```

Copy from `config.php.example` in the phonebook repo.

## AMI permissions

The phonebook AMI user needs **Read → `call`** for `CoreShowChannels` (maps PBX extensions to IVR/bridge state).

## Status pipeline

`ami_status_batch.php` (~10 s poll):

1. **AMI** `CoreShowChannels` — detect IVR (`dmr-portal` / `sip-dmr-ivr` contexts) and trunk legs (`sip-dmr-exchange`)
2. **HTTPS** `GET /bridges` and `/stats` from PBX host
3. **Join** by talkgroup → `extension_in_dmr`, `dmr_bridges`, `dmr_capacity`

## Access control interaction

Only allowlisted users (Misc Applications) reach the IVR. Denied dial attempts create **no channel** — phonebook shows no DMR activity for them.

## Do not

- Add extension **234** to the `users` table or `STATIC_EXTENSIONS`
- Log `SIP_AUTH_TOKEN` or exchange secrets in phonebook logs

## Test checklist

| Step | Expected |
|------|----------|
| Allowed user dials feature code | DMR tab IVR row + BLF tooltip |
| User enters talkgroup | Bridge row + `/bridges` session |
| Hang up | Clears from tab and BLF |
| Denied user dials feature code | Fast reject, no DMR rows |
| `curl` bridges URL from PBX | JSON response, `dmr_reachable` true |

## Related

- [FreePBX integration](freepbx.md)
- Phonebook repo: `docs/ARCHITECTURE.md`, `docs/DETAILED_SETUP.md`
