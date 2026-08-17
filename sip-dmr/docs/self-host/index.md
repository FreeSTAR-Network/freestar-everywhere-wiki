# Self-Hosting

Run your own SIP-DMR portal on a Linux server with Docker.

## Overview

| Piece | Repo | Deployed as |
|-------|------|-------------|
| Exchange | sip-dmr-exchange | Docker Compose, host network |
| Bridge image | sip-dmr-bridge | Built locally, referenced by exchange |
| Dashboard (optional) | sip-dmr-exchange-dashboard | Static files behind nginx |

## Suggested layout on server

```
/opt/sip-dmr/
  sip-dmr-exchange/     # clone, .env, docker-compose.yaml
  sip-dmr-bridge/       # clone, docker build
  sip-dmr-exchange-dashboard/   # optional
```

## Minimum VM sizing

| Concurrent calls | RAM | CPU |
|------------------|-----|-----|
| 1–2 | 1–2 GB | 2 vCPU |
| 10 | 8 GB | 4 vCPU |
| 15+ | 12–16 GB | 4+ vCPU |

See [Scaling](../operations/scaling.md) for growth planning.

## Pages in this section

- [Prerequisites](prerequisites.md)
- [Exchange](exchange.md)
- [Bridge image](bridge.md)
- [Configuration](configuration.md)
