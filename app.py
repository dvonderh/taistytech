# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]))
def home():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

