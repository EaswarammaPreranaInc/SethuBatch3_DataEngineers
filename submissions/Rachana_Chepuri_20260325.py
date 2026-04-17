'''
Write  a  program  to  generate  all   prime  divisors  of  a  number  also  print  how  many  prime  divisors  are  existing

Hint:  Reuse  the  prime()  function  defined  in   prog3a   but  do  not  rewrite

1) What  are  the  outputs  if  input  is  30 ?  --->  Prime divisors : [2, 3, 5]
                                                                               Number  of  prime  divisors :  3

2) What  are  the  outputs  if  input  is  84 ?  --->  Prime divisors : [2, 3, 7]
                                                                               Number  of  prime  divisors :  3

3) What  are  the  outputs  if  input  is  49 ?  --->  Prime divisors : [7]
                                                                               Number  of  prime  divisors :  1
'''
from srilekha_thundla_20260323 import prime
def  prime_divisors(n):
        l = []
        for i in range(2,n+1):
                if n%i==0 and prime(i):
                        l.append(i)
        return l                
print(prime_divisors(n=int(input('Enter any number : '))))

# Keyword  only   arguments  demo  program
# def   f1(* , a , b):
#         print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
# f1(a = 10 , b = 20) # a  :  10     b : 20
# f1(b = 30 , a = 40) # a  :  30     b : 40
# f1(50 , 60) #error because after * there should be key word arguements only
# f1(70 , b = 80)#error because after * there should be key word arguements only
# f1(a = 15 , 25)#error because after * there should be key word arguements only

#Find  outputs (Home  work)
# def  f1(a , * , b , c):
#         print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
# f1(10 , b = 20 , c = 30)#a  : 10   b : 20   c : 30
# f1(a = 40 , b = 50 , c = 60)#a  : 40   b : 90   c : 60
# f1(c = 100 , b = 90 , a = 80)#a  : 80   b : 90   c : 100
# f1(70 , 80 , c = 90)# error because there is positional arguement after *
# f1(70 , 80 , 90)#error because after * there should key word arguements only 
# f1(c = 15 , b = 25 , 35)#error because there should not be positional arhuement after key word arguement

# Identify error (Home  work)
# def   f1(a  , b , *):#error after * there should be at least one arguement
        
#         pass

#  Positional  only  arguments  demo  program
# def   f1(a , b , /):
#         print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
# f1(10 , 20)#a : 10  b : 20
# f1(a = 30 ,  b = 40)#error because here positional only  arguements  accepted
# f1(50 , b = 60)#error because here positional only arguements  accepted
# f1(a = 70 , 80)#error because here positional only arguements  accepted

# Find  outputs (Home  work)
# def  f1(a , b , / , c):
#         print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
# f1(10 , 20 , 30)#a : 10   b : 20  c  : 30
# f1(40 , 50 , c = 60)#a : 40   b : 50  c  : 60
# f1(a = 70 , b = 80 , c = 90)#error because a,b should be positional arguements only
# f1(a = 100 , b = 110 , 120)#error because a,b should be positional arguements only and after key word arguement there should not be positional arguements
# f1(a = 130 , 140 , c = 150)##error because a should be positional arguements only and after key word arguement there should not be positional arguements
# f1(160 , b = 170 , 180)# error
# f1(190 , b = 200 , c = 210)#error

# Find outputs(Home  work)
# def  f1(a , b , / , c , d , * , e  , f):
#         print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
# f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#a : 10  b : 20  c : 30  d : 40  e : 50  f : 60
# f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)##error b should be positional atguement
# f1(1 , 2 , 3 , 4 , 5 , f = 6)#error because e should be keyword arguement
# f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#error because after key word arguements positional arguements are not acceptable
# f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#a : 10  b : 20  c : 30  d : 40  e : 50  f : 60


# Identify error (Home  work)
# def  f1(/ , a , b ,  c):#error / should be after atleast one arguement
#         pass
# def   f2(a , b , c , *):#error * should be before atleast one arguement
#         pass

# Identify  error  (Home  work)
# def  f4(* , a , b , c , /):#invalid
# 	        pass

# Find  outputs  (Home  work)
# def  f1(x):
# 	print('1st  function : ' , x)
# def  f1(y):
# 	print('2nd  function : ' , y)
# def  f1(z):
# 	print('3rd  function : ' , z)
# f1(z = 10)#3rd function : 10
# f1(y = 20)#error
# f1(x = 30)#error

# Default  arguments  demo  program
# def   add(a , b = 20 , c = 30):
#         return   a + b + c
#end  of  the  functiom
# print(add(100))   #  150
# print(add(100 , 200))  #  330
# print(add(100 , 200 , 300))  #   600
# print(add(100 , c = 200))# 320
# print(add(c = 100 , b = 200 , a = 300)) # 600
# print(add(c = 100 , a = 200)) # 320
# print(add())#error
# print(add(a = 100 , 200))# after key word arguements positional arguements are not accepted
# print(add(100 ,  , 300))# error invalid syntax

# Identify  Error
# def   f1(a = 10 ,  b ,  c = 20 ,  d): # after default arguements there should not be non-default arguemnt
# 	pass
# def   f2(b , d , a = 10 , c = 20):
# 	pass

#  Find  outputs (Home  work)
# def   f1(a = 10):
#         print(a)
# End  of  the  function
# f1(20)# 20
# f1()# 10
# f1(a = 30) # 30

# Find  outputs (Home  work)
# def  add(a , b , c = 10 , d = 20):
#         return  a + b + c + d
# End  of  the  function
# print(add(100 , 200)) # 330
# print(add(100 , 200 , 300)) #  620
# print(add(100 , 200 , 300 , 400)) # 1000
# print(add(b = 100 , a = 200)) # 330
# print(add(100 , 200 , d = 300)) # 610
# print(add(d = 100 , a = 200 , b = 300)) # 610
# print(add(c = 100 , d = 200 , 300 , 400)) # error after key word arguements positional args are not accepted
# print(add(100 , 200 , c = 300 , x = 400)) # errro x is not function header
# print(add()) # error because expected 4 but here it is taking 2 args

#  Find  outputs (Home  work)
# def    f1(x = 25):
#         return  x
# def   f2(x):
#         return  x
# End  of  the  function
# print(f1(10))# 10
# print(f1()) # 25
# print(f2(20)) # 20
# print(f2()) # expected 1 arg but 0 are there


# Find  outputs (Home  work)
# def   disp(ch = '*' , n = 4):
#         print(ch *  n)
# End of the function
# disp('-' , 6) # ------
# disp('$') # $$$$
# disp()# ****
# disp(n = 5) # *****
# disp(5) # 20
# disp(n = 7 , ch = '%') # %%%%%%%
# disp(7 , '@') # @@@@@@@
# disp(7 , n = 6) # 42
# disp(ch = '!' ,  5) # error after key word arguement positional arguements are not accepted 


# Find  outputs (Home  work)
# def  power(a , b  =  2):
#         return  a ** b
# End  of the function
# print(power(2 , 6)) # 64
# print(power(5)) # 25
# print(power(b = 3 , a = 4.5)) # 4.5**3
# print(power(3 + 4j))# 3 + 4j**2
# print(power(True)) # 1
# def   power(b = 2 , a) # error after default arguement non-default arguements are not accepted 
#  	 pass


# Find outputs  (Home  work)
# def   add(a , b):
# 	print('2-argument  function')
# 	return a + b
# def  add(a , b , c):
# 	print('3-argument  function')
# 	return a + b + c
# def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
# 	print('4-argument  function')
# 	return a + b  + c + d
# End  of  the  function
# print(add(10 , 20 , 30 , 40)) #  4-argument  function <next line> 100
# print(add(50 , 60 , 70))# 4-argument  function <next line> 184
# print(add(80 , 90))# 4-argument  function <next line> 177
# print(add(100))# 4-argument  function <next line> 109
# print(add())# 4-argument  function <next line> 10

# Find outputs  (Home  work)
# def  disp(a , b):
#         print('2-argument function  :  ' , a , b)
# def  disp(a , b , c , d):
#         print('4-argument  function  :  ' , a , b , c , d)
# def disp(a , b , c = 25):
#         print('3-argument  function  :  ' , a , b , c)
#end
# disp(10 , 20 , 30) #3-argument  function  :  10 , 20 , 30 
# disp(40 , 50 , 60 , 70) # error 
# disp(80 , 90)# 3-argument  function  :  80 , 90, 25

# Find outputs(Home  work)
# def   add(* , a = 10 , b = 20):
#         return  a + b
# End of  the  function
# print(add(a = 30 , b = 40))# 70
# print(add()) # 30
# print(add(a = 50)) # 70
# print(add(b = 60 , a = 70)) # 130
# print(add(80 , 90)) # erro

# Find  outputs(Home  work)
# def   add(a = 10 , b , c): # error
#         pass
# def   add( * , a = 10 , b , c ):
#         return  a + b + c
# End  of  the  function
# print(add(a = 30 , b = 40 , c = 50)) # 1120
# print(add(b = 60 , c = 70)) # 140
# print(add(c = 80 , b = 90 , a = 100)) # 270
# print(add(c = 25 , a = 43)) # error 
# print(add(1 , 2 , 3)) # error
# def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f): # error
# 		pass


# Find  output (Home  work)
# def   f1(a = []):
#         pass
# print(f1 . __defaults__) # ([],)

# Find  outputs (Home  work)
# def   f1(x , a = []):
# 	a . append(x)
# 	print('List :  ' ,  a)
#end  of  the  function
# print('__defaults__  :  ' , f1.__defaults__) #__defaults__  : ([],)
# f1(3) # List : [3]
# print('__defaults__  :  ' , f1.__defaults__) #__defaults__  :  ([3],)
# f1(4 , [1 , 2 , 3]) # List : [1,2,3,4]
# print('__defaults__  :  ' , f1.__defaults__) # __defaults__  : ([3],) 
# f1(9)# List :   [3, 9]
# print('__defaults__  :  ' , f1.__defaults__) #__defaults__  :   ([3, 9],)
# f1(40 , [10 , 20 , 30]) # List :   [10, 20, 30, 40]
# print('__defaults__  :  ' , f1.__defaults__) #__defaults__  :   ([3, 9],)
# f1(5) #List :   [3, 9, 5]
# print('__defaults__  :  ' , f1.__defaults__)# __defaults__  :   ([3, 9, 5],)
# f1([6 , 7 , 8])#List :   [3, 9, 5, [6, 7, 8]]
# print('__defaults__  :  ' , f1.__defaults__) #__defaults__  :   ([3, 9, 5, [6, 7, 8]],)

# Find  outputs(Home  work)
# def     f1(x , a = []):
# 	for  i  in  range(x):
# 		a . append(i * i)
# 	return  a
# End  of  the  function
# print('__defaults_  :  ' , f1.__defaults__) #__defaults_  :   ([],)
# print(f1(3)) #[0,1,4]
# print('__defaults_  :  ' , f1.__defaults__) ##__defaults_  :   ([0,1,4],)
# print(f1(4 , [10 , 20 , 15 , 18])) #[10, 20, 15, 18, 0, 1, 4, 9]
# print('__defaults_  :  ' , f1.__defaults__) #__defaults_  :   ([],)
# print(f1(5))#[0,1,4,9,16]
# print('__defaults_  :  ' , f1.__defaults__)#__defaults_  :   ([0,1,4,9,16],)
# print(f1(a = [100 , 200 , 300],   x = 6 ))#[100 , 200 , 300,0,1,4,9,16,25]
# print('__defaults_  :  ' , f1.__defaults__)#__defaults_  :   ([],)
# print(f1(6))#[0,1,4,9,16,25]
# print('__defaults_  :  ' , f1.__defaults__)#__defaults_  :   ([0,1,4,9,16,25],)

# Find  outputs
# def   f1(a = 'Hyd' , b = []):
# 	a += "Sec"
# 	b += [1 , 2 , 3]
# 	print('a :  ' , a)
# 	print('b :  ' , b)
# End of the function
# print('Default Values  :  ' , f1 . __defaults__)#Default Values  :(Hyd, [])
# f1()# a : HydSec
    # b : [1 , 2 , 3]
# print('Default Values  :  ' , f1 . __defaults__)#Default Values  : (Hyd,[] )
# f1()# a : HydSec
#     # b : [1 , 2 , 3]
# print('Default Values  :  ' , f1 . __defaults__) #Default Values  : (Hyd,[] )
# f1()# a : HydSec
#     # b : [1 , 2 , 3]

#  Variable  number  of  arguments  demo  program
# def   f1(*t):
# 	print(t)
# 	print(type(t))
# 	print(len(t))
# 	print()
# End  of  the  function
# f1(10 , 20 , 15 , 18)#(10 , 20 , 15 , 18)
    #<class 'tuple'>
	#4
	
# f1()#()
#<class 'tuple'>
#0
	
# f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
#([10, 20], (30, 40, 50), {80, 90, 60, 70})
#<class 'tuple'>
#3
# f1('Hyd')
#('Hyd',)
#<class 'tuple'>
#1
# tpl = (100 , 200 , 150)
#((100 , 200 , 150),)
#<class 'tuple'>
#1
# f1(tpl)
# f1(t = (10 , 20 , 30)) #   Error

#Find  outputs (Home  work)
# def   f1(a = 25  , *b):
#         print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
# f1(10 , 20 , 30 , 40)# a : 10  b : (20 , 30 , 40)
# f1(50 , 60)# a : 50  b : (60,)
# f1(70)# a : 70  b : ()
# f1(a = 80)#  a : 80  b : ()
# f1(b = (10 , 20 , 30) , a = 40)# error
# f1() # a : 25  b : ()
# f1(a = 10 , (20 , 30 , 40))#error
# f1(25 , b = (10 , 20 , 30))error
# f1((10 , 20 , 30) , 10 , 20 , 30)a : (10 , 20 , 30)  b : (10 , 20 , 30)
# f1(a = (10 , 20 , 30) , 10 , 20 , 30)#error

# Find  outputs (Home  work)
# def    f1(*a , b):
# 	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
# f1(10 , 20 , 30 , b = 40) #a  :  (10, 20, 30)         b  :  40
# f1(50 , b = 60)#a  :  (50,)         b  :  60
# f1(b = 70) # a  :  ()         b  :  70
# f1(b = 10 , a = (20 , 30 , 40))#error
# f1(b = 10 , (20 , 30 , 40))#error
# f1()#error
# f1(10 , 20 , 30 , (10 , 20 , 30))#error
# f1(10 , 20 , 30 , 40)#error
# f1(25)#error
# f1(10 , 20 , 30 , b = (10 , 20 , 30))#a  :  (10, 20, 30)         b  :  (10,20,30)

#Find  outputs (Home  work)
# def   f1(a , *b , c):
#         print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
# f1(10 , 20 , 30 , 40 , c = 50)#a : 10   b : (20,30,40)   c : 50
# f1(60 , 70 , c = 80)#a : 60   b : (70,)   c : 80
# f1(90 , c = 100)#a : 90  b : ()   c : 100
# f1(a = 1 , 2 , c = 3)#error
# f1(1 , 2 , 3)#errror
# f1(a = 1 , b = 2 , c = 3)#error
# f1(a = 25 , 100 , 200 , 300 , c = 35)#error

# Which  of  the  following  are  valid  ?  (Home  work)
# def   f1(*a , *b):#invalid
#         pass
# def  f2(*a , b):#valid
#         pass
# def  f3(a , *b):#valid
#         pass
# def  f4(a , b):#valid
#         pass
# def    f5(a , *b , c):#valid
#         pass
# def   f6( * , a , *b , c):#invalid
#        pass
# def   f7(a , *b , c ,  /):#invalid
#        pass

# Find  outputs  (Home  work)
# def   f1(*a):
# 	print(a)#([10 , 20] , {30 , 40} , (50 , 60))
# 	print(type(a))#<class 'tuple'>
# 	for  x  in  a:
# 		print(x)#[10,20]<next line><class 'list'><next line>{30,40}<next line><class 'dict'><next line>(50,60)<next line><list 'tuple>
# 		print(type(x))
# # End  of  the  function
# f1([10 , 20] , {30 , 40} , (50 , 60))

# Variable  number  of  keyword  arguments  demo  program
# def   disp(**a):
# 	print('Results')#Results
# 	print(type(a))#<class 'dict'>
# 	print(a)
# 	print()
# # End  of  the  function
# disp(RollNo = 10 , StudName = 'Rama  Rao')
# disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
# disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
# disp()

# Find  outputs  (Home  work)
# def  f1(**a):
# 	print('Results')
# 	for  k , v   in   a . items():
# 		print(k , v , sep = ' ... ')
# # End  of  the  function
# f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
# f1()
# Results
# Empno ... 25
# Empname ... Rama  Rao
# Salary ... 10000.0
# Gender ... m
# Results

# Find  outputs (Home  work)
# def   f1(*a):
# 	print(type(a))
# 	print(a)
# def   f2(**a):
# 	print(type(a))
# 	print(a)
# End  of  the  function
# f1(25 , 10.8 , 'Hyd' , True)
# print()
# f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
# <class 'tuple'>
# (25, 10.8, 'Hyd', True)

# <class 'dict'>
# {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
# def  avg(*a):
# 	return sum(a)/len(a)
# # End  of  the  function
# print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18
# print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True
# print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
# print(avg())
# print(avg(25))
# print(avg(3 + 4j , 5 + 6j))
# tpl = (10 , 20 , 15 , 18)
# print(avg(tpl))

# Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
# def  concat(*a):
# 	c = ''
# 	for i in a:
# 		c+=i+' '
# 	return c
		
# End   of  the   function
# print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
# print(concat('Hyd', 'Is', 'Green', 'City'))
# print(concat('Python', 'Is', 'A', 'Great', 'Language'))
# print(concat())
# print(concat('Python'))
# print(concat(1, 2, 3))