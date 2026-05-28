# Modify  the  following  program  with  writerows()  method
import csv
def create(f):
    w = csv.writer(f)
    w.writerow(['EMP NO', 'EMP NAME', 'SALARY'])   # Header row - single row kabatti writerow() eh
    n = int(input('How Many Employees ? :   '))   # eval() badulu int() vadadam better & safe
    all_employees = []   # Andari data store cheyyadaniki empty list
    for i in range(n):  # Iteration n times
        empno = int(input('Enter Employee No : '))
        ename = input('Enter Employee Name : ')
        sal = float(input('Enter Employee Salary : '))
        all_employees.append([empno, ename, sal])  # Prati employee row ni list lo add chey
        w.writerows(all_employees)  # List of rows ni okesari file lo raayi
    print(f'File {f.name} is created with {n} records')
# End of the function
fname = input('Enter filename :   ')  # emp.csv
with open(fname, 'w', newline='') as f:  # with vadithe f.close() avasaram ledu
    create(f)

# Write  a  program  to  print  csv  file
import csv
def disp(f):
    r = csv.reader(f)
    for row in r:
        # Join chesi comma tho separate chesi clean ga chupinchadam
        print(' | '.join(row))
try:
    fname = input('Enter filename to read : ')
    with open(fname, 'r', newline='') as f:  # with vadithe close avasaram ledu
        disp(f)
except FileNotFoundError:
    print(f'File {fname} does not exist')
