# Employee Management System using Python

from os import system
import sys
# Importing mySQL
import mysql.connector 
# Retrieving hidden credentials to establish connection
import os
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

# Establish the connection
connection = mysql.connector.connect(
    host = db_host,        
    user = db_user,             
    password = db_pass 
)

# Checking if connection is successful
'''
if connection.is_connected():
    print("Connected to MySQL Server successfully")
    cursor = connection.cursor()
    cursor.close()
    connection.close()
    print("MySQL connection closed")

else:
    print("Failed to connect to MySQL Server")
'''

# Creating the Database
'''
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS BoilingPoint_EMS")

# Creating a table for employee information
cursor.execute("USE BoilingPoint_EMS")
cursor.execute("CREATE TABLE Employee_Database (EmpID INT(7) PRIMARY KEY, Name VARCHAR(100), \
    Email TEXT(100), PhoneNum INT(11), Address TEXT(1000), Position TEXT(100), Pay FLOAT(50), TipPerc INT(200))")
'''
c = connection.cursor()
c.execute("USE BoilingPoint_EMS")
#c.execute("ALTER TABLE Employee_Database MODIFY PhoneNum VARCHAR(20);")

# Add employee function
def add_emp():
    while True:
        print("{:>60}".format("===> Add Employee Record <==="))
        EmpID = int(input("Enter Employee ID: "))
        Name = input("Enter Employee Name: ")
        Email = input("Enter Employee Email: ")
        PhoneNum = input("Enter Employee Phone number: ")
        Address = input("Enter Employee Address: ")
        Position = input("Enter Employee Position: ")
        Pay = float(input("Enter Employee Pay: "))
        TipPerc = int(input("Enter Employee Tip%: "))

        # Display written information
        print("\nReview the information you entered:")
        print(f"ID: {EmpID}")
        print(f"Name: {Name}")
        print(f"Email: {Email}")
        print(f"Phone Number: {PhoneNum}")
        print(f"Address: {Address}")
        print(f"Position: {Position}")
        print(f"Pay: {Pay}")
        print(f"Tip%: {TipPerc}")

        # Ask user to confirm information is correct
        choice = input("\nIs the information correct? (yes to confirm, no to edit): ").strip().lower()
        if choice == 'yes':
            print("Information confirmed. Adding employee...")
            # Inserting employee data
            data = (EmpID, Name, Email, PhoneNum, Address, Position, Pay, TipPerc)
            sql = 'INSERT INTO employee_database (EmpID, Name, Email, PhoneNum, Address, Position, Pay, TipPerc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
            try:
                c.execute(sql, data)
                connection.commit()
                print("Successfully Added Employee Record")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            break
        elif choice == 'no':
            print("Let's try again.")
            continue

# Creating a menu to interact with the management system
def menu():
    system("cls")
    print("{:>60}".format("===========> Employee Management System <==========="))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Delete Employee")
    print("5. Search Employee Database")
    print("6. Exit\n")
    print("{:>54}".format("===> Type either: [1/2/3/4/5/6] <==="))
    
    ans = input("Enter number: ")
    if ans == '1':
        system("cls")
        # Call add function
        add_emp()
    elif ans == '2':
        system("cls")
        # Call display function
    elif ans == '3':
        system("cls")
        # Call update function
    elif ans == '4':
        system("cls")
        # Call delete function
    elif ans == '5':
        system("cls")
        # Call search function
    elif ans == '6':
        print("Exiting the program")
        sys.exit()  # Gracefully exit the program
    else:
        print("Unavailable option, try again")
     
# Calling menu
if __name__ == "__main__":
    menu()