'''
Write  a  program  to  generate  all   prime  divisors  of  a  number  also  print  how  many  prime  divisors  are  existing
Hint:  Reuse  the  prime()  function  defined  in   prog3a   but  do  not  rewrite
1) What  are  the  outputs  if  input  is  30 ?  --->  Prime divisors : [2, 3, 5]
       Number  of  prime  divisors :  3
2) What  are  the  outputs  if  input  is  84 ?  --->  Prime divisors : [2, 3, 7]
         Number  of  prime  divisors :  3
3) What  are  the  outputs  if  input  is  49 ?  --->  Prime divisors : [7]                                                                          Number  of  prime  divisors :  1
'''
# Read  input
# call  the  function
# print  results


from prime_number import prime
def  prime_divisors(n):
	c=[]
	for i in range(2,n+1):
	    if  n%i==0 and prime(i):
						c.append(i)
	return c
n=int(input("Enter the n value:"))
prime_divisors(n)
print("Prime divisors :",prime_divisors(n))
print("length of Prime divisors :",len(prime_divisors(n)))

		
		

# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#a  :  10  \t  b :  20
f1(b = 30 , a = 40)#a  :  40  \t  b :  30
f1(50 , 60)#error funtion f1 takes only the keyword arguments only but here  a,b is PA
f1(70 , b = 80)#error funtion f1 takes only the keyword arguments only but here a is PA
f1(a = 15 , 25)#error funtion f1 takes only the keyword arguments only but here b is PA,  
#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)#a  :  10  \t  b :  20  \t  c  :  30
f1(a = 40 , b = 50 , c = 60)#a  :  40  \t  b :  50  \t  c  :  60
f1(c = 100 , b = 90 , a = 80)#a  :  80  \t  b :  90  \t  c  :  100
f1(70 , 80 , c = 90)# error funtion f1 only takes key word arguments  b and c  ,but b is PA here  
f1(70 , 80 , 90)#error  because f1(a , * , b , c) takes b and c as kA arguments but here passing PA
f1(c = 15 , b = 25 , 35)#error PA arfuments are not accepeted after KA
# Identify error (Home  work)
def   f1(a  , b , *):#error after * expected atleast 1 argument
        pass
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)#a  :  10  \t  b  :  20
f1(a = 30 ,  b = 40)#error  a  and b are expected PA but passing KA
f1(50 , b = 60)#error  a  and b are expected PA but passing  b=60 KA
f1(a = 70 , 80)#error  a  and b are expected PA but passing  a=70 KA and no PA accepeted  after KA
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)#a  :  10  \t  b :  20  \t  c  :  30
f1(40 , 50 , c = 60)#a  :  40  \t  b :  50  \t  c  :  60
f1(a = 70 , b = 80 , c = 90)#error ,in function  a and b are PA but here a and b are KA
f1(a = 100 , b = 110 , 120)#error  no PA after the KA 120 is causing error here and a and b are expected as PA
f1(a = 130 , 140 , c = 150)# no positional args after the keyword arguments and a should be PA
f1(160 , b = 170 , 180)#no positional args after the keyword arguments and b should be PA
f1(190 , b = 200 , c = 210)#error f1  function excepts a,b as positional but  b is KA
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#a  :  10  \t  b  :  20  \t  c  :  30  \t  d  :  40  \t  e  :  50  \t  f  :  60'
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)#error funtion expected  b as PA  but passing b = 2 KA
f1(1 , 2 , 3 , 4 , 5 , f = 6)#error funtions f1 expecting e as KA but passing PA
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#after KA  not allow the PA error due to 40
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#a  :  10  \t  b  :  20  \t  c  :  30  \t  d  :  40  \t  e  :  50  \t  f  :  60'
# Identify error (Home  work)
def  f1(/ , a , b ,  c):#error / it should not be before formal arguments
        pass
def   f2(a , b , c , *):#error   becoz after * it  expected at least one argument 
        pass
# Identify  error  (Home  work)
def  f4(* , a , b , c , /):#error becsuse befor / all should be PA ONLY after * all should be KA but  here due to / we getting erreor
	        pass
# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)#f1(x) is discarded
def  f1(y):
	print('2nd  function : ' , y)#f1(x) is discarded
def  f1(z):
	print('3rd  function : ' , z)#3rd  function : 10
f1(z = 10)
f1(y = 20)#error no agrument y in formal parameters
f1(x = 30)#error no agrument x in formal parameters
# Default  arguments  demo  program
def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))   #  150
print(add(100 , 200))  #  330
print(add(100 , 200 , 300))  #   600
print(add(100 , c = 200))#320
print(add(c = 100 , b = 200 , a = 300))#600
print(add(c = 100 , a = 200))#320
print(add())#error becoze no arguments are passing to funtion but funtion add(a , b = 20 , c = 30) expects a value atleast
print(add(a = 100 , 200))#error no potional arguments after the KA
print(add(100 ,  , 300))#error due to syntax  ,  , 
print(add(100 ,  b , 300))#error becoz b not defined value to b
# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):#error  non-default arguments defined   before the default arguments  in the funtion defination due to b and d  so error 
	pass
def   f2(b , d , a = 10 , c = 20):
	pass
 #  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)#20
f1()#10
f1(a = 30)#30
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))#330
print(add(100 , 200 , 300))#620
print(add(100 , 200 , 300 , 400))#1000
print(add(b = 100 , a = 200))#330
print(add(100 , 200 , d = 300))#610
print(add(d = 100 , a = 200 , b = 300))#610
print(add(c = 100 , d = 200 , 300 , 400))#error becoz  no PA should allow  after the kA 
print(add(100 , 200 , c = 300 , x = 400))#620
print(add())# error ,becoz postional aguments  a,b are not passing to formal parameters 
#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))#10
print(f1())#25
print(f2(20))#20
print(f2())#25
# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)#------
disp('$')#$$$$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%
disp(7 , '@')#error n is expected int value but got @ so error  
disp(7 , n = 6)#42
disp(ch = '!' ,  5)#error because of 5, no  PA after the KA
# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5)) #4.5^3=91.125
print(power(3 + 4j))#(-7+24j)
print(power(True))#1
def   power(b = 2 , a):#error Positional Arguments are  should  before the default argument  error becoz a is after defalt arguments 
 	 pass
# Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function')
	return a + b		#this  function  add(a , b) is discarded as new funtion is created with same name add(a , b , c)
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c		#this  function  add(a , b , c) is discarded as new funtion is created with same name add(a  = 1 , b  = 2 , c   = 3 , d = 4)
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
print(add(10 , 20 , 30 , 40))#'4-argument  function'<nextline>100
print(add(50 , 60 , 70))#'4-argument  function'<nextline>204
print(add(80 , 90))#'4-argument  function'<nextline>177
print(add(100))#'4-argument  function'<nextline>109
print(add())#'4-argument  function'<nextline>10
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
								#this funtion disp(a , b) is discarded as new funtion  is created disp(a , b , c , d)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
								#this funtion disp(a , b , c , d) is discarded as new funtion  is created disp(a , b , c = 25)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)#3-argument  function  :   <space> 10 <space> 20 <space> 30
disp(40 , 50 , 60 , 70)#error expected 2 or 3 funtion . args passing 4 so error 
disp(80 , 90)#3-argument  function  :   <space> 80 <space> 90 <space> 25
# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))#70
print(add())#30
print(add(a = 50))#70
print(add(b = 60 , a = 70))#130
print(add(80 , 90))#error as the funtion  contains * it demands KA arguments only after the * but passing PA
# Find  outputs(Home  work)
def   add(a = 10 , b , c):# error in header as  the non default arguments are not defined after the default arguments 
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#120
print(add(b = 60 , c = 70))#140
print(add(c = 80 , b = 90 , a = 100))#270
print(add(c = 25 , a = 43))#error value for b is not passing value for b is missing
print(add(1 , 2 , 3))#6
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):#error non-default parameters/arguments are  defined before default arguments but error due to c here
		pass
# Find  output (Home  work)
def   f1(a = x):# error ,x is not defined 
        pass
print(f1 . _defaults_)#error,becoz the  _defaults_ should be as __defaults__.
# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)#_defaults_ :([],)
f1(3)#List :  [3]
print('_defaults_  :  ' , f1.__defaults__)#_defaults_ :([3],)
f1(4 , [1 , 2 , 3])#[1 , 2 , 3 , 4]
print('_defaults_  :  ' , f1.__defaults__)#_defaults_ :([3],)
f1(9)#List :  [9]
print('_defaults_  :  ' , f1.__defaults__)#_defaults_ :([3,9],)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1.__defaults__)#_defaults_ :([3,9],)
f1(5)#List :  [5]
print('_defaults_  :  ' , f1.__defaults__)#_defaults_ :([3,9,5],)
f1([6 , 7 , 8])#[[6 , 7 , 8]]
print('_defaults_  :  ' , f1.__defaults__)#_defaults_ :([3,9,5,[6 , 7 , 8]],)
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__)#_defaults_ :([],)
print(f1(3))#[0,1,4]
print('_defaults  :  ' , f1.__defaults__)#_defaults_ :([0,1,4],)
print(f1(4 , [10 , 20 , 15 , 18]))#[10 , 20 , 15 , 18 , 0 , 1 , 4 , 9 ]
print('_defaults  :  ' , f1.__defaults__)#_defaults_ :([0,1,4],)
print(f1(5))#[0,1,4,9,16]
print('_defaults  :  ' , f1.__defaults__)#_defaults_ :([0,1,4,0,1,4,9,16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100 , 200 , 300 , 0 , 1 , 4 , 9 , 16 , 25]
print('_defaults  :  ' , f1.__defaults__)#_defaults_ :([0,1,4,0,1,4,9,16],)
print(f1(6))#[0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)#_defaults_ :([0,1,4,0,1,4,9,16,0,1,4,9,16,25],)
# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)#Default Values  :('Hyd',[])
f1()# a : HydSec <nextline> b : [1 , 2 , 3 ]
print('Default Values  :  ' , f1 . __defaults__)#Default Values  :(HydSec, [1 , 2 , 3 , 1,2,3])
f1()# a : HydSec <nextline> b : [1 , 2 , 3 ,1 ,2 ,3 ]
print('Default Values  :  ' , f1 . __defaults__)#Default Values  :(HydSec, [1 , 2 , 3 ,1,2,3,1,2,3,])
f1()#a :HydSec <nextline> b : [1 , 2 , 3 1 ,2 ,3 ,1,2,3] 

#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)#(10 , 20 , 15 , 18) <nextline> <class 'Tuple'> <nextline> 4 <nextline> nothing is printed
f1()#None
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})#([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) <class 'Tuple'> <nextline> 3 <nextline> nothing is printed
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)#((100 , 200 , 150))  <nextline> <class 'Tuple'> <nextline> 1 <nextline> nothing is printed
f1(t = (10 , 20 , 30)) #   Error
#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):
         return sum(a)/len(a)
	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) # 15.75
print(avg(25 , 10.8 , True))  #   12.266
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))#14.26
print(avg())#error, zero division error 
print(avg(25))#25.0
print(avg(3 + 4j , 5 + 6j))#4+5j
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))#15.75
# Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
def  concat(*a):
        return ' '.join(a)
	#Write  code  to  return  join  of  all  the  strings  passed  to  the  function  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))#Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language'))#Python Is A Great Language
print(concat())# noting is printed 
print(concat('Python'))#Python
print(concat(1, 2, 3))# error ,cannot cancat the numbers  int only strings are supported
#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10  	\t   b  :  (20, 30, 40)
f1(50 , 60)#a : 50  \t   b  :  (60,) 
f1(70)# a : 70   \t   b  :  ()
f1(a = 80)#a : 80   \t   b  :  ()
f1(b = (10 , 20 , 30) , a = 40)#a : 40  \t   b  :  (10 , 20 , 30)
f1()#a : 25  \t   b  :  ()
f1(a = 10 , (20 , 30 , 40))## error ,no PA after the keyword arguments 
f1(25 , b = (10 , 20 , 30))#a : 25  \t   b  :  (10 , 20 , 30)
f1(25 , a = (10 , 20 , 30))#error no arg for b PA pass in order how they   written  the function call in the function
f1((10 , 20 , 30) ,(10 , 20 , 30))#a : (10 , 20 , 30)  \t   b  :  (10 , 20 , 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)#error becoz not accepet PA after the KA
# Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#a  :(10 , 20 , 30)   \t   b  :  40
f1(50 , b = 60)#a  :(50,)   \t   b  : 60 
f1(b = 70)#a  :()   \t   b  :  70
f1(b = 10 , a = (20 , 30 , 40))#a  :((20 , 30 , 40))   \t   b  :  10
f1(b = 10 , (20 , 30 , 40))#error the #error becoz not accepet PA after the KA
f1()#no  argumants for function 
f1(10 , 20 , 30 , (10 , 20 , 30))#error b  mandatory  keyword-only argument
f1(10 , 20 , 30 , 40) #error 
f1(25)#error  b argument value is missing 
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a  :  (10,20,30)   \t   b  :  (10 , 20 , 30)
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a  :  10  \t  b  :  (20 , 30 , 40)  \t  c  :  50
f1(60 , 70 , c = 80)#a  :  60  \t  b  :  (70,)  \t  c  :  80
f1(90 , c = 100)#a  :  90  \t  b  :  ()  \t  c  :  100
f1(a = 1 , 2 , c = 3)#error no PA after KA arguments  error due to 2
f1(1 , 2 , 3)# error c should be KA ONLY BUT GIVING PA
f1(a = 1 , b = 2 , c = 3)#error b should be only PA arguments but passing KA
f1(a = 25 , 100 , 200 , 300 , c = 35)##error no PA after KA arguments  error due to 100 and 200,300
# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):#invalid
        pass
def  f2(*a , b):#valid
        pass
def  f3(a , *b):#valid
        pass
def  f4(a , b):#valid
        pass
def    f5(a , *b , c):#valid
        pass
def   f6( * , a , *b , c):#invalid
       pass
def   f7(a , *b , c ,  /):#invalid
       pass
 # Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))#([10 , 20] , {30 , 40} , (50 , 60)) <nextline>  <class 'tuple> <nextline> [10 , 20] <nextline> <class 'list> <nextline>{30 , 40}  <nextline> <class 'set'> <nextline> (50 , 60)  <nextline> <class 'tuple'>
 # Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
# End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')# Results <nextline> <class 'dict'> <nextline> {RollNo :10 , StudName :'Rama  Rao'}<nextline> 
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)#Results <nextline> <class 'dict'> <nextline> {EmpNo : 25 , EmpName : 'Sita' , Salary : 10000.0}<nextline> 
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')#Results <nextline> <class 'dict'> <nextline> {AcNo : 30 , CustName : 'Kiran' , Balance : 20000.0 , Gender : 'm'}<nextline>
disp()#Results <nextline> <class 'dict'> <nextline> {}<nextline> 
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')#Results <nextline> (Empno... 25)  <nextline> (Empname...'Rama  Rao')  <nextline> (Salary...10000.0) <nextline>(Gender...'m')
f1()#error no because no argurs passed for function
# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)#<class 'tuple'> <nextline> (25 , 10.8 , 'Hyd' , True)
print()#<nextline>
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)#<class 'dict'> <nextline> {EmpNum : 25 , EmpName : 'Sita' , Salary : 10000.0}
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)#Emp  Number  :  25  \t  Emp  Name  :  'Sita'  \t  Salary  :	10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0) #error because  actual keyword  arguments  names are not correct as defined in function f1
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)#Emp  Number  :  25  \t  Emp  Name  :  'Sita'  \t  Salary  :	10000.0
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)#error because  actual keyword  arguments  names are not correct as defined in function f1
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)#25<nextline>
print()#<nextline>
f1('Hyd' , 10 , 20 , 30)#'Hyd' <nextline>  (10 , 20 , 30) 
print()#<nextline>
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)#10.8<nextline>(25 , 'Hyd' , True)<nextline>{ EmpNo : 12 , EmpName : 'Rama  Rao' , Salary : 10000.0}