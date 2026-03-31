#   Find  outputs
def  f1():
	global  a		
	if  a:
		print(a)	#3
		a = a - 1	#2 <next line> 1
		f1()
		print('Hello')	#Hello <next line> Hii <next line> 0
		print('Hi')	#Hello <next line> Hii <next line> 0 
		print(a)	#Hello <next line> Hii <next line> 0 
	print('Bye')	#Bye
# End  of  the  function
a = 3
f1()
print('End')	#End



#  Tricky  program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:	#10 > 40 #False
		return
	x += y
	f1(x , y)
	print(x)	#43 <next line> 32 <next line> 21
# End  of  the  function
x = 10
f1(x , x := x + 1)
print(x)	#11



# Find  outputs   (Home  work)
def  f1(x):
	print(x)	#3 <next line> 2 <next line> 1 <next line> 0 
	if   x:
		f1(x - 1)
	print(x)	#3 <next line> 2 <next line> 1 <next line> 0 
# End  of  the  function
f1(3)


#  Find  outputs
def  f1():
	print('f1  function')
	f2()	#error
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()	#f1 function <next line> End of the f2 function


#  Find  outputs  (Home  work)
def  f1():
        print('f1    function')
def  f2():
        print('f2  function')
# End  of  the  function
f1()	#f1    function
f2()	#f2  function
print(f1  is  f2)	#False
f2 = f1
f2()	#f1    function
print(f1  is  f2)	#True
f2 = f1()		#f1    function 
print(f2)		#None
f2()			#error



# Find  outputs (Home  work)
p=print		#How  to  assign  ref  'p'  to  print()  function
p("Hyd")	#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')	#error None type object
p("Hello")	#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'



# Find   outputs (Home  work)
x=id	#How  to  assign  ref  'x'  to  id()  function
print(x(25))	#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=len 		#How  to  assign  ref  'p'  to  len()  function
print(p("Hyd")) #How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd



#  Find  outputs (Home  work)
def  outer():
	print('Outer  function')	#Outer function
	def  inner():
		print('Inner  function')	#Inner function
	# End  of  inner  function
	print('Hello')	#Hello
	inner()
	print('Back  to  outer  function')	#Back to outer function
def  other():
	inner()		#error
	print('Other  function')
# End  of  the  function
print('Begin')	#Begin
outer()
print('Hi')	#Hi
inner()		#error
other()		#error
print('Bye')	#Bye





# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))	#60




# Find  outputs (Home  work)
def  outer():
	print('Outer  function')	#Outer function
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')
	print('Hi')		#Hi
	inner2()	#2nd  inner  function
	print('Hello')	#Hello
	inner1()	#1st  inner  function
	print('Back  to  outer  function')	#Back  to  outer  function
# End  of  the  function
print('Begin')	#Begin
outer()
print('Bye')	#Bye





# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)	#30
		print(globals()['x'])	#10
	inner()
outer()
print('Bye')	#Bye



# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)	#20
		print(globals()['x'])	#10
	inner()
outer()




# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)	#10
	inner()
outer()



# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)	#20
		x +=  7		#27
	# End  of  inner  function
	print(x)	#10
	x += 5		
	inner()
	print(x)	#15
# End  of  the  function
outer()
print('Bye')		#Bye



#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)	#10
		x = 20
		print(x)	#20
		x += 5
	# End  of  inner  function
	print(x)	#25
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
print(x)	#error x is not defined




#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)	#error
		nonlocal  x	#error
		x = 20
		print(x)	#20
		x += 5
	# End  of  inner  function
	print(x)	#15	
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
		print(x)	#20
		x += 5
	# End  of  inner  function
	print(x)	#10
	x += 5
	inner()
	print(x)	#15
# End  of  outer  function
outer()
print(x)	#25




# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x	#error x is not defined
		x = 20
		print(x)	#20
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)	#error x is not defined



# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)	#20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)	#25
# End  of  the  function
outer()
print(x)	#25




#  Identify  Error
def   f1():
        nonlocal   x	#error x is not defined


# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)	#100 20
	# End  of  inner  function
	print(a , b)	#10 20
	inner()
	print(a , b)	#100 200
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
print(f1())	#Hello



# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20	#error
		print(x)
	# End  of  inner  function
	gun()
# End  of  outer function
fun()	#10


#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x	#error x is not global and nonlocal




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
f1()	#10