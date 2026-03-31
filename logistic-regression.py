import pandas as pd
from sklearn.linear_model import LogisticRegression
# Sample dataset (binary classification)
# X represents features, y represents labels (0 or 1)
X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]
# Train logistic regression model
model = LogisticRegression().fit(X, y)
# Make a prediction
prediction = model.predict([[5]])[0]
probability = model.predict_proba([[5]])[0]
print("Prediction for 5:", prediction)
print("Probability distribution:", probability)