import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("spam.csv", encoding='latin-1')
data = data[['v1', 'v2']]
data.columns = ['label', 'email']
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Features
X = data['email']
y = data['label']

# Vectorize
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# UI
st.title("📩 Spam Email Classifier")

user_input = st.text_input("Enter your message:")

if st.button("Check"):
    input_vec = vectorizer.transform([user_input])
    prediction = model.predict(input_vec)
    prob = model.predict_proba(input_vec)

    if prediction[0] == 1:
        st.error(f"Spam ❌ (Confidence: {prob[0][1]:.2f})")
    else:
        st.success(f"Not Spam ✅ (Confidence: {prob[0][0]:.2f})")