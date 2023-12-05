# app.py
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

ingredients = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
        if ingredient not in ingredients:
            ingredients.append(ingredient)
 
    return render_template("index.html", ingredient_list=ingredients)


if __name__ == "__main__":
    app.run(debug=True)

