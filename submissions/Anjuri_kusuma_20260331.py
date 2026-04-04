 # Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))#120
print(adder2(200))#220
print(adder1(300 , 400))#700
----------------------------------------------------------
 #Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()#type and add
print(a(20))#30
print(add(30)(40))#70
------------------------------------------------------------
 # Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #[(5 , 'Amar' , 1300.0),(10 , 'Rama' , 1000.0),(15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()
c = sorted(a , reverse = True)
print(c)  #  [(20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (5 , 'Amar' , 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)#[(5 , 'Amar' , 1300.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)#[(15 ,'Rajesh' , 500.0),(10 , 'Rama' , 1000.0),(5 , 'Amar' , 1300.0),(20 , 'Sita' , 2000.0),(18 , 'Kiran' , 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)#[(5 , 'Amar' , 1300.0),(10 , 'Rama' , 1000.0),(15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)#[(20 , 'Sita' , 2000.0),(10 , 'Rama' , 1000.0),(15 ,'Rajesh' , 500.0),(18 , 'Kiran' , 2800.0),(5 , 'Amar' , 1300.0)]
print(sorted(a , key = x[1]))#error
---------------------------------------------------------------
 # Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)[{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999},{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},{'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}]
print(sorted(a))#[{'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013},{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008}, {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999}]
---------------------------------------------------------------
 # Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] ))#(25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] ))#(15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] ))#(20 , 'Sita' , 2800.0)
print(max(a))#(25 , 'Kiran' , 1500.0)
----------------------------------------------------------------
 # Find  outputs   (Home  work)
def  f1(x):                         #3
	print(x)#3                  #2
	if   x:                     #1
		f1(x - 1)           #0 
	print(x)#2                  #0
# End  of  the  function            #1
f1(3)                               #2
----------------------------------------------------------------
 #  Find  outputs
def  f1():                            #f1 function
	print('f1  function')         #f2 function
	f2()                          #f1 function
	print('End  of  f1  function')#........continues no stop
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()
---------------------------------------------------------------
 #  Find  outputs  (Home  work)
def  f1():                        #f1 function
        print('f1    function')   #f2 function
def  f2():                        #False
        print('f2  function')     #f2 function
# End  of  the  function          #True
f1()                              
f2()
print(f1  is  f2)#False
f2 = f1 
f2()
print(f1  is  f2)
f2 = f1()
print(f2)
f2()
----------------------------------------------------------------
 # Find  outputs (Home  work)
p=print #How  to  assign  ref  'p'  to  print()  function
p("Hyderabad") #How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')#error
p("Hello") #How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
-----------------------------------------------------------------
# Find   outputs (Home  work)
x=id #How  to  assign  ref  'x'  to  id()  function
x() # How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=len #How  to  assign  ref  'p'  to  len()  function
p() #How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
------------------------------------------------------------------
#  Find  outputs (Home  work)
def  outer():                                #Begin
	print('Outer  function')             #outer function
	def  inner():                        #Hello
		print('Inner  function')     #Back to outer function
	# End  of  inner  function           #Hi
	print('Hello')                       #error
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
--------------------------------------------------------------------
 # Find  output(Home  work)                 #10+20+30=60
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))
-------------------------------------------------------------------
 # Find  outputs (Home  work)                       #Begin
def  outer():                                       #Outer function
	print('Outer  function')                    #Hi
	def  inner1():                              #2nd inner function
		print( '1st  inner  function')      #Hello
	def  inner2():                              #1st inner function
		print('2nd  inner  function')       #Back to outer function
	print('Hi')                                 #Bye
	inner2()
	print('Hello')
	inner1()
	print('Back  to  outer  function')
# End  of  the  function
print('Begin')
outer()
print('Bye')
--------------------------------------------------------------
 # Find  outputs  (Home  work)            #30
x = 10                                    #10
def  outer():                             #Bye
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer()
print('Bye')
----------------------------------------------------------------
 # Find  outputs  (Home   work)               #20
x = 10                                        #10
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()
------------------------------------------------------------------
 # Find  outputs  (Home  work)           #10
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()
-----------------------------------------------------------------
 # Find  outputs  (Home  work)
def  outer():                             #10
	x = 10                            #20
	def  inner():                     #15
		x = 20                    #Bye
		print(x)
		x +=  7--->27
	# End  of  inner  function
	print(x)
	x += 5--->15
	inner()
	print(x)
# End  of  the  function
outer()
print('Bye')
------------------------------------------------------------------
 #  Find  outputs  (Home  work)
def  outer():                     #10
	x = 10                    #15
	def  inner():             #20
		nonlocal  x       #25
		print(x)          #error
		x = 20
		print(x)
		x += 5--->25
	# End  of  inner  function
	print(x)
	x += 5-->15
	inner()
	print(x)
# End  of  outer  function
outer()
print(x)
--------------------------------------------------------------------
 #  Find  outputs  (Home  work)
def  outer():                         #10
	x = 10                        #error
	def  inner():                 #20
		print(x)              #25
		nonlocal  x           
		x = 20
		print(x)
		x += 5-->25
	# End  of  inner  function
	print(x)
	x += 5--->15
	inner()
	print(x)
# End  of  outer  function
outer()
--------------------------------------------------------------------
 #  Find   outputs(Home  work)              #10
def  outer():                               
	x = 10                              #20
	def  inner():                       #15
		global   x                  #25
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
--------------------------------------------------------------------
 # Find  outputs(Home  work)                 #error x is not defined
def  outer():                                #20
	def  inner():                        #error
		nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)
----------------------------------------------------------------------
 # Find  outputs(Home  work)               #20
def  outer():                              #25
	def  inner():                      #25
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
-------------------------------------------------------------------
 #  Identify  Error               #x is not defined
def   f1():
        nonlocal   x
------------------------------------------------------------------
 # Find  outputs (Home  work)           #10 20
def  outer():                           #100 200
	a = 10                          #100 20
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
--------------------------------------------------------------------
# Find  outputs (Home  work)            #John
def   f1():                             #Hello
	x = 'John'                      #Hello
	def  f2():
		nonlocal  x
		x =  'Hello'
	# End  of  inner  function
	f2()
	return  x
# End  of  outer  function
print(f1())
-------------------------------------------------------------------
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
------------------------------------------------------------------
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x
--------------------------------------------------------------------
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