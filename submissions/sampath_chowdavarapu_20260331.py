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
'''3
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
End'''


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


# Find  outputs   (Home  work)
def  f1(x):
	print(x)#3
	if   x:
		f1(x - 1)
	print(x)
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
''' f1 function
   f2 function 
   f1 function..... Enters into a loop''' 
   
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
f2()#Error
'''
f1 function 
f2 function 
False
f1   function
True
f1   function
None'''


# Find  outputs (Home  work)
p=print#How  to  assign  ref  'p'  to  print()  function
p("Hyderabad")#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')#Error print is none so none cannot be called
p("Hello")#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'


# Find   outputs (Home  work)
x=id#How  to  assign  ref  'x'  to  id()  function
print(x(25))#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=len#How  to  assign  ref  'p'  to  len()  function
print(p("Hyd"))#How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd


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
	inner()#Error
	print('Other  function')
# End  of  the  function
print('Begin')
outer()
print('Hi')
inner()#Error
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
Bye'''



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
Bye'''


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
'''
30
10
Bye'''

# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)#20
		print(globals()['x'])#10
	inner()
outer()
'''
20
10'''


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
print('Bye')
'''
10
20
15
Bye'''


#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)#10
		x = 20
		print(x)#20
		x += 5#25
	# End  of  inner  function
	print(x)#10
	x += #15
	inner()
	print(x)#25
# End  of  outer  function
outer()
print(x)#Error
'''10
10
20
25'''


#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)#x is not yet defined in inner function 
		nonlocal  x
		x = 20
		print(x)#20
		x += 5#25
	# End  of  inner  function
	print(x)#10
	x += 5#15
	inner()
	print(x)25
# End  of  outer  function
outer()
'''10
20
25'''

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
'''10
20
15
25'''


# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x#Error there is no local x in outer function so it cannot be used in inner function 
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
		print(x)#20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)#25
# End  of  the  function
outer()
print(x)#25
'''20
25
25'''


#  Identify  Error
def   f1():
        nonlocal   x#nonlocal cannot be used in outer function 


# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)# 100 200
	# End  of  inner  function
	print(a , b)#10 20
	inner()
	print(a , b)#100 20
#end of outer function
outer()
'''10 20
100 200
100 20'''

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
print(f1())#Hello


# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20#Error there is no variable x in gun() 
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
		nonlocal  x#Error x is already treated as global again it cannot be treated as non local 


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
