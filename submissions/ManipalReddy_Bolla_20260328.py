#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)#[10 , 20 , 15 , 18]
change(a)
print(a)#[10 , 17 , 18 , 25]


# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)#[10 , 20 , 30 , 40]
change(a)#[50 , 60 , 70 , 80]
print(a)#[10 , 20 , 30 , 40]


#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)#10
f1(x)#20
print(x)#10


#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
# End  of  the  function
a = (10 , 20 , 15 , 18)
print(a)#(10 , 20 , 15 , 18)
f1(a)#error tuple cannot be modified
print(a)#(10 , 20 , 15 , 18)


# Find  outputs (Home  work)
square = lambda  x = 10  :    x * x
print(square(5)) #25
print(square())#100


# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))#49
print( lambda   x  :  x * x(7))#function type and its address
print( lambda   x  :   x * x)#function type and its address
print( (lambda  x = 25 :  x * x) () )#625
square = lambda  x :  x  *  x
print(square(5))#25


# Find  output (Home  work)
add= lambda x,y : x+y
#How  to  define  lambda  function   to  return  sum   of  two  arguments#above line
print(add(10 , 20))#30
print(add(10.6 , 20.8)#31.4)
print(add('Hyder' , 'abad'))#Hyderabad
print(add(True , False))#1
print(add(25 , 10.8))#35.8
print(add(3 + 4j , 5 + 6j))#8+10j
print(add(10 , '20'))#error int+str
print(add())#error arguments not given
print(add)#function type and address


#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))#30
print(add())#3


#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )#30
print((lambda  x , y : x + y) (10.8 , 20.6))#31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad'))#Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))#function type and its address


#  Find  outputs (Home  work)
large = lambda x,y :x if x>y else y
How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20))#20
print(large(10.7  ,  5.6))#10.7
print(large('g'  ,  's'))#s
print(large('Rama'  ,  'Rajesh'))#Rama
print(large(True  ,  False))#True


#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))#2*2*2=8
print(power(4.5 , 4))#4.5*4.5*4.5*4.5
print(power())#3.5*3.5
print(power(9))##9*9


# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))#class 'typle'
print(x)#(17, 3, 70, 1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p)#11
print(q)#7
print(r)#18
print(s)#4.5


#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())#Hyd
print(a)#function type and address


# Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()#Hyd
#Sec <nextline> Cyb 


#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))#function type and address
print(lambda  x  :  print(x) (s))#function type and address
print((lambda  x  :  print(x)) (s))#Hyd <nextline> None
(lambda  x  :  print(x)) (s)#Hyd


# Tricky  porgram
# Find  outputs
x = 5
adder1 = lambda    y  :  x + y
x = 10
adder2 = lambda    y  :  x + y
x = 20
adder3 = lambda    y  :  x + y
print(adder1(100))#120
x = 30
print(adder2(200))#230
x = 40
print(adder3(300))#340


#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
#25 <nextline> 125 <nextline> 625


#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()  #Hyd <nextline> Sec
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]#error
print(a)#[fuction f1  and address of f1 , fuction f2 and address of f2]


# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])#function name and address
print(a[key](5))#125


# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
#  End  of  the  function		
lamb = f1(3)
print(type(f1))#class <funtion>
print(type(lamb))#class <function>
print(lamb(2))#3**2
print(lamb(5))#3**9
print(lamb)#function name and address
print(lamb())#error argument got given


# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))#3*2**2+4*2+5
print(lam(2.5))#3*2.5**2+4*2.5+5
print(lam(4))#3*4**2+2*4+5


#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))#30
print(add(30)(40))#70


# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))#False
add = lambda  x = 25 :   x == 35
print(add())##False
add = lambda  x  :   x = 25#error
add = lambda  x  :   x := 25#error


'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  two  numbers
1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3
2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''

def  gcd(m , n):
	if  n==0:
		return  m
	else:
		return   gcd(n,m%n)
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   gcd(m,n))

'''
output
Enter  any  number  :  36
Enter  any  number  :  24
Gcd :   12
'''


'''
Write  a  recursive  function  to  find  sum of  the  digits  of  a  number
'''


def   sod(n):
	if  n==0
		return 0
	else:
		return  n%10 + sod(n//10)
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , sod(n))

'''
output
Enter  any  number :   9247
Sum of the digits :    22
'''


'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series
'''


def  fib(i):
	if  i==1:
		return 0
	if  i==2:
		return  1
	return fib(i-1)+fib(i-2)
n = int(input('How many terms ? :  '))
print(F'{n}th  term is',fib(n))
print('Fibonacci  series : ',end='')
for j in range(1,n+1):
	print(fib(j),end=' ')
	
'''
output
How many terms ? :  5
5th  term is 3
Fibonacci  series : 0 1 1 2 3
'''


'''
Write  a  recursive  power  function
'''


def power(a, b):
    if b == 0:
        return 1
    if b > 0:
        return a * power(a, b - 1)
    if b < 0:
        return (1 / a) * power(a, b + 1)
a = float(input('Enter base : '))
b = int(input('Enter power : '))
result = power(a, b)
print(f"{a} to the power {b} is: {result}")


'''
output
Enter base : 4.5
Enter power : 3
4.5 to the power 3 is: 91.125
Enter base : 4.5
Enter power : -3
4.5 to the power -3 is: 0.010973936899862825
'''


'''
Write  a   recursive  function  to  reverse  a  number
'''


def  rev(n):
	if  n==0:
		return  0
	else:
		return  (n % 10) *(pow(10, len(str(n))-1)) + rev(n // 10)
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))

'''
output
Enter  any  number :  678
Reverse   Number :   876
'''



