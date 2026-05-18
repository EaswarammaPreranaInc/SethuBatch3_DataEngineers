#1
import  os
list = ['a' , 'b']
print(list)
for   x  in  list:  # infinite loop
	list . append(x)  #   ['a' , 'b' ,   'a' , 'b' , 'a' , 'b' , 'a']
	print(list)	
	os . system('pause')
	


# Modify  the  following  program  with  writerows()  method
import   csv
def   create(f):
	w = csv . writer(f)
	l = []
	l . append(['EMP NO' , 'EMP NAME' , 'SALARY'])
	n = eval(input('How Many Employees ? :   '))   #   3
	for  i  in  range(n):
		empno = eval(input('Enter Employee No : '))
		ename = input('Enter Employee Name : ')
		sal = eval(input('Enter Employee Salary : '))
		l . append([empno , ename , sal])

	w . writerows(l)
	# End  of  for  loop
	print(F'File  {f . name}  is  created')
# End  of  the  function
fname = input('Enter   filename  :   ')  #   emp.csv
f = open(fname , 'w' , newline = '')
create(f)
f . close()



# Write  a  program  to  print  csv  file
import  csv
def  disp(f):
	r = csv . reader(f) # How  to  itertae  thru  csv  file  using  reader  object
	for x in r:
            print(x)
# End  of  function
try:
	filename = input('Enter the File Name:')
	f = open(filename , 'r') # How  to  open  the  file
	disp(f) # How  to  print  the  file
	f . close # How  to  close  the  file	
except  FileNotFoundError:
	print(F'File  {filename}  does  not  exist')
