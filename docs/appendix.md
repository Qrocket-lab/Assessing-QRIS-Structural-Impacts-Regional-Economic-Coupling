# Technical Appendix & Data Lineage

## Data Source Verification
- **Metric A (PDRB):** Laju Pertumbuhan PDRB atas Dasar Harga Konstan (Provinsi). Source: BPS API Domain 0000.
- **Metric B (QRIS):** Jumlah Merchant Terdaftar (Provinsi). Source: Bank Indonesia Statistik Sistem Pembayaran (SSP) - Monthly Aggregates.

## Inferential Definitions
- **The $r$ Value:** We interpret a negative correlation ($r \approx -0.3$) as a "Growth Lead" signal. This suggests that QRIS expansion is penetrating high-growth emerging markets faster than traditional banking infrastructure, acting as a primary driver of financial inclusion.

## GDELT Signal Processing
We utilize the GDELT DOC API v2 with the `sourcecountry:ID` filter to isolate Indonesian media sentiment. Keywords focus on technical stability and regulatory shifts (MDR/Tarif).