# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) #105
print(adder2(200)) #210
print(adder1(300 , 400)) #700



#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) #30
print(add(30)(40)) #70



# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a) 
print(b) #  #[(5,'Amar',1300.0),(10,'Rama',1000.0),(15,'Rajesh',500.0),(17,'Kiran',28000.0),(20,'Sita',2000.0)]
print()
c = sorted(a , reverse = True)
print(c)  # #[(20,'Sita',2000.0),(17,'Kiran',28000.0),(15,'Rajesh',500.0),(10,'Rama',1000.0),(5,'Amar',1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [(5,'Amar',1300.0),(17,'Kiran',28000.0),(15,'Rajesh',500.0),(10,'Rama',1000.0),(20,'Sita',2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2]) 
print(e) #[(15,'Rajesh',500.0),(10,'Rama',1000.0),(5,'Amar',1300.0),(20,'Sita',2000.0),(17,'Kiran',28000.0)]
print()
f = sorted(a , key = lambda   x  :  x[0]) 
print(f) 
print() #[(5,'Amar',1300.0),(10,'Rama',1000.0),(15,'Rajesh',500.0),(17,'Kiran',28000.0),(20,'Sita',2000.0)]
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) #[(20,'Sita',2000.0),(17,'Kiran',28000.0),(15,'Rajesh',500.0),(10,'Rama',1000.0),(5,'Amar',1300.0)]
print(sorted(a , key = x[1])) #Error 



# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) #[{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999},{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},{'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}]
print(sorted(a)) #Error



# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] )) #(20 , 'Sita' , 2800.0)
print(max(a , key = lambda  x  :  x[1] )) #(15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] )) #(20 , 'Sita' , 2800.0
print(max(a)) #(25 , 'Kiran' , 1500.0)



#   Find  outputs
def  f1():
	global  a
	if  a:
		print(a) #3 None 2 none 
		a = a - 1 #3-1 = 2-1 = 1-1 =0
		f1()
		print('Hello') #hello 
		print('Hi') #Hi
		print(a) #0
	print('Bye') #Bye
# End  of  the  function
a = 3
f1()
print('End') #End 



def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))
[1:20 pm, 31/03/2026] +91 99482 50500: # Find  outputs (Home  work)
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
[1:20 pm, 31/03/2026] +91 99482 50500: # Find  outputs  (Home  work)
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
[1:20 pm, 31/03/2026] +91 99482 50500: # Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()
[1:21 pm, 31/03/2026] +91 99482 50500: # Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()
[1:21 pm, 31/03/2026] +91 99482 50500: # Find  outputs  (Home  work)
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
[1:31 pm, 31/03/2026] +91 99482 50500: #  Find  outputs  (Home  work)
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
[1:31 pm, 31/03/2026] +91 99482 50500: #  Find  outputs  (Home  work)
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
[1:31 pm, 31/03/2026] +91 99482 50500: #  Find   outputs(Home  work)
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
[1:31 pm, 31/03/2026] +91 99482 50500: # Find  outputs(Home  work)
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
[1:31 pm, 31/03/2026] +91 99482 50500: # Find  outputs(Home  work)
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
[1:31 pm, 31/03/2026] +91 99482 50500: #  Identify  Error
def   f1():
        nonlocal   x
[1:33 pm, 31/03/2026] +91 99482 50500: # Find  outputs (Home  work)
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
[1:33 pm, 31/03/2026] +91 99482 50500: # Find  outputs (Home  work)
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
[1:33 pm, 31/03/2026] +91 99482 50500: # Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)
	# End  of  inner  function
	gun()
# End  of  outer function
fun()
[1:34 pm, 31/03/2026] +91 99482 50500: #  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x
[1:34 pm, 31/03/2026] +91 99482 50500: #  Find  outputs  (Home   work)
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
