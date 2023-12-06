# app.py
from flask import Flask, render_template, request, jsonify
from edemam import search_recipes

app = Flask(__name__)

ingredients = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
        if ingredient not in ingredients and ingredient != '':
            ingredients.append(ingredient)

    return render_template("index.html", ingredient_list=ingredients)


@app.route("/get_ingredients", methods=["GET"])
def get_ingredients():
    if ingredients != []:
        return jsonify({'ingredients': ingredients})

@app.route("/find_recipes", methods=["GET"])
def find_recipes():
    recipes=search_recipes(ingredients)
    return jsonify({'recipes': recipes})

if __name__ == '__main__':
    app.run(debug=True)
