# app.py
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        mydb = mysql.conector.connect(
            host = "localhost",
            user = "dvonderh",
            password = "goirish",
            database = "dvonderh"
        )

        ingredient = request.form["ingredient"]
        mycursor = mydb.cursor()
        query = 'insert into ingredients (user, ingredient, availability) values (%s, %s, %s)'
        mycursor.execute(query, ('dvonderh', ingredient, True))
        mydb.commit()
        mydb.close() 
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

