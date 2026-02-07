# Viva Preparation: Email Spam Detection using Network Traffic Analysis

## Common Questions & Answers

### 1. Why did you choose Rule-Based Filtering over Machine Learning?
**Answer:**
*   **Speed & Efficiency:** Network traffic analysis needs to be fast. Rule-based systems check static patterns (like blacklisted domains or specific keywords) much faster than ML models, which require feature extraction and inference time.
*   **Explainability:** If a sender is blocked, we can say exactly why (e.g., "Matched blacklist rule #4"). ML models are often "black boxes."
*   **Resource Constraints:** In a real-time network environment (like a router or firewall), lightweight rule engines are preferred over heavy ML libraries.
*   *Note:* Real-world systems often use a hybrid approach (Rules for obvious spam, ML for subtle cases). This project demonstrates the foundational "first line of defense."

### 2. How does the packet capture work?
**Answer:**
We use the **Scapy** library in Python. The script sniffs the network interface for TCP packets on **port 25** (SMTP). 
*   `sniff(filter="tcp port 25", ...)`: Captures the traffic.
*   `packet.haslayer(Raw)`: Extract the payload.
*   We look for SMTP commands like `MAIL FROM` to identify the sender.

### 3. Why only check Port 25?
**Answer:**
Port 25 is the standard port for server-to-server SMTP communication. 
*   **Port 587 (Submission)** and **Port 465 (SMTPS)** are often encrypted (TLS/SSL).
*   Analyzing encrypted traffic requires **SSL Termination** or **Man-in-the-Middle** proxies, which is out of scope for this project. Port 25 traffic is often unencrypted plain text (or uses STARTTLS which we can see the start of), making it suitable for this educational demonstration.

### 4. Is the sample_logs.pcap real?
**Answer:**
The provided `.pcap` file is a **simulation** generated using Scapy. It constructs valid Ethernet/IP/TCP/SMTP packets that mirror what real traffic would look like. This allows us to test the extraction logic without needing a live spam server sending emails during the demo.

### 5. What are the limitations?
**Answer:**
*   Cannot read encrypted emails (SMTPS).
*   Static rules can be bypassed by changing the domain name (needs dynamic blacklist updating).
*   Does not analyze the *content* of the email body deeply (like an ML model would).
