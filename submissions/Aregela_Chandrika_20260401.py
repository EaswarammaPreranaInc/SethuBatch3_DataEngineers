
# Find  outputs
def  f1():
	a = 3
	if  a:
		print(a) # 3 3 3 ...
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1()
print('End')
