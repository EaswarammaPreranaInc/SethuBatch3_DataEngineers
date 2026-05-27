# Modify  the  following  program  with  writerows()  method
import csv

def create(filename):
    n = int(input('How Many Employees? : '))
    a = []
    
    for i in range(n):
        empno = int(input('Enter Employee No: '))
        ename = input('Enter Employee Name: ')
        sal = float(input('Enter Employee Salary: '))
        a.append([empno, ename, sal])
    with open(filename, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['EMP NO', 'EMP NAME', 'SALARY'])
        w.writerows(a)
        print(f'File {filename} created successfully.')

fname = input('Enter filename (e.g., emp.csv): ')
create(fname)



# Write  a  program  to  print  csv  file
import  csv
def  disp(r):
	for x in r:
		print(x)#How  to  itertae  thru  csv  file  using  reader  object
# End  of  function
try:
	fname=input("Enter the Filename:")#How  to  read  the  filename
	f =open(fname)
	r = csv.reader(f)#How  to  open  the  file
	print(disp(r))#How  to  print  the  file
	f.close()#How  to  close  the  file	
except  FileNotFoundError:
	print(F'File  {fname}  does  not  exist')
