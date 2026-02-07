from scapy.all import sniff, TCP, Raw

def process_packet(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load
        if b"SMTP" in payload or b"MAIL FROM" in payload:
            with open("smtp_logs.txt", "ab") as f:
                f.write(payload + b"\n")

if __name__ == "__main__":
    print("Starting packet sniffing on TCP port 25...")
    sniff(filter="tcp port 25", prn=process_packet, store=0)
