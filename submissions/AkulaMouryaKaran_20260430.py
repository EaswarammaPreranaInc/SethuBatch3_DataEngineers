import mysql.connector
import os

def insert_multiple_emp():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="student",     
            password="Student@123,
            database="studentdb"
        )
        
        cursor = conn.cursor()


        n = int(input("How many rows would you like to insert? : "))
        
        employees = []
        for i in range(1, n + 1):
            print(f"Employee : {i}")
            empno = int(input("Enter employee number : "))
            ename = input("Enter employee name : ")
            sal = float(input("Enter salary : "))
            
            # Appending data as a tuple
            employees.append((empno, ename, sal))

        #SQL Query for insertion
        sql_query = "INSERT INTO emp (empno, ename, sal) VALUES (%s, %s, %s)"

        # Executing multiple rows at once
        cursor.executemany(sql_query, employees)
        
        # Committing the transaction
        conn.commit()
        print(f"{cursor.rowcount} rows are inserted")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # 5. Safe closure of cursor and connection
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            # This logic ensures it closes only if the connection is active.
        
        os.system("pause")

if __name__ == "__main__":
    insert_multiple_emp()