# Firewall

**Firewall** is a security system designed to monitor and control incoming and outgoing network traffic based on predetermined security rules. Firewalls can be either hardware or software-based, and they are commonly used to protect networks from unauthorized access or threats.

## What is a Firewall?
A firewall serves as a barrier between a trusted internal network and untrusted external networks, such as the internet. It monitors network traffic and can permit or block data transmissions based on a set of security rules. Firewalls are essential for protecting sensitive data and ensuring that only authorized traffic can enter or leave the network.

## Types of Firewalls

### 1. **Packet-Filtering Firewall**
A packet-filtering firewall examines network packets (units of data) and makes decisions based on predefined rules, such as the packet's source IP address, destination IP address, and port number. If a packet matches the rule, it is either allowed or denied access. This type of firewall is efficient but lacks deeper inspection features.

### 2. **Stateful Inspection Firewall**
Stateful firewalls track the state of active connections and use this context to determine whether a packet should be allowed. This is a more secure option than a simple packet filter since it can evaluate packets within the context of a session.

### 3. **Proxy Firewall**
A proxy firewall operates by acting as an intermediary between a client and a server. It intercepts requests and responses, analyzes them, and makes decisions based on content and other parameters. Proxy firewalls provide an extra layer of security by hiding the true identity of the internal network.

### 4. **Next-Generation Firewall (NGFW)**
NGFWs combine the features of traditional firewalls with additional features like deep packet inspection, intrusion prevention systems (IPS), and application awareness. They offer more comprehensive protection by inspecting traffic at a deeper level and recognizing threats from applications and protocols.

### 5. **Web Application Firewall (WAF)**
A WAF specifically protects web applications by filtering and monitoring HTTP/HTTPS traffic. It is designed to block attacks such as SQL injection, cross-site scripting (XSS), and other vulnerabilities that can affect web applications.

## Firewall Categories

### Stateful
This type of firewall uses the entire information from a connection; rather than inspecting an individual packet, this firewall determines the behaviour of a device based upon the entire connection.

This firewall type consumes many resources in comparison to stateless firewalls as the decision making is dynamic. For example, a firewall could allow the first parts of a TCP handshake that would later fail.

If a connection from a host is bad, it will block the entire device.

### Stateless
This firewall type uses a static set of rules to determine whether or not individual packets are acceptable or not. For example, a device sending a bad packet will not necessarily mean that the entire device is then blocked.

Whilst these firewalls use much fewer resources than alternatives, they are much dumber. For example, these firewalls are only effective as the rules that are defined within them. If a rule is not exactly matched, it is effectively useless.

However, these firewalls are great when receiving large amounts of traffic from a set of hosts (such as a Distributed Denial-of-Service attack).

## How Firewalls Work
Firewalls use rules or policies to determine which traffic should be allowed or blocked. These rules are based on criteria such as:

- **Source IP address**: The address from which the data is coming.
- **Destination IP address**: The address where the data is being sent.
- **Port numbers**: The application or service to which the data is directed.
- **Protocol**: The type of communication protocol being used (e.g., TCP, UDP).

When a packet of data arrives at the firewall, the firewall inspects the packet based on these parameters. If the packet matches an allowed rule, it is forwarded to the target system. If it matches a blocked rule, it is discarded.

## Firewall Configurations
Firewalls can be configured to block or allow traffic based on various factors:

### 1. **Inbound and Outbound Rules**
- **Inbound rules** control the traffic that can come into your network from external sources.
- **Outbound rules** control the traffic that can leave your network and reach external systems.

### 2. **Allowlist (Whitelisting) and Blocklist (Blacklisting)**
- **Allowlist**: Only traffic from trusted sources or to specific services is allowed.
- **Blocklist**: Traffic from known bad sources or certain types of traffic is blocked.

### 3. **Logging and Monitoring**
Many firewalls provide the option to log traffic, which can help administrators monitor suspicious activity, review past events, and troubleshoot issues.

## Firewall Policies
A firewall policy is a set of rules and procedures that define how the firewall should behave. These policies include:

- **Access Control**: Defining what type of network traffic is allowed or denied.
- **Traffic Monitoring**: Monitoring the flow of traffic and identifying potential threats.
- **Incident Response**: Actions taken when suspicious traffic is detected, such as blocking IP addresses or generating alerts.
- **Security Zones**: Segmenting the network into different zones, such as a DMZ (demilitarized zone) for public-facing servers and an internal network for sensitive data.

## Common Use Cases
Firewalls are widely used for various purposes in both small and large organizations:

1. **Network Security**: Protecting the internal network from external threats.
2. **Intrusion Prevention**: Detecting and preventing malicious traffic or unauthorized access.
3. **Content Filtering**: Blocking access to harmful websites or applications.
4. **VPN Security**: Securing remote connections to a private network via Virtual Private Networks (VPNs).
5. **Compliance**: Ensuring compliance with regulations like PCI-DSS, HIPAA, and GDPR by controlling access to sensitive data.
