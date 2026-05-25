# Modify  the  following  program  with  writerows()  method
import csv
def create(f):
    w = csv.writer(f)
    w.writerow(['EMP NO', 'EMP NAME', 'SALARY'])   
    n = int(input('How Many Employees ? :   '))   
    all_employees = []   
    for i in range(n):  
        empno = int(input('Enter Employee No : '))
        ename = input('Enter Employee Name : ')
        sal = float(input('Enter Employee Salary : '))
        all_employees.append([empno, ename, sal])  
        w.writerows(all_employees)  
    print(f'File {f.name} is created with {n} records')
# End of the function
fname = input('Enter filename :   ')  # emp.csv
with open(fname, 'w', newline='') as f:  
    create(f)

# Write  a  program  to  print  csv  file
import csv
def disp(f):
    r = csv.reader(f)
    for row in r:
        
        print(' | '.join(row))
try:
    fname = input('Enter filename to read : ')
    with open(fname, 'r', newline='') as f:  
        disp(f)
except FileNotFoundError:
    print(f'File {fname} does not exist')