# Find  outputs
def  f1():
	a = 3
	if  a:
		print(a)#3,2,1
		a = a - 1#2,1,0
		f1()#
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1()
print('End')

# outputs:=
# 3
# 2
# 1
# Bye
# Hello
# Hi
# 0
# Hello
# Hi
# 1
# Hello
# Hi
# 2
# End

