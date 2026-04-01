# Find  outputs
def  f1():
	a = 3   ---> a is not 0 so True
	if  a:
		print(a)  # 3
		a = a - 1 # a=2
		f1()      # callin f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1()
print('End')


# Endlessloop

