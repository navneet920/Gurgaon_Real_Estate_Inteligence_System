# 🏙️ Gurgaon Housing Intelligence — AI-Powered Real Estate Insights

> **A Smart Streamlit Web App for Price Prediction, Analytics, and Recommendations in Gurgaon’s Housing Market**

[![Python Version](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️%20by%20Navneet%20Kumar-red)](#contact)

---

## 🌟 Overview

**Gurgaon Housing Intelligence** is a comprehensive AI-powered dashboard that predicts real estate prices, provides insightful analytics, and recommends properties based on user preferences. It leverages machine learning models and data visualization techniques to simplify property-related decisions in Gurgaon.

---

## ⚡ Key Features

✅ **Smart Price Prediction** – Estimate property prices based on key features like BHK, size, and location.
✅ **Interactive Analytics** – Visualize market trends with sector-wise insights, price distributions, and word clouds.
✅ **Personalized Recommendations** – Discover similar or nearby properties using AI-based similarity search.
✅ **Streamlit-Powered UI** – A clean and interactive web interface for real-time exploration.
✅ **Modular Codebase** – Organized and scalable with distinct modules for prediction, analytics, and recommendations.

---

## 🧠 Project Architecture

```
/ (root)
├── app.py                     # Main Streamlit navigation hub
├── price_prediction.py        # Price prediction logic & UI
├── Analytics_app.py           # Data analysis and visualizations
├── recomendation_system.py    # AI-based recommendation system
├── requirements.txt           # Python dependencies
├── model/                     # Trained ML models (.pkl files)
│   ├── pipeline.pkl
│   ├── df.pkl
│   ├── feature_text.pkl
│   ├── location_distance.pkl
│   ├── cosine_sim1.pkl
│   ├── cosine_sim2.pkl
│   └── cosine_sim3.pkl
├── datasets/                  # Input datasets
│   └── data_vz1.xls
└── README.md                  # This file
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/gurgaon-housing-intelligence.git
cd gurgaon-housing-intelligence
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
# Activate it
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
# 💻 Tech Stack

Language: Python 3.11

Framework: Streamlit

ML Toolkit: Scikit-learn, Pandas, NumPy

Visualization: Matplotlib, Seaborn, Plotly, WordCloud

# 🚀 Future Enhancements

🧠 Add NLP model for price reasoning (text-to-price explanation)

📍 Integrate Google Maps API for real-time geo insights

# ☁️ Deploy on Render/Streamlit Cloud

🧾 Add user authentication & data persistence

# 🤝 Contribution Guide

## Fork this repository.

Create a new branch: git checkout -b feature-name.

Commit changes: git commit -m 'Add new feature'.

Push to branch: git push origin feature-name.

Create a Pull Request 🚀.

# 🧾 License

This project is licensed under the MIT License — see the LICENSE file for details.

# 📬 Contact

👤 Author: Navneet Kumar

📧 [Email](navneetgautam920@gmail.com) 

💼 [LinkedIn](https://www.linkedin.com/in/navneet-kumar96/)

🐙 [GitHub](https://github.com/navneet920)
