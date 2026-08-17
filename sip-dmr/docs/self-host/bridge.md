# Bridge image

**sip-dmr-bridge** runs as a **Docker container per active call**, spawned by the exchange.

## Build

```bash
git clone https://github.com/FreeSTAR-Network/sip-dmr-bridge.git
cd sip-dmr-bridge
docker build -t sip-dmr-bridge:latest .
```

The image includes MMDVM bridge components from [sip-usrp-bridge](https://github.com/FreeSTAR-Network/sip-usrp-bridge).

Exchange expects the tag configured in `.env`:

```
BRIDGE_IMAGE_NAME=sip-dmr-bridge:latest
```

## Per-call behaviour

- Exchange assigns unique `MMDVM_BRIDGE_DMR_LOCAL_PORT` from configured range
- Container name typically based on callsign
- **HEALTHCHECK** must pass before exchange connects SIP media
- Container is removed when the call ends

## Resource usage

- ~130–150 MB RAM per container
- CPU spikes during AMBE encode/decode and `md380-emu`

Plan host RAM as: `(MAX_ACTIVE_CALLS × 150 MB)` + ~1 GB exchange/OS headroom.

## Updating the image

After pulling bridge changes:

```bash
cd sip-dmr-bridge
docker build -t sip-dmr-bridge:latest .
```

New calls use the new image; active calls keep running on the old container until hangup.
