import sqlite3

 
conn = sqlite3.connect('clothing_sales.db')

 
cursor = conn.cursor()
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    year INTEGER,
    sales INTEGER,
    price REAL,
    inventory INTEGER
);
""")

 
sales_data = [
    ('T-shirt A', 'T-shirts', 2020, 150000, 19.99, 500),  
    ('T-shirt B', 'T-shirts', 2020, 120000, 22.50, 600),
    ('Jeans A', 'Jeans', 2020, 180000, 49.99, 400),
    ('Jeans B', 'Jeans', 2021, 200000, 55.00, 450),
    ('Jacket A', 'Jackets', 2021, 170000, 79.99, 350),
    ('Jacket B', 'Jackets', 2021, 210000, 89.99, 300),
    ('T-shirt C', 'T-shirts', 2021, 140000, 21.00, 550),
    ('Jeans C', 'Jeans', 2022, 220000, 52.50, 420),
    ('Jacket C', 'Jackets', 2022, 230000, 95.00, 280),
    ('T-shirt D', 'T-shirts', 2022, 160000, 18.99, 600),
]

cursor.executemany("""
INSERT INTO sales (product_name, category, year, sales, price, inventory) VALUES (?, ?, ?, ?, ?, ?)
""", sales_data)


conn.commit()


conn.close()

print("Clothing store sales, price, and inventory database created and sample data inserted!")
