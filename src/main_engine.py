import os
import json
import pandas as pd
import requests
import time
from dotenv import load_dotenv
from scipy.stats import pearsonr

# Load Environment Variables (BPS_API_KEY)
load_dotenv()

class DKSP_Intelligence_Unit:
    """
    REGIONAL SEISMOGRAPH v3: Policy Assessment & Innovation Tool
    Target: Bank Indonesia - DKSP (ITSP Research Fellowship)
    """
    
    # 2. EXPANDED GDELT TARGETS (The "BroadNet" List)
    # These are mapped to specific BI strategic interests
    SENTIMENT_TARGETS = {
        "RISK_FRAUD": "QRIS AND (Penipuan OR Palsu OR Sticker OR Phishing OR 'Saldo Hilang')",
        "TECH_STABILITY": "QRIS AND (Gangguan OR Error OR Down OR 'Gagal Scan' OR 'Susah Connect')",
        "LIFESTYLE_ADOPTION": "(Cashless OR 'Non Tunai' OR 'Bayar Pakai HP') AND (Trend OR Gaya Hidup OR Milenial OR Gen-Z)",
        "REGULATORY_MOVES": "(Bank Indonesia OR OJK) AND (QRIS OR MDR OR 'Biaya Admin' OR 'Tarif Transaksi')",
        "SME_GROWTH": "(UMKM OR 'Pedagang Kecil' OR Pasar) AND (Digital OR QRIS OR 'Naik Kelas')"
    }

    def __init__(self):
        self.bps_key = os.getenv("BPS_API_KEY")
        self.data = None

    def load_vault(self):
        """Loads the Hand-Curated Benchmark Dataset (Auditability Protocol)."""
        try:
            path = os.path.join('data', 'benchmarks.json')
            with open(path, 'r') as f:
                vault = json.load(f)
            self.data = pd.DataFrame(vault['regional_matrix'])
            print(f"[SUCCESS] Vault Loaded. Sources: {vault['metadata']['source_qris']}")
            return True
        except Exception as e:
            print(f"[ERROR] Could not load vault: {e}")
            return False

    def validate_bps_handshake(self):
        """Validates API connectivity to BPS (Data Governance Protocol)."""
        if not self.bps_key:
            print("[WARNING] BPS_API_KEY missing in .env. Handshake skipped.")
            return False
            
        url = f"https://webapi.bps.go.id/v1/api/list/model/subject/domain/0000/key/{self.bps_key}/"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print("[SUCCESS] BPS API Handshake Verified (Secure Connection).")
                return True
        except:
            print("[OFFLINE] BPS API unreachable. Proceeding with Benchmarks.")
        return False

    def run_inferential_engine(self):
        """Calculates Pearson Correlation (r) between QRIS Density and PDRB Growth."""
        if self.data is None: return
        
        r_val, p_val = pearsonr(self.data['qris_density'], self.data['pdrb_growth'])
        
        print("\n" + "="*50)
        print(f"      INFERENTIAL POLICY SIGNAL: r = {r_val:.4f}")
        print("="*50)
        
        if r_val < -0.3:
            print("ASSESSMENT: OPPORTUNITY GAP DETECTED.")
            print("STRATEGY: Prioritize SIAP QRIS in high-growth 'Blue Ocean' regions.")
        elif r_val > 0.3:
            print("ASSESSMENT: MATURE COUPLING.")
            print("STRATEGY: Focus on transaction depth in high-density regions.")
        else:
            print("ASSESSMENT: DECOUPLED/STABLE.")

    def run_broadnet_radar(self):
        """
        Executes BroadNet Intelligence Scanning across 5 Policy Pillars.
        Utilizes GDELT V2 API for real-time Indonesian media monitoring.
        """
        print("\n" + "-"*50)
        print("INITIATING BROADNET SENTIMENT RADAR (GDELT v2)")
        print("-"*50)
        
        for category, query in self.SENTIMENT_TARGETS.items():
            print(f"\n[SCANNING] Pillar: {category}")
            
            # Protocol: Filter by sourcecountry:ID to ensure local relevance
            api_url = "https://api.gdeltproject.org/api/v2/doc/doc"
            params = {
                "query": f"{query} sourcecountry:ID",
                "mode": "artlist",
                "maxrecords": "2",
                "timespan": "1month",
                "format": "json"
            }
            
            try:
                # Rate limiting protocol (1.5s delay to prevent IP blocking)
                time.sleep(1.5) 
                response = requests.get(api_url, params=params, timeout=15)
                
                if response.status_code == 200:
                    results = response.json()
                    articles = results.get('articles', [])
                    
                    if articles:
                        for art in articles:
                            print(f" >> {art['title'][:75]}...")
                    else:
                        print(" >> Result: No significant noise in last 30 days.")
                else:
                    print(f" >> Error: API returned status {response.status_code}")
            except Exception as e:
                print(f" >> Connection interrupted for {category}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Create the Fellow Intelligence Object
    engine = DKSP_Intelligence_Unit()
    
    # Step 1: Secure Handshake
    engine.validate_bps_handshake()
    
    # Step 2: Ingest Validated Data
    if engine.load_vault():
        
        # Step 3: Run Macroeconomic Math (Pearson r)
        engine.run_inferential_engine()
        
        # Step 4: Run Real-time Ecosystem Monitoring
        engine.run_broadnet_radar()

    print("\n" + "="*50)
    print("      REPORT COMPLETE: DATA LOCKED FOR SUBMISSION")
    print("="*50)