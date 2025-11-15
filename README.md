# Li-ion Battery Remaining Useful Life (RUL) Prediction: Feature Engineering
### 🔋Project Overview 

This project explores battery degradation using data from NASA’s Li-ion Battery Dataset (batteries B0005, B0007, and B0018).

The objective is to develop a regression model to predict the current State-of-Health (SOH), quantified by the discharged capacity (Ah) ($\mathbf{Y}$), using features derived from the charge phase ($\mathbf{X}$). The chosen feature is the Differential Capacity ($\mathbf{dQ/dV}$) curve, an electrochemical signature that reliably captures internal battery degradation mechanisms.

## ✅ Week 1 Accomplishments: Data Pipeline Success

The most challenging task—cleaning and engineering features from the noisy raw data (NASA PCoE Dataset: B05, B07, B18) has been completed.
1. Problem Solved: The raw dataset contains cycles (like impedance tests or rest cycles) that lack a valid discharge capacity, which would crash a standard pipeline.
2. Result: The pipeline successfully filtered $\sim 940$ raw cycles to isolate 472 valid charge/discharge pairs. The final dataset has $0$ missing values.
3. Final Output: A clean matrix of 472 samples with 200 $\mathbf{dQ/dV}$ features and corresponding capacity targets, ready for machine learning model training.
## ✅ Week 2 Accomplishments: Feature Validation & BiLSTM Setup

1. Feature Validation: Verified processed dQ/dV features through EDA, confirming non-linear capacity degradation and characteristic peak shifts across all batteries.
2. Data Preparation: Implemented sequential data structuring (create_sequences) with a 10-cycle lookback and applied Leave-One-Out (LOO) Cross-Validation:

   Train/Validation: B05, B07 | Unseen Test: B18

Model Training: Built and trained a Bidirectional LSTM (BiLSTM) for RUL prediction with early stopping to prevent overfitting and preserve optimal weights.
## ✅ Week 3 Accomplishments: Conversational AI Integration

The project successfully transitioned from a static evaluation script into an interactive, LLM-powered RUL explanation system.
1. Problem Solved: Users often struggle to interpret RUL metrics like RMSE, MAE, or a negative RUL error. A normal chatbot would hallucinate or generalize to unrelated scenarios (e.g., Tesla batteries, mileage).
2. Result: A controlled conversational backend was built using a local Ollama server running Llama 3, with a strict system prompt and a “Metrics Context” that forces the model to answer only from the final evaluation metrics (including the −223 cycles RUL error). The logic was validated through an interactive CLI loop.
3. Final Output: A modular Streamlit web app with:

`chatbot.py` handling metric retrieval and Ollama API calls

`app.py` displaying core evaluation metrics and hosting the chat interface

----
## 📚 Dataset Reference
Experiments on Li-Ion batteries. Charging and discharging at different temperatures. Records the impedance as the damage criterion. The data set was provided by the NASA Prognostics Center of Excellence (PCoE).

Download: [NASA-Battery-Data-Set](https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip)

Data Set Citation: B. Saha and K. Goebel (2007). “Battery Data Set”, NASA Prognostics Data Repository, NASA Ames Research Center, Moffett Field, CA

## ✍️ Author

### Aashi Chatterjee

Student | Machine Learning & AI Enthusiast
