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
        
# Display employee function
def display_emp():
    print("{:>60}".format("===> Display Employee Record <==="))
    # Selecting all rows from database table
    sql = 'SELECT * FROM employee_database'
    c = connection.cursor()
    c.execute(sql)
    
    # Fetching
    table = c.fetchall()
    for record in table:
        print("Employee ID:", record[0])
        print("Employee Name:", record[1])
        print("Employee Email:", record[2])
        print("Employee Phone Number:", record[3])
        print("Employee Address:", record[4])
        print("Employee Position:", record[5])
        print("Employee Pay:", record[6])
        print("Employee Tip%:", record[7])
        print("\n")
        
# Update employee record function
def update_emp():
    print("{:>60}".format("===> Update Employee Record <==="))
    # Asking for employee ID or Name 
    emp = input("Enter employee ID or employee Name")
    if emp.isdigit():
        empID = int(emp)
        sql = "SELECT * FROM employee_database WHERE EmpID = %s"
    elif not emp.isdigit():
        empName = emp
        sql = "SELECT * FROM employee_database WHERE Name = %s"
    else:
        print("No employee found with that ID or Name.")
        return
        
    print("\n")
    print("Choose the field to update:")
    print("1. Name")
    print("2. Email")
    print("3. Phone Number")
    print("4. Address")
    print("5. Position")
    print("6. Pay")
    print("7. Tip Percentage")
    choice = input("Enter the number of the field you want to update: ")

    # Initialize an update query and execute based on the choice
    if choice == '1':
        data = input("Enter new Name: ")
        sql = "UPDATE employee_database SET Name = %s WHERE EmpID = %s" if emp.isdigit() else "UPDATE employee_database SET Name = %s WHERE Name = %s"
    elif choice == '2':
        data = input("Enter new Email: ")
        sql = "UPDATE employee_database SET Email = %s WHERE EmpID = %s" if emp.isdigit() else "UPDATE employee_database SET Email = %s WHERE Name = %s"
    elif choice == '3':
        data = input("Enter new Phone Number: ")
        sql = "UPDATE employee_database SET PhoneNum = %s WHERE EmpID = %s" if emp.isdigit() else "UPDATE employee_database SET PhoneNum = %s WHERE Name = %s"
    elif choice == '4':
        data = input("Enter new Address: ")
        sql = "UPDATE employee_database SET Address = %s WHERE EmpID = %s" if emp.isdigit() else "UPDATE employee_database SET Address = %s WHERE Name = %s"
    elif choice == '5':
        data = input("Enter new Position: ")
        sql = "UPDATE employee_database SET Position = %s WHERE EmpID = %s" if emp.isdigit() else "UPDATE employee_database SET Position = %s WHERE Name = %s"
    elif choice == '6':
        data = input("Enter new Pay: ")
        sql = "UPDATE employee_database SET Pay = %s WHERE EmpID = %s" if emp.isdigit() else "UPDATE employee_database SET Pay = %s WHERE Name = %s"
    elif choice == '7':
        data = input("Enter new Tip Percentage: ")
        sql = "UPDATE employee_database SET TipPerc = %s WHERE EmpID = %s" if emp.isdigit() else "UPDATE employee_database SET TipPerc = %s WHERE Name = %s"
    else:
        print("Invalid choice. Try again.")
        return

    # UpdTING employee record with new data
    c.execute(sql, (data, empID if emp.isdigit() else empName))
    connection.commit()
    
    print("Employee record updated successfully.")
    
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
        display_emp()
    elif ans == '3':
        system("cls")
        # Call update function
        update_emp()
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