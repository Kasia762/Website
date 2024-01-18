import sqlite3
import pandas as pd

def createTable(cursor):
    cursor.execute('''
        CREATE TABLE products(
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price NUMERIC,
            color TEXT,
            img TEXT,
            status TEXT
        )''')
    
def loadDataFromCSV(cursor):
    csvdata.to_sql('products', connect, 
                   if_exists='append', index=False)
    
def add_ids_to_null_ids(cursor):
    # Update rows with null id to have a unique id
    cursor.execute('''
        UPDATE products
        SET id = (SELECT MAX(id) FROM products) + ROWID
        WHERE id IS NULL
    ''')


def insertNewData(table):
    return
def tableState(table, cursor):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
    result = cursor.fetchone()
    return result is None
def insertData(table):
    col=csvdata.columns.tolist()
    print(f"column names {col}")


    for index, row in csvdata.iterrows():
        print(f"csv file, {row}, rowid {row[index]}")
        # Extract values from the current row
        id,name,category,price,color,img,status = col["id"],
        row['name'],row['category'],row['price'],
        row['color'],row['img'],row['status']
        # Use placeholders to avoid SQL injection
        cursor.execute('''
            INSERT INTO products (id,name,category,price,color,img,status)
            VALUES (?,?,?,?,?,?,?)
        ''', (id,name,category,price,color,img,status))

    print("Data from CSV has been inserted into the table.")



#Connect to SQL DB
connect = sqlite3.connect("productsDB.db")
cursor = connect.cursor()
#Read CSV
csvdata=pd.read_csv("products.csv", delimiter='\t')

#Check if a table 'productsDB' exists
table = 'productsDB'
tableExistStatus = tableState(table,cursor)
print(f"table state {tableExistStatus}")

if tableExistStatus:
    print(f"The table '{table}' exists.")
    insertData(table)

elif tableExistStatus is False:
    createTable(cursor)
    print(f"The table '{table}' does not exist.")
else: raise KeyError

#insert unique id
def add_ids_to_null_ids(cursor):
    # Update rows with null id to have a unique id
    cursor.execute('''
        UPDATE products
        SET id = (SELECT MAX(id) FROM products) + ROWID
        WHERE id IS NULL
    ''')    
add_ids_to_null_ids(cursor)

####READ SQL FILE#####
# Execute a simple SELECT query to fetch all rows from the 'products' table
query = 'SELECT * FROM products'
df = pd.read_sql_query(query, connect)

# Print the DataFrame
print(df)

connect.commit()
connect.close()