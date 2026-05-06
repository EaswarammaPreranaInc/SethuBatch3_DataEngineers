import pandas as pd
from sqlalchemy import create_engine

# Connect to MySQL
engine = create_engine("mysql+pymysql://root:yourpassword@localhost/empdb")

# Number of rows
n = int(input("How many rows would you like to insert? : "))

records = []

# Input using for loop
for i in range(n):
    print(f"\nEmployee : {i+1}")
    
    emp_id = int(input("Enter employee number : "))
    emp_name = input("Enter employee name : ")
    salary = int(input("Enter salary : "))
    
    records.append([emp_id, emp_name, salary])

# Create DataFrame
df = pd.DataFrame(records, columns=["emp_id", "emp_name", "salary"])

# Insert into emp table
df.to_sql(
    name="emp",
    con=engine,
    if_exists="append",
    index=False
)

print(f"\n{n} rows are inserted")