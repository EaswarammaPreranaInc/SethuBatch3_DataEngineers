import   csv
def display(f):
	r=csv.reader(f)
	while True:
		try:
			row=next(r)
			print(f"{row[0]} {row[1]} {row[2]}")
		except:
			break
	
def   create(f):
	w = csv . writer(f)
	w . writerow(['EMP NO' , 'EMP NAME' , 'SALARY'])
	data=[]
	n = eval(input('How Many Employees ? :   '))   #   3
	for  i  in  range(n):  #  Iteration   3
		empno = eval(input('Enter Employee No : '))
		ename = input('Enter Employee Name : ')
		sal = eval(input('Enter Employee Salary : '))
		data.append([empno,ename,sal])
	w . writerows(data)
	# End  of  for  loop
	print(F'File  {f . name}  is  created')
# End  of  the  function
fname = input('Enter   filename  :   ')  #   emp.csv
f = open(fname , 'w' , newline = '')
create(f)
f . close()
f = open(fname , 'r' )
display(f)