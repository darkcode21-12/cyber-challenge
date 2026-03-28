# IP Address Classes: Class D and Class E (Detailed Guide)

---

## Overview

In IPv4 addressing:
- Class D → Multicast communication
- Class E → Experimental / Reserved

---

# Class D (Multicast)

## Range
224.0.0.0 – 239.255.255.255

## Purpose
Used for multicast (one-to-many communication)

## Key Points
- No subnetting like normal IP classes
- Devices join multicast groups to receive data
- Efficient for streaming and real-time data

## Common Uses
- IPTV (live streaming)
- Video conferencing
- Online gaming updates
- Financial data feeds

## Important Addresses
- 224.0.0.1 → All hosts
- 224.0.0.2 → All routers
- 239.x.x.x → Private multicast

## Security Risks
- Multicast flooding
- Unauthorized access to streams

---

# Class E (Experimental)

## Range
240.0.0.0 – 255.255.255.254

## Purpose
Reserved for experimental use and research

## Key Points
- Not used in public networks
- Unsupported by most systems
- Usually blocked by routers

## Special Address
255.255.255.255 → Broadcast to all devices in local network

## Security Notes
- Rarely used in attacks
- Sometimes used in testing or evasion techniques

---

# Summary

- Class D → Multicast (active use)
- Class E → Experimental (not used)
- Neither are used for standard host assignment

---

# References

- RFC 1112 – IP Multicasting
- RFC 5771 – Multicast Address Assignments
- IANA IPv4 Address Registry
- Cisco Networking Academy
