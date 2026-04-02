# Find  outputs
def  f1():
	a = 3
	if  a:
		print(a) #3,2,1
		a = a - 1
		f1()
        #Stack --> 200(3),200(2),200(1)
		print('Hello')
		print('Hi')
		print(a)#0,1,2,3
	print('Bye')
# End  of  the  function
a = 3
f1()
#Stack --> 100
print('End')

"""
output:
3
3
3
3
3
...
Untill function limit
"""
