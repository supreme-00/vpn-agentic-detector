# src/extract_features.py

from scapy.all import rdpcap, IP, TCP, UDP
import pandas as pd
import numpy as np
import os

def extract_from_pcap(path, label):
    print(f"Processing: {path} (label={label})")
    packets = rdpcap(path)
    flows = {}

    for pkt in packets:
        if IP not in pkt:
            continue
        
        ip = pkt[IP]

        if TCP in pkt:
            proto = "TCP"
            l4 = pkt[TCP]
        elif UDP in pkt:
            proto = "UDP"
            l4 = pkt[UDP]
        else:
            continue

        key = (ip.src, ip.dst, l4.sport, l4.dport, proto)

        size = len(pkt)
        ts = float(pkt.time)

        if key not in flows:
            flows[key] = []
        flows[key].append((size, ts))

    rows = []

    for key, pkt_list in flows.items():
        sizes = [x[0] for x in pkt_list]
        times = [x[1] for x in pkt_list]

        inter = np.diff(sorted(times))
        inter = inter if len(inter) > 0 else [0]

        row = {
            "num_packets": len(sizes),
            "total_bytes": sum(sizes),
            "mean_packet_size": np.mean(sizes),
            "std_packet_size": np.std(sizes),
            "min_packet_size": np.min(sizes),
            "max_packet_size": np.max(sizes),
            "mean_interarrival_time": np.mean(inter),
            "std_interarrival_time": np.std(inter),
            "small_pkt_frac": sum(s < 200 for s in sizes) / len(sizes),
            "medium_pkt_frac": sum(200 <= s <= 800 for s in sizes) / len(sizes),
            "large_pkt_frac": sum(s > 800 for s in sizes) / len(sizes),
            "label": label
        }
        rows.append(row)

    return pd.DataFrame(rows)


def build_dataset():
    base = "data/raw/"
    all_rows = []

    for file in os.listdir(base):
        if not (file.endswith(".pcap") or file.endswith(".pcapng")):
            continue

        filename = file.lower()

        if filename.startswith("vpn"):
            label = 1
        elif filename.startswith("nonvpn"):
            label = 0
        else:
            raise ValueError(f"Unknown file naming format: {file}")
        
        df = extract_from_pcap(os.path.join(base, file), label)
        all_rows.append(df)

    final = pd.concat(all_rows, ignore_index=True)
    final.to_csv("data/processed/vpn_flows.csv", index=False)
    print("Saved dataset → data/processed/vpn_flows.csv")


if __name__ == "__main__":
    build_dataset()
