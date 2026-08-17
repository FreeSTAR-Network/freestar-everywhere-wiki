# Getting Started

A minimal path from zero to one successful SIP → DMR call.

## What you need

| Component | Notes |
|-----------|--------|
| **Linux VM** | Docker, host networking recommended, public IP for SIP |
| **sip-dmr-exchange** | Listens UDP 5060, spawns bridge containers |
| **sip-dmr-bridge image** | Built locally or pulled if published |
| **DMR network** | SystemX / MMDVM server you are allowed to use |
| **PBX** | FreePBX, Asterisk, or similar — outbound SIP trunk to exchange |

## Steps

### 1. Deploy the exchange

```bash
git clone https://github.com/FreeSTAR-Network/sip-dmr-exchange.git
cd sip-dmr-exchange
cp .env.example .env
# Edit .env — HOST_IP, SIP_AUTH_TOKEN, DMR_ADDRESS, etc.

docker compose up -d --build
```

See [Exchange deployment](self-host/exchange.md) and [Configuration](self-host/configuration.md).

### 2. Build the bridge image

```bash
git clone https://github.com/FreeSTAR-Network/sip-dmr-bridge.git
cd sip-dmr-bridge
docker build -t sip-dmr-bridge:latest .
```

See [Bridge image](self-host/bridge.md).

### 3. Firewall

Restrict SIP to your PBX only:

```bash
# Example — replace PBX_IP
iptables -A INPUT -p udp --dport 5060 -s PBX_IP -j ACCEPT
iptables -A INPUT -p udp --dport 5060 -j DROP
```

### 4. Configure the PBX trunk

- Trunk name e.g. `sip-dmr-exchange`
- IP auth to your portal host UDP **5060**
- Inject headers: `X-Auth-Token`, `X-Callsign`, optional `X-DMR-SSID`
- Talkgroup = SIP URI user part: `PJSIP/12345@sip-dmr-exchange`

See [FreePBX / Asterisk](integration/freepbx.md).

### 5. Test

```bash
# On portal host
curl -sS http://127.0.0.1:8080/bridges
curl -sS http://127.0.0.1:8080/stats
```

Place a test call from the PBX, enter a talkgroup, confirm a bridge appears in `/bridges`.

## FreeSTAR Everywhere production

FreeSTAR runs this stack with feature code **234**, Misc Application allowlists, and capacity limits. Production hostnames and operator runbooks are not published here — contact the FreeSTAR team for access.

## Next

- [Architecture](architecture.md)
- [Prerequisites](self-host/prerequisites.md)
- [Troubleshooting](operations/troubleshooting.md)
