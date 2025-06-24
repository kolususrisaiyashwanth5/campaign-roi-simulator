# Campaign ROI Simulator

This is a simple and interactive tool that helps estimate how an ad campaign might perform based on expected budget, CPC, CTR, and conversion rate. It’s designed for marketers or analysts who want quick, data-based projections before launching a campaign.

You can enter your planned campaign numbers and get instant forecasts for impressions, clicks, conversions, revenue, and ROI — all visualized with a clear bar chart.

## Key Features

- Forecasts campaign results based on:
  - Budget
  - Expected Cost Per Click (CPC)
  - Click-Through Rate (CTR)
  - Conversion Rate
- Calculates:
  - Impressions
  - Clicks
  - Conversions
  - Cost per Conversion
  - Revenue (based on assumed conversion value)
  - Estimated ROI (%)
- Includes a simple bar chart comparing budget vs. projected revenue

## Built With

- Python
- Streamlit
- Plotly

## How to Run Locally

```bash
# Clone the repo or download as ZIP
cd campaign_roi_simulator

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
