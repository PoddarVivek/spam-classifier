#  Import libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#  Load dataset
data = pd.read_csv("spam.csv", encoding='latin-1')

#  Keep only useful columns
data = data[['v1', 'v2']]
data.columns = ['label', 'email']

#  Convert labels to numbers
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

#  Split into input (X) and output (y)
X = data['email']
y = data['label']

# Train-Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#  Convert text → numbers
vectorizer = CountVectorizer()

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

#  Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

#  Evaluate model
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test with custom input
test_email = ["login bonus and 99 percent off"]

test_X = vectorizer.transform(test_email)

prediction = model.predict(test_X)
probability = model.predict_proba(test_X)

print("\nTest Email:", test_email[0])
print("Prediction:", "Spam" if prediction[0] == 1 else "Not Spam")
print("Probability [Not Spam, Spam]:", probability)