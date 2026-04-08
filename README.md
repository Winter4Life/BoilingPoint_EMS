# Employee Management System

A command-line Employee Management System (EMS) built with Python and MySQL, designed to manage employee records for a restaurant or food service business.

---

## Overview

BoilingPoint EMS allows users to add, view, update, delete, and search employee records stored in a MySQL database. The system is built with a simple menu-driven interface and uses environment variables to securely manage database credentials.

---

## Technologies Used

- **Python** – Core application logic
- **MySQL** – Relational database for storing employee records
- **mysql-connector-python** – Python library for MySQL connectivity
- **Environment Variables** – Secure credential management via `os.getenv()`

---

## Features

- **Add Employee** – Input and confirm new employee records before saving
- **Display All Employees** – View every employee record in the database
- **Update Employee Record** – Search by ID or name, then update any field
- **Delete Employee** – Remove a record by employee ID or name
- **Search Employee** – Look up a specific employee by ID or name

---

## Usage

Once running, a menu will appear with the following options:

```
===========> Employee Management System <===========
1. Add Employee
2. Display Employee Record
3. Update Employee Record
4. Delete Employee
5. Search Employee Database
6. Exit
```

Enter the corresponding number to navigate the system. When searching, updating, or deleting, you can look up employees by either their **Employee ID** or **Name**.

---

## Security Note

Database credentials are stored as environment variables and never hardcoded in the source. Make sure to configure `DB_HOST`, `DB_USER`, and `DB_PASS` before running the application.

---

