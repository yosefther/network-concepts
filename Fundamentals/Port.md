# Ports in Networking

## What is a Port?
A **port** in computer networking is a logical endpoint for communication. It acts as a designated channel through which data is sent and received between devices. Ports help distinguish different types of network traffic, ensuring that data reaches the correct application or service.

### How Ports Work
When two devices communicate over a network, data packets contain:
- **Source IP Address**: Identifies the sender.
- **Destination IP Address**: Identifies the receiver.
- **Source Port**: The port from which the request originates.
- **Destination Port**: The port where the request is directed.

Networking devices enforce **strict rules** to control communication. If a connection is established (as per the **Transport Layer** in the OSI model), all transmitted data passes through **specific ports**. 

Since ports range from **0 to 65535**, managing them can become overwhelming. To maintain order, **standardized port assignments** ensure applications operate predictably. For instance, all web browsers know to send and receive HTTP traffic via **port 80**.

---

## Port Ranges
Ports are divided into three main categories:

| Port Range      | Description |
|----------------|-------------|
| **0 - 1023**   | Well-known ports (reserved for core services and protocols). |
| **1024 - 49151** | Registered ports (assigned for specific applications). |
| **49152 - 65535** | Dynamic/private ports (used for temporary connections). |

---

## Common Well-Known Ports
These ports follow standard rules to ensure seamless communication:

| Protocol | Port Number | Description |
|----------|------------|-------------|
| **FTP** | 21 | File transfer protocol for sharing files in a client-server model. |
| **SSH** | 22 | Secure text-based remote system login. |
| **HTTP** | 80 | The foundation of the World Wide Web (downloads text, images, videos, etc.). |
| **HTTPS** | 443 | Secure version of HTTP using encryption. |
| **SMB** | 445 | Allows file and device sharing, including printers. |
| **RDP** | 3389 | Remote desktop access using a graphical interface. |

While these ports have standard uses, applications **can be configured to use non-standard ports**. For example, a web server might run on **port 8080 instead of 80**. However, when using a non-standard port, users must specify it explicitly—e.g., `http://example.com:8080`.

---

## Ports and the Transport Layer
Ports function at the **Transport Layer** of the OSI and TCP/IP models. The two primary transport protocols are:

- **TCP (Transmission Control Protocol)**: Reliable, connection-oriented communication.
- **UDP (User Datagram Protocol)**: Faster, connectionless communication.

### Example: How HTTP Uses Ports
1. A user enters `http://example.com` in a web browser.
2. The browser sends an HTTP request to **port 80** of the web server.
3. The server responds with the requested webpage.

For secure communication, HTTPS uses **port 443**.

---

## Checking Open Ports
To check open ports on a system:
- **Linux/macOS**: `netstat -tulnp` or `ss -tulnp`
- **Windows**: `netstat -ano`
- **Nmap**: `nmap -p 1-65535 <IP>`

---

