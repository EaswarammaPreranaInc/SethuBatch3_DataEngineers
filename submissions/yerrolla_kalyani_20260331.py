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
a = add()#error second argument is missing 
print(a(20))#30
print(add(30)(40))#70

# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #  [(5 , 'Amar' , 1300.0)  , (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()#nothimg is printed
c = sorted(a , reverse = True)
print(c)  #  [(20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (5 , 'Amar' , 1300.0)]
print()#nothing is printed 
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [(5 , 'Amar' , 1300.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0)]
print()#nothimg is printed
e = sorted(a , key =  lambda   x  :  x[2])
print(e)#[(15 ,'Rajesh' , 500.0),(10 , 'Rama' , 1000.0),(5 , 'Amar' , 1300.0),(20 , 'Sita' , 2000.0),(18 , 'Kiran' , 2800.0)]
print()#nothimg is printed
f = sorted(a , key = lambda   x  :  x[0])
print(f) #  [(5 , 'Amar' , 1300.0)  , (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()#nothimg is printed
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)#[(20 , 'Sita' , 2000.0),(10 , 'Rama' , 1000.0),(15 ,'Rajesh' , 500.0), (18 , 'Kiran' , 2800.0),(5 , 'Amar' , 1300.0)  ]
print(sorted(a , key = x[1]))#error it is not lambda function and ,and x[1] is invalid 

# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])# [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,  {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
print(b)# [  {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,  {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},{'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ]
print(sorted(a))####


#  Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] ))#(25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] ))#(15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] ))#(20 , 'Sita' , 2800.0)
print(max(a))#(25 , 'Kiran' , 1500.0)


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
	#inner()#error def and : are mandatory to create the function 
	print('Other  function')#Other function
# End  of  the  function
print('Begin')#Begin
outer()#Outer  function <nextline> Hello   <nextline>Inner  function <nextline> Inner  function <nextline>Back  to  outer  function
print('Hi')#Hi
# inner()#error outer funtions can only access the inner function outside the function statments and other funtions cannot access the outer function 
other()#error <nxtline>Other function 
print('Bye')#bye


# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))# 60


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
print('Begin')#Begin
outer()#Hi<nxt>Outer  function<nxt> Hii <nxt>2nd  inner  function <nextline> Hello <nxt> 1st  inner  function <nextline>Back  to  outer  function
print('Bye')#Bye
 

# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer()#30<nxt>10
print('Bye')#Bye


# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()#20<nxt>10



# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()#10



 
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
outer()#10<nxt>20<nxt>15<nxt>
print('Bye')#Bye



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
outer()#10<nxt><nxt>15<nxt>20<nxt>25<nxt>
print(x)#x is not defined



#   Find  outputs  (Home  work)
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
outer()#10<nxt>15<nxt>20<nxt>25



#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)
		x += 5#25 gv
	# End  of  inner  function
	print(x)
	x += 5#15
	inner()
	print(x)
# End  of  outer  function
outer()#10<nxt>20<nxt>15
print(x)#25


# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x#error because there is no non local x to use in this function
		x = 20
		print(x)#20 if no nonlocal  x
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()#20<nxt>x is not defined 
print(x)# x is not defined



# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)
		x = x + 5#25
	# End  of  inner  function
	inner()
	print(x)#25
# End  of  the  function
outer()#20<nxt>25<nxt>
print(x)#25



#  Identify  Error
def   f1():
        nonlocal   x# error ,nonlocal keyword should use only in the innerfunctions  or nested functions where fi is just an single function so nonlocal keyword is not allowed



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
outer()#10<space>20<space>100<space>200<space>100<space>20



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
		x =  x +  20#error creating Lv but right side agsin x so a functin variable behaves 100% as Gv or Lv but not 50-50.
		print(x)#10 ,ie. x =  x +  20 if this line is not present  in function block
	# End  of  inner  function
	gun()
# End  of  outer function
fun()#10


 #  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x#error asking function to use gv x=10 and again telling use x=20 of nonlocal variable (outer function )so error 100% as Gv or Lv but not 50-50.

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
f1()#10