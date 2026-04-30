'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''



# Write  a  program  to  insert  multiple  rows  into  emp  table

import mysqlconnector as mc

# Connect to database
con = mc.connect(database="empdb",user="root")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS emp (
    emp_id INTEGER,
    emp_name TEXT,
    salary INTEGER
)
""")

n = int(input("Enter number of employees: "))

data = []

for i in range(n):
    print(f"\nEnter details for Employee {i+1}")
    emp_id = int(input("Enter ID: "))
    emp_name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))
    
    data.append((emp_id, emp_name, salary))

cur.executemany("INSERT INTO emp VALUES (?, ?, ?)", data)

con.commit()
con.close()

print("\nMultiple rows inserted successfully!")