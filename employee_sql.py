import mysql.connector

# Global variable
con = mysql.connector.connect(host='localhost', database='sample', user='root', password='')


def add_employee():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email_address = input("Enter email address: ")
    query = "INSERT INTO test_py (`first_name`, `last_name`, `email_address`) VALUES ('" + first_name + "', '" + last_name + "', '" + email_address + "')"
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    cur.close()
    print("Successfully Inserted Record!")


def view_employee():
    print("'View_all' to view all record\n'View_id' to view record by id")
    print("----------------------------------------")
    view_choice = input("View_all or View_id: ")
    if view_choice == "View_all" or view_choice == "view_all":
        query = "SELECT * FROM test_py"
        cur = con.cursor()
        cur.execute(query)
        records = cur.fetchall()
        print("Number of records in the table: ", cur.rowcount)
        for row in records:
            print("ID : ", row[0])
            print("First name : ", row[1])
            print("Last name : ", row[2])
            print("Email address: ", row[3])
            print("----------------------")
    elif view_choice == "View_id" or view_choice == "view_id":
        view_id = input("Enter id: ")
        query = "SELECT * FROM test_py WHERE ID = '" + view_id + "'"
        cur = con.cursor()
        cur.execute(query)
        record = cur.fetchone()
        print(record)
        print("--------------------------")
    else:
        print("Incorrect keyword")


def update_employee():
    user_id = input("Enter ID: ")
    # Before update
    select_query = "SELECT * FROM test_py WHERE ID = '" + user_id + "'"
    cur = con.cursor()
    cur.execute(select_query)
    record = cur.fetchone()
    print(record)
    # update
    update_firstname = input("Update first name: ")
    update_lastname = input("Update last name: ")
    update_emailadd = input("Update email address: ")
    print("----------------------------------------")
    update_query = "UPDATE test_py SET first_name ='" + update_firstname + "', last_name='" + update_lastname + "', email_address ='" + update_emailadd + "' WHERE ID= '" + user_id + "'"
    cur.execute(update_query)
    con.commit()
    print("Successfully Update Record")
    print("----------------------------------------")
    print("Data after update:")
    cur.execute(select_query)
    record = cur.fetchone()
    print(record)
    print("----------------------------------------")


def delete_employee():
    query = "SELECT * FROM test_py"
    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print("Number of records in the table: ", cur.rowcount)
    for row in records:
        print("ID : ", row[0])
        print("First name : ", row[1])
        print("Last name : ", row[2])
        print("Email address: ", row[3])
        print("----------------------")
    del_id = input("Enter id number to delete: ")
    del_query = "DELETE FROM test_py WHERE ID = '" + del_id + "'"
    cur.execute(del_query)
    con.commit()
    print("Successfully Deleted Record")


while True:
    print("'Insert' keyword for inserting data\n'View' keyword for viewing data\n'Update' keyword for updating the record\n'Delete' keyword for deleting the record")
    print("----------------------------------------")
    keyword = input("Enter keyword: ")
    print("----------------------------------------")
    if keyword == "Insert" or keyword == "insert":
        add_employee()
    elif keyword == "View" or keyword == "view":
        view_employee()
    elif keyword == "Update" or keyword == "update":
        update_employee()
    elif keyword == "Delete" or keyword == "delete":
        delete_employee()
    else:
        print("Incorrect keyword")

    choice = input("Enter Y to continue or N to stop: ")
    print("----------------------------------------")
    if choice == "Y" or choice == "y":
        pass
    else:
        break
