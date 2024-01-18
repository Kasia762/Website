import sqlite3
import pandas as pd

table_name = "products"

def createTable(cursor, table_name):
    cursor.execute(f'''
        CREATE TABLE {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price NUMERIC,
            color TEXT,
            img TEXT,
            status TEXT
        )''')

def add_ids_to_null_ids(cursor, table_name):
    # Update rows with null id to have a unique id
    cursor.execute(f'''
        UPDATE {table_name}
        SET id = (SELECT MAX(id) FROM {table_name}) + ROWID
        WHERE id IS NULL
    ''')

def tableState(cursor, table_name):
    cursor.execute(f'''
        SELECT name FROM sqlite_master 
        WHERE type='table' 
        AND name='{table_name}'
    ''')
    result = cursor.fetchone()
    return result is None

# Connect to SQL DB
connect = sqlite3.connect(f"{table_name}.db")
cursor = connect.cursor()

# Check if a table {table_name} exists
tableExistStatus = tableState(cursor, table_name)

if tableExistStatus:
    print(f"The table '{table_name}' exists.")
elif tableExistStatus is False:
    createTable(cursor, table_name)
    print(f"The table '{table_name}' does not exist.")
else:
    raise KeyError

# Input data
def inputData(table_name):
    '''
    name = input("Enter the name: ")
    category = input("Enter the category: ")
    price = float(input("Enter the price: "))
    color = input("Enter the color: ")
    img = input("Enter the image name: ")
    status = input("Enter the status: ")'''
    # Sample data
    name = "Sample Product"
    category = "Sample Category"
    price = 19.99
    color = "Blue"
    img = "sample_image.jpg"
    status = "In Stock"
    # Use placeholders to avoid SQL injection
    cursor.execute(f'''
        INSERT INTO {table_name} (name, category, price, color, img, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, category, price, color, img, status))
    print(f"Data has been inserted into the '{table_name}' table.")
    connect.commit()

#inputData(table_name)
# Sample data
name = "Sample Product"
category = "Sample Category"
price = 19.99
color = "Blue"
img = "sample_image.jpg"
status = "In Stock"
# Use placeholders to avoid SQL injection
cursor.execute(f'''
    INSERT INTO {table_name} (name, category, price, color, img, status)
    VALUES (?, ?, ?, ?, ?, ?)
''', (name, category, price, color, img, status))
print(f"Data has been inserted into the '{table_name}' table.")
connect.commit()


# Insert unique id
add_ids_to_null_ids(cursor)

# Read SQL data
query = f'SELECT * FROM {table_name}'
df = pd.read_sql_query(query, connect)

# Print the DataFrame
print(df)

connect.commit()
connect.close()
