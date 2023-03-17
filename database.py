import sqlite3

#  Таблица пользователей
def create_users_table():
    database = sqlite3.connect('nice_snacks.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT 
    );
    ''')
    database.commit()
    database.close()


# Таблица карточки
def create_carts_table():
    database = sqlite3.connect('nice_snacks.db')
    cursor = database.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carts(
            cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES users(user_id),
            total_price DECIMAL(12, 2) DEFAULT 0,
            total_products INTEGER DEFAULT 0
        );
        ''')
    database.commit()
    database.close()


def create_cart_products_table():
    database = sqlite3.connect('nice_snacks.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart_products(
        cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cart_id INTEGER REFERENCES carts(cart_id),
        product_name VARCHAR(50) NOT NULL,
        quantity INTEGER NOT NULL,
        final_price DECIMAL(12, 2) NOT NULL,

        UNIQUE(cart_id, product_name)    
        );
    ''')
    database.commit()
    database.close()


#create_cart_products_table()
#create_carts_table()
#create_users_table()

def create_categories_table():
    database = sqlite3.connect('nice_snacks.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name VARCHAR(20) NOT NULL UNIQUE
    );
    ''')
    database.commit()
    database.close()



def insert_categories():
    database = sqlite3.connect('nice_snacks.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO categories(category_name) VALUES
    ('Лаваши'),
    ('Бургеры'),
    ('Кебаб'),
    ('Хот-Дог'),
    ('Десерты'),
    ('Напитки');
    ''')
    database.commit()
    database.close()

#create_categories_table()
#insert_categories()



# ______________________________________________



def create_products_table():
    database = sqlite3.connect('nice_snacks.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        product_name VARCHAR(20) NOT NULL UNIQUE,
        price DECIMAL(12, 2) NOT NULL,
        description VARCHAR(100),
        image TEXT,
        
        
        FOREIGN KEY(category_id) REFERENCES categories(category_id)
    );
    ''')
    database.commit()
    database.close()

#create_products_table()





def insert_products_table():
    database = sqlite3.connect('nice_snacks.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO products(category_id, product_name, price, description, image) VALUES
    (1, 'Лаваш говяжий', 25000, 'Мясо, тесто, помидоры, огурчики, чипсы', media/lavash/lavash_1.jpg),
    (1, 'Лаваш говяжий', 25000, 'Мясо, тесто, помидоры, огурчики, чипсы', media/lavash/lavash_2.jpg),
    (1, 'Лаваш говяжий', 25000, 'Мясо, тесто, помидоры, огурчики, чипсы', media/lavash/lavash_3.jpg)
    ''')
    database.commit()
    database.close()