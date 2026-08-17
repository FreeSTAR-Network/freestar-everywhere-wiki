# SIP-DMR Portal

Connect **SIP/VoIP handsets** on your PBX to **DMR talkgroups** on a SystemX or MMDVM network. Users dial a feature code, enter a talkgroup, and the portal provisions a per-call bridge.

## Repositories

| Repository | Role |
|------------|------|
| [sip-dmr-exchange](https://github.com/FreeSTAR-Network/sip-dmr-exchange) | SIP B2BUA, Docker orchestration, HTTP `/bridges` and `/stats` API |
| [sip-dmr-bridge](https://github.com/FreeSTAR-Network/sip-dmr-bridge) | Per-call MMDVM bridge container |
| [sip-usrp-bridge](https://github.com/FreeSTAR-Network/sip-usrp-bridge) | USRP/MMDVM components baked into the bridge image |
| [sip-dmr-exchange-dashboard](https://github.com/FreeSTAR-Network/sip-dmr-exchange-dashboard) | Optional static ops dashboard |

!!! note "Legacy repos"
    `dmr-portal` and `dmr-portal-dashboard` are superseded by the stack above.

## Typical flow

1. User dials your feature code (e.g. **234**) on the PBX
2. IVR collects a talkgroup number
3. PBX sends `INVITE` to **sip-dmr-exchange** with custom SIP headers
4. Exchange spawns a **sip-dmr-bridge** Docker container
5. Audio is bridged SIP ↔ MMDVM ↔ your DMR network

See [Architecture](architecture.md) for a detailed diagram.

## Who is this for?

- **Self-hosters** — run exchange + bridge on a Linux VM with Docker ([Self-Hosting](self-host/index.md))
- **PBX admins** — FreePBX/Asterisk trunk, IVR, and access control ([FreePBX integration](integration/freepbx.md))
- **FreeSTAR Everywhere** — production deployment uses this stack with Misc Application allowlists and the [phonebook DMR tab](integration/phonebook.md)

## Quick links

- [Getting Started](getting-started.md)
- [Configuration reference](self-host/configuration.md)
- [Scaling guide](operations/scaling.md)

## Licence and access

Source repositories are currently private within the FreeSTAR-Network organisation. Documentation here is written for a future public or friends-and-family release. **Never commit** `SIP_AUTH_TOKEN`, `.env` secrets, or production credentials to git.
