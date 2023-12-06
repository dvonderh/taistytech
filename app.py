# app.py
from flask import Flask, render_template, request, jsonify
from edemam import search_recipes

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
    return jsonify({'ingredients': ingredients})

@app.route("/get_recipies", methods=["GET", "POST"])
def get_recipes():
    if request.method == "POST":
        recipes = request.form.get("recipe")
        for i in ingredients:
            recipes = search_recipes(i)
    

if __name__ == "__main__":
    app.run(debug=True)

