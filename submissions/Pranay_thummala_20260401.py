# Find  outputs
def  f1():
	a = 3
	if  a:
		print(a)
		a = a - 1
		#f1()           #Error due to maximum  recursion  depth  exceeded
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1()
print('End')

'''
3
Hello
Hi
2
Bye
End
'''