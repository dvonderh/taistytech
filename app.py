# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_ingr", methods['GET', 'POST'])
def add_ingr():
    if requests.method == 'POST':
        ingredient = request.form['ingredient']

if __name__ == "__main__":
    app.run(debug=True)

