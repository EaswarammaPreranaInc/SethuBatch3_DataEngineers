# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) #105
print(adder2(200)) # 110
print(adder1(300 , 400)) #700



#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # 30
print(add(30)(40)) # 70



# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #  [ (5 , 'Amar' , 1300.0)) , (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()
c = sorted(a , reverse = True)
print(c)  #  [(20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (5 , 'Amar' , 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [(5 , 'Amar' , 1300.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e) #[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f) # [(5 , 'Amar' , 1300.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) # [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1]))



# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
      {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
      {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) # [{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999},{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} , {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ]
print(sorted(a)) # error



# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] )) # 25 , 'Kiran' , 1500.0
print(max(a , key = lambda  x  :  x[1] )) # 15 , 'Vamsi' , 2000.0
print(max(a , key = lambda  x  :  x[2] )) # 20 , 'Sita' , 2800.0
print(max(a)) # 25 , 'Kiran' , 1500.0



#   Find  outputs
def  f1():
	global  a
	if  a:
		print(a)
		a = a - 1
		f1() # 3
		print('Hello') # Hello
		print('Hi') # Hi
		print(a) # 2
	print('Bye') # Bye
# End  of  the  function
a = 3
f1()
print('End') # End


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
print(x) # 43 , 32, 21, 11



# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x) # 3 2 1 0
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
f1() # f1 function
     # f2 function
     # f1 function
     # f2 function
     # f1 function
     # f2 function


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
# f1 function
# f2 function
# False
# f2 function
  True
none


# Find  outputs (Home  work)
How  to  assign  ref  'p'  to  print()  function
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello') # Hello
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
#p = print
 p = none
 p('Hyderabad')
 p('Hello')



#  Find  outputs (Home  work)
def  outer():
	print('Outer  function') # outer function
	def  inner():
		print('Inner  function') # Inner function
	# End  of  inner  function
	print('Hello') # Hello
	inner()
	print('Back  to  outer  function') #Back to outer function
def  other():
	inner()
	print('Other  function')
# End  of  the  function
print('Begin') # Begin
outer()
print('Hi') # Hi
inner()
other()
print('Bye') # Bye



# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x) # 30
		print(globals()['x']) # 10
	inner()
outer()
print('Bye') # Bye


# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x) # 20
		print(globals()['x']) # 10
	inner()
outer()



# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x) # 10
	inner()
outer()



# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x) # 10
		x +=  7
	# End  of  inner  function
	print(x) #20
	x += 5
	inner()
	print(x) # 15
# End  of  the  function
outer()
print('Bye') # Bye



#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)  # 15
		x = 20
		print(x) # 20
		x += 5
	# End  of  inner  function
	print(x) 
	x += 5
	inner()
	print(x)  # 25
# End  of  outer  function
outer()
print(x) # 10



#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x) 
		nonlocal  # error
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
		print(x) # 20
		x += 5
	# End  of  inner  function
	print(x) # 10
	x += 5
	inner()
	print(x) # 15
# End  of  outer  function
outer()
print(x) # 25


# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x # error
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
		print(x) # 20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x) # 25
# End  of  the  function
outer()
print(x) # 25


#  Identify  Error
def   f1():
        nonlocal   x # error


# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b) # 100,200
	# End  of  inner  function
	print(a , b) # 10 , 20
	inner()
	print(a , b) # 100,20
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
		print(x) # error
	# End  of  inner  function
	gun()
# End  of  outer function
fun() # error


#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x # 
		nonlocal  x # error



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