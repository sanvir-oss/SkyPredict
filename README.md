# ✈️ SkyPredict – Flight Price Prediction

SkyPredict is a Machine Learning web application that predicts estimated flight ticket prices based on flight details. It uses a **Random Forest Regression** model and a **Flask** web interface to make flight fare estimation simple and interactive.

## 🌐 Live Demo

**Try SkyPredict here:** https://skypredict-ij8u.onrender.com/

## ✨ Features

- Predict estimated flight ticket prices.
- Enter flight details through an interactive web form.
- Machine Learning model built using Random Forest Regression.
- User-friendly website built with Flask, HTML, and CSS.
- Deployed online for easy access.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn, Random Forest Regression
- **Data Analysis:** Pandas, NumPy
- **Web Framework:** Flask
- **Frontend:** HTML, CSS
- **Deployment:** Render
- **Version Control:** Git and GitHub

## ⚙️ How It Works

1. The user enters the required flight details.
2. The application processes the inputs into the features expected by the trained model.
3. The Random Forest model estimates the flight fare.
4. The predicted price is displayed on the website.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/sanvir-oss/SkyPredict.git
cd SkyPredict
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python main.py
```

Open http://127.0.0.1:5000/ in your browser.

## 📊 Model Evaluation

The Random Forest model was evaluated using a test dataset.

- **Mean Absolute Error (MAE):** Approximately ₹1,736
- **R² Score:** Approximately 0.61

These are evaluation results from the development dataset. Actual prediction accuracy may vary depending on the flight details.

## 📁 Project Structure

```text
SkyPredict/
├── main.py
├── flight_features (1).pkl
├── flight_price_model (1) (1).pkl
├── requirements.txt
├── templates/
│   ├── index.html
│   └── predict.html
├── check_features.py
└── README.md
```

## 👩‍💻 Author

**GitHub:** https://github.com/sanvir-oss

## 📌 Note

SkyPredict provides estimated fares for educational and demonstration purposes. Predictions may differ from actual airline ticket prices.


