# Exchange deployment

Deploy **sip-dmr-exchange** on your portal host.

## Clone and configure

```bash
git clone https://github.com/FreeSTAR-Network/sip-dmr-exchange.git
cd sip-dmr-exchange
cp .env.example .env
```

Edit `.env` — minimum fields:

| Variable | Example | Notes |
|----------|---------|-------|
| `HOST_IP` | `203.0.113.10` | Public IP peers send SIP to |
| `SIP_AUTH_TOKEN` | *(random secret)* | Required for production |
| `DMR_ADDRESS` | `dmr.example.com` | Your MMDVM/SystemX host |
| `DMR_PORT` | `62031` | MMDVM port |
| `DMR_PASSWORD` | *(from server admin)* | |
| `MAX_ACTIVE_CALLS` | `2` | Cap concurrent bridges |

See [Configuration](configuration.md) for all variables.

## Build and run

```bash
docker compose up -d --build
```

Uses **host networking** — exchange binds directly to host UDP 5060.

!!! tip "Routine deploys"
    Full rebuild compiles PJSIP and can take a long time on small VMs. For code-only changes, use thin rebuild patterns documented in your team's ops notes (wheel-only layer updates).

## Verify

```bash
docker compose ps
curl -sS http://127.0.0.1:8080/stats
curl -sS http://127.0.0.1:8080/bridges
```

## Optional: HTTPS dashboard

Clone [sip-dmr-exchange-dashboard](https://github.com/FreeSTAR-Network/sip-dmr-exchange-dashboard) and serve via nginx:

- `/dashboard/` — static UI
- `/bridges`, `/stats` — reverse proxy to `127.0.0.1:8080`

## Orphan bridge containers

If the exchange container is recreated while calls were active, old `sip-dmr-bridge` containers may linger. Compare `docker ps` with `/bridges` and remove orphans manually until startup reconciliation is implemented in exchange.

## Related

- [Bridge image](bridge.md)
- [Troubleshooting](../operations/troubleshooting.md)
