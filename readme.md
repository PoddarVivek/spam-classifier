# 📩 Spam Email Classifier (ML + Web App)

## 🚀 Overview

This project is a Machine Learning-based Spam Email Classifier built using Python and deployed as a web app using Streamlit.

## 🧠 Features

* Classifies messages as Spam or Not Spam
* Displays prediction probability
* Simple interactive UI

## ⚙️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

## 📊 Workflow

1. Load dataset
2. Clean and preprocess data
3. Convert text to numerical features (CountVectorizer)
4. Train model using Naive Bayes
5. Deploy using Streamlit

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🎯 Example

Input: "Win money now"
Output: Spam (High confidence)

## 💡 Learnings

* NLP basics (text vectorization)
* Machine learning pipeline
* Model deployment using Streamlit
