Write  a  program  to  generate  all   prime  divisors  of  a  number  also  print  how  many  prime  divisors  are  existing

Hint:  Reuse  the  prime()  function  defined  in   prog3a   but  do  not  rewrite

1) What  are  the  outputs  if  input  is  30 ?  --->  Prime divisors : [2, 3, 5]
                                                                               Number  of  prime  divisors :  3

2) What  are  the  outputs  if  input  is  84 ?  --->  Prime divisors : [2, 3, 7]
                                                                               Number  of  prime  divisors :  3

3) What  are  the  outputs  if  input  is  49 ?  --->  Prime divisors : [7]
                                                                               Number  of  prime  divisors :  1
'''
# Code :
# prog3a.py
def prime(n):
    i = 2
    while i <= (n//2):
        if n % i == 0:
            return False
        i+=1
    return True
if __name__ == "__main__":
    n = int(input('Enter  any  integer  number  :  '))  
    if  n < 2:
        print('Invalid  input')
    elif  prime(n):
        print('Prime  number')
    else:
        print('Composite  number')
# prog3c.py
from prog3a import prime
def  prime_divisors(n):
    list = []
    for i in range(2,n+1):
        if n % i == 0 and prime(i):
            list.append(i)
    return list
n = int(input("Enter any integer number : "))
list = prime_divisors(n)
print("Prime divisors : ",list)
print("Number of prime divisors : ",len(list) )

''' 
Output:
Enter any integer number : 30
Prime divisors :  [2, 3, 5]
Number of prime divisors :  3

'''

 # Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # a  :  10 <tab> b  :  20
f1(b = 30 , a = 40) # a  :  40 <tab> b  :  30
f1(50 , 60) # Error because the arguments should be keyword arguments
f1(70 , b = 80) # Error because after '*' operator all the arguments should be keyword arguments
f1(a = 15 , 25) # Error because the positional arguments cannot be used after keyword arguments

#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)  # a  : 10 <tab> b  :  20 <tab> c  :  30
f1(a = 40 , b = 50 , c = 60) # a  : 40 <tab> b  :  50 <tab> c  :  60
f1(c = 100 , b = 90 , a = 80) # a  : 80 <tab> b  :  90 <tab> c  :  100
f1(70 , 80 , c = 90) # Error because after '*' operator all the arguments should be keyword arguments
f1(70 , 80 , 90) # Error because after '*' operator all the arguments should be keyword arguments
f1(c = 15 , b = 25 , 35) # Error because the positional arguments cannot be used after keyword arguments

# Identify error (Home  work)
def   f1(a  , b , *):
        pass
# Error because atleast one argument should be there after '*' operator

#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # a  :  10 <tab> b  :  20
f1(a = 30 ,  b = 40) # Error because all the arguments before '\' operator should be positional arguments
f1(50 , b = 60) # Error because all the arguments before '\' operator should be positional arguments
f1(a = 70 , 80) # Error because the positional arguments cannot be used after keyword arguments

# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a  :  10 <tab> b  :  20 <tab> c  : 30
f1(40 , 50 , c = 60) # a  :  40 <tab> b  :  50 <tab> c  : 60
f1(a = 70 , b = 80 , c = 90) # Error because all the arguments before '\' operator should be positional arguments and not keyword arguments
f1(a = 100 , b = 110 , 120)  # Error because the positional arguments cannot be used after keyword arguments
f1(a = 130 , 140 , c = 150) # Error because the positional arguments cannot be used after keyword arguments
f1(160 , b = 170 , 180) # Error because the positional arguments cannot be used after keyword arguments
f1(190 , b = 200 , c = 210) # Error because all the arguments before '\' operator should be positional arguments and not keyword arguments

# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)  # a  :  10 <tab>  b  :  20 <tab> c  :  30 <tab> d  :  40 <tab> e  :  50 <tab> f  :  60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error because all the arguments before '\' operator should be positional arguments and not keyword arguments
f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error because after '*' operator all the arguments should be keyword arguments
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error because the positional arguments cannot be used after keyword arguments
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # a  :  10 <tab>  b  :  20 <tab> c  :  30 <tab> d  :  40 <tab> e  :  50 <tab> f  :  60

# Identify error (Home  work)
def  f1(/ , a , b ,  c): # Error atleast one argument should be before '\' operator
        pass
def   f2(a , b , c , *): # Error atleast one argument should be after '*' operator
        pass

# Identify  error  (Home  work)
def  f4(* , a , b , c , /):  # Here we cannot use both '*' and '\' operator because the arguments cannot be both positional and keyword only
	        pass

# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) # 3rd  function : 10
f1(y = 20) # Error because argument y is not defined in function f1()
f1(x = 30) # Error because argument x is not defined in function f1()

# Default  arguments  demo  program
def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))   #  150
print(add(100 , 200))  #  330
print(add(100 , 200 , 300))  #   600
print(add(100 , c = 200)) #  320
print(add(c = 100 , b = 200 , a = 300)) #  600
print(add(c = 100 , a = 200))  # 320
print(add()) # Error because the argument a should be passed in function call
print(add(a = 100 , 200)) # Error because the positional arguments cannot be followed after keyword arguments
print(add(100 ,  , 300)) # Error because of invalid syntax
print(add(100 ,  b , 300)) # Error the value of b is not defined

 # Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):  # Here the non default arguments cannot be followed after default arguments
	pass
def   f2(b , d , a = 10 , c = 20):  # No error
	pass

#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20) # 20
f1() # 10
f1(a = 30) # 30

# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400)) # 1000
print(add(b = 100 , a = 200)) # 330
print(add(100 , 200 , d = 300)) # 610
print(add(d = 100 , a = 200 , b = 300)) # 610
print(add(c = 100 , d = 200 , 300 , 400)) # Error the positional arguments cannot be followed by keyword arguments
print(add(100 , 200 , c = 300 , x = 400)) # Error because of undefined argument x
print(add()) # Error because arguments a and b are passed from the function call

#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) # 10
print(f1()) # 25
print(f2(20)) # 20
print(f2()) # Error because one argument is required

# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # '------'
disp('$') # '$$$$'
disp() # '****'
disp(n = 5) # '*****'
disp(5) # 20
disp(n = 7 , ch = '%') # '%%%%%%%'
disp(7 , '@') # '@@@@@@@'
disp(7 , n = 6) # 42
disp(ch = '!' ,  5) # Error because the positional arguments cannot followed by the keyword arguments

# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5)) # 91.125
print(power(3 + 4j)) # -7 + 24j
print(power(True)) # 1
def   power(b = 2 , a): # Error because the positional arguments cannot be follwed after keyword argument
 	 pass

# Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
print(add(10 , 20 , 30 , 40)) # 4-argument function <nextline> 100
print(add(50 , 60 , 70)) # 4-argument function <nextline> 184
print(add(80 , 90)) # 4-argument function <nextline> 177
print(add(100)) # 4-argument function <nextline> 109
print(add()) # 4-argument function <nextline> 10

# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :  10 20 30
disp(40 , 50 , 60 , 70) # Error the disp() function requires three arguments but not four
disp(80 , 90)  # 3-argument  function  :  80 90 25

# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # 70
print(add()) # 30
print(add(a = 50)) 70
print(add(b = 60 , a = 70)) # 130
print(add(80 , 90)) # Error because the add() function keyword only argument

# Find  outputs(Home  work)
def   add(a = 10 , b , c): # Error the non default argument cannot be passed after default argument
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))  # 120
print(add(b = 60 , c = 70)) # 140
print(add(c = 80 , b = 90 , a = 100)) # 270
print(add(c = 25 , a = 43)) # Error the argument b is not defined
print(add(1 , 2 , 3)) # Error because add() function accepts only keyword arguments
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):  # Error the non default argument cannot be passed after default argument
		pass

# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . _defaults_) ([],)

# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_) # __defaults__  :  ([],)
f1(3)  # List  :  [3]
print('_defaults_  :  ' , f1._defaults_) # __defaults__  :  ([3],)
f1(4 , [1 , 2 , 3])  # List  :  [1 , 2 , 3 , 4]
print('_defaults_  :  ' , f1._defaults_) # __defaults__  :  ([3],)
f1(9) # List  :  [3 , 9]
print('_defaults_  :  ' , f1._defaults_) # __defaults__  :  ([3 , 9],)
f1(40 , [10 , 20 , 30]) # List  :  [10 , 20 , 30 , 40]
print('_defaults_  :  ' , f1._defaults_) # __defaults__  :  ([3 , 9],)
f1(5) # List  :  [3 , 9 , 5]
print('_defaults_  :  ' , f1._defaults_) # __defaults__  :  ([3 , 9 , 5],)
f1([6 , 7 , 8]) # List  :  [3 , 9 , 5 , [6 , 7 , 8]]
print('_defaults_  :  ' , f1._defaults_) # __defaults__  :  ([3 , 9 , 5 , [6 , 7 , 8]],)

# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_) # __defaults__  :  ([],)
print(f1(3)) # [0 , 1 , 4]
print('_defaults  :  ' , f1._defaults_) # __defaults__  :  ([0 , 1 , 4],)
print(f1(4 , [10 , 20 , 15 , 18]))  # [10 , 20 , 15 , 18 , 0 , 1 , 4 , 9]
print('_defaults  :  ' , f1._defaults_) # __defaults__  :  ([0 , 1 , 4],)
print(f1(5)) # [0 , 1 , 4 , 0 , 1 , 4 , 9 , 16]
print('_defaults  :  ' , f1._defaults_) # __defaults__  :  ([0 , 1 , 4 , 0 , 1 , 4 , 9 , 16],)
print(f1(a = [100 , 200 , 300],   x = 6 )) # [100 , 200 , 300 , 0 , 1 , 4 , 9 , 16 , 25]
print('_defaults  :  ' , f1._defaults_) # __defaults__  :  ([0 , 1 , 4 , 0 , 1 , 4 , 9 , 16],)
print(f1(6)) # [ 0 , 1 , 4 , 0 , 1 , 4 , 9 , 16 , 0 , 1 , 4 , 9 , 16 , 25]
print('_defaults  :  ' , f1._defaults_) # __defaults__  :  ([0 , 1 , 4 , 0 , 1 , 4 , 9 , 16 , 0 , 1 , 4 , 9 , 16 , 25],)

# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . _defaults_) # ( 'Hyd' , [] )
f1() # a : HydSec <nextline> b : [1 , 2 , 3]
print('Default Values  :  ' , f1 . _defaults_) # ( 'Hyd' , [1 , 2 , 3] )
f1() # a : HydSec <nextline> b : [1 , 2 , 3 , 1 , 2 , 3]
print('Default Values  :  ' , f1 . _defaults_) # ( 'Hyd' , [1 , 2 , 3 , 1 , 2 , 3] )
f1() # a : HydSec <nextline> b : [1 , 2 , 3 , 1 , 2 , 3 , 1 , 2 , 3]

#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18) # (10 , 20 , 15 , 18) <nextline> <class 'tuple'> <nextline> 4 
f1() # () <nextline> <class 'tuple'> <nextline> 0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) # ([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) <nextline> <class 'tuple'> <nextline> 3
f1('Hyd') # ('Hyd',) <nextline> <class 'tuple'> <nextline> 1 
tpl = (100 , 200 , 150)
f1(tpl)  # ((100,200,150),) <nextline> <class 'tuple'>  <nextline> 1 
f1(t = (10 , 20 , 30)) #   Error

#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):
    if len(a) == 0:
         return 0
    try:
         return sum(a)/len(a)
    except:
         return sum(a[0])/len(a[0])
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18
print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))

'''
Output:
15.75
12.266666666666666
14.26
0
25.0
(4+5j)
15.75

'''
# Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
def  concat(*a):
	return ''.join(a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))

'''
Outputs:
SankarDayalSarma
HydIsGreenCity
PythonIsAGreatLanguage

Python
Error cannot concat int and int
'''

#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a  :  10 <tab> b : (20 , 30 , 40)
f1(50 , 60) # a  :  50 <tab> b : (60,)
f1(70) # a  :  70 <tab> b : ()
f1(a = 80) # a  :  80 <tab> b : ()
f1(b = (10 , 20 , 30) , a = 40) # Error because argument b is not defined in f1() function
f1() # a  :  25 <tab> b : ()
f1(a = 10 , (20 , 30 , 40)) # Error because positional argument cannot be followed after keyword arguments
f1(25 , b = (10 , 20 , 30)) # Error because argument b is not defined in f1() function
f1(25 , a = (10 , 20 , 30)) # a  :  (10 , 20 , 30) <tab> b : (25,)
f1((10 , 20 , 30) , 10 , 20 , 30) # a  :  (10 , 20 , 30) <tab> b : (10 , 20 , 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30) # Error because positional argument cannot be followed after keyword arguments

# Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a  : (10 , 20 , 30) <tab> b  :  40
f1(50 , b = 60) # a  : (50,) <tab> b  :  60
f1(b = 70) # a  : () <tab> b  :  70
f1(b = 10 , a = (20 , 30 , 40)) # Error because of undefined argument a
f1(b = 10 , (20 , 30 , 40)) # Error the positional arguments cannot be followed by keyword arguments
f1() # Error because the argument b should be passed to the function f1()
f1(10 , 20 , 30 , (10 , 20 , 30)) # Error because of missing one keyword argument b
f1(10 , 20 , 30 , 40)  # Error because of missing one keyword argument b
f1(25) # Error because of missing one keyword argument b
f1(10 , 20 , 30 , b = (10 , 20 , 30)) # a  : (10 , 20 , 30) <tab> b  :  (10 , 20 , 30)

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a  : 10 <tab> b : (20 , 30 , 40 ) <tab> c : 50
f1(60 , 70 , c = 80) # a  : 60 <tab> b : (70,) <tab> c : 80
f1(90 , c = 100) # a  : 90 <tab> b : () <tab> c : 100
f1(a = 1 , 2 , c = 3) # Error the positional arguments cannot be followed after keyword arguments
f1(1 , 2 , 3) # Error required keyword argument for c
f1(a = 1 , b = 2 , c = 3) # Error undefined argument b in function call
f1(a = 25 , 100 , 200 , 300 , c = 35) # Error the positional arguments cannot be followed after keyword arguments

# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b): # Invalid because only one * operator is allowed
        pass
def  f2(*a , b): # Valid
        pass
def  f3(a , *b): # Valid
        pass
def  f4(a , b):  # Valid
        pass
def    f5(a , *b , c): # Valid
        pass
def   f6( * , a , *b , c): # Invalid beacuse * operator is for variable length positional arguments
       pass
def   f7(a , *b , c ,  /): # Valid
       pass

# Find  outputs  (Home  work)
def   f1(*a):
	print(a) 
	print(type(a))
	for  x  in  a:
		print(x) 
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

''' Output:
([10,20] ,{30 , 40} , (50 , 60))
<class 'tuple'>
[10 , 20]
<class 'list'>
{30 , 40}
<class 'set'>
(50 , 60)
<class 'tuple'>
'''

# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
# End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

''' Outputs:
Results
<class 'dict'>
{ 'RollNo' : 10 , 'StudName' : 'Rama  Rao'}

Results
<class 'dict'>
{ 'EmpNo' : 25 , 'EmpName' : 'Sita' , 'Salary' = 10000.0}

Results
<class 'dict'>
{ 'AcNo' : 30 , 'CustName' : 'Kiran' , 'Balance' = 20000.0 , 'Gender' = 'm'}

Results
<class 'dict'>
{}
'''

# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

''' Output:
<class 'tuple'>
(25 , 10.8 , 'Hyd' ,True)

<class 'dict'>
{ 'EmpNum' : 25 , 'EmpName' : 'Sita' , 'Salary' = 10000.0}
'''

#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  :	10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # Error due to undefined argument eno
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}


# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)

''' Output:
25

Hyd
(10 , 20 , 30)

10.8
(25 , 'Hyd' , True)
{'EmpNo' : 12 , 'EmpName' : 'Rama Rao' , 'Salary' : 10000.0}