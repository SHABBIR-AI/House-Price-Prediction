from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])

    price = model.predict([[area, bedrooms]])[0]
    price = round(price, 2)

    return render_template(
        "index.html",
        prediction=f"Estimated House Price: ₹ {price} Lakhs"
    )

if __name__ == "__main__":
    app.run(debug=True)
