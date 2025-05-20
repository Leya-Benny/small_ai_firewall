from scapy.all import sniff, IP, TCP
import joblib
import datetime
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

def extract_features(packet):
    src_port = packet[TCP].sport
    dst_port = packet[TCP].dport
    size = len(packet)
    return pd.DataFrame([[src_port, dst_port, size]], columns=["src_port", "dst_port", "packet_size"])

def check_packet(packet):
    if IP in packet and TCP in packet:
        features = extract_features(packet)
        prediction = model.predict(features)[0]
        if prediction == 1:
            print(f"[{datetime.datetime.now()}] Blocked malicious packet from {packet[IP].src}")

# Start packet sniffing
print("Firewall started. Press Ctrl+C to stop.")
sniff(prn=check_packet, store=0)

