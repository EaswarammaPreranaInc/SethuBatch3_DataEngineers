import  os
list = ['a' , 'b']
print(list)
for   x  in  list:  #   'x'  is  
	list . append(x)  #   ['a' , 'b' ,   'a' , 'b' , 'a' , 'b' , 'a']
	print(list)	
	os . system('pause')


# Modify  the  following  program  with  writerows()  method
import   csv
def   create(f):
	w=csv.writer(f)
	w.writerow(['EMP NO','EMP NAME','SALARY'])
	n=eval(input('How Many Employees ? : '))
	data=[]
	for i in range(n):
		empno=eval(input('Enter Employee No : '))
		ename=input('Enter Employee Name : ')
		sal=eval(input('Enter Employee Salary : '))
		data.append([empno,ename,sal])
	w.writerows(data)
	print(f'File {f.name} is created')
fname=input('Enter filename : ')
f=open(fname,'w',newline='')
create(f)
f.close()


# Write  a  program  to  print  csv  file
import  csv
def  disp(f):
	#How  to  itertae  thru  csv  file  using  reader  object
	x = csv.reader(f)
	for row in x:
		print(row)
# End  of  function
try:
	fname = input('Enter csv file :')#How  to  read  the  filename
	f = open(fname, 'r')#How  to  open  the  file
	disp(f)#How  to  print  the  file
	f.close()#How  to  close  the  file	
except  FileNotFoundError:
	print(F'File  {fname}  does  not  exist')
	