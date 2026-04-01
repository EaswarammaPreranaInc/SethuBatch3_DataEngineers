x = 5
adder1 = lambda  y , x = x  : x + y # x=5
x = 10
adder2 = lambda  y , x = x : x + y # x=10
x = 20
print(adder1(100)) # 105
print(adder2(200)) # 210
print(adder1(300 , 400)) # 700

add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add() # x = 10
print(a(20)) # 30
print(add(30)(40)) # 70

a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b)  # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

c = sorted(a , reverse = True)
print(c)  # [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

d = sorted(a , key = lambda x : x[1])
print(d)  # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

e = sorted(a , key = lambda x : x[2])
print(e) # [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

f = sorted(a , key = lambda x : x[0])
print(f) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

g = sorted(a , key = lambda x : x[1] , reverse = True)
print(g) # [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]

print(sorted(a , key = x[1]))  # ERROR 

a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
      {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
      {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]

b = sorted(a , key = lambda x : x['Year'])
print(b) # [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]

print(sorted(a)) # ERROR

a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda x : x[0] )) # (25, 'Kiran', 1500.0)
print(max(a , key = lambda x : x[1] )) # (15, 'Vamsi', 2000.0)
print(max(a , key = lambda x : x[2] )) # (20, 'Sita', 2800.0)
print(max(a)) # (25, 'Kiran', 1500.0)

def f1():
    global a
    if a:
        print(a)        # 3 2 1
        a = a - 1
        f1()
        print('Hello')  # Hello Hello Hello
        print('Hi')     # Hi Hi Hi
        print(a)        # 0 0 0
    print('Bye')        # Bye Bye Bye Bye

a = 3
f1()
print('End')            # End

def f1(x , y):
    if x > 40:
        return
    x += y
    f1(x , y)
    print(x)   # 43 32 21 10
x = 10
f1(x , x := x + 1)
print(x)      # 11

def f1(x):
    print(x)        # 3 2 1 0
    if x:
        f1(x - 1)
    print(x)        # 0 1 2 3
f1(3)

def f1():
    print('f1 function')              
    f2()
def f2():
    print('f2 function')              
    f1()
# f1() # Infinite recursion → RuntimeError

def f1():
    print('f1    function')   
def f2():
    print('f2  function')   

f1()
f2()
print(f1 is f2) # False
f2 = f1
f2() # f1    function
print(f1 is f2) # True
f2 = f1() # f1    function
print(f2) # None
# f2() # ERROR 

p = print
p('Hyderabad') # Hyderabad
print = None
# print('Hello') # ERROR 
p('Hello') # Hello

x = id
x(25) # (memory address)
p = len
p('Hyd') # 3

def outer():
    print('Outer function')        
    def inner():
        print('Inner function')    
    print('Hello')                 
    inner()
    print('Back to outer function')

def other():
    # inner() # ERROR 
    print('Other function')

print('Begin') # Begin
outer()
print('Hi') # Hi
# inner() # ERROR

def   f1(a): 
	def   f2():
		return  10
	return  f2() + 20 +  a 
print(f1(30)) # 60

def outer():
    print('Outer function')
    def inner1():
        print('1st inner function')
    def inner2():
        print('2nd inner function') 
    print('Hi') # Hi
    inner2() # 2nd inner function
    print('Hello') # Hello
    inner1() # 1st inner function
    print('Back to outer function') # Back to outer function
outer() 

x = 10  
def outer():
    x = 20  
    def inner():
        x = 30
        print(x) # 30
        print(globals()['x']) # 10
    inner()
outer()

def  outer():
	x = 10
	def  inner():
		x = 20
		print(x) # 20
		x +=  7
	print(x) # 10
	x += 5
	inner()
	print(x) # 15
outer()

def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x) # 15
		x = 20
		print(x) # 20
		x += 5
	print(x) # 10
	x += 5
	inner()
	print(x) # 25
outer()

def  outer():
	x = 10
	def  inner():
		# print(x)
		# nonlocal x # ERROR 
		x = 20
	inner()
outer()

def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x) # 20
	print(x) # 10
	inner()
	print(x) # 15
outer()
print(x) # 25

def  outer():
	def  inner():
		# nonlocal x # SyntaxError
		pass
	inner()

def  outer():
	def  inner():
		global   x
		x = 20
		print(x) # 20
		x = x + 5
	inner()
	print(x) # 25
outer()
print(x) # 25

def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b) # 100 200
	print(a , b) # 10 20
	inner()
	print(a , b) # 100 20
outer()

def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	f2()
	return  x
print(f1()) # Hello

def  fun():
	x = 10
	def   gun():
		# x =  x +  20 # Error
		pass
	gun()

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