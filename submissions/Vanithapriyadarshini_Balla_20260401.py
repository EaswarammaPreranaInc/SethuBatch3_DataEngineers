# Find  outputs
def  f1():
	a = 3
	if  a:
		print(a)
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1()# 3 <nl> 3  infinite recursion 3 's
print('End')

# towers of honai
def toh(n,p1,p2,p3):
	if n>0:
		toh(n-1,p1,p3,p2)
		print(f'{p1}--->{p3}')
		toh(n-1,p2,p1,p3)
n=int(input("Enter no.of disks : "))
toh(n,1,2,3)