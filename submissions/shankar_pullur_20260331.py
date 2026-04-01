x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))  # 105
print(adder2(200))  #210
print(adder1(300 , 400)) #700

add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) #30
print(add(30)(40)) #70


a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
print(b) #  [(5 , 'Amar' , 1300.0), (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()
c = sorted(a , reverse = True)
print(c)  #  [(20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (5 , 'Amar' , 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)  #  [(5 , 'Amar' , 1300.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) ,(10 , 'Rama' , 1000.0)  , (20 , 'Sita' , 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)  #[(15 ,'Rajesh' , 500.0) ,(10 , 'Rama' , 1000.0),(5 , 'Amar' , 1300.0),(18 , 'Kiran' , 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)#[(5 , 'Amar' , 1300.0), (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (20 , 'Sita' , 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)  #[(20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0) , (15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0) , (5 , 'Amar' , 1300.0)]
#print(sorted(a , key = x[1])) error


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

'''
3
2
1
bye
hello  hello hello 
hi     hi    hi    
0      0      0    
bye   bye    bye
end
'''


def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x) 
# End  of  the  function
x = 10
f1(x , x := x + 1)
print(x) # 11
'''
43
32
21
11
'''

def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)
'''
3
2
1
0
0
3
2
1





'''

def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
#f1()

'''
infinite calls function1 and function2
'''

def  f1():
        print('f1    function')
def  f2():
        print('f2  function')
# End  of  the  function
f1()   # f1 function
f2()   # f2 function
print(f1  is  f2) # false
f2 = f1
f2()   # f1 function
print(f1  is  f2) # True
f2 = f1()  # f1 function
print(f2)  #None
#f2()   error

p=print
print("hello world")
p("hyderabad")
#print = None
#print('Hello') # error
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
p=print
p("hello")


def  outer():
	print('Outer  function')
	def  inner():
		print('Inner  function')
	# End  of  inner  function
	print('Hello')
	inner()
	print('Back  to  outer  function')
def  other():
	#inner() # because inner can called inside outer function because acope
	print('Other  function')
# End  of  the  function
print('Begin') # b3gin
outer()
print('Hi')
#inner() # error
other()
print('Bye')
'''
outer function
hello
hello inner function
back to outer function
Other function
bye
'''

def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) #60


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

'''
Begin
Outer function
hi
2nd inner function
hello
1st inner function
back to outer function
bye
'''

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
'''
30
10
bye
'''


x = 10  
def  outer():
	x = 20
	def   inner():
		print(x) #20
		print(globals()['x']) #10
	inner()
#outer()

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
'''
10
20
15
bye

'''


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
#print(x) #error
'''
10
15
20
25
'''



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
print("hello")
outer()

print(x)
'''
10
20
15
25
'''

#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		#nonlocal  x # error
		
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

def  fun():
	x = 10
	def    gun():
		#x =  x +  20 error
		print(x)  
	# End  of  inner  function
	gun()
# End  of  outer function
fun()