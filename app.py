import streamlit as st


st.set_page_config(page_title="Campaign ROI Simulator", layout="centered")
st.title("📊 Campaign ROI Simulator & Forecasting Tool")

st.markdown("""
This tool helps you estimate campaign performance based on your ad budget and expected metrics.
Enter your values below to simulate results.
""")


budget = st.number_input("Total Campaign Budget (₹)", min_value=0, value=10000)
cpc = st.number_input("Expected Cost Per Click (₹)", min_value=0.1, value=5.0)
ctr = st.slider("Expected Click-Through Rate (%)", min_value=0.1, max_value=20.0, value=3.0)
conversion_rate = st.slider("Expected Conversion Rate (%)", min_value=0.1, max_value=50.0, value=5.0)


ctr_decimal = ctr / 100
conversion_rate_decimal = conversion_rate / 100

impressions = int((budget / cpc) / ctr_decimal)
clicks = int(budget / cpc)
conversions = int(clicks * conversion_rate_decimal)
cost_per_conversion = round(budget / conversions, 2) if conversions > 0 else 0

value_per_conversion = 500  
revenue = conversions * value_per_conversion
roi = round(((revenue - budget) / budget) * 100, 2) if budget > 0 else 0


st.markdown("---")
st.header("📈 Forecast Results")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Estimated Impressions", value=f"{impressions:,}")
    st.metric(label="Estimated Clicks", value=f"{clicks:,}")
    st.metric(label="Estimated Conversions", value=f"{conversions:,}")

with col2:
    st.metric(label="Cost Per Conversion (₹)", value=f"{cost_per_conversion:,.2f}")
    st.metric(label="Estimated Revenue (₹)", value=f"{revenue:,.0f}")
    st.metric(label="Estimated ROI (%)", value=f"{roi}%")
import plotly.graph_objects as go

# --- CHART VISUALIZATION ---
st.markdown("---")
st.subheader("📊 Revenue vs Budget Comparison")

fig = go.Figure()

# Add budget bar
fig.add_trace(go.Bar(
    x=["Campaign Projection"],
    y=[budget],
    name="Budget (₹)",
    marker_color="#36a2eb"
))

# Add revenue bar
fig.add_trace(go.Bar(
    x=["Campaign Projection"],
    y=[revenue],
    name="Estimated Revenue (₹)",
    marker_color="#2ecc71"
))

fig.update_layout(
    barmode="group",
    xaxis_title="Campaign Forecast",
    yaxis_title="Amount in ₹",
    title="Estimated Revenue vs Budget",
    height=400,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(size=14)
)

st.plotly_chart(fig, use_container_width=True)
