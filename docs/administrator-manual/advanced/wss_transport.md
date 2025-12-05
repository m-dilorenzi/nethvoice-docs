---
title: WSS Transport
sidebar_position: 7
---

# WSS Transport {#wss-transport}

NethVoice on NethServer 8 supports WebSocket Secure (WSS) transport for extensions. Each NethVoice instance exposes a specific WSS port dedicated to WebSocket connections.

:::warning Network Constraint
This configuration relies on direct connectivity and **does not function behind NAT**. Ensure the instance has direct network visibility to the client endpoints.
:::

## Service Configuration {#service-configuration}

The WSS port assigned to the specific NethVoice instance is defined dynamically.

* **Variable:** `ASTERISK_WSS_PORT`
* **Location:** Inside the module environment variables.

Clients connecting to NethVoice via WebRTC or other websocket-based protocols must target this specific port.

## Extension Setup {#extension-setup}

To utilize WSS, the extension must be configured within the **Advanced Interface** (FreePBX).



### Prerequisites {#prerequisites}

1.  Create a new **Custom Extension** or edit an existing one.
2.  Access the **Advanced Interface**.

### Transport Settings {#transport-settings}

Modify the extension `Advanced` settings with the following parameters to enable secure websocket transport:

1.  **Outbound Proxy:** Remove proxy configurations for this specific extension.
2.  **Transport:** Set to `0.0.0.0-wss`.
3.  **Enable AVPF:** Set to `Yes`.
4.  **Enable ICE Support:** Set to `Yes`.
5.  **Enable rtcp Mux:** Set to `Yes`.
6.  **Media Encryption:** Set to `DTLS`.
7.  **Enable WebRTC Defaults:** Enable this setting to apply standard WebRTC optimizations.

## Client Configuration {#client-configuration}

Configure your client with the following settings. Ensure your client device has network access to the NethVoice instance.

| Parameter | Value / Instruction |
| :--- | :--- |
| **SIP Server / Domain** | The FQDN of your NethVoice instance. |
| **SIP Proxy** | (Leave empty). |
| **Transport Protocol** | **WSS** (Secure WebSocket). |
| **Port** | The value of `ASTERISK_WSS_PORT` (check your module environment variables). |
| **Path** | `/ws` (Default Asterisk WebSocket path). |
| **Username / Extension** | The extension number (e.g., `1001`). |
| **Password / Secret** | The extension secret defined in FreePBX. |
| **Media Encryption** | **DTLS** (Mandatory for WebRTC/WSS). |
| **AVPF** | Enabled / Yes. |
| **ICE Support** | Enabled / Yes. |

:::warning SSL Certificate Trust
WSS requires a valid SSL certificate. If you are using a self-signed certificate, the client device (or browser) **must explicitly trust the certificate Authority (CA)** before the connection can be established.
:::

