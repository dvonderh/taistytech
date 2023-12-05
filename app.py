# app.py
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'db8.cse.nd.edu',
    'user': 'dvonderh',
    'password': 'goirish',
    'database': 'dvonderh',
}

@app.route("/")
def home():
    return render_template("index.html")

def insert_ingredient(ingredient):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO ingredients (user, ingredient, availability) VALUES (%s, %s, %s)"
        cursor.execute(query, ('dvonderh', ingredient, True))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connection.close()

@app.route("/add_ingredient", methods=['POST'])
def add_ingredient():
    ingredient = request.form.get('ingredients')
    if ingredient:
        success = insert_ingredient(ingredient)
        if success:
            return jsonify({'message': 'Ingredient added successfully'})
        else:
            return jsonify({'error': 'Failed to add ingredient'})
    else:
        return jsonify({'error': 'Invalid ingredient'})


if __name__ == "__main__":
    app.run(debug=True)

