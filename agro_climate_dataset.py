import pandas as pd
import numpy as np

np.random.seed(42)
years = np.arange(2000, 2025)
crops = ['Rice', 'Wheat', 'Maize']

data = []
for crop in crops:
    for y in years:
        rainfall = np.random.normal(900, 100)
        temp = np.random.normal(27, 1.5)
        co2 = np.random.normal(410, 10)
        yield_tph = (
            4.5 + 0.002*(rainfall-900)
            - 0.05*(temp-27)
            + 0.001*(co2-410)
            + np.random.normal(0, 0.1)
        )
        data.append([y, crop, rainfall, temp, co2, yield_tph])

df = pd.DataFrame(data, columns=['Year', 'Crop', 'Rainfall(mm)', 'Temperature(°C)', 'CO2(ppm)', 'Yield(t/ha)'])
df.to_csv("sample_agro_data.csv", index=False)
print("✅ sample_agro_data.csv generated successfully!")
