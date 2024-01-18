import sqlite3
import pandas as pd
import keyboard as key
from tabulate import tabulate

#--------------Database and table names--------------#
db_name = "products.db"
table_name = "products"

#--------------Create table-------------#
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
    conn.commit()

#--------------Print content of product DB--------------#
def print_table_contents(cursor):
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql_query(query, conn)
    print("Products Contents:")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid',
                   numalign="right",stralign="right"))

#--------------Print content of selected product ID--------------#
def print_product_content_byID(cursor, id):
    query = f'SELECT * FROM {table_name} WHERE id=?'
    df = pd.read_sql_query(query, conn,params=(id,))
    print(f"Product Information of ID[{id}] :")
    print(df)

#--------------SQL manipulation of data base--------------#
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
    conn.commit()

def edit_data(cursor, column_data,id_data, new_name):
    cursor.execute(f'''
        UPDATE {table_name}
        SET {column_data}=?
        WHERE id=?
        ''',(new_name, id_data))
    conn.commit()

def delete_data(cursor, id_data):
    cursor.execute(f'''
        DELETE FROM {table_name}
        WHERE id=?
        ''',(id_data,))
    conn.commit()
    return

#--------------User input/decision board--------------#
def choice_add_another_product():
    choice=input("Continue with another product? (y/n): ").lower()
    return choice
def choice_is_data_correct():
    choice=(input("Is data ok? (True/False): "))
    return choice
def choice_data_operation():
    choice=input("DataBaseManipulation (Add/Import/Delete/Edit/Leave): ").lower()
    return choice
def choice_edit_data_operation():
    choice_id=int(input("Select the ID of the data row: "))
    choice_column=input("Select column data (name, category, img, status,price): ")
    choice_new_input=input("New name/price: ")
    return choice_id, choice_column,choice_new_input
def choice_delete():
    choice=int(input("Select ID of the product you want to delete: "))
    return choice

#--------------User database SQL manipulation--------------#
def add_data_operation():
    while True:
        #Get user input
        product_data=input_product_data()
        print(f"user entry: {product_data}")
        # Add another entry or finish
        user_confirmation = choice_is_data_correct()
        if user_confirmation=="True":
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

def import_from_csv_operation():
    while True:
        #Get user input
        user_csv_file_path=input("CSV file path: ")
        # Add another entry or finish
        user_confirmation = choice_is_data_correct()
        if user_confirmation=="True":
            import_csv_data(cursor, table_name, user_csv_file_path)
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
        if user_confirmation=="True":
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
        product_id=choice_delete()
        print(f"user entry: {product_id}")
        print_product_content_byID(cursor, product_id)
        # Add another entry or finish
        user_confirmation = choice_is_data_correct()
        if user_confirmation=="True":
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

#--------------Import CSV data--------------#
def import_csv_data(cursor, table_name, csv_file_path):
    csv_data=pd.read_csv(csv_file_path)
    for index,row in csv_data.iterrows():
        name, category, price, color, img, status = row['name'], row['category'], float(row['price']), row['color'], row['img'], row['status']
        cursor.execute(f'''
            INSERT INTO {table_name} (name, category, price, color, img, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, category, price, color, img, status))
        conn.commit()
    print("Import Complete")

#--------------Connect to DB--------------#
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
#--------------Create table--------------#
create_table(cursor)

#--------------User board--------------#
while True:
    operation=choice_data_operation()
    if operation=="add":
        print("you choose ADD")
        add_data_operation()
    elif operation=="import":
        print("you choose Import from CSV")
        import_from_csv_operation()
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

#--------------Finalize connection--------------#
conn.commit()
conn.close()