🚀 **Agentic VPN Traffic Detection Prototype**
**Machine Learning + Agentic Reasoning Layer + FastAPI**

This project demonstrates an end-to-end VPN traffic detection system built using real network captures.
It extracts flow-level features from PCAPs, trains a machine-learning classifier, and layers it with an agentic decision workflow exposed via a FastAPI service.

**🧩 Project Highlights**   

✔ Real VPN & non-VPN traffic captured using Wireshark  
✔ Flow-level feature extraction with Scapy  
✔ RandomForest classifier achieving ~99% accuracy  
✔ Agentic reasoning layer (ML + rule-based decision logic)  
✔ FastAPI microservice for interactive classification  
✔ Clean modular architecture suitable for research extension

**📊 System Architecture**  


<img width="1259" height="179" alt="image" src="https://github.com/user-attachments/assets/6da4060e-f33a-4af5-aeb3-af3609501c47" />

**🔍 How It Works**  

1️⃣ Capture network traffic (VPN & non-VPN)  
2️⃣ Convert PCAP → flow-level features (packet sizes, timings, distributions)  
3️⃣ Train ML model to classify VPN vs non-VPN  
4️⃣ Add agentic layer for:  
Label refinement  
Confidence scoring  
Human-readable explanation  
5️⃣ Expose API endpoint:  /classify

<img width="1167" height="165" alt="image" src="https://github.com/user-attachments/assets/42f18a1d-6ac2-4958-8355-157149893b4a" />

**🛠️ Tech Stack**  
_Component	        Technology_
Traffic Capture	        Wireshark
Feature Extraction	Scapy, NumPy, Pandas
Model	                RandomForestClassifier (scikit-learn)
Agentic Reasoning	Custom decision agent
API Framework	        FastAPI + Uvicorn
Deployment Ready	Docker (optional)

�**� Run Locally**  
1. Clone the repo
        _git clone https://github.com/yourusername/vpn-agentic-detector.git
        cd vpn-agentic-detector_
        
2. Install dependencies
        _pip install -r requirements.txt_

3. (Optional) Rebuild the dataset
        _python src/extract_features.py
        python src/train_model.py_

4. Start the API
        _uvicorn api.app:app --reload_


Open interactive docs:
➡ http://127.0.0.1:8000/docs

**🧪 Example Classification Response**  
        {  
                "probability_vpn": 0.94,  
                "final_label": "HIGH_CONFIDENCE_VPN",  
                "explanation": "Model probability >= 0.85 — strong VPN pattern"  
        }  

**📦 Repository Structure**  
        vpn-agentic-detector/  
        ├── data/  
        ├── models/  
        ├── src/  
        ├── api/  
        ├── requirements.txt  
        ├── test_request.py  
        └── README.md  

**🔮 Future Improvements**  
-Add JA3/TLS fingerprint extraction  
-Integrate IP reputation + ASN threat intelligence  
-Extend agent workflow using LLM-based reasoning  
-Add automated PCAP ingestion pipeline  

**👨‍💻 Author**  

Shashank Singh  
Final-year CSE · AI Research Enthusiast  
LinkedIn: your link here  
