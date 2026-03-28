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

# in detail

---
Physical Layer (Bit Level)
This layer deals with the actual hardware, cables, and radio waves.

Wiretapping: Physically tapping into a fiber or copper cable to intercept data as it passes through.

Device Destruction: A "denial of service" in its most literal form—smashing a router or cutting a power line.

Signal Jamming: Sending "noise" on the same frequency as a Wi-Fi or radio signal to drown out legitimate communication.

2️⃣ Data Link Layer (Frames/MAC Addresses)
This layer handles communication between two devices on the same local network.

MAC Spoofing: Changing your network card's ID to impersonate a trusted device (e.g., to bypass a router's "Allowed List").

ARP Poisoning: Sending fake Address Resolution Protocol messages to link your MAC address with the IP address of the legitimate gateway, allowing you to intercept local traffic.

CAM Table Overflow: Flooding a switch with so many fake MAC addresses that its memory (the CAM table) fails, forcing the switch to act like a "hub" and broadcast all traffic to every port, making it easy to sniff.

3️⃣ Network Layer (Packets/IP Addresses)
This layer is responsible for routing data between different networks.

IP Spoofing: Creating IP packets with a forged source IP address to hide the identity of the sender or to impersonate another computer system.

ICMP Flood (Ping Flood): Overwhelming a target with "Echo Request" (ping) packets until the target can no longer respond to real traffic.

BGP Hijacking: Falsely announcing to the internet's "routing table" (BGP) that your network is the best path for a certain set of IP addresses, effectively "stealing" or redirecting global internet traffic.

4️⃣ Transport Layer (Segments/TCP & UDP)
This layer ensures data arrives correctly via ports and protocols like TCP (reliable) and UDP (fast).

SYN Flood: Exploiting the TCP "3-way handshake." The attacker sends many SYN (connection) requests but never responds to the target's SYN-ACK, leaving the target's connection slots hanging open until it crashes.

Port Scanning: Using tools like nmap to see which ports (like 80, 443, 22) are "open" and listening for connections.

Session Hijacking: Stealing a user's active session token to take over their connection after they have already logged in.

5️⃣ Session Layer (Dialog Management)
Manages the start, stop, and restart of connections between applications.

Replay Attacks: Capturing a valid data transmission (like a login request) and re-sending it later to trick the system into granting access again.

6️⃣ Presentation Layer (Data Formatting/Encryption)
Translates data between the application and the network (e.g., JPEG, GIF, SSL/TLS).

SSL/TLS Downgrade: Forcing a connection to use an older, weaker version of encryption (like SSL 3.0) that the attacker knows how to crack.

Encryption Attacks: Directly attempting to break or bypass the mathematical algorithms protecting the data.

7️⃣ Application Layer (The User Interface)
Where the user interacts with software (Web browsers, Email, File transfers).

SQL Injection (SQLi): Inserting malicious SQL code into an input field (like a login box) to trick a database into revealing sensitive info.

Cross-Site Scripting (XSS): Injecting malicious JavaScript into a website so that it executes in the browser of other people visiting that site.

Command Injection: Tricking an application into executing system-level commands (like rm -rf or whoami) on the host server.

Phishing: Social engineering via email or fake websites to trick users into giving up passwords or downloading malware.