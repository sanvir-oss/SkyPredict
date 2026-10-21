
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and feature names
model = joblib.load("flight_price_model (1) (1).pkl")
features = joblib.load("flight_features (1).pkl")

# Get available duration options from the saved features
duration_options = sorted({
    feature.replace("Duration_", "", 1)
    for feature in features
    if feature.startswith("Duration_")
})


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        airline = request.form.get("airline")
        source = request.form.get("source")
        destination = request.form.get("destination")
        stops = request.form.get("stops")
        duration = request.form.get("duration")

        if not all([airline, source, destination, stops, duration]):
            return render_template(
                "predict.html",
                message="Please fill in all flight details.",
                duration_options=duration_options
            )

        # Create all 391 features in the model's original order
        input_data = pd.DataFrame(
            0, index=[0], columns=features
        )

        # Match categorical values to the saved dummy columns
        categories = {
            "Airline": airline,
            "Source": source,
            "Destination": destination,
            "Duration": duration,
            "Total_Stops": {
                "0": "non-stop",
                "1": "1 stop",
                "2": "2 stops",
                "3": "3 stops",
                "4": "4 stops"
            }.get(stops)
        }

        for prefix, value in categories.items():
            column = f"{prefix}_{value}"
            if column in input_data.columns:
                input_data.loc[0, column] = 1

        # Predict the flight fare
        predicted_price = float(model.predict(input_data)[0])

        return render_template(
            "predict.html",
            prediction=round(predicted_price, 2),
            duration_options=duration_options
        )

    return render_template(
        "predict.html",
        duration_options=duration_options
    )


if __name__ == "__main__":
    app.run(debug=True)
