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
''''
[10,20,15,18]
[10,17,18,25]'''


# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)
change(a)
print(a)
'''
[10, 20, 30, 40]
[50 , 60 , 70 , 80]
[10, 20, 30, 40]
'''


#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)
f1(x)
print(x)
'''
10
20
10
'''


#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25#error-tuple is immutable
# End  of  the  function
a = (10 , 20 , 15 , 18)
print(a)
f1(a)
print(a)
'''
(10 , 20 , 15 , 18)
'''


# Find  outputs (Home  work)
square = lambda  x = 10  :    x * x
print(square(5)) #25
print(square())#100


# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))#49
print( lambda   x  :  x * x(7))#Type and  address  of  lambda  function
print( lambda   x  :   x * x)#Type and  address  of  lambda  function
print( (lambda  x = 25 :  x * x) () )#625
square = lambda  x :  x  *  x
print(square(5))#25


# Find  output (Home  work)
#How  to  define  lambda  function   to  return  sum   of  two  arguments
add=lambda x,y:x+y
print(type(add))#<class 'function'>
print(add(10 , 20))#30
print(add(10.6 , 20.8))#31.4
print(add('Hyder' , 'abad'))#'hyderabad'
print(add(True , False))#1
print(add(25 , 10.8))#35.8
print(add(3 + 4j , 5 + 6j))#8+10j
print(add(10 , '20'))#error-str and int cannot be added/concatinated
print(add())#error-arguments are not passed
print(add)#type and address of lambda function


#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))#30
print(add())#3


#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )#30
print((lambda  x , y : x + y) (10.8 , 20.6))#31.3
print((lambda  x , y : x + y) ('Hyder' , 'abad'))#'Hyderabad'
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))#type and address of lambda function


#  Find  outputs (Home  work)
How  to  define  lambda  to  detrmine  largest  of  two  arguments
large= lambda x,y: x if(x>y) else y
print(large(10  ,  20))#20
print(large(10.7  ,  5.6))#107
print(large('g'  ,  's'))#'s'
print(large('Rama'  ,  'Rajesh'))#'Rama'
print(large(True  ,  False))#True


#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))#2**3=8
print(power(4.5 , 4))#4.5**4=410.0625
print(power())#3.5**2=12.25
print(power(9))#9**2=81


# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)#(17,3,70,1.42)
print(type(x))#<class 'function'>
print(x)#(17,3,70,1.42)
p , q , r , s = all(9 , 2)
print(p)#11
print(q)#7
print(r)#18
print(s)#4.5


#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())#'Hyd'
print(a)#type and address of lambda function


# Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()
'''
'Sec'
'Cyb'
'Hyd'
'''


#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))#type and address of lambda function
print(lambda  x  :  print(x) (s))#'Hyd'
print((lambda  x  :  print(x)) (s))#'None'
(lambda  x  :  print(x)) (s)#'Hyd'


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
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
'''
25
125
625'''



#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]#['Hyd','Sec']
for  x  in  a:
	     x()
'Hyd'
'Sec'
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]#error-function defination should be outside
print(a)#error-the defination is not proper



# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])#type and address of lambda function
print(a[key](5))#{125}


# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
#  End  of  the  function		
lamb = f1(3)
print(type(f1))#<class 'function'>
print(type(lamb))#<class 'function'>
print(lamb(2))#9
print(lamb(5))#243
print(lamb)#<type and address of lamb>
print(lamb())#error-no argument is passed


# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))#25
print(lam(2.5))#33.75
print(lam(4))#69

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))#30
print(add(30)(40))#40


# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))#False
add = lambda  x = 25 :   x == 35
print(add())#False
add = lambda  x  :   x = 25#assignment is not possible
add = lambda  x  :   x := 25#assignment is not possible


'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  two  numbers

1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
op1 % op2 = op1  if  op1 < op2

def  gcd(m , n):
	if  n==0:
		return  m
	else:
		return  gcd(n,m%n)
'''
1) gcd(4 , 6)= gcd(6,4)=gcd(4,2)=gcd(2,0)=2
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,  gcd(m,n))
	  

      
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
	if  n>0:
		return  n%10+sod(n//10)
	else:
		return  0
'''
1) sod(9427) = 9427%10+sod(9427//10)=7+sod(942)=7+942%10+sod(942//10)=7+2+sod(94)=7+2+94%10+sod(94//10)=7+2+4+sod(9)=7+2+4+9=22
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , ???)