# Prerequisites

## Server

- **OS:** Linux (Debian/Ubuntu recommended)
- **Docker** and **Docker Compose** v2
- **Public IP** (or routable address) for SIP — set `HOST_IP` in exchange `.env`
- **Host networking** for exchange container (default in `docker-compose.yaml`)

## Network

| Port | Protocol | Purpose |
|------|----------|---------|
| 5060 | UDP | SIP from PBX |
| 8080 | TCP | HTTP API (`/bridges`, `/stats`) — bind localhost if using nginx |
| 62040–64040 | UDP | MMDVM local ports per bridge (configurable range) |

Firewall SIP to your PBX source IP only.

## PBX

- Asterisk / FreePBX with outbound PJSIP or SIP trunk
- Ability to add custom dialplan (IVR + `Dial()` with pre-dial headers)
- Custom sounds for IVR prompts (optional but recommended)

## DMR backend

- A SystemX, MMDVM, or compatible server you are authorised to use
- Credentials (`DMR_ADDRESS`, `DMR_PORT`, `DMR_PASSWORD` in `.env`)
- Confirm your network allows **multiple concurrent MMDVM logins** from one public IP if you plan more than one call

## Build tools (first-time bridge build)

Building `sip-dmr-bridge` may require:

- Git with SSH access to `sip-usrp-bridge` if submodules/private deps apply
- Sufficient disk for Docker layers and build cache (~10 GB+ comfortable)

## Secrets

Generate a strong random token for `SIP_AUTH_TOKEN`. Store on exchange (`.env`) and configure PBX to send it as `X-Auth-Token`. **Never commit secrets to git.**
