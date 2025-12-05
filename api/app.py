from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("models/vpn_rf.joblib")
feature_order = joblib.load("models/feature_order.joblib")

class FlowInput(BaseModel):
    num_packets: float
    total_bytes: float
    mean_packet_size: float
    std_packet_size: float
    min_packet_size: float
    max_packet_size: float
    mean_interarrival_time: float
    std_interarrival_time: float
    small_pkt_frac: float
    medium_pkt_frac: float
    large_pkt_frac: float

def decision_agent(prob):
    if prob >= 0.85:
        return "HIGH_CONFIDENCE_VPN", "Model probability >= 0.85 — strong VPN pattern"
    elif prob >= 0.60:
        return "SUSPICIOUS_VPN_LIKE", "Moderate probability — resembles VPN flows"
    else:
        return "LIKELY_NON_VPN", "Low probability — normal traffic pattern"

@app.post("/classify")
def classify_flow(flow: FlowInput):
    features = flow.dict()

    x = np.array([features[f] for f in feature_order]).reshape(1, -1)
    prob = float(model.predict_proba(x)[0][1])

    label, explanation = decision_agent(prob)

    return {
        "probability_vpn": prob,
        "final_label": label,
        "explanation": explanation
    }
