1) Modify  the  following  program  with  writerows()  method
import   csv
def   create(f):
	w = csv . writer(f)
	data = []
	data.append(['EMP NO', 'EMP NAME', 'SALARY'])
	n = eval(input('How Many Employees ? :   '))   
	for  i  in  range(n):  
		empno = eval(input('Enter Employee No : '))
		ename = input('Enter Employee Name : ')
		sal = eval(input('Enter Employee Salary : '))
		data.append([empno, ename, sal])
		w . writerows(data) 
	# End  of  for  loop
	print(F'File  {f . name}  is  created')
# End  of  the  function
fname = input('Enter   filename  :   ')  #   emp.csv
f = open(fname , 'w' , newline = '')
create(f)
f . close()

2) Write  a  program  to  print  csv  file
import  csv
def  disp(f):
	obj = csv,reader(f) 
	for x in obj:
	   for y in x:
		print(y, end ="\t") #How  to  itertae  thru  csv  file  using  reader  object
# End  of  function
try:
	fname = input("Enter file name:") #How  to  read  the  filename
	f = open(fname, 'r') #How  to  open  the  file
	disp(f) #How  to  print  the  file
	f.close() #How  to  close  the  file	
except  FileNotFoundError:
	print(F'File  {fname}  does  not  exist')