import requests

sample = {
    "num_packets": 120,
    "total_bytes": 54000,
    "mean_packet_size": 450,
    "std_packet_size": 80,
    "min_packet_size": 60,
    "max_packet_size": 1500,
    "mean_interarrival_time": 0.01,
    "std_interarrival_time": 0.005,
    "small_pkt_frac": 0.2,
    "medium_pkt_frac": 0.6,
    "large_pkt_frac": 0.2
}

resp = requests.post("http://127.0.0.1:8000/classify", json=sample)
print(resp.json())
