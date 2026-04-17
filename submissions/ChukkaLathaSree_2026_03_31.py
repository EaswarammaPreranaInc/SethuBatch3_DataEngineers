# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) # 120
print(adder2(200)) # 280
print(adder1(300 , 400)) # Error

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))# type and addr of fun
print(add(30)(40)) # 70


# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #  [(5 , 'Amar' , 1300.0)  , (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print() #
c = sorted(a , reverse = True)
print(c)  #  [(20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (5 , 'Amar' , 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  ['Amar' , 'Rama' , 'Rajesh', 'Kiran' , 'Sita']
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e) # [(1300.0) , (1000.0) , (500.0) , (2800.0) , (2000.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f) # [(5) , (10) , (15) , (18) , (20)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) # ['Sita' , 'Kiran' , 'Rajesh' , 'Rama' , 'Amar']
print(sorted(a , key = x[1])) # ['Amar' , 'Rama' , 'Rajesh' , 'Kiran' , 'Sita']

# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) # (2013, 1999 , 2008)
print(sorted(a)) # (1999 , 2008 , 2013 )

# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] )) # 25
print(max(a , key = lambda  x  :  x[1] )) # Vamsi
print(max(a , key = lambda  x  :  x[2] )) # 2800
print(max(a)) # 25

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
print('End') # 3
               2
               Hello
               Hi
               2
               Bye
               End

#  Tricky  program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y) # Error
	print(x) # 10
# End  of  the  function
x = 10
f1(x , x := x + 1)
print(x) # 10
           

# Find  outputs   (Home  work)
def  f1(x):
	print(x) # 3
	if   x:
		f1(x - 1) # 2
	print(x) # 3
# End  of  the  function
f1(3)

#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()
 # f1 function
   f2 function
   End of f1 function
   End of f2 function


#  Find  outputs  (Home  work)
def  f1():
        print('f1    function')
def  f2():
        print('f2  function')
# End  of  the  function
f1() # f1 function
f2() #f2 function
print(f1  is  f2) # f1 and f2 points to same obj
f2 = f1
f2() 
print(f1  is  f2) # f1 function
f2 = f1() #f1 function
print(f2) # f1 function
f2() #f1 function

# Find  outputs (Home  work)
How  to  assign  ref  'p'  to  print()  function
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
 # 
 p = print
 p('Hyderabad')
 p()
 p('Hello')

# Find   outputs (Home  work)
How  to  assign  ref  'x'  to  id()  function
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
How  to  assign  ref  'p'  to  len()  function
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd

 # x = id
   x(25)
   x(len)=p
   p('Hyd)

#  Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner():
		print('Inner  function')
	# End  of  inner  function
	print('Hello')
	inner()
	print('Back  to  outer  function')
def  other():
	inner()
	print('Other  function')
# End  of  the  function
print('Begin')
outer()
print('Hi')
inner()
other()
print('Bye')
 # 
  Begin
  Outer function
  Hello
  Inner function
  Back to outer function
  Hi
  Inner function
  Inner function
  Other function
  Bye
  
# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a # 50
# End  of  f1  function
print(f1(30)) # 50
                10

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
# End  of  the  function
print('Begin')
outer()
print('Bye')
 # Begin
   Outer function
   Hi
   2nd inner function
   Hello
   1st inner function
   Back to outer function
   Bye 

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
#
10
30
20



# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()
 # 
10
10


# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()
 # 10
   
# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x) # 20
		x +=  7
	# End  of  inner  function
	print(x) # 10
	x += 5 #15
	inner() # 27
	print(x) # 15
# End  of  the  function
outer()
print('Bye') # Bye


#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x) # 10
		x = 20
		print(x) 10
		x += 5 # 15
	# End  of  inner  function
	print(x) #15
	x += 5
	inner()
	print(x) # 20
# End  of  outer  function
outer()
print(x) #20

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x) # 10
		nonlocal  x
		x = 20
		print(x) # 20
		x += 5
	# End  of  inner  function
	print(x) #20
	x += 5 # 25
	inner()
	print(x) #25
# End  of  outer  function
outer()

#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x # 10
		x = 20
		print(x) #10
		x += 5
	# End  of  inner  function
	print(x) #10
	x += 5
	inner() 
	print(x) #15
# End  of  outer  function
outer()
print(x) # 15

# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x
		x = 20
		print(x) #error
	# End  of  inner  function
	inner()
	print(x) #Error
# End  of  the  function
outer()
print(x) #Error
 
# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x) # Error
		x = x + 5
	# End  of  inner  function
	inner() 
	print(x) # Error
# End  of  the  function
outer()
print(x) #Errror

#  Identify  Error
def   f1():
        nonlocal   x # Error

# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b) # (100 , 20)
	# End  of  inner  function
	print(a , b) # (100 , 20)
	inner()
	print(a , b) # (100 , 20)
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
print(f1()) # Hello


# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x) #30
	# End  of  inner  function
	gun()
# End  of  outer function
fun()

#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x # 10
		nonlocal  x # 10

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

# 10
  
