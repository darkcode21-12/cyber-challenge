# TCP vs UDP – Detailed Comparison

## 📌 Overview

**TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** are core transport layer protocols in networking. They define how data is transmitted over the internet.

---

## 🔹 TCP (Transmission Control Protocol)

### ✅ Key Features
- **Connection-oriented**
- **Reliable data transfer**
- **Ordered delivery**
- **Error checking & recovery**
- **Flow control & congestion control**

### ⚙️ How It Works
TCP uses a **3-way handshake**:
1. SYN (synchronize)
2. SYN-ACK (synchronize-acknowledge)
3. ACK (acknowledge)

### 📦 Characteristics
- Ensures all packets arrive
- Retransmits lost packets
- Slower due to overhead

### 🌍 Real-world Uses
- Web browsing (HTTP/HTTPS)
- File transfer (FTP)
- Email (SMTP, IMAP)

---

## 🔸 UDP (User Datagram Protocol)

### ✅ Key Features
- **Connectionless**
- **Unreliable (no guarantee of delivery)**
- **No ordering**
- **No error recovery**
- **Low latency / fast**

### ⚙️ How It Works
- Sends packets (datagrams) directly
- No handshake
- No confirmation from receiver

### 📦 Characteristics
- Faster than TCP
- Minimal overhead
- Possible packet loss

### 🌍 Real-world Uses
- Video streaming
- Online gaming
- VoIP (calls)
- DNS queries

---

## ⚖️ TCP vs UDP (Comparison Table)

| Feature            | TCP                          | UDP                          |
|------------------|-----------------------------|-----------------------------|
| Connection Type   | Connection-oriented         | Connectionless              |
| Reliability       | High                        | Low                         |
| Speed             | Slower                      | Faster                      |
| Ordering          | Guaranteed                  | Not guaranteed              |
| Error Checking    | Yes (with recovery)         | Basic (no recovery)         |
| Header Size       | Larger                      | Smaller                     |
| Use Case          | Secure & accurate transfer  | Fast & real-time transfer   |

---

## 🧠 Simple Analogy

- **TCP** → Like a phone call 📞  
  (You confirm everything is heard correctly)

- **UDP** → Like sending a letter 📩  
  (You send it and hope it arrives)

---

## 🚀 Summary

- Use **TCP** when accuracy and reliability are critical.
- Use **UDP** when speed and real-time performance matter more than reliability.

---

## 🔗 Common Ports

| Port | Protocol | Service        |
|------|---------|---------------|
| 80   | TCP     | HTTP          |
| 443  | TCP     | HTTPS         |
| 22   | TCP     | SSH           |
| 53   | UDP     | DNS           |
| 123  | UDP     | NTP           |

---

