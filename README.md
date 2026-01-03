# QRIS-Regional Seismograph: A Dual-Stream Policy Intelligence Tool
### Targeted for: DKSP-Bank Indonesia ITSP Research Fellowship

## Project Overview
This project provides a **Diagnostic & Inferential Assessment** of the Indonesian Digital Payment Ecosystem. It bridges the gap between traditional macroeconomic indicators (PDRB) and modern digital adoption metrics (QRIS Merchant Density).

## The Core Problem
Does digital payment penetration follow regional wealth, or does it act as a leading catalyst for economic growth? By utilizing a **Pearson Correlation Engine**, this tool identifies "Opportunity Gaps" where high PDRB growth exists despite low QRIS saturation.

## Methodology & Technology Stack
- **Quantitative Engine:** Python-based integration with the **BPS (Badan Pusat Statistik) Web API** for real-time regional GDP growth data.
- **Sentiment Sentinel:** Automated scraping of the **GDELT Project** to monitor Indonesian-language media narratives regarding system reliability and fraud risks.
- **Statistical Framework:**
  - *Pearson Correlation Coefficient ($r$):* To measure the coupling between digital infrastructure and economic velocity.
  - *Quadrant Analysis:* Mapping provinces into 'Stars', 'Saturated', 'Opportunity Gaps', and 'Sleeping Giants'.

## Deployment
1. Ensure Python 3.9+ is installed.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the assessment: `python src/seismograph_v3.py`