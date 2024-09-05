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