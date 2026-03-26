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
def  prime_divisors(n):
	return   list  of  all  prime  divisors  of  'n'
Read  input
call  the  function
print  results



# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # a:10 b:20
f1(b = 30 , a = 40) # a:40 b:30
f1(50 , 60) # error
f1(70 , b = 80) #error
f1(a = 15 , 25) # error




#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a:10 b:20 c:30
f1(a = 40 , b = 50 , c = 60) #a:40 b:50 c:60
f1(c = 100 , b = 90 , a = 80) # a:80 b:90 c:100
f1(70 , 80 , c = 90) # error
f1(70 , 80 , 90) # error
f1(c = 15 , b = 25 , 35) # error



# Identify error (Home  work)
def   f1(a  , b , *):
        pass # error as no arguments after stare


#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)  # error
f1(a = 30 ,  b = 40) # a:30 b:40
f1(50 , b = 60) # a:50 b:60
f1(a = 70 , 80) # error




# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a:10 b:20 c:30
f1(40 , 50 , c = 60) #a:40 b:50 c:60
f1(a = 70 , b = 80 , c = 90) # a: 70 b:80 c:90
f1(a = 100 , b = 110 , 120) #error
f1(a = 130 , 140 , c = 150) # a:130 b:140 c:150
f1(160 , b = 170 , 180) # error
f1(190 , b = 200 , c = 210) # a:190 b:200 c:210



# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) #a:10 b:20 c:30 d:40 e:50 f:60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # error
f1(1 , 2 , 3 , 4 , 5 , f = 6) # error
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # error
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # a:10 b:20 c:30 d:40 e:50 f:60


# Identify error (Home  work)
def  f1(/ , a , b ,  c):
        pass # error as their is / before arguments
def   f2(a , b , c , *):
        pass  # error as their is * After arguments


# Identify  error  (Home  work)
def  f4(* , a , b , c , /): # at a time * and / not permitted
	        pass 



# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x) 
def  f1(y):
	print('2nd  function : ' , y) 
def  f1(z):
	print('3rd  function : ' , z) 
f1(z = 10) # 10
f1(y = 20) # error
f1(x = 30) # error




# Default  arguments  demo  program
def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))   #  150
print(add(100 , 200))  #  330
print(add(100 , 200 , 300))  #   600
print(add(100 , c = 200)) #320
print(add(c = 100 , b = 200 , a = 300)) #600
print(add(c = 100 , a = 200)) # 320
print(add()) # error
print(add(a = 100 , 200)) # error
print(add(100 ,  , 300)) # error
print(add(100 ,  b , 300)) # error



# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d): #Non-default arguments go first → b, d
	pass 
def   f2(b , d , a = 10 , c = 20): # Non-default arguments go first → b, d
	pass


#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a) # 10
# End  of  the  function
f1(20) # 20
f1() # 10
f1(a = 30) # 30



# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))#330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400)) #1000
print(add(b = 100 , a = 200)) # 330 
print(add(100 , 200 , d = 300)) # 610
print(add(d = 100 , a = 200 , b = 300)) #610
print(add(c = 100 , d = 200 , 300 , 400)) # error
print(add(100 , 200 , c = 300 , x = 400)) # error
print(add()) # error


#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x # 25
# End  of  the  function
print(f1(10)) # 10
print(f1()) # 25
print(f2(20))# 20
print(f2()) # error



# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # ------
disp('$') # $$$$
disp() # error
disp(n = 5) # *****
disp(5) # 20
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # @@@@@@@
disp(7 , n = 6) # 7777777
disp(ch = '!' ,  5) # !!!!!



# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5)) # 91.125
print(power(3 + 4j)) # (-7+24j)
print(power(True)) # 1
def   power(b = 2 , a): # error
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
print(add(10 , 20 , 30 , 40)) # 100
print(add(50 , 60 , 70)) # 184
print(add(80 , 90)) #177
print(add(100)) #109
print(add()) # 10


# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 10 20 30
disp(40 , 50 , 60 , 70) # error
disp(80 , 90) # 80 90 25



# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) #70
print(add()) #30
print(add(a = 50)) #70
print(add(b = 60 , a = 70)) #130
print(add(80 , 90)) # error



# Find  outputs(Home  work)
def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) #120
print(add(b = 60 , c = 70)) # 140 
print(add(c = 80 , b = 90 , a = 100)) # 270
print(add(c = 25 , a = 43)) # error
print(add(1 , 2 , 3)) # error
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass 


# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . __defaults__) # ([],)




# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)
f1(3) #([3],)
print('__defaults__  :  ' , f1.__defaults__)
f1(4 , [1 , 2 , 3]) # ([1,2,3,4])
print('__defaults__  :  ' , f1.__defaults__)
f1(9) #([3,9],)
print('__defaults__  :  ' , f1.__defaults__)
f1(40 , [10 , 20 , 30]) # ([10,20,30,40)]
print('__defaults__  :  ' , f1.__defaults__)
f1(5) #([3,9,5],)
print('__defaults__  :  ' , f1.__defaults__)
f1([6 , 7 , 8]) # [3,9,5,[6,7,8]]
print('__defaults__  :  ' , f1.__defaults__)


# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('__defaults_  :  ' , f1.__defaults__)
print(f1(3)) #(3,)
print('__defaults_  :  ' , f1.__defaults__)
print(f1(4 , [10 , 20 , 15 , 18])) #[4,10,20,15,18]
print('__defaults_  :  ' , f1.__defaults__)
print(f1(5)) #([3, 5],)
print('__defaults_  :  ' , f1.__defaults__)
print(f1(a = [100 , 200 , 300],   x = 6 )) #error
print('__defaults_  :  ' , f1.__defaults__)
print(f1(6)) #([3,5,6],)
print('__defaults_  :  ' , f1.__defaults__)



# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)#('Hyd',[])
f1() # a :  HydSec
       b :  [1, 2, 3]
print('Default Values  :  ' , f1 . __defaults__) # ('Hyd', [1, 2, 3])
f1() # a :  HydSec
       b :  [1, 2, 3, 1, 2, 3]
print('Default Values  :  ' , f1 . __defaults__) #
f1() # a :  HydSec
b :  [1, 2, 3, 1, 2, 3, 1, 2, 3]




#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18) # (10, 20, 15, 18)
<class 'tuple'>
4
f1() # ()
<class 'tuple'>
0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30)) #   Error



#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 10 	  b  :  (20, 30, 40)
f1(50 , 60) # a : 50 	  b  :  (60,)
f1(70) # a : 70  b  :  ()
f1(a = 80) # a : 80 	  b  :  ()
f1(b = (10 , 20 , 30) , a = 40) # error
f1()
f1(a = 10 , (20 , 30 , 40)) # error
f1(25 , b = (10 , 20 , 30)) # error
f1(25 , a = (10 , 20 , 30))# error
f1((10 , 20 , 30) , 10 , 20 , 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)


#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a  :  10  	  b  :  (20, 30, 40)  	  c  :  50
f1(60 , 70 , c = 80) # a  :  60  	  b  :  (70,)  c  :  80
f1(90 , c = 100) # a  :  90  	  b  :  ()  	  c  :  100
f1(a = 1 , 2 , c = 3) # error
f1(1 , 2 , 3) # error
f1(a = 1 , b = 2 , c = 3) # error
f1(a = 25 , 100 , 200 , 300 , c = 35) # error


# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):
        pass   # vaild
def  f2(*a , b):
        pass # vaild
def  f3(a , *b):
        pass # vaild
def  f4(a , b):
        pass # vaild
def    f5(a , *b , c):
        pass # vaild
def   f6( * , a , *b , c): # invaild
       pass
def   f7(a , *b , c ,  /): # invaild
       pass




#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # Emp  Number  :  25 	  Emp  Name  :  Sita 	  Salary  : 10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # error  
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)




# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print() # 25
f1('Hyd' , 10 , 20 , 30)
print() # Hyd (10, 20, 30)
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
