# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def home():
    if requests.method == 'POST':
        ingredient = request.form['ingredient']
        
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

