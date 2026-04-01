# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))	        # 105 
print(adder2(200))	        # 210
print(adder1(300 , 400))    # 700

#==============================================================================================================

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))		# 30
print(add(30)(40))	# 70
    
#==============================================================================================================

# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #  [(5 , 'Amar' , 1300.0)  , (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()
c = sorted(a , reverse = True)
print(c)  #  [(20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (5 , 'Amar' , 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [(5 , 'Amar' , 1300.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)  #  [(15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (5 , 'Amar' , 1300.0) , (20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)  #  [(5 , 'Amar' , 1300.0)  , (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)  #  [(20 , 'Sita' , 2000.0) , (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0) ]
# print(sorted(a , key = x[1]))	# error

#==============================================================================================================

# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
      {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
      {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008}]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)     # [{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} , {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} , {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}]
print(sorted(a)) # error , python is not permitted to compare the dictionary. 
                 # but the above one is possible. becoz it compares by using 'year'

#==============================================================================================================

# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] ))	# (25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] ))	# (15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] ))	# (20 , 'Sita' , 2800.0)
print(max(a))		                        # (25 , 'Kiran' , 1500.0)

#========================================================================================================

#   Find  outputs
def  f1():
	global  a
	if  a:
		print(a)	# 3
		a = a - 1
		f1()		# type and address
		print('Hello')	# Hello
		print('Hi')	# Hi
		print(a)	# 2
	print('Bye')		# Bye
# End  of  the  function
a = 3
f1()
print('End')			# End

# 3
# 2
# 1
# Bye
# Hello
# Hi
# 0
# Bye
# Hello
# Hi
# 0
# Bye
# Hello
# Hi
# 0
# Bye
# End

#========================================================================================================

#  Tricky  program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)	# 10
# End  of  the  function
x = 10
f1(x , x := x + 1)
print(x)		# 11

# 43
# 32
# 21
# 11

#========================================================================================================

# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)

# 3
# 2
# 1
# 0
# 0
# 1
# 2
# 3

#========================================================================================================

#  Find  outputs
def  f1():
	print('f1  function')
	# f2() 			# error due to infinate recursion
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()

# f1 function
# f2 function
# end of f1 function
# end of f2 function

#========================================================================================================

#  Find  outputs  (Home  work)
def  f1():
        print('f1    function')
def  f2():
        print('f2  function')
# End  of  the  function
f1()
f2()
print(f1  is  f2)
f2 = f1
f2()
print(f1  is  f2)
f2 = f1()
print(f2)
# f2()

# f1 function
# f2 function
# False
# f1 function
# True
# f1 function
# None

#========================================================================================================

# Find  outputs (Home  work)
# How  to  assign  ref  'p'  to  print()  function
p = 'Hyderabad'		# How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print(p)
# print = None		# error , becoz 'NoneType' object is not callable 
print('Hello')
p = 'Hello'		# How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'

#========================================================================================================

# Find   outputs (Home  work)
def id():				# How  to  assign  ref  'x'  to  id()  function
    x = 25
    return x
print(id())				# How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25

def len():				# How  to  assign  ref  'p'  to  len()  function
    p = 'Hyd' 
    print(len(p))
len()					# How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd'

#========================================================================================================

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
	# inner()
	print('Other  function')
# End  of  the  function
print('Begin')
outer()
print('Hi')
# inner()
other()
print('Bye')

# Begin
# Outer function
# Hello
# inner function
# Back to outer function
# Hi
# Other function
# Bye

#========================================================================================================

# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))	# 10 + 20 + 30 = 60

#========================================================================================================

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
# Outer function
# Hi
# 2nd inner function
# Hello
# 1st inner function
# Back to outer function
# Bye

#========================================================================================================

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

# 30
# 10
# Bye

#========================================================================================================

# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()

# 20
# 10

#========================================================================================================

# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()  			# 10

#========================================================================================================

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

# 10
# 20
# 15
# Bye

#========================================================================================================

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
# print(x)

# 10
# 15
# 20
# 25

#========================================================================================================

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		# print(x)
		# nonlocal  x
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

# 10
# 20
# 15

#========================================================================================================

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

# 10
# 20
# 15
# 25

#========================================================================================================

# Find  outputs(Home  work)
def  outer():
	def  inner():
		# nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	# print(x)
# End  of  the  function
outer()
# print(x)

# 20

#========================================================================================================

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

# 20
# 25
# 25

#========================================================================================================

#  Identify  Error
# def   f1():
#         nonlocal   x

#========================================================================================================

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

# 10 20 
# 100 200
# 100 20    # becoz a = 10 is non local so, thats why a = 100 is assigned

#========================================================================================================

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

# Hello

#========================================================================================================

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

# error , becoz x = 10 is local variable of fun(). but is assingned another function gun()

#========================================================================================================

#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		# nonlocal  x
		print(x)
	inner()

outer()

#========================================================================================================

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