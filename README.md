# Phishing-URL-Detection-Using-ML

[![Python](https://img.shields.io/badge/python-v3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)



🔍 Project Overview

A web-based phishing detection system where users can paste a URL to check whether it's legitimate or phishing.

Uses Machine Learning to analyze URL features and classify in real-time.

Goal: Demonstrate an ML-based cybersecurity approach and provide instant phishing detection.



🚀 Features

Paste and check URLs via a web interface

Real-time ML-based phishing detection

Feature extraction from URL (length, special characters, domain info)

User-friendly design

Easy to extend (browser extension, corporate filter)



🧠 How It Works

User enters a URL in the portal

Features are extracted from the URL (length, special characters, domain, etc.)

Features are passed to a trained ML model

Model predicts: Phishing or Legitimate

Result is displayed instantly on the web interface



🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python (Flask)

Machine Learning: Scikit-learn

Dataset: Public Phishing URL Dataset

Model Type: Supervised ML Classifier



📂 Project Structure

phishing-ml-web/
│

├── __pycache__/             # Python cache (ignore in git)

├── data/                    # Dataset files

│   ├── processed_urls.csv

│   └── urls.csv

├── frontend/                # Web frontend

│   └── index.html

├── app.py                   # Flask app main

├── feature_extraction.py    # Feature extraction logic

├── phishing_model.pkl       # Trained ML model

├── prepare_data.py          # Data preprocessing script

├── test_api.py              # API testing script

├── test.py                  # Unit testing script

├── train_model.py           # Model training script



▶️ How to Run Locally

Clone the repo: 

git clone https://github.com/username/phishing-ml-web.git

cd phishing-ml-web

Install dependencies: 

ip install -r requirements.txt

Run the web app: 

python src/app.py

Open in browser: 

http://localhost:5000



🎯 Use Cases

Detect phishing websites before visiting

Educational demo for ML-based cybersecurity

Can be extended to browser extensions or corporate email filters



🔧 Notes

Ensure phishing_model.pkl is in the model/ folder

Datasets are in data/ folder

Scripts are organized in src/ for easy maintenance

.gitignore prevents unnecessary files from being pushed


👤 Authors

Nikesh Babu S

Harshith Kumar B S

