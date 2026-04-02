#   Find  outputs
def  f1():
	global  a
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
# 3
# 2
# 1
# Bye
# Hello
# Hii
# 0
# Bye 
# Hello
# Hii
# 0
# Bye
# Hello
# Hii
# End
#  Tricky  program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return#None
	x += y#21,32,43
	f1(x , y)#(21,11),(32,11),(43,11)
	print(x)#21,32,43
# End  of  the  function
x = 10
f1(x , x := x + 1)#(10,11)
print(x)

#  Find  outputs
def  f1():
	print('f1  function')#f1 function
	f2()
	print('End  of  f1  function')#End of f1 function
def  f2():
	print('f2  function')#f2 function
	f1()
	print('End  of  f2  function')#End of f2 function
f1()

#  Find  outputs  (Home  work)
def  f1():
        print('f1    function')#f1 function
def  f2():
        print('f2  function')#f2 function
# End  of  the  function
f1()
f2()
print(f1  is  f2)#False
f2 = f1
f2()#f1    function
print(f1  is  f2)#True
f2 = f1()
print(f2)#None
f2()#error

# Find  outputs
def  f1():
	a = 3
	if  a:
		print(a)#3,2,1
		a = a - 1#2,1,0
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1()
print('End')
#3
# 2
# 1
# Bye
# Hello
# Hii
# 0
# Bye
# Hello
# Hii
# 1
# Bye
# Hello
# Hii
# 2
# Bye
# Hello
# Hii
# 1
# Bye
# End
