🌾 Agro Climate Intelligence
<p align="center"> <img src="https://img.shields.io/badge/AI%20%26%20Climate-Agro%20Intelligence-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/Built%20with-Streamlit-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/Forecasting-Prophet-orange?style=for-the-badge" /> </p>
🧠 Overview

Agro Climate Intelligence is an AI-powered project designed to study how climate variables such as rainfall, temperature, and CO₂ emissions affect crop yields.
It leverages data analytics, machine learning, and time-series forecasting to predict agricultural performance and visualize potential future impacts of climate change.

This project aims to support farmers, researchers, and policymakers in making data-driven decisions for sustainable agriculture. 🌱

🚀 Features

✅ Multivariate climate data analysis
✅ Time-series forecasting using Prophet and LSTM-ready data
✅ Interactive Streamlit dashboard for visualization
✅ Real-time simulation of rainfall & temperature impact
✅ Integrates datasets from FAO, NASA, and local sources

🏗️ Tech Stack
Category	Technologies Used
Programming Language	Python
Libraries	Pandas, NumPy, Plotly, Prophet, Matplotlib
Dashboard Framework	Streamlit
Data Sources	NASA EarthData, FAO, Local datasets
Version Control	Git & GitHub
🧩 Project Structure
Agro_Climate_Intelligence/
│
├── agro_climate_dataset.py        # Synthetic dataset generator
├── dashboard_app.py               # Streamlit interactive dashboard
├── yield_forecast_prophet.py      # Prophet-based forecasting model
├── requirements.txt               # Python dependencies
└── README.md                      # Documentation

⚙️ Installation & Usage
🔹 Step 1 — Clone the Repository
git clone https://github.com/Muskanyadavvv/Agro_Climate_Intelligence.git
cd Agro_Climate_Intelligence

🔹 Step 2 — Install Dependencies
pip install -r requirements.txt

🔹 Step 3 — Generate Dataset
python agro_climate_dataset.py

🔹 Step 4 — Run the Dashboard
streamlit run dashboard_app.py


The dashboard will open in your browser at 👉 http://localhost:8501

📊 Dashboard Highlights
Section	Description
Forecast Visualization	Displays historical vs. predicted yield for selected crops
Climate Simulation	Allows users to modify rainfall/temperature and view projected effects
Insights Panel	Shows future yield estimates and key metrics
🌐 Streamlit Cloud Deployment

Push this repo to GitHub (if not already).

Visit 👉 https://share.streamlit.io

Click “New App” → Select your repository

Set main file path to:

dashboard_app.py


Click Deploy

Your live app will be hosted at:
🔗 https://muskanyadavvv-agro-climate-intelligence.streamlit.app

📈 Future Enhancements

Integrate LSTM deep learning for more robust forecasting

Add geospatial crop mapping (GIS)

Include real-world FAO/NASA datasets

Expand dashboard with region-wise yield analytics

🤝 Contributors

👩‍💻 Muskan Yadav
Final Year B.Tech Student | AI & Data Analytics Enthusiast
📧 muskanyadav632@gmail.com

🌐 LinkedIn
 (optional)

🪴 Acknowledgement

Special thanks to FAO, NASA EarthData, and the Streamlit & Prophet open-source communities for providing tools and datasets that made this research project possible.

🧭 License

This project is licensed under the MIT License — feel free to use and modify it for educational or research purposes.
