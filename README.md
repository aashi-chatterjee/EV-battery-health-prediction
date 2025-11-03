# Li-ion Battery Remaining Useful Life (RUL) Prediction: Feature Engineering
### 🔋Project Overview 

This project explores battery degradation using data from NASA’s Li-ion Battery Dataset (batteries B0005, B0007, and B0018).

The objective is to develop a regression model to predict the current State-of-Health (SOH), quantified by the discharged capacity (Ah) ($\mathbf{Y}$), using features derived from the charge phase ($\mathbf{X}$). The chosen feature is the Differential Capacity ($\mathbf{dQ/dV}$) curve, an electrochemical signature that reliably captures internal battery degradation mechanisms.

## ✅ Week 1 Accomplishments: Data Pipeline Success

The most challenging task—cleaning and engineering features from the noisy raw data (NASA PCoE Dataset: B05, B07, B18) has been completed.
1. Problem Solved: The raw dataset contains cycles (like impedance tests or rest cycles) that lack a valid discharge capacity, which would crash a standard pipeline.
2. Result: The pipeline successfully filtered $\sim 940$ raw cycles to isolate 472 valid charge/discharge pairs. The final dataset has $0$ missing values.
3. Final Output: A clean matrix of 472 samples with 200 $\mathbf{dQ/dV}$ features and corresponding capacity targets, ready for machine learning model training.
----
## 📚 Dataset Reference
Experiments on Li-Ion batteries. Charging and discharging at different temperatures. Records the impedance as the damage criterion. The data set was provided by the NASA Prognostics Center of Excellence (PCoE).

Download: https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip

Data Set Citation: B. Saha and K. Goebel (2007). “Battery Data Set”, NASA Prognostics Data Repository, NASA Ames Research Center, Moffett Field, CA

## ✍️ Author

### Aashi Chatterjee

Student | Machine Learning & Data Analysis Enthusiast

“I built this project as part of my exploration into predictive modeling for energy systems, focusing on how electrochemical features can reveal battery health over time.”
