'''Find outputs  (Home  work)'''
# x = 5
# adder1 = lambda  y , x = x  : x + y
# x = 10
# adder2 = lambda  y , x = x : x + y
# x = 20
# print(adder1(100))#105
# print(adder2(200))#210
# print(adder1(300 , 400))#700
'''Nested  lambda  function  (Home  work)'''
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))#30
print(add(30)(40))#70
'''Find  outputs'''
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
print(e) # [(15 ,'Rajesh' , 500.0),(10 , 'Rama' , 1000.0) ,(5 , 'Amar' , 1300.0) , (20 , 'Sita' , 2000.0),(18 , 'Kiran' , 2800.0)  ]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f) #   [(5 , 'Amar' , 1300.0)  , (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) # [(20 , 'Sita' , 2000.0),(10 , 'Rama' , 1000.0),(15 ,'Rajesh' , 500.0),(18 , 'Kiran' , 2800.0),(5 , 'Amar' , 1300.0)]
print(sorted(a , key = x[1])) #error
'''Find outputs  (Home  work)'''
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)
print(sorted(a))
'''output'''
# [{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008}, {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}]
# [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999}]
'''Find outputs  (Home  work)'''
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] ))#(25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] ))#(15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] ))#(20 , 'Sita' , 2800.0)
print(max(a))#(25, 'Kiran', 1500.0)
'''Find  outputs'''
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
'''output'''
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
'''Tricky  program'''
#  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y #(10,11),(21,11),(32,11),(43,11)
	f1(x , y)
	print(x)
# End  of  the  function
x = 10
f1(x , x := x + 1)#(10,11)
print(x)
'''output'''
# 43
# 32
# 21
# 11
'''Find  outputs   (Home  work)'''
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)
'''output'''
# 3
# 2
# 1
# 0
# 0
# 1
# 2
# 3
'''  Find  outputs'''
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()
'''output'''
# f1 function
# f2 function
# f1 function
# f2 function
# f1 function
# f2 function
# ...because there is no flase condition
'''Find  outputs  (Home  work)'''
def  f1():
        print('f1    function')
def  f2():
        print('f2  function')
End  of  the  function
f1()
f2()
print(f1  is  f2)
f2 = f1
f2()
print(f1  is  f2)
f2 = f1()
print(f2)
f2()
'''output'''
# f1  function
# f2  function
# False
# f1  function
# True
# f1 function
# None
''' Find  outputs (Home  work)'''
p=print#How  to  assign  ref  'p'  to  print()  function
p('Hyderabad')# How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print=None# print = None
# print('Hello')
p('Hello')# How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
'''# Find   outputs (Home  work)'''
x=id# How  to  assign  ref  'x'  to  id()  function
print(x(25))# How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=len# How  to  assign  ref  'p'  to  len()  function
print(p('Hyd'))# How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
'''Find  outputs (Home  work)'''
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
'''# Find  output(Home  work)'''
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a  # 60
# End  of  f1  function
print(f1(30))
'''Find  outputs (Home  work)'''
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
'''output'''
# Begin
# Outer  function
# Hi
# 2nd  inner  function
# Hello
# 1st  inner  function
# Back  to  outer  function
# Bye
'''Find  outputs  (Home  work)'''
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
''' Find  outputs  (Home   work)'''
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)#20
		print(globals()['x'])#10
	inner()
outer()
'''Find  outputs  (Home  work)'''
x = 10
def  outer():
	def   inner():
		print(x)#10
	inner()
outer()
''' Find  outputs  (Home  work)'''
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)#20
		x +=  7
	# End  of  inner  function
	print(x)#10
	x += 5
	inner()
	print(x)#15
# End  of  the  function
outer()
print('Bye')#Bye
'''  Find  outputs  (Home  work)'''
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
'''output'''
# 10
# 15
# 20
# 25
'''  Find  outputs  (Home  work)'''
def  outer():
	x = 10
	def  inner():
		print(x)
		#nonlocal  x #Error
		x = 20
		print(x)   #20
		x += 5
	# End  of  inner  function
	print(x)#10
	x += 5
	inner()
	print(x)#15
# End  of  outer  function
outer()
'''Find   outputs(Home  work)'''
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
'''output'''
# 10
# 20
# 15
# 25
''' Find  outputs(Home  work)'''
def  outer():
	def  inner():
		nonlocal  x # Error
		x = 20
		print(x) #20
	# End  of  inner  function
	inner()
	print(x)#Error--x is not defined in outer
# End  of  the  function
outer()
print(x)#Error--x is not defined in outer
''' Find  outputs(Home  work)'''
def  outer():
	def  inner():
		global   x
		x = 20
		print(x) #20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)#25
# End  of  the  function
outer()
print(x)#25
'''Identify  Error'''
def   f1():
        nonlocal   x #Error---there is no local host
'''Find  outputs (Home  work)'''
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)#(10,20)
	# End  of  inner  function
	print(a , b)#(100,200)
	inner()
	print(a , b)#(100,20)
#end of outer function
outer()
''' Find  outputs (Home  work)'''
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	# End  of  inner  function
	f2()
	return  x #Hello
# End  of  outer  function
# print(f1())
''' Find  output(Home  work)'''
def  fun():
	x = 10
	def    gun():
		x =  x +  20 #Error---x is not defined
		print(x)
	# End  of  inner  function
	gun()
# End  of  outer function
fun()
'''Identify  Error'''
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x#error--no local host
'''  Find  outputs  (Home   work)'''
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





