# OSI Model (Sender vs Receiver) + Layer-by-Layer Attack Analysis

---

## 🔁 Why the Receiver Uses Reverse OSI Layers

The OSI Model works differently on the sender and receiver side because of:

- Encapsulation (Sender)
- Decapsulation (Receiver)

### 📤 Sender (Encapsulation)
Data moves from Layer 7 → Layer 1

Each layer adds its own header:

Application → Presentation → Session → Transport → Network → Data Link → Physical

Example:
- Application creates data
- Transport adds port (TCP/UDP)
- Network adds IP address
- Data Link adds MAC address
- Physical sends bits

---

### 📥 Receiver (Decapsulation)
Data moves from Layer 1 → Layer 7

Each layer removes headers in reverse order:

Physical → Data Link → Network → Transport → Session → Presentation → Application

### 🧠 Key Idea
Sender wraps data → Receiver unwraps it

---

# ⚔️ OSI Layer Attacks (Detailed)

## 1️⃣ Physical Layer
- Wiretapping
- Device destruction
- Signal jamming

## 2️⃣ Data Link Layer
- MAC Spoofing
- ARP Poisoning
- CAM Table Overflow

## 3️⃣ Network Layer
- IP Spoofing
- ICMP Flood
- BGP Hijacking

## 4️⃣ Transport Layer
- SYN Flood
- Port Scanning
- Session Hijacking

Common Ports:
- 80 (HTTP)
- 443 (HTTPS)
- 22 (SSH)
- 21 (FTP)

## 5️⃣ Session Layer
- Session Hijacking
- Replay Attacks

## 6️⃣ Presentation Layer
- SSL/TLS Downgrade
- Encryption attacks

## 7️⃣ Application Layer
- SQL Injection
- XSS
- Command Injection
- Phishing

---

# 📚 References

- RFC 1122
- RFC 793
- RFC 826
- OWASP Top 10
- NIST Cybersecurity Framework
- Cisco Networking Academy
