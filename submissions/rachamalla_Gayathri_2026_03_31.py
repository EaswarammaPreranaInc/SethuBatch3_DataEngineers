# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))#105
print(adder2(200))#220
print(adder1(300 , 400))#700
 #Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()#
print(a(20))#30
print(add(30)(40))#70
 # Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #  [()  , () , () , () , ()]
print()
c = sorted(a , reverse = True)
print(c)  #  [() , () , () , () , ()]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [() , () , () , () , ()]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)#
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)
print(sorted(a , key = x[1]))
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)#(2013 ,1999,2008)
print(sorted(a))
 # Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] ))#(25,'kiran',1500.0)
print(max(a , key = lambda  x  :  x[1] ))#(20,'sita',2800.0)
print(max(a , key = lambda  x  :  x[2] ))#(15,'vamshi',2000.0)
print(max(a))#(25,'kiran',1500.0
# Find  outputs (Home  work)
def  outer():
	print('Outer  function')#outer function 2 
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')#2nd inner function 4
	print('Hi')#hi 3
	inner2()
	print('Hello')#hello 5
	inner1()#1st inner function 6
	print('Back  to  outer  function')#Back to outer function
# End  of  the  function
print('Begin')#begin 1
outer()
print('Bye')#Bye 7
 # Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)#30
		print(globals()['x'])#global=10
	inner()
outer() #
print('Bye')#bye

# Find  outputs  (Home  work)
x = 10
def  outer(): 
	def   inner():
		print(x)#10
	inner()
outer()
# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)#20
		x +=  7#27
	# End  of  inner  function
	print(x)#10
	x += 5#15
	inner()
	print(x)
# End  of  the  function
outer()
print('Bye')#bye
 #  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)#10
		x = 20
		print(x)#20
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)#15
# End  of  outer  function
outer()
print(x)#10 1
 #  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)#erropr
		nonlocal  x
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x) #20 2 
		x += 5
	# End  of  inner  function
	print(x)#10 1
	x += 5
	inner()
	print(x) #25
# End  of  outer  function
outer()
print(x)
 # Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x
		x = 20 #error no local
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x) # Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)#20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)#25
# End  of  the  function
outer()
print(x)#25
#  Identify  Error
def   f1():
        nonlocal   x
 # Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b) #100 200
	# End  of  inner  function
	print(a , b)#10,20
	inner()
	print(a , b)#100,20
#end of outer function
outer()
 # Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	# End  of  inner  function
	f2()
	return  x #hello
# End  of  outer  function
print(f1())
 # Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)# cannot take global here
	# End  of  inner  function
	gun()
# End  of  outer function
fun()
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x
#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x 10
		def  f3():
			nonlocal   x
			print(x)#10 1
		f3()
	f2()
f1()
