'''
Repeat prog8b(fetchmany) but validate input
i.e. Print a msg when input > number of tuples

Hint: Use fetchmany() method
'''
import sqlite3

try:
    con = sqlite3.connect('employee.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM emp")
    all_data = cursor.fetchall()
    total_rows = len(all_data)

    n = int(input("How many rows ? : "))
    
    if n <= 0 or n > total_rows:
        print("Invalid input")
    else:
        cursor.execute("SELECT * FROM emp")
        rows = cursor.fetchmany(n)
        
        print(f"{'empno':<10} {'ename':<15} {'sal':<10}")
        for row in rows:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
        
        print(f"Number of rows : {len(rows)}")

except Exception as e:
    print("Error:", e)

finally:
    if con:
        con.close()
        


#2
# Write a program to insert multiple rows into emp table
import mysql.connector
def insert_employees():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        cursor = conn.cursor()
        try:
            num_rows = int(input("How many rows would you like to insert?: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        for i in range(1, num_rows + 1):
            print(f"Employee : {i}")
            emp_no = input("Enter employee number: ")
            name = input("Enter employee name: ")
            salary = input("Enter salary: ")

            query = "INSERT INTO emp (emp_no, name, salary) VALUES (%s, %s, %s)"
            
            try:
                cursor.execute(query, (emp_no, name, salary))
                conn.commit()
                print("Row inserted successfully.")
            except mysql.connector.Error as err:
                print(f"Error for employee {emp_no}: {err}")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")

insert_employees()