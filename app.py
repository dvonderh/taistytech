# app.py
from flask import Flask, render_template, request, jsonify
from edemam import *
from collections import defaultdict

app = Flask(__name__)

ingredients = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
        if ingredient not in ingredients and ingredient != '':
            ingredients.append(ingredient)
 
    return render_template("index.html", ingredient_list=ingredients)


@app.route("/get_ingredients", methods=["GET"])
def get_ingredients():
    if ingredients != []:
        return jsonify({'ingredients': ingredients})

@app.route('/my-link', methods=["POST"])
def findRecipes():
    count = defaultdict(int)
    for i in ingredients:
        recipe = search_recipes(i)
        for j in recipe:
            count[j['recipe']['label']] += 1

    final = []
    for i in count:
        if count[i] == len(ingredients):
            final.append(i)

    for i in final:
        recipe = search_recipes(i) 



if __name__ == "__main__":
    app.run(debug=True)

