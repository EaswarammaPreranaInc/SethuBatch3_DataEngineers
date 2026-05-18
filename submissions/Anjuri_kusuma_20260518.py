# Modify  the  following  program  with  writerows()  method
import csv

def create(f):
    w = csv.writer(f)
    data = []
    data.append(['EMP NO', 'EMP NAME', 'SALARY'])
    n = eval(input('How Many Employees ? : '))
    for i in range(n):
        empno = eval(input('Enter Employee No : '))
        ename = input('Enter Employee Name : ')
        sal = eval(input('Enter Employee Salary : '))
        data.append([empno, ename, sal])
    w.writerows(data)
    print(F'File {f.name} is created')
fname = input('Enter filename : ')   # emp.csv
f = open(fname, 'w', newline='')
create(f)
f.close()--------------------------------------------------------------------------------
# Write  a  program  to  print  csv  file
import csv
def disp(f):
    r = csv.reader(f)
    for row in r:
        print(row)
try:
    fname = input('Enter filename : ')
    f = open(fname, 'r')
    disp(f)
    f.close()
except FileNotFoundError:
    print(F'File {fname} does not exist')