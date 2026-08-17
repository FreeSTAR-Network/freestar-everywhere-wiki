# Configuration reference

Environment variables for **sip-dmr-exchange** (from `.env.example`).

## Host / HTTP

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST_IP` | — | Public IP for SIP Contact/Via headers |
| `HTTP_PORT` | `8080` | HTTP API port |
| `LOG_LEVEL` | `INFO` | Logging verbosity |

## DMR server

| Variable | Default | Description |
|----------|---------|-------------|
| `DMR_ADDRESS` | — | MMDVM/SystemX hostname |
| `DMR_PORT` | `62031` | MMDVM port |
| `DMR_PASSWORD` | — | MMDVM password |

## DMR local ports

Each bridge binds a unique UDP port in this range:

| Variable | Default |
|----------|---------|
| `DMR_LOCAL_PORT_START` | `62040` |
| `DMR_LOCAL_PORT_END` | `64040` |

## SIP

| Variable | Default | Description |
|----------|---------|-------------|
| `SIP_BIND_ADDR` | `0.0.0.0` | Listen address |
| `SIP_BIND_PORT` | `5060` | Listen port |
| `SIP_AUTH_TOKEN` | — | If set, require `X-Auth-Token` header on INVITE |

## Bridge defaults

Used when PBX does not supply headers:

| Variable | Default | Description |
|----------|---------|-------------|
| `BRIDGE_DEFAULT_CALLSIGN` | `N0CALL` | Fallback callsign |
| `BRIDGE_DEFAULT_DMR_ID` | `-1` | Fallback ID (RadioId lookup may override) |
| `BRIDGE_DEFAULT_SSID` | `73` | Fallback SSID suffix |
| `BRIDGE_IMAGE_NAME` | `sip-dmr-bridge:latest` | Docker image tag |
| `MAX_ACTIVE_CALLS` | unlimited | Hard cap; excess calls get SIP 503 |
| `SOUND_PATH` | `/sounds` | Exchange sound files |

## PBX-side configuration

Mirror `SIP_AUTH_TOKEN` on the PBX:

- Store secret in a root-only file (e.g. `/root/sip-dmr-exchange.token`)
- Inject via dialplan: `PJSIP_HEADER(add,X-Auth-Token)=...`
- Set `X-Callsign` from user cidname
- Optional `X-DMR-SSID` for SystemX client suffix

See [FreePBX integration](../integration/freepbx.md).

## Phonebook display (FreeSTAR Everywhere)

On the PBX phonebook host, optional `config.php` defines:

```php
define('DMR_PORTAL_MAX_ACTIVE_CALLS', 2);  // should match exchange
define('DMR_PORTAL_BRIDGES_URL', 'https://portal.example.com/bridges');
define('DMR_PORTAL_STATS_URL', 'https://portal.example.com/stats');
```

See [Phonebook integration](../integration/phonebook.md).
