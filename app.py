# app.py
from flask import Flask, render_template, request, jsonify
import mysql.connector
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key='dvonderh'
app.config['MYSQL_HOST'] = 'db8.cse.nd.edu'
app.config['MYSQL_USER'] = 'dvonderh'
app.config['MYSQL_PASSWORD'] = 'goirish'
app.config['MYSQL_DB'] = 'dvonderh'

mysql = MYSQL(app)

@app.route("/")
def home():
    return render_template("index.html")

def insert_ingredient(ingredient):
    try:
        cursor = mysql.connection.cursor()
        query = "INSERT INTO ingredients (user, ingredient, availability) VALUES (%s, %s, %s)"
        cursor.execute(query, ('dvonderh', ingredient, True))
        mysql.connection.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()

@app.route("/add_ingredient", methods=['POST'])
def add_ingredient():
    if request.method == 'POST':
        ingredient = request.form['ingredients']
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

