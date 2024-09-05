# Employee Management System using Python

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
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS BoilingPoint_EMS")

# Creating a table for employee information
cursor.execute("USE BoilingPoint_EMS")
cursor.execute("CREATE TABLE Employee_Database (EmpID INT(7) PRIMARY KEY, Name VARCHAR(100), \
    Email TEXT(100), PhoneNum INT(11), Address TEXT(1000), Position TEXT(100), Pay FLOAT(50), TipPerc INT(200))")