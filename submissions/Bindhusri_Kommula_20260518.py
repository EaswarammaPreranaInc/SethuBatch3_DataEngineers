import  os
list = ['a' , 'b']
print(list)
for   x  in  list:  #   'x'  is  
	list . append(x)  #   ['a' , 'b' ,   'a' , 'b' , 'a' , 'b' , 'a']
	print(list)	
	os . system('pause')


import csv
def create(f):
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



import csv
def disp(f):
	r=csv.reader(f)
	for row in r:
		for x in row:
			print(x,end='\t')
		print()
try:
	fname=input('Enter filename : ')
	f=open(fname,'r')
	disp(f)
	f.close()
except FileNotFoundError:
	print(f'File {fname} does not exist')