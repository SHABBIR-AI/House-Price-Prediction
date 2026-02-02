import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Simple dataset
data = {
    "area": [800, 1000, 1200, 1500, 1800],
    "bedrooms": [1, 2, 2, 3, 3],
    "price": [40, 55, 65, 85, 95]  # price in lakhs
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
print("Model saved")
