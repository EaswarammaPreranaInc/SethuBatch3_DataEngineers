# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))#105
print(adder2(200))#210
print(adder1(300 , 400))#700

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))#30
print(add(30)(40))#70
# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #  [(5 , 'Amar' , 1300.0)  , (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()
c = sorted(a , reverse = True)
print(c)  #  [(20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (5 , 'Amar' , 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [('Amar') , ('Kiran') , ('Rajesh') , ('Rama') , ('Sita')]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)#[( 500.0),( 1000.0),(1300.0),(2000.0),(2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)#[(5),(10),(15),(18),(20)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)#[('Sita'),('Rama'),('Rajesh'),('Kiran'),('Amar')]
print(sorted(a , key = x[1]))#
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)#[('Year' : 2013,),('Year' : 1999),('Year' : 2008)]
print(sorted(a))#[1999,2008,2013]
 # Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] ))#20
print(max(a , key = lambda  x  :  x[1] ))#'vamsi'
print(max(a , key = lambda  x  :  x[2] ))#2800.0
print(max(a))#(25 , 'Kiran' , 1500.0)

#  Find  outputs (Home  work)
def  outer():
	print('Outer  function')#Outer function
	def  inner():
		print('Inner  function')#Inner function
	# End  of  inner  function
	print('Hello')#Hello
	inner()
	print('Back  to  outer  function')#Back to outer function
def  other():
	inner()
	print('Other  function')#Other function
# End  of  the  function
print('Begin')#Begin
outer()
print('Hi')#Hi
inner()#error
other()
print('Bye')
 # Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))#60
 # Find  outputs (Home  work)
def  outer():
	print('Outer  function')#outer
	def  inner1():
		print( '1st  inner  function')#1st inner function
	def  inner2():
		print('2nd  inner  function')#2nd inner function
	print('Hi')#Hi
	inner2()
	print('Hello')#Hello
	inner1()
	print('Back  to  outer  function')#Back to outer function
# End  of  the  function
print('Begin')#Begin
outer()
print('Bye')#Bye
 # Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)#30
		print(globals()['x'])#10
	inner()
outer()
print('Bye')#Bye
 # Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)#20
		print(globals()['x'])#10
	inner()
outer()
# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)#error
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
	print(x)#27
# End  of  the  function
outer()
print('Bye')#Bye
 #  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)#15
		x = 20
		print(x)#20
		x += 5#25
	# End  of  inner  function
	print(x)#10
	x += 5#15
	inner()#
	print(x)#25
# End  of  outer  function
outer()
print(x)#error
 #  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)#15
		nonlocal  x
		x = 20
		print(x)#20
		x += 5#25
	# End  of  inner  function
	print(x)#10
	x += 5#15
	inner()
	print(x)#25
# End  of  outer  function
outer()
#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)#20
		x += 5#25
	# End  of  inner  function
	print(x)#10
	x += 5#15
	inner()
	print(x)#15
# End  of  outer  function
outer()
print(x)#25
 # Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x
		x = 20
		print(x)#20
	# End  of  inner  function
	inner()
	print(x)#20
# End  of  the  function
outer()
print(x)#error
 # Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)#20
		x = x + 5#25
	# End  of  inner  function
	inner()
	print(x)#25
# End  of  the  function
outer()
print(x)#25
 #  Identify  Error
def   f1():
        nonlocal   x#error because there is no x value
 # Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)#100 200
	# End  of  inner  function
	print(a , b)#10 20
	inner()
	print(a , b)#100 20
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
	return  x#Hello
# End  of  outer  function
print(f1())#Hello
 # Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)#error
	# End  of  inner  function
	gun()
# End  of  outer function
fun()
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x#error
		nonlocal  x#error
 #  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)#10
		f3()
	f2()
f1()

