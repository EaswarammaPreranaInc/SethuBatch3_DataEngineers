'''
1) # Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))  # 105
print(adder2(200))  # 210
print(adder1(300 , 400))  # 700
'''
'''
2) #Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))  # 30
print(add(30)(40))  # 70
'''
'''
3) # Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b)  # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a , reverse = True)
print(c)  # [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)  # [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)  # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)  # [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1]))  # Error because x is not defined
'''
'''
4) # Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)  # [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a))  # Error because dictionaries cannot be compared like that
'''
'''
5) # Find outputs  (Home  work)
a = ((10, 'Rama', 1000.0),(20, 'Sita', 2800.0),(15, 'Vamsi', 2000.0),(25, 'Kiran', 1500.0),(5, 'Amar', 1300.0))
print(max(a, key=lambda x: x[0]))  # (25, 'Kiran', 1500.0)
print(max(a, key=lambda x: x[1]))  # (15, 'Vamsi', 2000.0)
print(max(a, key=lambda x: x[2]))  # (20, 'Sita', 2800.0)
print(max(a  # (25, 'Kiran', 1500.0)
'''
'''
6)  # Find  outputs
def f1():
    global a
    if a:
        print(a)
        a = a - 1
        f1()
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')
# End of the function

a = 3
f1()
print('End')   # 3 <nextline> 2 <nextline> 1 <nextline> Bye <nextline> Hello <nextline> Hi <nextline> 0 <nextline> Bye <nextline> Hello <nextline> Hi <nextline> 0                              <nextline> Bye <nextline> Hello <nextline> Hi <nextline> 0 <nextline> Bye <nextline> End
'''
'''
7) def f1(x, y):
    if x > 40:
        return
    x += y
    f1(x, y)
    print(x)
x = 10
f1(x, x := x + 1)
print(x)   # 43 <nextline> 32 <nextline> 21 <nextline> 10 <nextline> 11
'''
'''
8) def f1(x):
    print(x)
    if x:
        f1(x - 1)
    print(x)
# End of the function
f1(3)   # 3 <nextline> 2 <nextline> 1 <nextline> 0 <nextline> 0 <nextline> 1 <nextline> 2 <nextline> 3
'''
'''
9) def f1():
    print('f1  function')
    f2()
    print('End  of  f1  function')
def f2():
    print('f2  function')
    f1()
    print('End  of  f2  function')
f1()  # f1 function <nextline> f2  function <nextline> f1  function <nextline> f2  function <nextline> ...Error: because there is no condition specified for it to stop
'''
'''
10) def f1():
    print('f1    function')
def f2():
    print('f2  function')
# End of the function
f1()
f2()
print(f1 is f2)
f2 = f1
f2()
print(f1 is f2)
f2 = f1()
print(f2)
f2() # f1    function <nextline> f2  function <nextline> False <nextline> f1    function <nextline> True <nextline> f1    function <nextline> None <nextline> TError because None is not callable
'''
'''
11) # Find  outputs (Home  work)
How  to  assign  ref  'p'  to  print()  function
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
'''
p = print
p('Hyderabad')
print = None
p('Hello')
'''
12) # Find   outputs (Home  work)
How  to  assign  ref  'x'  to  id()  function
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
How  to  assign  ref  'p'  to  len()  function
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
'''
x = id
print(x(25))
p = len
print(p('Hyd'))
'''
'''
13) #  Find  outputs (Home  work)
def outer():
    print('Outer  function')
    def inner():
        print('Inner  function')
    # End of inner function
    print('Hello')
    inner()
    print('Back  to  outer  function')
def other():
    inner()
    print('Other  function')
# End of the function
print('Begin')
outer()
print('Hi')
inner()  # Error because inner is not defined (def is not written at upside)
other()
print('Bye')   # Begin <nextline> Outer  function <nextline> Hello <nextline> Inner  function <nextline> Back  to  outer  function <nextline> Hi
'''
'''
14) # Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))  # 60
'''
'''
15) # Find  outputs  (Home   work)
def outer():
    print('Outer  function')
    def inner1():
        print('1st  inner  function')
    def inner2():
        print('2nd  inner  function')
    print('Hi')
    inner2()
    print('Hello')
    inner1()
    print('Back  to  outer  function')
# End of the function
print('Begin')
outer()
print('Bye')   # Begin <nextline> Outer  function <nextline> Hi <nextline> 2nd  inner  function <nextline> Hello <nextline> 1st  inner  function <nextline> Back  to  outer  function <nextline> Bye
'''
'''
16)  # Find  outputs  (Home   work) 
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)
        print(globals()['x'])
    inner()
outer()
print('Bye')   # 30 <nextline> 10 <nextline> Bye
'''
'''
17) # Find  outputs  (Home   work)
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)
        print(globals()['x'])
    inner()
outer()
print('Bye')  # 30 <nextline> 10 <nextline> Bye
'''
'''
18) # Find  outputs  (Home   work)
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()  # 20 <nextline> 10
'''
'''
19) # Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()  # 10
'''
'''
20) # Find  outputs  (Home  work)
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
print('Bye')  # 10 <nextline> 20 <nextline> 15 <nextline> Bye
'''
'''
21) #  Find  outputs  (Home  work)
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
outer()  # 10 <nextline> 15 <nextline> 20 <nextline> 25 <nextline> NameError: name 'x' is not defined
print(x)  # Error because x is not defined
'''
'''
22) #  Find  outputs  (Home  work)
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
outer()  # Error
'''
'''
23) def outer():
    x = 10
    def inner():
        global x
        x = 20
        print(x)
        x += 5
    # End of inner function
    print(x)
    x += 5
    inner()
    print(x)
# End of outer function
outer()
print(x)  # 10 <nextline> 20 <nextline> 15 <nextline> 25
'''
'''
24) # Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()  # Error
print(x)
'''
'''
25) def outer():
    def inner():
        global x
        x = 20
        print(x)
        x = x + 5
    # End of inner function
    inner()
    print(x)
# End of the function
outer()
print(x)   # 20 <nextline> 25 <nextline> 25
'''
'''
26) #  Identify  Error
def   f1():
        nonlocal   x  # Error because There is no variable named x in outer function
'''
'''
27) def outer():
    a = 10
    b = 20
    def inner():
        nonlocal a
        a = 100
        b = 200
        print(a, b)
    # End of inner function
    print(a, b)
    inner()
    print(a, b)
# end of outer function
outer()   # 10 20 <nextline> 100 200 <nextline> 100 20
'''
'''
28) # Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	# End  of  inner  function
	f2()
	return  x
# End  of  outer  function
print(f1())  # Hello
'''
'''
29) # Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)
	# End  of  inner  function
	gun()
# End  of  outer function
fun()   #  Error because local variable 'x' is before assignment
'''
'''
30) #  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x  # Error because x is non local and global which is not possible
'''
'''
31) #  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)
		f3()
	f2()
f1()  # 10
'''