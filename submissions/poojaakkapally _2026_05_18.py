# Modify  the  following  program  with  writerows()  method
import csv
def create(f):
    w = csv.writer(f)
    w.writerow(['EMP NO', 'EMP NAME', 'SALARY'])

    n = eval(input('How Many Employees ? : '))  # 3
    rows = []

    for i in range(n):  # Iteration 3
        empno = eval(input('Enter Employee No : '))
        ename = input('Enter Employee Name : ')
        sal = eval(input('Enter Employee Salary : '))
        rows.append([empno, ename, sal])

    w.writerows(rows)
    print(f'File {f.name} is created')

fname = input('Enter filename : ')  # emp.csv
f = open(fname, 'w', newline='')
create(f)
f.close() 


# Write  a  program  to  print  csv  file
import csv

def disp(f):
    reader = csv.reader(f)
    for row in reader:
        print(row)

# End of function

try:
    fname = input("Enter filename: ")
    f = open(fname, "r", newline="")
    disp(f)
    f.close()

except FileNotFoundError:
    print(f"File {fname} does not 