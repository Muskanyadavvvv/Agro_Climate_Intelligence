from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_agro_data.csv")
crop = 'Rice'
data = df[df['Crop']==crop][['Year','Yield(t/ha)']].rename(columns={'Year':'ds','Yield(t/ha)':'y'})

model = Prophet()
model.fit(data)
future = model.make_future_dataframe(periods=5, freq='Y')
forecast = model.predict(future)

model.plot(forecast)
plt.title(f"{crop} Yield Forecast")
plt.show()
