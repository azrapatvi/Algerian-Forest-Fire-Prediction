# 🔥 Algerian Forest Fire Prediction (Machine Learning + Flask Web App)

## 📌 Project Overview

This project predicts forest fire risk in Algeria using machine learning and provides an interactive **Flask-based web application** for real-time predictions.

It covers the complete ML workflow — data preprocessing, EDA, feature selection, model training, evaluation — and deployment using a modern web interface.

---

## 🌐 Web Application Features

* User-friendly prediction form (HTML + Bootstrap)
* Takes real-time meteorological inputs
* Uses trained ML model for prediction
* Displays **Fire Weather Index (FWI)**
* Indicates fire risk level based on predicted value

---

## 📂 Project Structure

```
Algerian-Forest-Fire-Prediction/
│
├── Algerian_forest_fire.ipynb
├── feature_selection_and_model_training.ipynb
├── main.py                 # Flask backend
├── templates/
│   └── index.html          # Frontend UI
├── models.pkl              # Trained ML models
├── scaler.pkl              # Feature scaler
├── dataset/ (optional)
├── README.md
```

---

## 🧪 Key Steps Performed

### Machine Learning

* Data cleaning & preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering & selection
* Model training (Linear Regression)
* Model evaluation
* Model serialization using Pickle

### Deployment

* Flask backend (`main.py`)
* HTML + Bootstrap frontend
* Real-time prediction pipeline

---

## 🛠️ Technologies Used

* Python
* Google Colab
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Flask
* HTML, CSS, Bootstrap

---

## 📊 Dataset

The dataset includes environmental and meteorological features:

* Temperature
* Relative Humidity (RH)
* Wind Speed (WS)
* Rain
* FFMC, DMC, ISI indices
* Region

Target: Fire Weather Index (FWI)

---

## 📈 Model Output

The application predicts **FWI (Fire Weather Index)**:

* Low FWI → Low fire risk
* High FWI → High fire risk



## ⭐ If you find this project useful, consider giving
