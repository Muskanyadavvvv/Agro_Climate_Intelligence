import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Agro-Climate Intelligence", layout="centered")

st.title("🌾 Agro-Climate Intelligence")
st.subheader("AI-Based Crop Yield Prediction under Changing Climate")

df = pd.read_csv("sample_agro_data.csv")
crop = st.selectbox("Select Crop", df['Crop'].unique())

data = df[df['Crop'] == crop][['Year', 'Yield(t/ha)']].rename(columns={'Year': 'ds', 'Yield(t/ha)': 'y'})

model = Prophet()
model.fit(data)

future = model.make_future_dataframe(periods=5, freq='Y')
forecast = model.predict(future)

fig = go.Figure()
fig.add_trace(go.Scatter(x=data['ds'], y=data['y'], mode='lines+markers', name='Actual Yield'))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Predicted Yield'))
fig.update_layout(title=f"{crop} Yield Forecast (Prophet Model)",
                  xaxis_title="Year", yaxis_title="Yield (t/ha)",
                  template='plotly_white')
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 🌦️ Simulate Climate Change Impact")
rain_change = st.slider("Change in Rainfall (%)", -20, 20, 0)
temp_change = st.slider("Change in Temperature (°C)", -2, 2, 0)

avg_yield = forecast['yhat'][-5:].mean()
adj_yield = avg_yield * (1 + rain_change/100 - temp_change*0.03)

st.success(f"📊 Predicted Average Yield (next 5 years): {adj_yield:.2f} t/ha")

st.caption("This is a prototype using AI (Prophet model) for climate impact forecasting.")
