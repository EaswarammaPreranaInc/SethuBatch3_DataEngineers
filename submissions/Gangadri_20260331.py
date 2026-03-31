# 1 . 
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

# output : 
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

#----------------------------------------------
# 2.
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
print(x)

# output : 
43
32
21
11

#--------------------------------------------------

# 3 .
# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)

# output : 
3
2
1
0
0
1
2
3

#--------------------------------------------------
# 4. #  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()

# output : 
f1 function
f2 function
f1 function
f2 function
f1 function
f2 function
...

#----------------------------------------------------
# 5 . 
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
f2()

# output : 
f1    function
f2  function
False
f1    function
True
f1    function
None
TypeError: 'NoneType' object is not callable

#-----------------------------------------------------
# 6.
# Find  outputs (Home  work)
How  to  assign  ref  'p'  to  print()  function
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'

# output : 
p = print     
p('Hyderabad')    

print = None      

# print('Hello') 

p('Hello')      

# -------------------------------------------------------
# 7 .
# Find   outputs (Home  work)
How  to  assign  ref  'x'  to  id()  function
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
How  to  assign  ref  'p'  to  len()  function
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd

# output : 
x = id
print(x(25))

p = len
print(p('Hyd'))

#---------------------------------------------------------

# 8 . #  Find  outputs (Home  work)
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

# output : 
Begin
Outer  function
Hello
Inner  function
Back  to  outer  function
Hi
NameError: name 'inner' is not defined

# --------------------------------------------------------------

# 9 . # Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))

# output : 60

# -----------------------------------------------------------

# 10 . # Find  outputs (Home  work)
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

# output : 

Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye

#-----------------------------------------------------------------

# 11 . # Find  outputs  (Home  work)
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

# output : 
30
10
Bye

#-------------------------------------------------------------------

# 13 .

# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()

# output : 
20
10

#---------------------------------------------------------------------

# 14 . 

# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()

# output : 
10

# -------------------------------------------------------------------

# 15 . 

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

# output : 
10
20
15
Bye

# --------------------------------------------------------------------

# 16 . 

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

# output : 

10
15
20
25
NameError: name 'x' is not defined

# -----------------------------------------------------------------------

# 17 . 

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

# output : SyntaxError: name 'x' is used prior to nonlocal declaration

#---------------------------------------------------------------------------

# 18 .

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

# output : 

10
20
15
25


# -------------------------------------------------------------------------------

# 19 .

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

# output : 
SyntaxError: no binding for nonlocal 'x' found

# ----------------------------------------------------------------------------

# 19 . 

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

# output : 

20
25
25

# --------------------------------------------------------------------

# 2o . 

#  Identify  Error
def   f1():
        nonlocal   x

# output : 
SyntaxError: no binding for nonlocal 'x' found

# --------------------------------------------------------------

# 21 . 

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


# ouput : 

10 20
100 200
100 20

# ------------------------------------------------------------

# 22 . 

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

# output : 
 
Hello

# ------------------------------------------------------

# 23 . 

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

# output : Error

# -----------------------------------------------------

# 24 . 

#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x

# output : name x is not defined

#--------------------------------------------------------

# 25 . 

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

# output : 10