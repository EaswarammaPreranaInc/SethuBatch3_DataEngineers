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


#3
#2
#1
#Hello
#Hi
#0
#Bye
#Hello
#Hi
#1
#Bye
#Hello
#Hi
#2
#End



-> stack : 1000 1000 1000
	    |	  |    |	 
