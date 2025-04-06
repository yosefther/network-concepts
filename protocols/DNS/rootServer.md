# Root Servers

## Introduction

In the context of the Domain Name System (DNS), root servers are a critical part of the infrastructure that ensures the internet's domain names are resolved correctly. These servers are responsible for the top-level resolution of domain names by directing queries to the appropriate authoritative name servers.

## What Are Root Servers?

Root servers are the servers responsible for managing the root zone of the DNS. The root zone is the highest level of the DNS hierarchy, containing the information for all top-level domains (TLDs) such as `.com`, `.org`, `.net`, `.edu`, and country-specific domains like `.us` or `.uk`.

There are **13 root servers** globally, named `A` to `M`. Despite the name, there are more than 13 physical machines due to the use of Anycast technology, which allows multiple machines to share the same IP address to provide redundancy and better performance.

## How Root Servers Work

1. **Query Process:**
   When a DNS query is made for a domain, it might first need to contact a root server to find out where the authoritative DNS server for that domain is located.
   
2. **Root Zone Information:**
   The root server responds with a referral to the authoritative servers for the appropriate top-level domain (TLD). For example, if the query is for `example.com`, the root server would provide information on where to find the `.com` TLD servers.

3. **Delegation:**
   After the TLD servers are contacted, they delegate the query to the authoritative DNS servers responsible for the domain in question (e.g., `example.com`).

4. **Final Answer:**
   The authoritative DNS server for the domain responds with the IP address of the queried domain.

## List of Root Servers

The 13 root servers are operated by different organizations around the world:


| Hostname               | IP Addresses                              | Operator                                  |
|------------------------|-------------------------------------------|-------------------------------------------|
| a.root-servers.net      | 198.41.0.4, 2001:503:ba3e::2:30          | Verisign, Inc.                           |
| b.root-servers.net      | 170.247.170.2, 2801:1b8:10::b            | University of Southern California, Information Sciences Institute |
| c.root-servers.net      | 192.33.4.12, 2001:500:2::c               | Cogent Communications                    |
| d.root-servers.net      | 199.7.91.13, 2001:500:2d::d              | University of Maryland                   |
| e.root-servers.net      | 192.203.230.10, 2001:500:a8::e           | NASA (Ames Research Center)              |
| f.root-servers.net      | 192.5.5.241, 2001:500:2f::f              | Internet Systems Consortium, Inc.        |
| g.root-servers.net      | 192.112.36.4, 2001:500:12::d0d           | US Department of Defense (NIC)           |
| h.root-servers.net      | 198.97.190.53, 2001:500:1::53            | US Army (Research Lab)                  |
| i.root-servers.net      | 192.36.148.17, 2001:7fe::53              | Netnod                                   |
| j.root-servers.net      | 192.58.128.30, 2001:503:c27::2:30        | Verisign, Inc.                           |
| k.root-servers.net      | 193.0.14.129, 2001:7fd::1                | RIPE NCC                                 |
| l.root-servers.net      | 199.7.83.42, 2001:500:9f::42             | ICANN                                    |
| m.root-servers.net      | 202.12.27.33, 2001:dc3::35               | WIDE Project                             |


## Importance of Root Servers

- **Stability and Redundancy**: Root servers are designed for high availability, and the use of Anycast ensures that users can always reach a nearby server.
- **Security**: Root servers are critical for the security of the DNS, and they are managed with strict policies to prevent malicious attacks.
- **Performance**: By providing the foundational lookup for DNS queries, root servers contribute to the efficiency of DNS resolution worldwide.
