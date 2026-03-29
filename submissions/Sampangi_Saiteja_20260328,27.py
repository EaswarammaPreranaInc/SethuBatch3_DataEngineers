#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)              # [10, 20, 15, 18]
change(a)
print(a)              # [10, 17, 18, 25]




# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)          # [50, 60, 70, 80]
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)              # [10, 20, 30, 40]
change(a)
print(a)              # [10, 20, 30, 40]




#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)          # 20
# End  of   the   function
x = 10
print(x)              # 10
f1(x)
print(x)              # 10




#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
# End  of  the  function
a = (10 , 20 , 15 , 18)
print(a)              # (10, 20, 15, 18)
f1(a)                 # error
print(a)              # not executed




# Find  outputs (Home  work)
square = lambda  x = 10  :    x * x
print(square(5))      # 25
print(square())       # 100




# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))          # 49
print( lambda   x  :  x * x(7))             # <function ...>
print( lambda   x  :   x * x)               # <function ...>
print( (lambda  x = 25 :  x * x) () )      # 625
square = lambda  x :  x  *  x
print(square(5))      # 25




# Find  output (Home  work)
# How  to  define  lambda  function   to  return  sum   of  two  arguments
add = lambda a, b : a + b
print(type(add))      # <class 'function'>
print(add(10 , 20))   # 30
print(add(10.6 , 20.8))   # 31.4
print(add('Hyder' , 'abad'))   # Hyderabad
print(add(True , False))       # 1
print(add(25 , 10.8))         # 35.8
print(add(3 + 4j , 5 + 6j))   # (8+10j)
print(add(10 , '20'))         # error
print(add())                  # error
print(add)                    # <function ...>




#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))   # 30
print(add())          # 3




#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )      # 30
print((lambda  x , y : x + y) (10.8 , 20.6))   # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad'))  # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # <function ...>




#  Find  outputs (Home  work)
# How  to  define  lambda  to  detrmine  largest  of  two  arguments
large = lambda a, b : a if a > b else b
print(large(10  ,  20))        # 20
print(large(10.7  ,  5.6))     # 10.7
print(large('g'  ,  's'))      # s
print(large('Rama'  ,  'Rajesh')) # Rajesh
print(large(True  ,  False))   # True




#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))     # 8
print(power(4.5 , 4))   # 410.0625
print(power())          # 12.25
print(power(9))         # 81




# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))     # <class 'tuple'>
print(x)           # (17, 3, 70, 1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p)           # 11
print(q)           # 7
print(r)           # 18
print(s)           # 4.5




#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())     # Hyd
print(a)       # <function ...>




# Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()            # Hyd
               # Sec
               # Cyb
              





#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))         # <function ...>
print(lambda  x  :  print(x) (s))     # <function ...>
print((lambda  x  :  print(x)) (s))   # Hyd
(lambda  x  :  print(x)) (s)          # Hyd





# Tricky  porgram
# Find  outputs
x = 5
adder1 = lambda    y  :  x + y
x = 10
adder2 = lambda    y  :  x + y
x = 20
adder3 = lambda    y  :  x + y
print(adder1(100))    # 120
x = 30
print(adder2(200))    # 230
x = 40
print(adder3(300))    # 340





#Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))     # 10
                          # 15
                          # 625




#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()               # Hyd
                          # Sec

a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a)                   # error





# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])      # <function ...>
print(a)   # 125





# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
#  End  of  the  function		
lamb = f1(3)
print(type(f1))    # <class 'function'>
print(type(lamb))  # <class 'function'>
print(lamb(2))     # 9
print(lamb(5))     # 243
print(lamb)        # <function ...>
print(lamb())      # error





# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))      # 25
print(lam(2.5))    # 33.75
print(lam(4))      # 69





# Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))         # 30
print(add(30)(40))   # 70





# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))       # False
add = lambda  x = 25 :   x == 35
print(add())         # False
add = lambda  x  :   x = 25        # error
add = lambda  x  :   x := 25       # error



'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  two  numbers

1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
op1 % op2 = op1  if  op1 < op2

def  gcd(m , n):
	if  n==0:
		return  (m)
	else:
		return  (n,m%n) 
'''
1) gcd(4 , 6)  =
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   gcd(m,n))

 '''
Write  a  recursive  function  to  find  sum of  the  digits  of  a  number

sod(678) =  678 % 10 + sod(678 // 10)
              =  8 + sod(67)
              =  8 + 67 % 10 + sod(67 // 10)
              =  8 + 7 + sod(6)
              =  8 + 7 + 6 % 10 + sod(6 // 10)
              =  8 + 7 + 6 + sod(0)
              =  8 + 7 + 6 + 0
			  = 21

1) How  many  function  calls  are  in  sod(678) ?  --->  4

2) How  many  function  calls  are  in  sod(n-digit  number) ?  --->  n + 1
'''
def   sod(n):
	if  n==0:
		return  0
	else:
		return  n%10
'''
1) sod(9427) =
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , sod(n))
 '''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , ......

2) What  is  the  formula  for  10th  term ?  ---> 9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  ---> 2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  ---> 0  and  1
'''
def  fib(i): #   'i'  is  term  number
	if  i==1:
		return  0
	if  i==2
		return  1
	return  0
'''
fib(5) =  5th  term  i.e.  3
'''
n = int(input('How many terms ? :  '))
print('Fibonacci  series')
How  to  print  first  'n'  terms  of  fibonacci  series
 '''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1 / 4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  --->  1
'''
def  power(a , b):
	if  b==0:
		return  1
	if  b<0
		return  1/power(a,-b)
	return  a*power(a,b-1)
'''
1) power(4.5 , 3) =

2) power(4.5 , -3) =

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
How  to  print  a , b  and  a ^ b
 '''
Write  a   recursive  function  to  reverse  a  number

rev(678) = 678 % 10 * 10 ^ 2 + rev(678 // 10)
               = 800 + rev(67)
               = 800 + 67 % 10 * 10 ^ 1 + rev(67 // 10)
               = 800 + 70 + rev(6)
               = 800 + 70 + 6 % 10 * 10 ^ 0 + rev(6 // 10)
               = 800 + 70 + 6 + rev(0)
               = 800 + 70 + 6 + 0
			   = 876

1) How  many  function  calls  are  in  rev(678) ?  --->  4

2) How  many  function  calls  are  in  rev(n-digit number)  ? ---> n + 1

3) How  to  obtain  length  of a  number ?  ---> len(str(number))
'''
from math import *
def  rev(n):
	if  n==0
		return  0
	else:
		return  ????
'''
rev(946)  =
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))



#------------------------------------------------------------------------------------------------------------
#home on 27.3.26

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)   # 20
	a += 1
#End  of  the  function
a = 10
print(a)   # 10
a += 1
f1()
print(a)   # 11

# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)   # 20
	dict = globals()
	print(dict['a'])   # 11
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)   # 10
a += 1
f1()
print(a)   # 40

# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)   # 10
	print(globals()['x'])   # 10
# end of the function
f1()

# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)   # 20
	print(globals()['x'])   # error
# End  of  the  function
f1()


# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)   # 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])   # 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)   # 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()


# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)   # 20
def   f2():
	global  x
	x = 30
	print(x)   # 30
	x += 1
def   f3():
	global  y
	y = 40
	print(y)   # 40
	y += 1
def   f4():
	x = 50
	global   x   # error
#  End  of  the  functions
x = 10
print(x)   # 10
x += 1
f1()
print(x)   # 11
f2()
print(x)   # 31
x += 1
f3()
print(y)   # 41
f4()   # error
print(x)


# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)   # 20
	print(globals()['a'])   # 20
	a = 30
# End of the function
a = 10
print(a)   # 10
f1()
print(a)   # 30


# Find  outputs(Home  work)
def  f1():
	global  a
	print(a)   # error
	a = 10
	print(globals()['a'])   # 10
	a = 20
	print(a)   # 20
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1()   # error
f2()
print(a)


# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)   # 10
	a = 20
def  f2():
	global  a
	print(a)   # 20
	a = 30
def  f3():
	print(a)   # 30
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)   # 40

# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)   # 10
	a = 20
def  f2():
	print(a)   # 20
	a = 30
	print(a)   # 30
def  f3():
	print(a)   # 20
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)   # 40


#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a   # error
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()   # error
print(a)
print(b)


# Find outputs (Home  work)
def  f1():
        global  a
        print(a)   # 11
        a += 1
def  f2():
        global  a
        print(a)   # 13
        a += 1
# End  of  the  function
a = 10
print(a)   # 10
a += 1
f1()
print(a)   # 12
a += 1
f2()
print(a)   # 14


# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)   # 20
def  f2():
	print(a)   # 11
	a += 1   # error
# End of the function
a = 10
print(a)   # 10
f1()
a += 1
f2()   # error
print(a)


# Find outputs (Home  work)
def  f1():
	a = 20
	global   a   # error
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)   # 10
a += 1
f1()   # error
print(a)


#  Find   outputs
def   f1():
	x = x + 5   # error
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)   # 15
# End of f2  function
x = 10
f1()   # error
f2()
print(x)   # 10