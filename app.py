from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from feature_extraction import extract_features
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("phishing_model.pkl")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return jsonify({"status": "Server is running ✅"})

    data = request.get_json()
    url = data.get("url", "")

    features = extract_features(url)
    df = pd.DataFrame([features])

    prediction = model.predict(df)[0]

    return jsonify({
        "url": url,
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)
