# Email Spam Detection Using Network Traffic Analysis

## Abstract
Spam emails consume network bandwidth, server resources, and pose security risks. This project focuses on detecting potential spam sources by analyzing SMTP network traffic and applying rule-based filtering techniques. The system captures live SMTP packets, extracts sender patterns, applies predefined spam detection rules, and generates reports of suspected spam senders.

## Problem Statement
Spam emails consume network and system resources and can be used for phishing, malware distribution, and fraud. There is a need to monitor SMTP network traffic and identify suspicious or spam-related senders using network-level analysis.

## Objectives
* To capture SMTP network traffic in real time
* To extract sender email patterns from SMTP packets
* To apply rule-based spam detection
* To generate reports of suspected spam sources

## Project Structure
```
email-spam-detection/
├── README.md
├── requirements.txt
├── capture/
│   └── capture_smtp.py
├── analysis/
│   └── extract_patterns.py
├── rules/
│   └── spam_rules.py
├── reports/
│   └── generate_report.py
└── data/
    └── sample_logs.pcap
```

## Tools & Technologies

### Tools
* Linux Operating System
* Mail Server (Postfix / Sendmail for testing)
* Tcpdump / Wireshark (for packet capture verification)

### Libraries
* Python 3
* Scapy

## Installation

1. **Install system tools:**
   ```bash
   sudo apt update
   sudo apt install tcpdump python3-pip
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Methodology

### Step 1: Capture SMTP Traffic
The system captures live SMTP packets using Scapy by sniffing TCP traffic on SMTP ports.
```bash
sudo python capture/capture_smtp.py
```
Captured SMTP payloads are stored in `smtp_logs.txt`.

### Step 2: Extract Sender Patterns
SMTP logs are parsed to extract sender email addresses using pattern matching on the `MAIL FROM` command.
* File: `analysis/extract_patterns.py`

### Step 3: Rule-Based Spam Filtering
The extracted sender addresses are checked against predefined spam rules such as:
* Known spam domains
* Suspicious sender patterns
* Repeated sender occurrences
* File: `rules/spam_rules.py`

### Step 4: Generate Spam Report
A final report is generated listing all detected spam senders.
```bash
python reports/generate_report.py
```
* Output file: `spam_report.txt`

## How It Works (System Flow)
1. Capture SMTP packets from the network
2. Extract sender email addresses
3. Apply rule-based spam detection
4. Generate spam detection report

## Supported SMTP Ports
* **Port 25 (SMTP)** — Used in this project for simplicity

*Note: In real-world environments, ports 465 (SMTPS) and 587 (SMTP Submission) are also used. Encrypted SMTP traffic cannot be inspected directly without decryption.*

## Sample Data
`sample_logs.pcap` is provided for demonstration and testing purposes.

## Limitations
* Encrypted SMTP traffic (SMTPS) cannot be analyzed
* Rule-based detection may not detect new or unknown spam domains
* Designed for educational and lab environments

## Future Scope
* Integration of IP reputation services
* Machine learning-based spam classification
* PCAP file-based offline analysis
* Support for encrypted SMTP inspection

## Applications
* Network security monitoring
* Email server traffic analysis
* Cybersecurity education and labs
* Spam source identification

## Conclusion
This project demonstrates a network-level approach to spam detection using SMTP traffic analysis. By capturing and analyzing live network packets and applying rule-based logic, the system provides a practical understanding of how spam detection can be implemented at the network layer.
