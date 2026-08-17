# About

## FreeSTAR SIP-DMR Portal

This wiki documents the **sip-dmr-exchange** stack: a SIP-to-DMR portal that lets VoIP users join DMR talkgroups through a per-call bridge container.

It is maintained by the [FreeSTAR Network](https://freestar.network) for use with **FreeSTAR Everywhere** and is intended to be reusable by other amateur radio groups running their own instances.

## Source code

| Repository | Description |
|------------|-------------|
| [sip-dmr-exchange](https://github.com/FreeSTAR-Network/sip-dmr-exchange) | Exchange service and HTTP API |
| [sip-dmr-bridge](https://github.com/FreeSTAR-Network/sip-dmr-bridge) | Bridge Docker image |
| [sip-usrp-bridge](https://github.com/FreeSTAR-Network/sip-usrp-bridge) | Low-level USRP/MMDVM bridge components |
| [sip-dmr-exchange-dashboard](https://github.com/FreeSTAR-Network/sip-dmr-exchange-dashboard) | Static dashboard |

## Contributing

Documentation changes: fork [FreeSTAR-Network/wiki](https://github.com/FreeSTAR-Network/wiki), edit under `sip-dmr/docs/`, open a pull request. See the [wiki README](https://github.com/FreeSTAR-Network/wiki/blob/main/README.md).

Code changes: pull requests welcome on the individual code repositories when you have access.

## Security

- Do not commit production tokens, `.env` files, or SSH keys
- Restrict UDP 5060 to your PBX IP
- Use `SIP_AUTH_TOKEN` on the exchange and inject matching `X-Auth-Token` from the PBX

## Licence

Refer to each code repository for licence terms. Documentation in this wiki is part of the FreeSTAR Network wiki project.
