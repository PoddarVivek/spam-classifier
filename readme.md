# 📩 Spam Email Classifier (ML + Web App)

## 🚀 Overview

This project is a Machine Learning-based Spam Email Classifier that predicts whether a message is **Spam or Not Spam**.
It is built using **Natural Language Processing (NLP)** techniques and deployed as a **live web application** using Streamlit.

---

## 🌍 Live Demo

👉 https://spam-classifier-h69raytvp9wu9lt7vyhf8m.streamlit.app/

---

## 🧠 Features

* Classifies messages as **Spam or Not Spam**
* Displays prediction **confidence (probability)**
* Simple and interactive **web interface**
* Works on real-world SMS/email data

---

## ⚙️ Tech Stack

* **Python**
* **Pandas** (data handling)
* **Scikit-learn** (ML model)
* **CountVectorizer** (text → numerical features)
* **Multinomial Naive Bayes** (classification model)
* **Streamlit** (web app deployment)

---

## 📊 Workflow

1. Load dataset from CSV file
2. Clean and preprocess data
3. Convert text into numerical vectors (feature extraction)
4. Train model using Naive Bayes
5. Evaluate model using accuracy
6. Deploy model using Streamlit

---

## 📈 Model Performance

* Achieved **~98–99% accuracy** on test data
* Provides **probability-based predictions**

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/spam-classifier.git
cd spam-classifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

### 4. Open in browser

```
http://localhost:8501
```

---

## 🧪 Example

**Input:**

```
Win money now!!!
```

**Output:**

```
Spam (High Confidence)
```

---

## 💡 Key Learnings

* Understanding of **ML pipeline (X, y, training, prediction)**
* Text preprocessing using **CountVectorizer**
* Importance of **data quality in ML**
* Model evaluation using **accuracy**
* Deploying ML models as **web applications**

---

## 📌 Future Improvements

* Use **TF-IDF Vectorizer** for better accuracy
* Save/load trained model for faster performance
* Improve UI/UX of the web app
* Deploy using Docker or cloud platforms

---

## 👨‍💻 Author

**Vivek Poddar**

* BTech (ECE), NIT Kurukshetra
* Aspiring ML & Data Analyst

---

⭐ If you like this project, give it a star!
