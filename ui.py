import sqlite3

db = 'product_db.db'

def display_menu_get_choice():
    print('MAKE SELECTION FROM THE MENU')
    '''Display choices for user, return users' selection'''
    print('''

        1. create a database and a table
        2. Add a row of data to the database table
        3. update a row in the database table
        4. Delete a row from the database table
        5. Display all the rows in the database table
        6. Display a single row of data based on an input
        q. Quit

    ''')

    choice = input('Enter your selection: ')

    return choice


conn = sqlite3.connect(db)
cur = conn.cursor()
print ("Opened database successfully\n")

def create_table():

    conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCT
        (ID                     INT    PRIMARY KEY     NOT NULL,
        NAME                    TEXT    NOT NULL,
        DESCRIPTION             TEXT     NOT NULL,
        SIZE                    TEXT,
        UNIT_PRICE              REAL,
        IN_STOCK                INT,
        ON_ORDER                INT)''')

    return

# cur.execute('drop table PRODUCT')

def add_new_product():

    ID = input('Enter product id: ')
    NAME = input('Enter name of product: ')
    DESCRIPTION = input('Enter product description: ')
    SIZE = input('Enter the size: ')
    UNIT_PRICE = input('Enter product unit price: ')
    IN_STOCK = input('Enter the quantity on hand: ')
    ON_ORDER = input('Enter the quantity on order: ')

    create_table()
    conn.execute('INSERT INTO PRODUCT VALUES (?,?,?,?,?,?,?)', (ID, NAME, DESCRIPTION, SIZE, UNIT_PRICE, IN_STOCK, ON_ORDER))
    conn.commit()
    "\n"
    return



def display_all_rows():
    c = cur.execute("SELECT * from PRODUCT")
    for row in c:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("DESCRIPTION = ", row[2])
        print("SIZE = ", row[3])
        print("UNIT_PRICE = ", row[4])
        print("IN_STOCK = ", row[5])
        print("ON_ORDER = ", row[6], "\n")

    print("Operation done successfully\n")

    return

def update_a_row():
    id = input('Enter ID: ')
    price = input('Enter the new price: ')
    create_table()
    c = cur.execute("UPDATE PRODUCT SET UNIT_PRICE = ?  WHERE ID = ?",(price, id) )
    conn.commit()
    return


def delete_a_row():

    id = input('Enter ID ')
    c = cur.execute("DELETE FROM PRODUCT WHERE ID = ?", (id,))

    conn.commit()

def display_a_row():
    id  = input('Enter the ID: ')
    c = cur.execute("SELECT * FROM  PRODUCT WHERE ID = ?", (id,))
    print(c.fetchall())


def message(msg):
    '''Display a message to the user'''
    print(msg)
