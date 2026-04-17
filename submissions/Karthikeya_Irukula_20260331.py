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
print(b) #  [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print() #<next line>
c = sorted(a , reverse = True)
print(c)  #  [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e) #  [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)  #  [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)  #  [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1])) # Error x is not defined 


# Find outputs  (Home  work)

a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) #[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a)) #Error due to key is not called.


# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] )) #(25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] )) #(15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] )) #(20 , 'Sita' , 2800.0)
print(max(a)) #(25 , 'Kiran' , 1500.0)


#   Find  outputs
def  f1():
	global  a
	if  a:
		print(a) #3 <nextline> 2 <nextline> 1
		a = a - 1
		f1()
		print('Hello') #Hello
		print('Hi') # Hi
		print(a) #2
	print('Bye') #Bye
# End  of  the  function
a = 3
f1()
print('End') #End

'''
output:
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
End '''



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
print(x) #11

'''
output:
43 <nextline> 32 <nextline> 21 <nextline> 11
'''

# Find  outputs   (Home  work)
def  f1(x):
	print(x) #3
	if   x:
		f1(x - 1)
	print(x)  
# End  of  the  function
f1(3)

'''
output:
3 <nextline> 2 <nextline> 1 <nextline> 0 <nextline> 0 <nextline> 1 <nextline> 2 <nextline> 3
'''


#  Find  outputs

def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1() # Error f1() is infinite.


#  Find  outputs  (Home  work)

def  f1():
        print('f1    function') 
def  f2():
        print('f2  function') 
# End  of  the  function
f1()#'f1    function'
f2() #'f2  function'
print(f1  is  f2) # False
f2 = f1
f2() #'f1    function'
print(f1  is  f2) #True
f2 = f1() #'f1    function'
print(f2) # None
f2() #Error due to no values / None


# Find  outputs (Home  work)
p = print #How  to  assign  ref  'p'  to  print()  function
p("Hyderabad")#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello') #Error due to None
p('Hello')#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello



# Find   outputs (Home  work)
x = id#How  to  assign  ref  'x'  to  id()  function
print(x(25))#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len #How  to  assign  ref  'p'  to  len()  function
print(p('Hyd'))#How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd'



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
	inner()
	print('Other  function')
# End  of  the  function
print('Begin') #Begin
outer() # 'Outer  function' <nextline> 'Hello' <nextline> 'Back  to  outer  function'
print('Hi') #Hi
inner() #Error not defined
other() #'Other  function'
print('Bye') #Bye



# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) #60



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
print('Begin') # 'Begin'
outer() # 'Outer  function' <nextline> 'Hi' <Nextline> '2nd  inner  function' <Nextline> 'Hello' <nextline> '1st  inner  function' <nextline> 'Back  to  outer  function'
print('Bye') #Bye



# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x) #30
		print(globals()['x']) #10
	inner()
outer() 
print('Bye') #Bye



# Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer() # 20 <nextline> 10



# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()  #10


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
outer() #10 <nextline> 20 <nextline> 15
print('Bye') #Bye




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
outer() # 10 <nextline> 15 <nextline> 20 <nextline> 15
print(x) # Error not defined x




#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)
		#nonlocal  x #Error it should be defined before print function
		x = 20
		print(x) #20
		x += 5
	# End  of  inner  function
	print(x) #10
	x += 5
	inner()
	print(x) #15
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
outer() #10 <nextline> 20 <nextline> 15
print(x) #25



# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x # X is not defined in global so error.
		x = 20
		print(x) # 20
	# End  of  inner  function
	inner()
	print(x) # x is not defined.
# End  of  the  function
outer() 
print(x) #Error



# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x 
		x = 20
		print(x) # 20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x) #25
# End  of  the  function
outer() #
print(x) #25



#  Identify  Error
def   f1():
        nonlocal   x #x is not defined globally.
		



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
outer() # 10 , 20 <nextline> 100,200 <nextline> 100 ,20




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
print(f1()) # 'Hello'



# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20 #Error due to x is not defined.
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
		nonlocal  x #Error
		

#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x) #10
		f3()
	f2()
f1() 