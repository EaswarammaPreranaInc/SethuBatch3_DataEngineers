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
#f1()
print('End')

"infinite loop"

def toh(a,b,c,n):
	if n>0:
		toh(a,c,b,n-1)
		print(f'{a}--->{b}')
		toh(c,b,a,n-1)
toh(1,2,3,2)