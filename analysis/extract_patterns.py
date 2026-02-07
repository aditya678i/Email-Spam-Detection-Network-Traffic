import re

def extract_senders(log_file):
    senders = []
    try:
        with open(log_file, "rb") as f:
            for line in f:
                # Decode line closely to avoid issues, or search bytes directly
                # The user's code searched bytes: re.search(rb"...", line)
                match = re.search(rb"MAIL FROM:<(.+?)>", line)
                if match:
                    try:
                        senders.append(match.group(1).decode('utf-8', errors='ignore'))
                    except:
                        pass
    except FileNotFoundError:
        print(f"Error: {log_file} not found.")
        return []
    return senders

if __name__ == "__main__":
    senders = extract_senders("smtp_logs.txt")
    for s in set(senders):
        print(s)
