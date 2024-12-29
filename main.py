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

@app.route("/")
def index():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    cards = cursor.execute("SELECT * FROM feedback").fetchall()
    connection.close()
    return render_template('index.html', feedback=cards)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/order")
def order():
    return render_template('order.html')

# Страница для оставления отзыва
@app.route('/leave_feedback')
def leave_feedback():
    return render_template('leave_feedback.html')

# Обработка формы для оставления отзыва
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form['feedback']
    rating = int(request.form['rating'])
    # Логика сохранения отзыва в базу данных или список
    print(f"Отзыв: {feedback}, Оценка: {rating}")
    return redirect(url_for('index'))


app.run(debug=True)