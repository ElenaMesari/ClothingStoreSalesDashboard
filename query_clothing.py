import pandas as pd
import sqlite3

 
conn = sqlite3.connect('clothing_sales.db')

 
query = """
SELECT year, category, product_name, sales, price, inventory, (sales * price) AS total_sales_value
FROM sales
WHERE category IN ('T-shirts', 'Jeans', 'Jackets')
AND year BETWEEN 2020 AND 2022
ORDER BY year DESC;
"""

df = pd.read_sql(query, conn)

conn.close()

print(df)
