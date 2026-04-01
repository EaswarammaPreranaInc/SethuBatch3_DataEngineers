# Find  outputs
def  f1():
	a = 3
	if  a:
		print(a)#3
		a = a - 1#2
		f1()
		print('Hello')#hello
		print('Hi')#hi
		print(a)#2
	print('Bye')#bye
# End  of  the  function
a = 3
f1()
print('End')#end