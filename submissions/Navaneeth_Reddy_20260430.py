# Write a program to insert multiple rows into emp table
import mysql.connector
def insert_employees():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
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