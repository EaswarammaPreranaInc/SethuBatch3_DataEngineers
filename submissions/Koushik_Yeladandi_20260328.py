#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)
change(a)
print(a)





# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)
change(a)
print(a)





#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)
f1(x)
print(x)






#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
# End  of  the  function
a = (10 , 20 , 15 , 18)
print(a)
f1(a)
print(a)






# Find  outputs (Home  work)
square = lambda  x = 10  :    x * x
print(square(5)) 
print(square())






# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))
print( lambda   x  :  x * x(7))
print( lambda   x  :   x * x)
print( (lambda  x = 25 :  x * x) () )
square = lambda  x :  x  *  x
print(square(5))







# Find  output (Home  work)
How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add))
print(add(10 , 20))
print(add(10.6 , 20.8))
print(add('Hyder' , 'abad'))
print(add(True , False))
print(add(25 , 10.8))
print(add(3 + 4j , 5 + 6j))
print(add(10 , '20'))
print(add())
print(add)








#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))
print(add())






#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )
print((lambda  x , y : x + y) (10.8 , 20.6))
print((lambda  x , y : x + y) ('Hyder' , 'abad'))
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))





#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )
print((lambda  x , y : x + y) (10.8 , 20.6))
print((lambda  x , y : x + y) ('Hyder' , 'abad'))
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))





#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))
print(power(4.5 , 4))
print(power())
print(power(9))





# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))
print(x)
p , q , r , s = all(9 , 2)
print(p)
print(q)
print(r)
print(s)







#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())
print(a)






# Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()




#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)






# Tricky  porgram
# Find  outputs
x = 5
adder1 = lambda    y  :  x + y
x = 10
adder2 = lambda    y  :  x + y
x = 20
adder3 = lambda    y  :  x + y
print(adder1(100))
x = 30
print(adder2(200))
x = 40
print(adder3(300))






#Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))







#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a)






# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))






# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
#  End  of  the  function		
lamb = f1(3)
print(type(f1))
print(type(lamb))
print(lamb(2))
print(lamb(5))
print(lamb)
print(lamb())






# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))
print(lam(2.5))
print(lam(4))






#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))
print(add(30)(40))





# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))
add = lambda  x = 25 :   x == 35
print(add())
add = lambda  x  :   x = 25
add = lambda  x  :   x := 25





Write  a  recursive  function  to  determine  gcd (or) hcf  of  two  numbers

1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
op1 % op2 = op1  if  op1 < op2

def  gcd(m , n):
	if  ???
		return  ???
	else:
		return   ???
'''
1) gcd(4 , 6)  =
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   ???)


# Program:

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


m = int(input("Enter any number: "))
n = int(input("Enter any number: "))

print("Gcd:", gcd(m, n))









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
	if  ???
		return  ???
	else:
		return  ???
'''
1) sod(9427) =
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , ???)

# Program:



def   sod(n):
	if  n==0:
		return 0
	else:
		return  n % 10 + sod(n//10)


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
	if  ???
		return  ???

	if  ???
		return  ???
	return  ???
'''
fib(5) =  5th  term  i.e.  3
'''
n = int(input('How many terms ? :  '))
print('Fibonacci  series')
How  to  print  first  'n'  terms  of  fibonacci  series

# Program 

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
n=int(input('Enter term :  '))
print(F'{n} term :' , fib(n))







'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1 / 4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  --->  1
'''
def  power(a , b):
	if  ???
		return  ???
	if  ???
		return  ???
	return  ???
'''
1) power(4.5 , 3) =

2) power(4.5 , -3) =

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
How  to  print  a , b  and  a ^ b

# Program:
def  power(a , b):
    if b== 0:
        return 1
    elif b>0:
        return a*power(a,b-1)
    else:
        return (1/a)*power(a,b+1)
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print('value : ',power(a,b))








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
	if  ???
		return  ???
	else:
		return  ??
'''
rev(946)  =
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))




# Program:


from math import *
def  rev(n):
	if  n==0:
		return 0
	length=len(str(n))-1
	return  (n % 10) * (10 ** length) + rev(n // 10)

n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))



