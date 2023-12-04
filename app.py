# app.py
from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

server = 'taistytech.database.windows.net'
database = 'TaistyTech'
username = 'dvonderh'
password = '0527Butterfly!'
driver = '{ODBC Driver 17 for SQL Server}'

@app.route("/templates")
def index():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template("login.html")

# Database update route
@app.route("/update-database", methods=['POST'])
def update_database():
    try:
        # Extract the ingredient from the JSON data
        ingredient = request.json.get('ingredient')

        # Connect to the database
        conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()

        # Execute a SQL query to update the database
        cursor.execute(f"INSERT INTO Ingredient (name, quantity) VALUES ('{ingredient}', 1)")
        conn.commit()

        # Close the database connection
        conn.close()

        # Respond with a success message
        return jsonify({'message': 'Ingredient added to the database successfully'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)

