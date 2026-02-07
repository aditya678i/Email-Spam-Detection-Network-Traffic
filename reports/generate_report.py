import sys
import os

# Ensure we can import modules from sibling directories
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from analysis.extract_patterns import extract_senders
from rules.spam_rules import is_spam

def generate():
    # Looking for smtp_logs.txt in the current directory or project root
    log_file = "smtp_logs.txt"
    if not os.path.exists(log_file):
        # Fallback to check if it's in data/
        if os.path.exists(os.path.join("data", "smtp_logs.txt")):
            log_file = os.path.join("data", "smtp_logs.txt")
        elif os.path.exists(os.path.join("..", "smtp_logs.txt")):
             log_file = os.path.join("..", "smtp_logs.txt")

    print(f"Analyzing {log_file}...")
    senders = extract_senders(log_file)
    spam = [s for s in senders if is_spam(s)]

    output_file = "spam_report.txt"
    # Ensure reports directory exists if we want to write there, but user said "reports/generate_report.py" writes to "spam_report.txt" (implicit CWD or same dir)
    # The user's snippet wrote to "spam_report.txt" in CWD.
    
    with open(output_file, "w") as f:
        for s in spam:
            f.write(s + "\n")

    print(f"Total spam detected: {len(spam)}")
    print(f"Report saved to {output_file}")

if __name__ == "__main__":
    generate()
