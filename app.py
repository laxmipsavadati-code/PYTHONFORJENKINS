from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = [
        {"name": "Laxmi", "age": 21},
        {"name": "Shivu", "age": 18},
        {"name": "Ganga", "age": 38},
        {"name": "Siddu", "age": 11}
    ]
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)