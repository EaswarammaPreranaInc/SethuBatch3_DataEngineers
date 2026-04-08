# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) # adder1(100) → 5 + 100 = 105
print(adder2(200))# adder2(200) → 10 + 200 = 210
print(adder1(300 , 400)) # adder1(300, 400) → 400 + 300 = 700

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # 30
print(add(30)(40)) # 70

# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) # [(5,'Amar',1300.0),(10,'Rama',1000.0),(15,'Rajesh',500.0),(18,'Kiran',2800.0),(20,'Sita',2000.0)]
print()
c = sorted(a , reverse = True)
print(c)  #  [(20,'Sita',2000.0),(18,'Kiran',2800.0),(15,'Rajesh',500.0),(10,'Rama',1000.0),(5,'Amar',1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [(5,'Amar',1300.0),(18,'Kiran',2800.0),(15,'Rajesh',500.0),(10,'Rama',1000.0),(20,'Sita',2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e) # [(15,'Rajesh',500.0),(10,'Rama',1000.0),(5,'Amar',1300.0),(20,'Sita',2000.0),(18,'Kiran',2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f) # same as b
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) # [(20,'Sita',2000.0),(10,'Rama',1000.0),(15,'Rajesh',500.0),(18,'Kiran',2800.0),(5,'Amar',1300.0)]
#print(sorted(a , key = x[1])) # Error

# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) # {'Make': 'Tesla', 'Model': 'X', 'Year': 1999},{'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008},{'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
#print(sorted(a)) # Error

# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] )) # (25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] )) # (15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] )) # (20 , 'Sita' , 2800.0)
print(max(a)) # (25 , 'Kiran' , 1500.0)

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
''' 
3
2
1
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
End
'''

#  Tricky  program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)
# End  of  the  function
x = 10
f1(x , x := x + 1)
print(x) # 32,21,11,11


# Find  outputs   (Home  work)
def  f1(x):
	print(x) # 3 , 2 , 1 , 0
	if   x:
		f1(x - 1)
	print(x) # 0 , 1 , 2 , 3 
# End  of  the  function
f1(3) # 3,2,1,0,0,1,2,3

#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1() # recursion error that is mutual recursion f1 is calling f2 and vice versa

#  Find  outputs  (Home  work)
def  f1():
        print('f1    function')
def  f2():
        print('f2  function')
# End  of  the  function
f1() # f1 function
f2() # f2 function
print(f1  is  f2) # False
f2 = f1
f2() # f1 funcion
print(f1  is  f2) # True
f2 = f1() # None
print(f2) # None
#f2() # Error bcz f2 is not a function anymore it is obejct so that non type object is not callable

# Find  outputs (Home  work)
p=print # How  to  assign  ref  'p'  to  print()  function
p("Hyd") # How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello') # Error
p("Hello") # How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'

# Find  outputs (Home  work)
x = id # How  to  assign  ref  'x'  to  id()  function
print(x(25)) # How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len # How  to  assign  ref  'p'  to  len()  function
print(len('Hyd')) # How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd

# Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')
	print('Hi')
	inner2()
	print('Hello')
	inner1()
	print('Back  to  outer  function')
	def  other():
		# inner() # Error
		print('Other  function')
# End  of  the  function
print('Begin')
outer()
print('Hi')
# inner() # Error
other()
print('Bye') 
''' 
Begin
Outer function
Hi
Hello
Back to outer funcion
Other function
Hi
Bye
'''

# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) # 60

# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer()
print('Bye')

# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()

# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()

# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)
		x +=  7
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  the  function
outer()
print('Bye')

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)
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
print(x)

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)
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
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
print(x)

# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)

# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)

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
		print(a , b)
	# End  of  inner  function
	print(a , b)
	inner()
	print(a , b)
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
	return  x
# End  of  outer  function
print(f1())

# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)
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
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)
		f3()
	f2()
f1()
