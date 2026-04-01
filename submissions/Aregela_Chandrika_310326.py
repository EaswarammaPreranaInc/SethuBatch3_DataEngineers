# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) # 5+100=105
print(adder2(200)) # 10+200=210
print(adder1(300 , 400)) # 700


#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # 10+20=30
print(add(30)(40)) # 30+40=70


# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #  [()  , () , () , () , ()]
print()
c = sorted(a , reverse = True)
print(c)  #  [() , () , () , () , ()]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [() , () , () , () , ()]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)
print(sorted(a , key = x[1]))




# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)  
 '''[
 {'Make': 'Tesla', 'Model': 'X', 'Year': 1999},
 {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008},
 {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}
 ]'''
print(sorted(a)) # Error 



# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] )) # (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) # (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) # (20, 'Sita', 2800.0)
print(max(a)) # (25, 'Kiran', 1500.0)



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
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)



#  Find  outputs
def  f1():
	print('f1  function') # f1 function
	f2()
	print('End  of  f1  function') # 
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()



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


# Find  outputs (Home  work)
How  to  assign  ref  'p'  to  print()  function
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'



# Find   outputs (Home  work)
How  to  assign  ref  'x'  to  id()  function
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
How  to  assign  ref  'p'  to  len()  function
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd

'''
x = id
print(x(25))

p = len
print(p('Hyd')) '''


#  Find  outputs (Home  work)
def  outer():
	print('Outer  function') # Outer function
	def  inner():
		print('Inner  function')
	# End  of  inner  function
	print('Hello') # Outer function
	inner()
	print('Back  to  outer  function') # Inner function
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




# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) # 60



# Find  outputs (Home  work)
def  outer():
	print('Outer  function') # Outer function
	def  inner1():
		print( '1st  inner  function') # 1st  inner  function
	def  inner2():
		print('2nd  inner  function')  # 2nd  inner  function
	print('Hi') # Hi 
	inner2()
	print('Hello') # Hello
	inner1()
	print('Back  to  outer  function') # Back  to  outer  function
# End  of  the  function
print('Begin') # Begin
outer()
print('Bye')




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
	print(x) # 20
	x += 5
	inner()
	print(x) # 
# End  of  the  function
outer()
print('Bye') # Bye



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
print(x)  # 25



#  Identify  Error
def   f1():
        nonlocal   x  # x is not found in outer function
        
        
        
# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b) # 10 20 
	# End  of  inner  function
	print(a , b) # 100 200
	inner()
	print(a , b) # 100 20
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
print(f1())







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


#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x
        
        
        
        
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
