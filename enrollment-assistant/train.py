"""Train the intent classifier: TF-IDF + Logistic Regression, 80/20 split."""
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

df = pd.read_csv("intents.csv")
X_train, X_test, y_train, y_test = train_test_split(
    df["question"], df["category"], test_size=0.2, random_state=42, stratify=df["category"]
)

model = make_pipeline(
    TfidfVectorizer(lowercase=True, ngram_range=(1, 2)),
    LogisticRegression(max_iter=1000),
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
labels = sorted(df["category"].unique())
print(f"Accuracy: {accuracy_score(y_test, pred):.2f}")
print("Labels:", labels)
print(confusion_matrix(y_test, pred, labels=labels))

# Refit on all data before saving so the deployed model sees every example.
model.fit(df["question"], df["category"])
joblib.dump(model, "model/intent_model.joblib")
print("Saved model/intent_model.joblib")
