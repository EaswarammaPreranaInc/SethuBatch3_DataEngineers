import csv
import os
list = ['a', 'b']
print(list)
for x in list:
    list . append(x)  # ['a' , 'b' ,   'a' , 'b' , 'a' , 'b' , ....infinite  ]
    print(list)
    os . system('pause')


''' Modify the following program with writerows() method '''


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
    print(f'File {f.name} is created')
fname = input('Enter filename : ')
f = open(fname, 'w', newline='')
create(f)
f.close()


''' Write a program to print csv file'''


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
    print(f'File {fname} does not exist')
