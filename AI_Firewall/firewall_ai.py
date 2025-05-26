from netfilterqueue import NetfilterQueue
from scapy.all import IP, TCP
import joblib
import logging

# Load your trained model
model = joblib.load("model.pkl")

# Setup logging to a file
logging.basicConfig(filename='blocked_packets.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def extract_features(packet):
    """Extract src port, dst port, and packet size as features."""
    src_port = packet[TCP].sport
    dst_port = packet[TCP].dport
    size = len(packet)
    return [[src_port, dst_port, size]]

def process_packet(pkt):
    """Called for every packet in the NFQUEUE."""
    scapy_pkt = IP(pkt.get_payload())  # Convert raw packet to scapy packet

    # Only process TCP packets
    if TCP in scapy_pkt:
        features = extract_features(scapy_pkt)
        prediction = model.predict(features)[0]

        if prediction == 1:
            # Malicious packet detected — block it!
            msg = f"Blocked malicious packet from {scapy_pkt.src}"
            print(msg)
            logging.info(msg)
            pkt.drop()  # Drop the packet (block it)
            return

    pkt.accept()  # Accept packet if not malicious

def main():
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, process_packet)  # Bind to queue number 1

    print("Firewall started. Press Ctrl+C to stop.")
    try:
        nfqueue.run()  # Start processing packets
    except KeyboardInterrupt:
        print("\nFirewall stopped by user.")
    finally:
        nfqueue.unbind()  # Clean up on exit

if __name__ == "__main__":
    main()



