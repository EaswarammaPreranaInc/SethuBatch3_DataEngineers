# Modify  the  following  program  with  writerows()  method

import   csv
def   create(f):
	w = csv . writer(f)
	w . writerow(['EMP NO' , 'EMP NAME' , 'SALARY'])
	n = eval(input('How Many Employees ? :   '))   #   3
	for  i  in  range(n):  #  Iteration   3
		empno = eval(input('Enter Employee No : '))
		ename = input('Enter Employee Name : ')
		sal = eval(input('Enter Employee Salary : '))
		w . writerow([empno , ename, sal])
	# End  of  for  loop
	print(F'File  {f . name}  is  created')
# End  of  the  function
fname = input('Enter   filename  :   ')  #   emp.csv
f = open(fname , 'w' , newline = '')
create(f)
f . close()




import csv
def create(f):
    w=csv.writer(f)
    w.writerow(['EMP NO','EMP NAME','SALARY'])
    rows=[]
    n=eval(input('How Many Employees ? : '))
    for i in range(n):
        empno=eval(input('Enter Employee No : '))
        ename=input('Enter Employee Name : ')
        sal=eval(input('Enter Employee Salary : '))
        rows.append([empno,ename,sal])
    w.writerows(rows)
    print(f'File {f.name} is created')
fname=input('Enter filename : ')
f=open(fname,'w',newline='')
create(f)
f.close()





# Write  a  program  to  print  csv  file

import csv
def disp(f):
    r=csv.reader(f)
    for i in r:
        print(i)
try:
    fname=input('Enter file name : ')
    f=open(fname,'r')
    disp(f)
    f.close()
except FileNotFoundError:
    print(f'File {fname} does not exist')