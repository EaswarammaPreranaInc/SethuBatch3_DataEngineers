# Find  outputs
def  f1():
	a = 3
	if  a:#True #True
		print(a) #3  #3
		a = a - 1#a=2 #a=2
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye') #'Bye'
# End  of  the  function
a = 3
f1()
print('End')
'''
error-infinte loop because the a value is always being 3 and at the time of recursion a value is again considered as 3 so the if condition always remains true and hence a value will be 3


'''