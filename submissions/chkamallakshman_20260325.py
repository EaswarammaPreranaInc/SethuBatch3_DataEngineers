# # Modify  following  program  such  that  every  function  should  be  executed
# # def  f1():
# # 	print('No-argument  function')
# # def  f1(x):
# # 	print('Single  argument  function  : ' , x)
# # def  f1(x , y):
# # 	print('Two  argument  function : ' , x , y)
# # def  f1(x , y , z):
# # 	print('Three  argument  function : ' , x , y , z)

# # correct one : 

# def f1(x=None, y=None, z=None):
#     if x is None and y is None and z is None:
#         print("No-argument function")
#     elif y is None and z is None:
#         print("Single argument function:", x)
#     elif z is None:
#         print("Two argument function:", x, y)
#     else:
#         print("Three argument function:", x, y, z)

# # Calls
# f1()
# f1(10)
# f1(10, 20)
# f1(10, 20, 30)



# #2. Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
# # also  print  how  many  prime  numbers  are  existing

# # Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

# # What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
# # 																		    
Number  of   prime  numbers : 4
# # '''
# # def  prime_numbers(n):
# # 	return  list  of  all  the  prime  numbers  between  2  and   n
# # Read  'n'  value
# # call  prime_numbers()  function  
# # print  the  list
# # print  number  of  prime  numbers


 def prime_numbers(n):
     primes = []
     for i in range(2, n + 1):
         is_prime = True
         for j in range(2, i):
             if i % j == 0:
                 is_prime = False
                 break
            
         if is_prime:
             primes.append(i)

     return primes
# Input
 n = int(input("Enter n value: "))
# # Function call
 result = prime_numbers(n)
 # Output
 print("Prime numbers :", result)
 print("Number of prime numbers :", len(result))




# 1 . Write  a  program  to  generate  all   prime  divisors  of  a  number  also  print  how  many  prime  divisors  are  existing

# Hint:  Reuse  the  prime()  function  defined  in   prog3a   but  do  not  rewrite

# 1) What  are  the  outputs  if  input  is  30 ?  --->  Prime divisors : [2, 3, 5]
#                                                                                Number  of  prime  divisors :  3

# 2) What  are  the  outputs  if  input  is  84 ?  --->  Prime divisors : [2, 3, 7]
#                                                                                Number  of  prime  divisors :  3

# 3) What  are  the  outputs  if  input  is  49 ?  --->  Prime divisors : [7]
#                                                                                Number  of  prime  divisors :  1
# '''
 def  prime_divisors(n):
# 	return   list  of  all  prime  divisors  of  'n'
# Read  input
# call  the  function
# print  results


# output : # Assume prime() function is already defined in prog3a and imported
# from prog3a import prime 

# def prime_divisors(n):
#     divisors = []

#     for i in range(2, n + 1):
#         if n % i == 0 and prime(i):   # check divisor + prime
#             divisors.append(i)

#     return divisors


# n = int(input("Enter a number: "))

# result = prime_divisors(n)

# print("Prime divisors :", result)
# print("Number of prime divisors :", len(result))



#------------------------------------------------------------------------

# 2 . # Keyword  only   arguments  demo  program
# def   f1(* , a , b):
#         print(F'a  :  {a}  \t  b :  {b}')
# # End  of  the  function
# f1(a = 10 , b = 20) # output : a  :  10     b :  20
# f1(b = 30 , a = 40) # output : a : 40  b : 30
#f1(50 , 60)  # error
#f1(70 , b = 80) # error
#f1(a = 15 , 25) # error
  
#--------------------------------------------------------------------------

# 3 . #Find  outputs (Home  work)
# def  f1(a , * , b , c):
#         print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# # End  of  function
# f1(10 , b = 20 , c = 30) # output : a : 10 b : 20 c : 30
# f1(a = 40 , b = 50 , c = 60) # output: a : 40 b : 50 c : 60
# f1(c = 100 , b = 90 , a = 80) # output : a : 80 b : 90 c ; 100
# #f1(70 , 80 , c = 90) # output : error
# f1(70 , 80 , 90) # output : error
# #f1(c = 15 , b = 25 , 35) : output : error

#-----------------------------------------------------------------------------

# 4 . # Identify error (Home  work)
#def   f1(a  , b , *): # error
  #      pass

#------------------------------------------------------------------------------

# 5 . #  Positional  only  arguments  demo  program
# def   f1(a , b , /):
#         print(F'a  :  {a}  \t  b  :  {b}')
# # End  of   the  function
# f1(10 , 20) # output : a : 10 b : 20
#f1(a = 30 ,  b = 40)
#f1(50 , b = 60)
#f1(a = 70 , 80)

# -----------------------------------------------------------------

# 6 . # Find  outputs (Home  work)
# def  f1(a , b , / , c):
#         print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# # End  of  function
# f1(10 , 20 , 30) # a: 10  b : 20  c : 30
# f1(40 , 50 , c = 60) # output : a : 50  c : 60
#f1(a = 70 , b = 80 , c = 90) # output : error
#f1(a = 100 , b = 110 , 120) : output : error
#f1(a = 130 , 140 , c = 150) : output : error
#f1(160 , b = 170 , 180) # output : error
#f1(190 , b = 200 , c = 210) # output : error

# ---------------------------------------------------------------------

# 7 . # Find outputs(Home  work)
# def  f1(a , b , / , c , d , * , e  , f):
#         print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# # End of the function
# f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # output : a  :  10  b  :  20   c  :  30   d  :  40   e  :  50   f  :  60
# #f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # output : error
# #f1(1 , 2 , 3 , 4 , 5 , f = 6) # output : error 
# #f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # output : eror
# f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # output : # output : a  :  10  b  :  20   c  :  30   d  :  40   e  :  50   f  :  60


#---------------------------------------------------------------------------------------------------

# 8 . # Identify error (Home  work)
# def  f1(/ , a , b ,  c):
#         pass
# def   f2(a , b , c , *):
#         pass

# def f1(a, /, b, c):
#     pass

def f2(a, b, c, *, d):
    pass

#------------------------------------------------------------------------------------------

# 9 . # Identify  error  (Home  work)
# def  f4(* , a , b , c , /):
# 	        pass

def f4(a, /, *, b, c):
    pass


# ---------------------------------------------------------------------------------------------

# 10 . #  Positional  only  arguments  demo  program
# def   f1(a , b , /):
#         print(F'a  :  {a}  \t  b  :  {b}') # output : a : 10  b : 20
# # End  of   the  function
# f1(10 , 20)
#f1(a = 30 ,  b = 40) # output : typeerror
#f1(50 , b = 60) # output : Typeerror
#f1(a = 70 , 80) # output : syntaxerror


# ---------------------------------------------------------------------------------------------

# 11 . # Find  outputs (Home  work)
# def  f1(a , b , / , c):
#         print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# # End  of  function
# f1(10 , 20 , 30) # output : a : 10  b : 20  c : 30 
# f1(40 , 50 , c = 60) # output : a : 40  b : 50  c : 60
#f1(a = 70 , b = 80 , c = 90) # output : Typeerror
#f1(a = 100 , b = 110 , 120) output : syntaxerror
#f1(a = 130 , 140 , c = 150) # output : syntaxerror
#f1(160 , b = 170 , 180) # output : syntaxerror
#f1(190 , b = 200 , c = 210) # ouptut : typeerror


# -----------------------------------------------------------------------

# 12 . # Find  outputs (Home  work)
# Find outputs(Home  work)
# def  f1(a , b , / , c , d , * , e  , f):
#         print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
#f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # output : a : 10  b : 20  c : 30 d : 40  e : 50  f  : 60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # output : typereeror
#f1(1 , 2 , 3 , 4 , 5 , f = 6) # output : typereeror
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) #output : syntaxerror
#f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # output : a : 10  b : 20  c : 30 d : 40  e : 50  f : 60

#  ------------------------------------------------------------------------------------

# 13 . # Identify error (Home  work)
# def  f1(/ , a , b ,  c): cannot be at the beginning
#         pass
def f1(a, /, b, c):
    pass
# def   f2(a , b , c , *): must be followed by a parameter
#         pass

def f2(a, b, c, *, d):
    pass

#------------------------------------------------------------------------------

# 14 . # Identify  error  (Home  work)
# def  f4(* , a , b , c , /):
# 	        pass

def f4(a, /, *, b, c):
    pass

# -----------------------------------------------------------------------

# 15 . # Find  outputs  (Home  work)
# def  f1(x):
# 	print('1st  function : ' , x)
# def  f1(y):
# 	print('2nd  function : ' , y)
# def  f1(z):
# 	print('3rd  function : ' , z) # output : 3rd  function :  10
# f1(z = 10) 
#f1(y = 20)
#f1(x = 30)

# ---------------------------------------------------------------------

# 16 . # Default  arguments  demo  program
# def   add(a , b = 20 , c = 30):
#         return   a + b + c
# #end  of  the  functiom
# print(add(100))   #  150
# print(add(100 , 200))  #  330
# print(add(100 , 200 , 300))  #   600
# print(add(100 , c = 200)) # output : 320
# print(add(c = 100 , b = 200 , a = 300)) # output : 600
# print(add(c = 100 , a = 200)) # output : 320
#print(add()) # output : error
#print(add(a = 100 , 200)) # output : syntax error
#print(add(100 ,  , 300)) # output : syntaxerror
#print(add(100 ,  b , 300)) # output : b is not defined

# ------------------------------------------------------------------------------------

# 17 . # Identify  Error
# def   f1(a = 10 ,  b ,  c = 20 ,  d):
# 	pass
# def f1(b, d, a=10, c=20):
#     pass
# def   f2(b , d , a = 10 , c = 20):
# 	pass

#---------------------------------------------------------------

# 18 . #  Find  outputs (Home  work)
# def   f1(a = 10):
#         print(a)
# # End  of  the  function
# f1(20)
# f1()
# f1(a = 30)


#----------------------------------------------------------------------------

# 19 . # Find  outputs (Home  work)
# def  add(a , b , c = 10 , d = 20):
#         return  a + b + c + d
# # End  of  the  function
# print(add(100 , 200)) # output : 330
# print(add(100 , 200 , 300)) # output : 620
# print(add(100 , 200 , 300 , 400)) # output : 1000
# print(add(b = 100 , a = 200)) # output : 330
# print(add(100 , 200 , d = 300)) # output : 610
# print(add(d = 100 , a = 200 , b = 300)) # output : 610
#print(add(c = 100 , d = 200 , 300 , 400)) # output : syntaxerror
#print(add(100 , 200 , c = 300 , x = 400)) # output : typeerror
#print(add()) # output : typeeeror


# ----------------------------------------------------------------

# 20 . #  Find  outputs (Home  work)
# def    f1(x = 25):
#         return  x
# def   f2(x):
#         return  x
# # End  of  the  function
# print(f1(10)) # output : 10
# print(f1()) # output : 25
# print(f2(20)) # output : 20
#print(f2()) # output ; typeerror

#------------------------------------------------------------------------------------

# 21 . # Find  outputs (Home  work)
# def   disp(ch = '*' , n = 4):
#         print(ch *  n)
# # End of the function
# disp('-' , 6) #  output : _ _ _ _ _ _ 
# disp('$') # output : $$$$
# disp()
# disp(n = 5)
# disp(5)
# disp(n = 7 , ch = '%') %%%%%%%
# disp(7 , '@') # @@@@@@@
# disp(7 , n = 6) # 46
#disp(ch = '!' ,  5) # output  syntaxerror

#---------------------------------------------------------------------------

# 22 . # Find  outputs (Home  work)
# def  power(a , b  =  2):
#         return  a ** b
# # End  of the function
# print(power(2 , 6)) # output :64
# print(power(5)) # output : 25
# print(power(b = 3 , a = 4.5)) # output :91.125
# print(power(3 + 4j))# output : (-7+24j)
# print(power(True)) # output : 25
# def   power(b = 2 , a): # syntax error
#  	 pass

#-------------------------------------------------------------------------------------

# 23 . # Find outputs  (Home  work)
# def   add(a , b):
# 	print('2-argument  function')
# 	return a + b
# def  add(a , b , c):
# 	print('3-argument  function')
# 	return a + b + c
# def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
# 	print('4-argument  function') # output : 4-argument  function
# 	return a + b  + c + d
# # End  of  the  function
# print(add(10 , 20 , 30 , 40))
# print(add(50 , 60 , 70))
# print(add(80 , 90))
# print(add(100))
# print(add())

# output : 4-argument  function
# 100
# 4-argument  function
# 184
# 4-argument  function
# 177
# 4-argument  function
# 109
# 4-argument  function
# 10

# ------------------------------------------------------------------------------

# 24 . # Find outputs  (Home  work)
# def  disp(a , b):
#         print('2-argument function  :  ' , a , b)
# def  disp(a , b , c , d):
#         print('4-argument  function  :  ' , a , b , c , d)
# def disp(a , b , c = 25):
#         print('3-argument  function  :  ' , a , b , c) # output : 3-argument  function  :   10 20 30
#                                                        # output : 3-argument  function  :   80 90 25
# #end
# disp(10 , 20 , 30)
# #disp(40 , 50 , 60 , 70) # output : typererror
# disp(80 , 90)


#------------------------------------------------------------------------------------

# 25 . # Find outputs(Home  work)
# def   add(* , a = 10 , b = 20):
#         return  a + b
# # End of  the  function
# print(add(a = 30 , b = 40)) # output : 70
# print(add()) # output : 30
# print(add(a = 50)) # output : 70
# print(add(b = 60 , a = 70)) # output : 130
#print(add(80 , 90)) # output : typererror

#------------------------------------------------------------------------------

# 26 . # Find  outputs(Home  work)
# def   add(a = 10 , b , c):
#         pass
# def   add( * , a = 10 , b , c ):
#         return  a + b + c
# # End  of  the  function
# print(add(a = 30 , b = 40 , c = 50)) # output : 120
# print(add(b = 60 , c = 70)) # output : 140
# print(add(c = 80 , b = 90 , a = 100)) # output :: 270
#print(add(c = 25 , a = 43)) # output : typererrpr
#print(add(1 , 2 , 3)) # output : typererror
# def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
# 		pass

# ----------------------------------------------------------------------------------------

# 27 . # Find  output (Home  work)
# def   f1(a = []):
#         pass
# print(f1 . _defaults_)

#correct code :
# def f1(a = []):
#     pass
# print(f1.__defaults__)


# -----------------------------------------------------------------------------------------

# 28 . # Find  outputs (Home  work)
# def   f1(x , a = []):
# 	a . append(x)
# 	print('List :  ' ,  a)
# #end  of  the  function
# #print('_defaults_  :  ' , f1._defaults_) # output : error
# f1(3)
# #print('_defaults_  :  ' , f1._defaults_) # output : error
# f1(4 , [1 , 2 , 3])
# #print('_defaults_  :  ' , f1._defaults_) # output : error
# f1(9)
# # print('_defaults_  :  ' , f1._defaults_) output : error
# f1(40 , [10 , 20 , 30])
# #print('_defaults_  :  ' , f1._defaults_) output : error
# f1(5)
# #print('_defaults_  :  ' , f1._defaults_) output : error
# f1([6 , 7 , 8])
#print('_defaults_  :  ' , f1._defaults_) output : error

# output : 
# List :   [3]
# List :   [1, 2, 3, 4]
# List :   [3, 9]
# List :   [10, 20, 30, 40]
# List :   [3, 9, 5]
# List :   [3, 9, 5, [6, 7, 8]]

# ---------------------------------------------------------------------------------------

# 29 . # Find  outputs(Home  work)
# def     f1(x , a = []):
# 	for  i  in  range(x):
# 		a . append(i * i)
# 	return  a
# # End  of  the  function
# #print('_defaults  :  ' , f1._defaults_) # output : error
# print(f1(3))
# #print('_defaults  :  ' , f1._defaults_) # output : error
# print(f1(4 , [10 , 20 , 15 , 18]))
# #print('_defaults  :  ' , f1._defaults_) # output : error
# print(f1(5)) 
# #print('_defaults  :  ' , f1._defaults_) # output : error
# print(f1(a = [100 , 200 , 300],   x = 6 ))
# #print('_defaults  :  ' , f1._defaults_) # output : error
# print(f1(6))
# #print('_defaults  :  ' , f1._defaults_) # output : error

# output :
# [0, 1, 4]
# [10, 20, 15, 18, 0, 1, 4, 9]
# [0, 1, 4, 0, 1, 4, 9, 16]
# [100, 200, 300, 0, 1, 4, 9, 16, 25]
# [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]

#---------------------------------------------------------------------------------

# 30 # Find  outputs
# def   f1(a = 'Hyd' , b = []):
# 	a += "Sec"
# 	b += [1 , 2 , 3]
# 	print('a :  ' , a)
# 	print('b :  ' , b)
# # End of the function
# print('Default Values  :  ' , f1 . _defaults_)
# f1()
# print('Default Values  :  ' , f1 . _defaults_)
# f1()
# print('Default Values  :  ' , f1 . _defaults_)
# f1()
# output : 
# [0, 1, 4]
# [10, 20, 15, 18, 0, 1, 4, 9]
# [0, 1, 4, 0, 1, 4, 9, 16]
# [100, 200, 300, 0, 1, 4, 9, 16, 25]
# [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]

#---------------------------------------------------------------------------------------------

# 31 . #  Variable  number  of  arguments  demo  program
# def   f1(*t):
# 	print(t)
# 	print(type(t))
# 	print(len(t))
# 	print()
# # End  of  the  function
# f1(10 , 20 , 15 , 18)
# f1()
# f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
# f1('Hyd')
# tpl = (100 , 200 , 150)
# f1(tpl)
#f1(t = (10 , 20 , 30)) #   Error

# output : (10, 20, 15, 18)
# <class 'tuple'>
# 4
# ()
# <class 'tuple'>
# 0
# ([10, 20], (30, 40, 50), {80, 90, 60, 70})
# <class 'tuple'>
# 3
# ('Hyd',)
# <class 'tuple'>
# 1
# ((100, 200, 150),)
# <class 'tuple'>
# 1


# ----------------------------------------------------------------------------------------

# 32 . #  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
# def  avg(*a):
# 	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# # End  of  the  function
# print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18
# print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True
# print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
# print(avg())
# print(avg(25))
# print(avg(3 + 4j , 5 + 6j))
# tpl = (10 , 20 , 15 , 18)
# print(avg(tpl))

# code : 
# def avg(*a):
#     return sum(a) / len(a) if len(a) != 0 else 0
# # Function calls
# print(avg(10 , 20 , 15 , 18))
# print(avg(25 , 10.8 , True))
# print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
# print(avg())
# print(avg(25))
# print(avg(3 + 4j , 5 + 6j))

# tpl = (10 , 20 , 15 , 18)
#print(avg(tpl))

# output : 15.75
# 12.266666666666666
# 14.26
# 0
# 25.0
# (4+5j)

#---------------------------------------------------------------------------

# 33 . # Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
# def  concat(*a):
# 	Write  code  to  return  join  of  all  the  strings  passed  to  the  function  (1  line)
# # End   of  the   function
# print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
# print(concat('Hyd', 'Is', 'Green', 'City'))
# print(concat('Python', 'Is', 'A', 'Great', 'Language'))
# print(concat())
# print(concat('Python'))
# print(concat(1, 2, 3))

# def concat(*a):
#     return " ".join(a)

# # Function calls
# print(concat('Sankar', 'Dayal', 'Sarma'))
# print(concat('Hyd', 'Is', 'Green', 'City'))
# print(concat('Python', 'Is', 'A', 'Great', 'Language'))
# print(concat())
# print(concat('Python'))
# print(concat(1, 2, 3))

# output : Sankar Dayal Sarma
# Hyd Is Green City
# Python Is A Great Language
# Python

#--------------------------------------------------------------------------------------------

# 34 . #Find  outputs (Home  work)
# def   f1(a = 25  , *b):
#         print(F'a : {a}  \t   b  :  {b} ')
# # End  of  the  function
# f1(10 , 20 , 30 , 40)
# f1(50 , 60)
# f1(70)
# f1(a = 80)
# #f1(b = (10 , 20 , 30) , a = 40) 
# f1()
# #f1(a = 10 , (20 , 30 , 40)) output : syntaxerror
# #f1(25 , b = (10 , 20 , 30))
# #f1(25 , a = (10 , 20 , 30)) output : syntaxerror
# f1((10 , 20 , 30) , 10 , 20 , 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30) # output : syntaxerror

# # output : a : 10             b  :  (20, 30, 40) 
# a : 50             b  :  (60,) 
# a : 70             b  :  () 
# a : 80             b  :  () 
# a : 25             b  :  () 
# a : (10, 20, 30)           b  :  (10, 20, 30) 

# ----------------------------------------------------------------------------------

# 35 . # Find  outputs (Home  work)
# def    f1(*a , b):
# 	print(F'a  :  {a}   \t   b  :  {b}')
# # End  of  the  function
# f1(10 , 20 , 30 , b = 40)
# f1(50 , b = 60)
# f1(b = 70)
# #f1(b = 10 , a = (20 , 30 , 40)) # output : error
# #f1(b = 10 , (20 , 30 , 40)) output : syntaxerror
# #f1()
# #f1(10 , 20 , 30 , (10 , 20 , 30))
# #f1(10 , 20 , 30 , 40)
# #f1(25)
# f1(10 , 20 , 30 , b = (10 , 20 , 30))

# output : a  :  (10, 20, 30)         b  :  40
# a  :  (50,)        b  :  60
# a  :  ()           b  :  70
# a  :  (10, 20, 30)         b  :  (10, 20, 30)


# ----------------------------------------------------------------------------------------

# 36 . #Find  outputs (Home  work)
# def   f1(a , *b , c):
#         print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# # End  of  the  function
# f1(10 , 20 , 30 , 40 , c = 50)
# f1(60 , 70 , c = 80)
# f1(90 , c = 100)
#f1(a = 1 , 2 , c = 3) # output : error
#f1(1 , 2 , 3)
#f1(a = 1 , b = 2 , c = 3)
#f1(a = 25 , 100 , 200 , 300 , c = 35)

# output : 
# a  :  10          b  :  (20, 30, 40)      c  :  50
# a  :  60          b  :  (70,)     c  :  80
# a  :  90          b  :  ()        c  :  100

# ---------------------------------------------------------------------------------------S

# 37 . # Which  of  the  following  are  valid  ?  (Home  work)
# def   f1(*a , *b): error
#         pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
# def   f6( * , a , *b , c): # output : error
#        pass
# def   f7(a , *b , c ,  /): # output : error
#        pass

#-----------------------------------------------------------------------------------
# 38 . # Find  outputs  (Home  work)
# def   f1(*a):
# 	print(a)
# 	print(type(a))
# 	for  x  in  a:
# 		print(x)
# 		print(type(x))
# # End  of  the  function
# f1([10 , 20] , {30 , 40} , (50 , 60))

# # output : 
# ([10, 20], {40, 30}, (50, 60))
# <class 'tuple'>
# [10, 20]
# <class 'list'>
# {40, 30}
# <class 'set'>
# (50, 60)
# <class 'tuple'>

#-------------------------------------------------------------------------------------------------

# 39 . # Variable  number  of  keyword  arguments  demo  program
# def   disp(**a):
# 	print('Results')
# 	print(type(a))
# 	print(a)
# 	print()
# # End  of  the  function
# disp(RollNo = 10 , StudName = 'Rama  Rao')
# disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
# disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
# disp()
# # output : 
# Results
# <class 'dict'>
# {'RollNo': 10, 'StudName': 'Rama  Rao'}
# Results
# <class 'dict'>
# {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
# Results
# <class 'dict'>
# {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
# Results
# <class 'dict'>
# {}

#-----------------------------------------------------------------------------------------------------------
# 40 . # Find  outputs  (Home  work)
# def  f1(**a):
# 	print('Results')
# 	for  k , v   in   a . items():
# 		print(k , v , sep = ' ... ')
# # End  of  the  function
# f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
# f1()

#output : 
# Results
# Empno ... 25
# Empname ... Rama  Rao
# Salary ... 10000.0
# Gender ... m
# Results

#---------------------------------------------------------------------------------------------------------

# 41 . # Find  outputs (Home  work)
# def   f1(*a):
# 	print(type(a))
# 	print(a)
# def   f2(**a):
# 	print(type(a))
# 	print(a)
# # End  of  the  function
# f1(25 , 10.8 , 'Hyd' , True)
# print()
# f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

# # output : 
# <class 'tuple'>
# (25, 10.8, 'Hyd', True)

# <class 'dict'>
# {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

#---------------------------------------------------------------------------------------------------------

# 42 . #  Find  outputs (Home work)
# def   f1(empno , ename , sal):
# 	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
# def   f2(**a):
# 	print(a)
# # End  of  the  function
# f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
# #f1(eno = 25 , empname = 'Sita' , salary = 10000.0)  
# f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
# f2(eno = 25 , empname = 'Sita' , salary = 10000.0)

# # output : 
# Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
# {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
# {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}



# 43 . # Find  outputs   (Home  work)
# def    f1(a ,  *b , **c):
# 	print(a)
# 	if   b:
# 		print(b)
# 	if  c:
# 		print(c)
# # End  of  the  function
# f1(25)
# print()
# f1('Hyd' , 10 , 20 , 30)
# print()
# f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)

# output : 25
# Hyd
# (10, 20, 30)

# 10.8
# (25, 'Hyd', True)
# {'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}