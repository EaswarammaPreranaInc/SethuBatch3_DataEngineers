1.
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


2.
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
'''
43
32
21
11
'''



3.
# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)
'''
3
2
1
0
0
1
2
3
'''



4.
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
'''
f1  function
f2  function
f1  function
f2  function
...
RecursionError
'''


5.
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
f2() # TypeError: 'NoneType' object is not callable
'''
f1    function
f2  function
False
f1    function
True
f1    function
None
'''


6.
# Find  outputs (Home  work)
# How  to  assign  ref  'p'  to  print()  function
# How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
# print = None
# print('Hello')
# How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
p = print
print('Hello')
print('Hyderabad')



7.
# Find   outputs (Home  work)
# How  to  assign  ref  'x'  to  id()  function
# How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
# How  to  assign  ref  'p'  to  len()  function
# How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd

x = id
print(id(25))

p = len
print(len('Hyd'))



8.
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
	#inner()
	print('Other  function')
# End  of  the  function
print('Begin')
outer()
print('Hi')
#inner()
other()
print('Bye')
'''
Begin
Outer function
Hello
Inner function
Back to outer function
Hi
Other function
Bye
'''



9.
# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))
'''
60
'''


10.
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
'''
Begin
Outer function
Hi
2nd inner function
Hello
1st inner function
Back to outer function
Bye
'''


11.
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
'''
30
10
Bye
'''


12.
# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()
'''
20
10
'''


13.
# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x) # 10
	inner()
outer()



14.
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
'''
10
20
15
Bye
'''


15.
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
print(x) # NameError: name 'x' is not defined
'''
10
15
20
25
'''


16.
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)
		#nonlocal  x # SyntaxError: name 'x' is used prior to nonlocal declaration
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
'''
10
20
15
'''


17.
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
'''
10
20
15
25
'''


18.
# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x # SyntaxError: no binding for nonlocal 'x' found
		x = 20 
		print(x) # 20
	# End  of  inner  function
	inner()
#	print(x)
# End  of  the  function
outer()
print(x) # NameError: name 'x' is not defined



19.
# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x) # 20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x) # 25
# End  of  the  function
outer()
print(x) # 25



20.
#  Identify  Error
def   f1():
        nonlocal  x # SyntaxError: no binding for nonlocal 'x' found



21.
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
'''
10 20
100 200
100 20
'''



22.
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



23.
# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20#UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
		print(x) # 10
	# End  of  inner  function
	gun()
# End  of  outer function
fun()


24.
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
#		global   x # SyntaxError: name 'x' is nonlocal and global
		nonlocal  x 




25.
#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x) # 10
		f3()
	f2()
f1()

