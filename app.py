# app.py
from flask import Flask, render_template, request, jsonify
#from edemam import *

app = Flask(__name__)

ingredients = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
        if ingredient not in ingredients:
            ingredients.append(ingredient)
 
    return render_template("index.html", ingredient_list=ingredients)


@app.route("/get_ingredients", methods=["GET"])
def get_ingredients():
    if ingredients != []:
        return jsonify({'ingredients': ingredients})

@app.route('/my-link/')
def my_link():
    print ('I got clicked!')
    return 'Click.' 

if __name__ == "__main__":
    app.run(debug=True)

