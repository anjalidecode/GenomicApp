# 🧬 Genomic Data Analysis: Identifying Genetic Variations Through Visualization

A simple full-stack AI-powered web app that identifies **genetic variations** from DNA sequences. Built using **Streamlit** (frontend), **Flask** (backend API), and a **dummy ML model** trained with **TensorFlow**.

---

## 📌 Features

- 🔤 DNA sequence input (e.g., ACGT)
- 🔄 Automatic encoding & scaling
- 🧠 ML model prediction of variations
- 📊 Visualizes genetic variation as bar chart
- 🔗 Flask API integrated with Streamlit frontend

---

## 📁 Project Structure


-app.py # Streamlit frontend
-api.py # Flask backend API
-Save_dummy_model.py # Script to train/save dummy ML model & scaler
-genomic_model.h5 # Saved dummy model
-scaler.pkl # Saved scaler
-requirements.txt # Python dependencies

---

## ⚙️ Technologies Used

- 🧠 Machine Learning: `TensorFlow`, `scikit-learn`
- 🧪 Data: Dummy encoded DNA sequence
- 🧰 Backend API: `Flask`
- 🌐 Frontend UI: `Streamlit`
- 📊 Charts: `Matplotlib`
- 🐍 Language: Python 3

---

## 🚀 How to Run the Project

### 1. Clone the Repo

```bash
git clone https://github.com/anjalidecode/GenomicApp.git
cd genomic-data-analysis

2. Create & Activate Virtual Environment (Recommended)
python3 -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# OR
.venv\Scripts\activate     # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Train Dummy Model & Save It
python Save_dummy_model.py

This will generate:
genomic_model.h5
scaler.pkl

5. Start Flask Backend
python api.py
Flask API runs at: http://127.0.0.1:5000

6. Run Streamlit Frontend
Open a new terminal tab (keep Flask running):
streamlit run app.py
App will open in your browser at http://localhost:8501

🧪 Sample Input
Enter DNA Sequence: ATCG
This will be encoded internally and passed to the backend for variation prediction.

📊 Output
Variation values (4 floats)
A bar chart showing genetic variation frequencies

```
