import sqlite3
import pandas as pd
import keyboard as key
from tabulate import tabulate

# Database and table information
db_name = "products.db"
table_name = "products"

# Function to create the table if it doesn't exist
def create_table(cursor):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price NUMERIC,
            color TEXT,
            img TEXT,
            status TEXT
        )''')

# Function to insert sample data into the table
def insert_sample_data(cursor):
    cursor.execute(f'''
        INSERT INTO {table_name} (name, category, price, color, img, status)
        VALUES 
        ('Pink Midi Dress', 'Dress', 48.50, 'Pink', 'pinkmididress.jpg', 'Online'),
        ('Dark Red Heels', 'Shoes', 39.99, 'Red', 'darkredshoes.jpg', 'Offline'),
        ('Black Leather Jacket', 'Jacket', 119.99, 'Black', 'blackleatherjacket.jpg', 'Online')
        ''')

# Function to print the contents of the table
def print_table_contents(cursor):
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql_query(query, conn)
    print("Products Contents:")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid',
                   numalign="right",stralign="right"))

# Function to print the contents of the product
def print_product_content_byID(cursor, id):
    query = f'SELECT * FROM {table_name} WHERE id=?'
    df = pd.read_sql_query(query, conn,params=(id,))
    print(f"Product Information of ID[{id}] :")
    print(df)

def input_product_data():
    name = input("Enter the name: ")
    category = input("Enter the category: ")
    price = float(input("Enter the price: "))
    color = input("Enter the color: ")
    img = input("Enter the image name: ")
    status = input("Enter the status: ")
    return name,category,price,color,img,status

def insert_data(cursor, product_data):
    cursor.execute(f'''
        INSERT INTO {table_name} (name, category, price, color, img, status)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', product_data)
def edit_data(cursor, column_data,id_data, new_name):
    cursor.execute(f'''
        UPDATE {table_name}
        SET {column_data}=?
        WHERE id=?
        ''',(new_name, id_data))
def delete_data(cursor, id_data):
    cursor.execute(f'''
        DELETE FROM {table_name}
        WHERE id=?
        ''',(id_data))
    return

def choice_add_another_product():
    choice=input("Continue with another product? (y/n): ").lower()
    return choice
def choice_is_data_correct():
    choice=input("Is data ok? (True/False): ")
    return choice
def choice_data_operation():
    choice=input("Add or delete or edit data? (Add/Delete/Edit/Leave): ").lower()
    return choice
def choice_edit_data_operation():
    choice_id=int(input("Select the ID of the data row: "))
    choice_column=input("Select column data (name, category, img, status,price): ")
    choice_new_input=input("New name/price: ")
    return choice_id, choice_column,choice_new_input
def choice_delete():
    choice=int(input("Select ID of the product you want to delete: "))
    return choice

def add_data_operation():
    while True:
        #Get user input
        product_data=input_product_data()
        print(f"user entry: {product_data}")
        # Add another entry or finish
        user_confirmation = choice_is_data_correct()
        if user_confirmation:
            insert_data(cursor,product_data)
            # Add another entry or finish
            user_choice = choice_add_another_product()
            if user_choice != 'y':
                break
        else:
            print("Aborted")
            # Add another entry or finish
            user_choice = choice_add_another_product()
            if user_choice != 'y':
                break

def edit_data_operation():
    while True:
        print_table_contents(cursor)
        #Get user input
        product_data=choice_edit_data_operation()
        id, col, new=product_data
        print(f"user entry: {product_data}")
        # Add another entry or finish
        user_confirmation = choice_is_data_correct()
        if user_confirmation:
            edit_data(cursor,col, id, new)
            # Add another entry or finish
            user_choice = choice_add_another_product()
            if user_choice != 'y':
                break
        else:
            print("Aborted")
            # Edit another or finish
            user_choice = choice_add_another_product()
            if user_choice != 'y':
                break

def delete_data_operation():
    while True:
        print_table_contents(cursor)
        #Get user input
        product_id=choice_edit_data_operation()
        print(f"user entry: {product_id}")
        print_product_content_byID(cursor, product_id)
        # Add another entry or finish
        user_confirmation = choice_is_data_correct()
        if user_confirmation:
            delete_data(cursor,product_id)
            #Delete another entry or finish
            user_choice = choice_add_another_product()
            if user_choice != 'y':
                break
        else: 
            print("Aborted")
            # Delete another or finish
            user_choice = choice_add_another_product()
            if user_choice != 'y':
                break
def go_to_menu():
    print("Pres 'Esc' to go back to menu")
    key.wait('esc')

# Connect to the database
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Create the table if it doesn't exist
create_table(cursor)

while True:
    operation=choice_data_operation()
    if operation=="add":
        print("you choose ADD")
        add_data_operation()
    elif operation=="edit":
        print("you choose EDIT")
        edit_data_operation()
    elif operation=="delete":
        print("you choose DELETE")
        delete_data_operation()
    elif operation=="view":
        print("you choose VIEW")
        print_table_contents(cursor)
        go_to_menu()
    elif operation=="leave":
        break
    else: 
        print("Select right operation")

#insert_sample_data(cursor)

# Commit changes and close the connection
conn.commit()
conn.close()
