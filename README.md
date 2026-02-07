# Email Spam Detection using Network Traffic Analysis

## Problem Statement
Spam emails consume network and system resources. This project aims to detect potential spam senders by analyzing SMTP network traffic and applying rule-based filtering.

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

## Tools & Libraries
* **Tools**: Linux, Mail Server (Postfix/Sendmail)
* **Libraries**: Python 3, Scapy

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: On Linux, you may need `sudo apt install tcpdump`.*

## Usage

### 1. Capture Traffic
To capture live SMTP traffic (root privileges required):
```bash
sudo python capture/capture_smtp.py
```
This will log SMTP packets to `smtp_logs.txt`.

### 2. Generate Report
To analyze the captured logs and generate a spam report:
```bash
python reports/generate_report.py
```
This will create `spam_report.txt` listing detected spam senders.

## How it Works
1. **Capture**: Sniffs TCP port 25 for "MAIL FROM" commands.
2. **extract**: Parses the captured logs to find sender email addresses.
3. **Filter**: Checks senders against a predefined list of spam domains (`rules/spam_rules.py`).
4. **Report**: Outputs the list of identified spam sources.
