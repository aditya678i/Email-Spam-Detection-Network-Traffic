from scapy.all import Ether, IP, TCP, wrpcap, Raw

def create_smtp_packet(src_ip, dst_ip, src_port, dst_port, payload):
    # Construct a packet with Ethernet, IP, TCP, and Raw (payload) layers
    pkt = Ether() / IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port) / Raw(load=payload)
    return pkt

def generate_pcap(filename="data/sample_logs.pcap"):
    packets = []
    
    # 1. Spam interaction (spam@spam.com)
    # Client connects
    packets.append(create_smtp_packet("192.168.1.100", "10.0.0.1", 54321, 25, b"EHLO mail.spam.com\r\n"))
    # Server responds (omitted for brevity, we focus on client output for analysis)
    packets.append(create_smtp_packet("192.168.1.100", "10.0.0.1", 54321, 25, b"MAIL FROM:<spam@spam.com>\r\n"))
    packets.append(create_smtp_packet("192.168.1.100", "10.0.0.1", 54321, 25, b"RCPT TO:<victim@example.com>\r\n"))
    packets.append(create_smtp_packet("192.168.1.100", "10.0.0.1", 54321, 25, b"DATA\r\n"))
    packets.append(create_smtp_packet("192.168.1.100", "10.0.0.1", 54321, 25, b"Subject: You won a lottery!\r\n\r\nClick here for free money.\r\n.\r\n"))
    packets.append(create_smtp_packet("192.168.1.100", "10.0.0.1", 54321, 25, b"QUIT\r\n"))

    # 2. Ham interaction (friend@gmail.com)
    packets.append(create_smtp_packet("192.168.1.101", "10.0.0.1", 54322, 25, b"EHLO mail.google.com\r\n"))
    packets.append(create_smtp_packet("192.168.1.101", "10.0.0.1", 54322, 25, b"MAIL FROM:<friend@gmail.com>\r\n"))
    packets.append(create_smtp_packet("192.168.1.101", "10.0.0.1", 54322, 25, b"RCPT TO:<user@example.com>\r\n"))
    packets.append(create_smtp_packet("192.168.1.101", "10.0.0.1", 54322, 25, b"DATA\r\n"))
    packets.append(create_smtp_packet("192.168.1.101", "10.0.0.1", 54322, 25, b"Subject: Hello\r\n\r\nHow are you?\r\n.\r\n"))
    packets.append(create_smtp_packet("192.168.1.101", "10.0.0.1", 54322, 25, b"QUIT\r\n"))

    # 3. Spam interaction (bot@fake-mail.org)
    packets.append(create_smtp_packet("192.168.1.102", "10.0.0.1", 54323, 25, b"EHLO mail.fake.org\r\n"))
    packets.append(create_smtp_packet("192.168.1.102", "10.0.0.1", 54323, 25, b"MAIL FROM:<bot@fake-mail.org>\r\n"))
    packets.append(create_smtp_packet("192.168.1.102", "10.0.0.1", 54323, 25, b"RCPT TO:<everyone@example.com>\r\n"))
    packets.append(create_smtp_packet("192.168.1.102", "10.0.0.1", 54323, 25, b"DATA\r\n"))
    packets.append(create_smtp_packet("192.168.1.102", "10.0.0.1", 54323, 25, b"Subject: Urgent Prize\r\n\r\nBuy now.\r\n.\r\n"))
    packets.append(create_smtp_packet("192.168.1.102", "10.0.0.1", 54323, 25, b"QUIT\r\n"))
    
    print(f"Writing {len(packets)} packets to {filename}...")
    wrpcap(filename, packets)
    print("Done.")

if __name__ == "__main__":
    generate_pcap()
