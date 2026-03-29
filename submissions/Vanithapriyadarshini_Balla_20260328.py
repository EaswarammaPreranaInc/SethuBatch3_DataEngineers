
#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
change(a) # b=[10,17,18,25]
print(a) # [10,17,18,25]

# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) #[10 , 20 , 30 , 40]
change(a) # [50 , 60 , 70 , 80]
print(a)  ##[10 , 20 , 30 , 40]

#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x) # 10
f1(x) # 20
print(x) # 10

#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25 # Error
# End  of  the  function
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18)
#f1(a) # Error, in func
print(a) 

# Find  outputs (Home  work)
square = lambda  x = 10  :    x * x
print(square(5)) # 25
print(square()) # 100

# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7)) # 49
print( lambda   x  :  x * x(7)) # Error, () mandatory for nameless func
print( lambda   x  :   x * x) # Error, arg should be passed 
print( (lambda  x = 25 :  x * x) () ) # 625
square = lambda  x :  x  *  x
print(square(5)) # 25

# Find  output (Home  work)
#How  to  define  lambda  function   to  return  sum   of  two  arguments
def add(x,y):
	return x+y
print(type(add)) # <class 'function'>
print(add(10 , 20)) # 30
print(add(10.6 , 20.8)) # 31.4
print(add('Hyder' , 'abad')) # Hyderabad
print(add(True , False)) # 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j)) # 8+10j
#print(add(10 , '20')) # Error, bcz int and str cant be concatenated
#print(add()) # Error, arg should be passed
print(add) # type of func and addr of func

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add()) # 3

#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # 30
print((lambda  x , y : x + y) (10.8 , 20.6)) # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # func name and add of func in Hexadecimal

#  Find  outputs (Home  work)
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
def large(x,y):
	if x>y:
		return x
	return y
print(large(10  ,  20)) # 20
print(large(10.7  ,  5.6)) # 10.7
print(large('g'  ,  's')) # s 
print(large('Rama'  ,  'Rajesh')) # Rama
print(large(True  ,  False)) # True

#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) # (2)^3
print(power(4.5 , 4)) # (4.5)^4
print(power()) # (3.5)^2
print(power(9)) # 9^2

# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x)) #<class 'tuple'>
print(x) # (17,3,70,1.42)
p , q , r , s = all(9 , 2)
print(p) # 11
print(q) # 7
print(r) # 18
print(s) # 4.5

#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # Hyd
print(a) # type and address of func

# Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()
# Sec
# Cyb
# Hyd

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # type and address
print(lambda  x  :  print(x) (s)) # type and address
print((lambda  x  :  print(x)) (s)) # Hyd None
(lambda  x  :  print(x)) (s) # Hyd 

# Tricky  porgram
# Find  outputs
x = 5
adder1 = lambda    y  :  x + y
x = 10
adder2 = lambda    y  :  x + y
x = 20
adder3 = lambda    y  :  x + y
print(adder1(100)) # 120 
x = 30
print(adder2(200)) # 230
x = 40
print(adder3(300)) # 340

#Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))# 10<nl>15<nl>625
		
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x() # Hyd <nl>Sec
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a) # Error

# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # Type and address
print(a[key](5)) # 125

# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
#  End  of  the  function		
lamb = f1(3)
print(type(f1)) # type and address in decimal
print(type(lamb)) # type and address
print(lamb(2)) # 9
print(lamb(5)) # 243
print(lamb) # type and address in hexa decimal
#print(lamb()) # in brackets arg is req

# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) # 25
print(lam(2.5)) # 33.75
print(lam(4)) # 69

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # 30
print(add(30)(40)) # 70

# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # False
add = lambda  x = 25 :   x == 35
print(add()) # False
#add = lambda  x  :   x = 25  # Error bcz, non def args cant be modified inside func
#add = lambda  x  :   x := 25

#Write  a  recursive  function  to  determine  gcd (or) hcf  of  two  numbers

def gcd(m, n):
    if n == 0:          
        return m
    else:              
        return gcd(n, m % n)
m=int(input("Enter m : "))
n=int(input("Enter n : "))
print(gcd(m,n))

#Write  a  recursive  function  to  find  sum of  the  digits  of  a  number

def   sod(n):
	if  n==0:
		return  0
	else:
		return  n%10+sod(n//10)
n=int(input("Enter n : "))
print(sod(n))

#Write  a  recursive  function  for  fibonacci  term
#Use  the  function  to  generate  fibonacci  series
def fib(i):
    f1=0
    f2=1
    if i==1:
        return 0
    if i==2:
        return 1
    for n in range(3,i+1):
        f3=f1+f2
        f1=f2
        f2=f3
    return f3
i=int(input("Enter n : "))
print(fib(i))

# Write  a  recursive  power  function
def pow(n,p):
    if p==0:
        return 1
    if p==1:
        return n
    return n*(pow(n,p-1))
n=eval(input("Enter n :"))
p=eval(input("Enter p :"))
print(pow(n,p))

# Write  a   recursive  function  to  reverse  a  number
def  rev(n):
	if  n<10:
		return  n
	else:
		return  n%10 * 10**(len(str(n))-1) + rev(n//10)
n =int(input("Enter n : "))
print(rev(n))





			
	