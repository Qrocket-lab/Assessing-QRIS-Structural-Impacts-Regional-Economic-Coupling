# Technical Appendix: QRIS Policy Optimization Framework

## Data Lineage & Governance
### Primary Data Sources
1. **Economic Indicators (BPS)**
   - API Endpoint: `https://webapi.bps.go.id/v1/api/`
   - Required Key: `BPS_API_KEY` (obtained from BPS developer portal)
   - Refresh Rate: Quarterly (aligned with GDP reporting)

2. **QRIS Metrics (BI Internal)**
   - Source: Bank Indonesia Statistik Sistem Pembayaran (SSP)
   - Metrics: Merchant density, transaction volume, value growth
   - Integration: Framework includes adapter pattern for BI's data formats

3. **Market Intelligence (GDELT)**
   - API: GDELT Project DOC API v2
   - Filter: `sourcecountry:ID` for Indonesian media only
   - Keywords: Curated for BI's strategic priorities

### Statistical Methodology
#### Correlation Analysis
- **Test**: Pearson Product-Moment Correlation
- **Significance**: α = 0.05 (95% confidence interval)
- **Power Analysis**: Minimum n=20 for policy decisions
- **Interpretation**: Contextualized for BI's operational reality

#### Quadrant Classification
- **Method**: Quartile-based segmentation
- **Dimensions**: QRIS density vs economic growth
- **Strategic Implications**:
  - Quadrant I (High-High): Success cases for replication
  - Quadrant II (High-Low): Efficiency optimization targets
  - Quadrant III (Low-High): Priority for "SIAP QRIS" campaigns
  - Quadrant IV (Low-Low): Foundational development focus

### Framework Scalability Metrics
| Dataset Size | Processing Time | Memory Usage | Statistical Power |
|--------------|----------------|--------------|-------------------|
| 4 provinces  | < 1 second     | < 50 MB      | Limited           |
| 20 provinces | 2-3 seconds    | < 100 MB     | Good              |
| 34 provinces | 4-5 seconds    | < 150 MB     | Excellent         |
| 500 districts | < 30 seconds  | < 500 MB     | Comprehensive    |

### API Integration Specifications
```yaml
BPS_API_Integration:
  authentication: API Key in header
  rate_limit: 100 requests/hour
  data_format: JSON
  error_handling: Exponential backoff retry
  
BI_Internal_Integration:
  authentication: OAuth 2.0 / Service Account
  data_formats: CSV, Excel, JSON, Database direct
  compliance: BI data governance standards
  audit_trail: Full data transformation logging
  
GDELT_Monitoring:
  authentication: None required (public API)
  rate_limit: 1.5 seconds between requests
  data_freshness: 15-minute delay for news articles
  geographic_filter: Indonesia-only (sourcecountry:ID)