# Modify  the  following  program  with  writerows()  method
'''
import   csv
def   create(f):
	w = csv . writer(f)
	n = eval(input('How Many Employees ? :   '))   #   3
	list=[['EMP NO' , 'EMP NAME' , 'SALARY']]
	for  i  in  range(n):  #  Iteration   3
		empno = eval(input('Enter Employee No : '))
		ename = input('Enter Employee Name : ')
		sal = eval(input('Enter Employee Salary : '))
		list.append([empno , ename, sal])
	w.writerows(list)
	# End  of  for  loop
	print(F'File  {f . name}  is  created')
# End  of  the  function
fname = input('Enter   filename  :   ')  #   emp.csv
f = open(fname , 'w' , newline = '')
create(f)
f . close()'''


# Write  a  program  to  print  csv  file
import  csv
def  disp(f):
	r=csv.reader(f)#How  to  itertae  thru  csv  file  using  reader  object
	for rec in r:
		print(r)
# End  of  function
try:
	fname=input("Enter file name : ") #How  to  read  the  filename
	f=open(fname,'r',newline='') #How  to  open  the  file
	disp(f) #How  to  print  the  file
	f.close() #How  to  close  the  file	
except  FileNotFoundError:
	print(F'File  {fname}  does  not  exist')
	


	
