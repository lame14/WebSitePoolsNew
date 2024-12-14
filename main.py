from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/products")
def products():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    cards = cursor.execute("SELECT * FROM products").fetchall()
    connection.close()
    print(cards)
    return render_template('products_new.html', products=cards)

app.run(debug=True)