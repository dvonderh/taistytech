# app.py
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key='dvonderh'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dvonderh'
app.config['MYSQL_PASSWORD'] = 'goirish'
app.config['MYSQL_DB'] = 'dvonderh'

mysql = MYSQL(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
        cursor = mysql.connection.cursor()
        query = 'insert into ingredients (user, ingredient, availability) values (%s, %s, %s)'
        cursor.execute(query, ('dvonderh', ingredient, True))
        mysql.connectoin.commit()
        cursor.close()
        
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

