#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1] 
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
change(a)
print(a) #[10 , 17 , 18, 25]

# ============================================

# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b) #[50 , 60 , 70 , 80]
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) #[10 , 20 , 30 , 40]
change(a)
print(a) #[10 , 20 , 30 , 40]

# ================================================

#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x) #20
# End  of   the   function
x = 10
print(x) # 10
f1(x)
print(x) #10

# ========================================================

#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25 
# End  of  the  function
a = (10 , 20 , 15 , 18) # Error
print(a)  # Error
f1(a)  # Error
print(a)  # Error

# ======================================================

# Find  outputs (Home  work)
square = lambda  x = 10  :    x * x
print(square(5)) #25
print(square())#100

# ==================================================

# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))#49
print( lambda   x  :  x * x(7))
print( lambda   x  :   x * x) # Function and address
# print( (lambda  x = 25 :  x * x) () ) #625
square = lambda  x :  x  *  x
print(square(5)) #25

# ==============================================

# Find  output (Home  work)
# How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) # class functio
print(add(10 , 20)) # 30
print(add(10.6 , 20.8))  #31.4
print(add('Hyder' , 'abad')) # Hyderabad
print(add(True , False)) # 1
print(add(25 , 10.8)) #35.8
print(add(3 + 4j , 5 + 6j)) #8+10j
print(add(10 , '20')) # Error
print(add()) #Error
print(add) # function

# =====================================================

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 ,  20)) # 30
print(add()) #3

# =====================================================

# #  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # 30
print((lambda  x , y : x + y) (10.8 , 20.6)) #31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # Fuction and address

# ======================================================================

#  Find  outputs (Home  work)
# How  to  define  lambda  to  detrmine  largest  of  two  arguments
large = lambda a, b: a if a > b else b
print(large(10  ,  20)) #20
print(large(10.7  ,  5.6)) #16.3
print(large('g'  ,  's')) #s
print(large('Rama'  ,  'Rajesh')) #Rama
print(large(True  ,  False)) # True
# ==============================================================================

#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) #8
print(power(4.5 , 4)) # 410.0
print(power()) #12.25
print(power(9)) # 81

# =============================================================================

# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7) #(17,3,70,1.42)
print(type(x)) # class function
print(x)  # (17,3,70,1.42)
p , q , r , s = all(9 , 2)
print(p) # 11
print(q) #7
print(r) #18
print(s) # 4.5

# ===============================================================================

#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # Hyd
print(a) # function and address

# =============================================================================

# Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a() # Sec <next line> cyb <next line> Hyd

# ==============================================

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # Function and address
print(lambda  x  :  print(x) (s)) # function and address
print((lambda  x  :  print(x)) (s)) # Hyd
(lambda  x  :  print(x)) (s) # None

# =============================================

# Tricky  porgram
# Find  outputs
x = 5
adder1 = lambda    y  :  x + y
x = 10
adder2 = lambda    y  :  x + y
x = 20
adder3 = lambda    y  :  x + y
print(adder1(100)) #120
x = 30
print(adder2(200)) #230
x = 40
print(adder3(300)) #340

# =========================================================
#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5)) # 25 <new line> 125< new line> 625 <new line>

# =============================================================

#  Find  outputs
def   f1():
	print('Hyd') # Hyd
def   f2():
	print('Sec') # Sec
a = [f1 , f2]
for  x  in  a:
	     x()
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a) # Addres and function
#

# ===================================================================

# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # Function and address
print(a[key](5)) # 125

# ===================================================================

# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
#  End  of  the  function		
lamb = f1(3)
print(type(f1)) # <class function>
print(type(lamb)) # <class function>
print(lamb(2)) # 9
print(lamb(5)) # 243
print(lamb) # < function and address>
print(lamb()) # Error

# ====================================================================

# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) # 25 (3 *4+8+5=25)
print(lam(2.5)) # 33.5
print(lam(4)) # 69

# ===================================================================

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add() #
print(a(20)) #  30
print(add(30)(40)) # 70

# =====================================================================

# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # False
add = lambda  x = 25 :   x == 35
print(add()) # False
add = lambda  x  :   x = 25 # Error (=) is not allowed
add = lambda  x  :   x := 25 # Error (:=) is not allowed

# ====================================================================

'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  two  numbers

1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
# op1 % op2 = op1  if  op1 < op2

def  gcd(m , n):
	if  n==0:
		return  m
	else:
		return   gcd(n, m%n)
'''
1) gcd(4 , 6)  =
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   gcd(m,n))

# ================================================
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
		return 0
	else:
		return  n %10 + sod(n//10)
'''
1) sod(9427) =
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , sod(n))

# ======================================================================

'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1 / 4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  --->  1
'''
def  power(a , b):
	if  b==a:
		return  1
	if  b<0:
		return  1/power(a,-b)

	return  a * power(a,b-1)
'''
1) power(4.5 , 3) =

2) power(4.5 , -3) =

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
# How  to  print  a , b  and  a ^ b
print(a,b , power(a,b))

# ============================================================


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
	if  n == 0:
		return  0
	else:
		return  (n % 10) * (10 ** (len(str(n)) - 1)) + rev(n // 10)
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))