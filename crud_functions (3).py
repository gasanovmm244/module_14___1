import sqlite3

connect = sqlite3.connect("database.db")
curs = connect.cursor()


def initiate_db():
    curs.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT
    )
    ''')
    connect.commit()

products_data = [
    ('1', 'Product 1', 'Солгар натуральный растительный комплекс', '2139р'),
    ('2', 'Product 2', 'Солгар комплекс мультивитаминов', '2596р'),
    ('3', 'Product 3', 'Солгар витамин C 500 mg', '1145 р'),
    ('4', 'Product 4', 'Солгар MULTI-ONE', '1888р')
]

#
# curs.executemany('INSERT INTO Products VALUES(?,?,?,?)',products_data)


def get_all_products():
    curs.execute("SELECT * FROM Products")
    return curs.fetchall()

