1) outputs  
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))#105
print(adder2(200))#210
print(adder1(300 , 400))#700

2) #Nested  lambda  function 
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))#30
print(add(30)(40))#70

3) outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a , reverse = True)
print(c)  # [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)#[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)#[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)#[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1]))

4) outputs  
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)#[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a))#Error because it is not permitted

5) outputs  
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  
print(max(a , key = lambda  x  :  x[0] ))#(25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] ))#(15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] ))#(20, 'Sita', 2800.0)
print(max(a))#(25, 'Kiran', 1500.0)

6) Tricky  program
#outputs
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)
# End  of  the  function
x = 10
f1(x , x := x + 1)
print(x)#43
	 32
	 21
	 11

7) outputs  
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)#3
      2
      1
      0
      0
      1
      2
      3

8) outputs
def  f1():
	print('f1  function')#f1 function
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')#f2 function
	f1()
	print('End  of  f2  function')
f1()

9) outputs 
def  f1():
        print('f1    function')#f1 function
def  f2():
        print('f2  function')#f2 function
# End  of  the  function
f1()
f2()
print(f1  is  f2)#False
f2 = f1
f2()
print(f1  is  f2)#True
f2 = f1()
print(f2)
f2()

10) outputs 
p = print() #How  to  assign  ref  'p'  to  print()  function
p('Hyderabad') #How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
p = print
print = None
print('Hello')
p('Hello') #How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'

11) outputs
x = id #How  to  assign  ref  'x'  to  id()  function
print(x(25)) #How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len #How  to  assign  ref  'p'  to  len()  function
p = (p('Hyd')) #How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd

12) outputs 
def  outer():
	print('Outer  function')#Outer function
	def  inner():
		print('Inner  function')#Inner function
	# End  of  inner  function
	print('Hello')#Hello
	inner()
	print('Back  to  outer  function')#Back to outer function
def  other():
	inner()
	print('Other  function')
# End  of  the  function
print('Begin')#Begin
outer()
print('Hi')#Hi
inner()
other()
print('Bye')#Bye

13) output
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))#60

14) outputs 
def  outer():
	print('Outer  function')#Outer function
	def  inner1():
		print( '1st  inner  function')#1st inner function
	def  inner2():
		print('2nd  inner  function')#2nd inner function
	print('Hi')#Hi
	inner2()
	print('Hello')#Hello
	inner1()
	print('Back  to  outer  function')#Back to outer function
# End  of  the  function
print('Begin')#Begin
outer()
print('Bye')#Bye

15) outputs 
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

16) outputs  
x = 10  
def  outer():
	x = 20
	def   inner():
		print(x)#20
		print(globals()['x'])#10
	inner()
outer()

17) outputs 
x = 10
def  outer():
	def   inner():
		print(x)#10
	inner()
outer()

18) outputs 
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

19) outputs
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)#10
		x = 20
		print(x)#20
		x += 5
	# End  of  inner  function
	print(x)#15
	x += 5
	inner()
	print(x)#25
# End  of  outer  function
outer()
print(x)#Error x is not defined

20) outputs  
def  outer():
	x = 10
	def  inner():
		print(x)#10
		nonlocal  x #Error because it is not valid
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()#Error because it is not valid
	print(x)
# End  of  outer  function
outer()

21) outputs
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)#20
		x += 5
	# End  of  inner  function
	print(x)#15
	x += 5
	inner()
	print(x)#25
# End  of  outer  function
outer()
print(x)#10

22) outputs
def  outer():
	def  inner():
		nonlocal  x #Error because it is not valid
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)

23) outputs
def  outer():
	def  inner():
		global   x
		x = 20
                print(x)#20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)#25
# End  of  the  function
outer()
print(x)#25

24) Identify  Error
def   f1():
        nonlocal   x #Error because x is not defined

25) outputs 
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)#10 20
	# End  of  inner  function
	print(a , b)#100 200
	inner()
	print(a , b)#100 20
#end of outer function
outer()

26) outputs 
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

27) output
def  fun():
	x = 10
	def    gun():
		x =  x +  20 #Error because x is local variable
		print(x)
	# End  of  inner  function
	gun()#Error because x is local variable
# End  of  outer function
fun()#Error because x is local variable

28) Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x #Error because it gets confused 
		nonlocal  x

29) outputs 
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