1.
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
f1()
print('End')
'''
infinite 3's
3
3
3
3
3
3
3
3
3
3
3
RecursionError: maximum recursion depth exceeded while calling a Python object
'''