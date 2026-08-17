# FreePBX / Asterisk integration

Reference setup for FreePBX 17 / Asterisk 22. Adapt extension numbers and hostnames for your deployment.

## Overview

| Piece | Purpose |
|-------|---------|
| **PJSIP trunk** | `sip-dmr-exchange` → portal host UDP 5060 |
| **Custom dialplan** | IVR contexts `[dmr-portal]`, `[sip-dmr-ivr]`, `[sip-dmr-headers]` |
| **Custom Destination** | Registers IVR entry for FreePBX GUI |
| **Misc Applications** | Per-extension allowlist for feature code |

!!! warning "Extension Routes do not gate internal feature codes"
    FreePBX **Extension Routes** only control **outbound routes**. To restrict who may dial your portal feature code, use **Misc Applications** (or equivalent dialplan ACL).

## 1. Custom Destination (required for GUI)

Before Misc Applications destinations work in the FreePBX GUI, register the dialplan target:

**Admin → Custom Destinations → Add**

| Field | Value |
|-------|--------|
| **Description** | `DMR Portal IVR` |
| **Custom Destination** | `dmr-portal,234,1` |
| **Return** | off |

Submit → **Apply Config**.

Without this step, Misc Applications show **Bad Dest: dmr-portal,234,1** in the destination dropdown.

## 2. PJSIP trunk

Configure custom PJSIP files (or GUI trunk equivalent):

| File | Purpose |
|------|---------|
| `pjsip.endpoint_custom.conf` | Endpoint `sip-dmr-exchange` |
| `pjsip.aor_custom.conf` | AOR to portal host |
| `pjsip.identify_custom.conf` | Identify by portal IP |

- IP authentication, no registration
- Portal host: `your-portal.example.com:5060`

## 3. Dialplan contexts

Add to `extensions_custom.conf` (feature code **234** shown as example):

### `[dmr-portal]`

1. Answer, set callsign variable from AMPUSER cidname
2. Play welcome prompt
3. `Goto(sip-dmr-ivr,start,1)`

### `[sip-dmr-ivr]`

1. `Read()` talkgroup (digits only, validate pattern)
2. Play connecting prompts
3. `Dial(PJSIP/${DMRTG}@sip-dmr-exchange,180,b(sip-dmr-headers^addheaders^1))`
4. On congestion / unavailable → play **portal-busy** (exchange at capacity)
5. Max retries → goodbye

### `[sip-dmr-headers]`

Pre-dial subroutine:

- `X-Auth-Token` — from secure file on PBX, matches exchange `SIP_AUTH_TOKEN`
- `X-Callsign` — uppercase cidname
- `X-DMR-SSID` — optional (e.g. `99` for SystemX suffix)

## 4. Access control (Misc Applications)

Each user who may dial the portal needs **one** Misc Application:

1. **Applications → Misc Applications → Add**
2. **Description:** `DMR Portal (CALLSIGN)`
3. **Feature Code:** `234/_EXTNUM` — e.g. `234/_10018` for extension 10018
4. **Destination:** **Custom Destinations → DMR Portal IVR**
5. **Submit** → **Apply Config**

**Denied users** hear “cannot complete as dialed” — no IVR, no trunk.

### Remove access

Delete or disable the user's Misc Application row → Apply Config.

## 5. IVR sounds

Install under `/var/lib/asterisk/sounds/custom/sip-dmr/`:

| File | Use |
|------|-----|
| `welcome` | Start |
| `enter-tg` | Talkgroup prompt |
| `invalid` | Bad input |
| `connecting`, `systemx` | Before dial |
| `portal-busy` | Exchange returned 503 |
| `goodbye` | Too many attempts |

## Verify

```bash
asterisk -rx "dialplan show customdests"
asterisk -rx "dialplan show 234@dmr-portal"
asterisk -rx "dialplan show 234/_10018@app-miscapps"   # example allowlisted ext
asterisk -rx "core show channels concise" | grep -E "234|sip-dmr|dmr-portal"
mysql asterisk -e "SELECT miscapps_id, description, ext, dest FROM miscapps;"
```

## What not to do

- Do **not** add a global `exten => 234` in `[from-internal-custom]` — bypasses allowlist
- Do **not** create PJSIP extension 234 — it is dialplan-only
- Do **not** commit auth tokens to git

## Portal busy (capacity)

When `MAX_ACTIVE_CALLS` is reached, exchange returns SIP **503**. Route `DIALSTATUS` of `CONGESTION` / `CHANUNAVAIL` to a **portal-busy** prompt.

## Multi-portal failover (advanced)

When running multiple portal nodes:

1. Add second trunk e.g. `sip-dmr-exchange-b`
2. Sequential `Dial()` in IVR to try primary then secondary
3. Set per-node `MAX_ACTIVE_CALLS`

Misc Application allowlist unchanged.

## Related

- [Architecture](../architecture.md)
- [Phonebook integration](phonebook.md)
- [Configuration](../self-host/configuration.md)
