import sqlite3

# Підключення до бази даних
connection = sqlite3.connect("database.sqlite")
cursor = sqlite3.Cursor(connection)

# Видалення старої таблиці (якщо вона існує) для тестування
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS feedback")

# Створення таблиці products, додано нове поле image_name
request = ("CREATE TABLE IF NOT EXISTS products"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255),"
           "price INTEGER,"
           "depth INTEGER,"
           "image_name VARCHAR(255))")
cursor.execute(request)

# Створення таблиці shopping_cart для збереження інформації про товари в корзині
feedback = ("CREATE TABLE IF NOT EXISTS feedback"
                        "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "text VARCHAR(255),"
                        "stars INTEGER)")
cursor.execute(feedback)

# Вставка даних у таблицю products з новим полем image_name
insert_request = ("INSERT INTO products"
                  "(name, description, price, depth, image_name) VALUES (?, ?, ?, ?, ?)")

cursor.execute(insert_request, ("бассейн 1", "Цей чудовий басейн ідеально підійде для вашого подвір'я, створюючи комфортне місце для відпочинку в спекотні дні.", "$200", "2m", "images (2).jpg"))
cursor.execute(insert_request, ("бассейн 2", "Цим басейном ви отримаєте можливість насолоджуватися водними розвагами разом з родиною та друзями!", "$400", "2m", "форма 2.jpg"))
cursor.execute(insert_request, ("бассейн 3", "Цей стильний басейн стане яскравим акцентом у вашому саду та додасть елегантності вашому простору.", "$600", "2m", "Форма 3.png"))
cursor.execute(insert_request, ("бассейн 4", "Ідеальний вибір для великих сімей, цей басейн дозволяє проводити час на воді весело і безпечно.", "$1200", "2m", "pool 4.jpg"))
cursor.execute(insert_request, ("бассейн 5", "Насолоджуйтеся розкішшю та комфортом з цим басейном, що ідеально підходить для розваг в літній сезон.", "$1600", "2m", "pool 5.webp"))
cursor.execute(insert_request, ("бассейн 6", "Відмінний вибір для тих, хто хоче створити ідеальне місце для відпочинку на свіжому повітрі.", "$3200", "2m", "pool 6.jpg"))

insert_request = ("INSERT INTO feedback"
                  "(text, stars) VALUES (?, ?)")

cursor.execute(insert_request, ("Чудовий сервіс! Басейн виявився ідеальним для нашої сім'ї.", "5"))
cursor.execute(insert_request, ("Дуже задоволені покупкою, все як описано.", "4"))
cursor.execute(insert_request, ("Басейн був доставлений вчасно. Рекомендуємо!", "5"))
cursor.execute(insert_request, ("Дякую за чудовий продукт і швидке обслуговування!", "5"))
cursor.execute(insert_request, ("Прекрасний досвід! Басейн став улюбленим місцем нашої родини.", "5"))

# Виведення всіх товарів з таблиці products
text = cursor.execute("SELECT * FROM products")
print("Товари в базі даних:")
for line in text.fetchall():
    print(line)

# Виведення всіх товарів в кошику
cart_items = cursor.execute("SELECT * FROM feedback")
print("\nТовари в кошику:")
for item in cart_items.fetchall():
    print(item)

# Збереження змін та закриття з'єднання
connection.commit()
connection.close()
