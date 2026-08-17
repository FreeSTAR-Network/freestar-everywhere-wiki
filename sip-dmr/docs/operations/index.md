# Operations

Day-2 operations for running a SIP-DMR portal.

| Guide | Description |
|-------|-------------|
| [Scaling](scaling.md) | Grow from 2 to 10+ concurrent calls |
| [Troubleshooting](troubleshooting.md) | Common failures and fixes |

## Monitoring

Poll regularly from your monitoring host:

```bash
curl -sS https://your-portal.example.com/stats
curl -sS https://your-portal.example.com/bridges
```

Alert on:

- Memory > 85%
- `calls` stuck > 0 after expected hangups
- Bridge count in `docker ps` exceeds `/bridges` length (orphans)

## Capacity

Tune `MAX_ACTIVE_CALLS` in exchange `.env` to match VM size. PBX should play a **portal-busy** prompt when exchange returns 503.

Match `DMR_PORTAL_MAX_ACTIVE_CALLS` in phonebook `config.php` if using Everywhere phonebook.

## Deploy hygiene

- Prefer thin rebuilds for routine exchange/bridge updates
- After exchange `docker compose up --force-recreate`, check for orphan bridge containers
- Periodically `docker system prune` on small disks

## FreeSTAR production

FreeSTAR Everywhere runs this stack in production with operator-managed allowlists and dedicated hosts. Internal runbooks (exact hostnames, extension lists) are maintained by the core team and are not published in this wiki.
