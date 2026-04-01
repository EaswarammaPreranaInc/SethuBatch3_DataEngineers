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




'''
output
3
3
3
3
3
infinite loop error
explanation
Call 1 at line 14 then f1() starts. a is set to 3 it prints 3 a becomes 2 it calls f1()
Call 2 A new f1() starts a is set to 3 again (because of a = 3) it prints 3 then a becomes 2 it calls f1()
Call 3,4 ....: This repeats forever because a is re-initialized to 3 at the start of every single call
problem is a=3 which is locally created newly for every function call
'''
