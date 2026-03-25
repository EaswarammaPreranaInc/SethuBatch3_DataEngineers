'''
1.Write  a  program  to  generate  all   prime  divisors  of  a  number  also  print  how  many  prime  divisors  are  existing
Hint:  Reuse  the  prime()  function  defined  in   prog3a   but  do  not  rewrite
1) What  are  the  outputs  if  input  is  30 ?  --->  Prime divisors : [2, 3, 5]
                                                                               Number  of  prime  divisors :  3
2) What  are  the  outputs  if  input  is  84 ?  --->  Prime divisors : [2, 3, 7]
                                                                               Number  of  prime  divisors :  3
3) What  are  the  outputs  if  input  is  49 ?  --->  Prime divisors : [7]
                                                                               Number  of  prime  divisors :  1
'''
def prime(n):
	for i in range(2,n//2+1):
		if n%i==0:
			return False
	return True

def  prime_divisors(n):
	list = []
	for i in range(2,n//2+1):
		if prime(i) and n%i==0:
			list.append(i)
	return list

n = int(input('Enter any Number : '))
new = prime_divisors(n)
print(new)

#------------------------------------------------------------------------

#2.Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function

f1(a = 10 , b = 20)  # a : 10      b : 20
f1(b = 30 , a = 40)  # a : 40      b : 30
f1(50 , 60)          # Positional Arg
f1(70 , b = 80)      # becoz of * so have to only KA
f1(a = 15 , 25)      # KA should be after PA

#----------------------------------------------------------------------------

#3.Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)      # a  :  10     b :  20     c  :  30
f1(a = 40 , b = 50 , c = 60)  # a  :  40     b :  50     c  :  60
f1(c = 100 , b = 90 , a = 80) # a  :  80     b :  90     c  :  100
f1(70 , 80 , c = 90)          # Error
f1(70 , 80 , 90)              # Error
f1(c = 15 , b = 25 , 35)      # Error

#-------------------------------------------------------------------------

#4.Identify error (Home  work)
def   f1(a  , b , *):
        pass             # after * one arg must be present it expects something

#---------------------------------------------------------------------------

#5.Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)          # a  : 10      b  :  20
f1(a = 30 ,  b = 40) # Error
f1(50 , b = 60)      # Error
f1(a = 70 , 80)      # Error

#-----------------------------------------------------------------------

#6.Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)               # a  :  10   b :  20     c  :  30
f1(40 , 50 , c = 60)           # a  :  40   b :  50     c  :  60
f1(a = 70 , b = 80 , c = 90)   # Error
f1(a = 100 , b = 110 , 120)    # Error
f1(a = 130 , 140 , c = 150)    # Error
f1(160 , b = 170 , 180)        # Error
f1(190 , b = 200 , c = 210)    # Error

#-------------------------------------------------------------------

#7.Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)   # a : 10    b : 20     c  : 30     d  : 40     e  : 50     f  : 60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error
f1(1 , 2 , 3 , 4 , 5 , f = 6)                 # Error
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)   # a : 10    b : 20     c  : 30     d  : 40     e  : 50     f  : 60
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)       # a : 10    b : 20     c  : 30     d  : 40     e  : 50     f  : 60

#-----------------------------------------------------------------------

#8.Identify error (Home  work)
def  f1(/ , a , b ,  c):
        pass             # posttional arg / should be last
def   f2(a , b , c , *):
        pass             # kA * should be first mean one element should be there

#--------------------------------------------------------------------------

#9.Identify  error  (Home  work)
def  f4(* , a , b , c , /):
	        pass            # it gives error becoz posional should be first then keyword

#-----------------------------------------------------------------------------

#10.Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)  # 3rd  function : 10
f1(y = 20)  # Error
f1(x = 30)  # Error

#----------------------------------------------------

#11.Default  arguments  demo  program
def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))               # 150
print(add(100 , 200))         # 330
print(add(100 , 200 , 300))   # 600
print(add(100 , c = 200))     # 320
print(add(c = 100 , b = 200 , a = 300)) # 600
print(add(c = 100 , a = 200)) # 320
#print(add())                  # Error
#print(add(a = 100 , 200))     # Error
#print(add(100 ,  , 300))      # Error
#print(add(100 ,  b , 300))    # Error

#----------------------------------------------------

#12.Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):
	pass
def   f2(b , d , a = 10 , c = 20):
	pass

#-----------------------------------------------------

#13.Find  outputs (Home  work)
def   f1(a = 10):
        print(a)  # 20 10 30
# End  of  the  function
f1(20)      
f1()
f1(a = 30)

#-----------------------------------------------------

#14.Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))                      # 330
print(add(100 , 200 , 300))                # 620
print(add(100 , 200 , 300 , 400))          # 1000
print(add(b = 100 , a = 200))              # 330
print(add(100 , 200 , d = 300))            # 610
print(add(d = 100 , a = 200 , b = 300))    # 620
print(add(c = 100 , d = 200 , 300 , 400))  # Error
print(add(100 , 200 , c = 300 , x = 400))  # Error x is not defined
print(add())                               # it expects 2 positional argumenets so Error

#------------------------------------------------------------

#15.Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))  # 10
print(f1())    # 25
print(f2(20))  # 20
print(f2())    # Error it expects 1 argument

#------------------------------------------------------

#16.Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)          # ------
disp('$')              # $$$$
disp()                 # ****
disp(n = 5)            # *****
disp(5)                # *****
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@')          # Error
disp(7 , n = 6)        # Error
disp(ch = '!' ,  5)    # bro u can not send ka first 

#----------------------------------------------------------

#17.Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6))            # 64
print(power(5))                # 25
print(power(b = 3 , a = 4.5))  # 4.5**3
print(power(3 + 4j))           # 3+4j**2
print(power(True))             # 1
def   power(b = 2 , a):        # Error
 	 pass

#--------------------------------------------------------

#18.Find outputs  (Home  work)
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
print(add(10 , 20 , 30 , 40)) 
print(add(50 , 60 , 70))
print(add(80 , 90))
print(add(100))
print(add())
'''
4-argument  function
100
4-argument  function
184
4-argument  function
177
4-argument  function
109
4-argument  function
10
'''

#--------------------------------------------------------

#19.Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)       
disp(40 , 50 , 60 , 70)  # Error
disp(80 , 90)
'''
3-argument  function  : 10 20 30
3-argument  function  : 80 90 25
'''

#-----------------------------------------------------------

#20.Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))   # 70
print(add())                  # 30
print(add(a = 50))            # 70
print(add(b = 60 , a = 70))   # 130
print(add(80 , 90))           # Error

#-----------------------------------------------------------

#21.Find  outputs(Home  work)
def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))    # 120
print(add(b = 60 , c = 70))             # 140
print(add(c = 80 , b = 90 , a = 100))   # 270
print(add(c = 25 , a = 43))             # Error
print(add(1 , 2 , 3))                   # 6
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass

#---------------------------------------------------------

#22.Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . _defaults_)   # ([],)

#---------------------------------------------------------

#23.Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_) # ([],)
f1(3)
print('_defaults_  :  ' , f1._defaults_)
f1(4 , [1 , 2 , 3])
print('_defaults_  :  ' , f1._defaults_)
f1(9)
print('_defaults_  :  ' , f1._defaults_)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1._defaults_)
f1(5)
print('_defaults_  :  ' , f1._defaults_)
f1([6 , 7 , 8])
print('_defaults_  :  ' , f1._defaults_)
'''
_defaults_  : ([],)
List : [3]
_defaults_  : ([3],)
List : [1,2,3,4]
_defaults_  : ([3],)
List : [3,9]
_defaults_  : ([3,9],)
List : [10,20,30,40]
_defaults_  : ([3,9],)
List : [3,9,5]
_defaults_  : ([3,9,5],)
List : [3,9,5,[6 , 7 , 8]]
_defaults_  : ([3,9,5,[6 , 7 , 8]],)
'''

#------------------------------------------------------

#24.Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__)
print(f1(3))
print('_defaults  :  ' , f1.__defaults__)
print(f1(4 , [10 , 20 , 15 , 18]))
print('_defaults  :  ' , f1.__defaults__)
print(f1(5))
print('_defaults  :  ' , f1.__defaults__)
print(f1(a = [100 , 200 , 300],   x = 6 ))
print('_defaults  :  ' , f1.__defaults__)
print(f1(6))
print('_defaults  :  ' , f1.__defaults__)
'''
_defaults  :  ([],)
[0,1,4]
_defaults  :  ([0,1,4],)
[10,20,15,18,0,1,4,9]
_defaults  :  ([0,1,4],)
[0,1,4,0,1,4,9,16]
_defaults  :  ([0,1,4,0,1,4,9,16],)
[100,200,300,0,1,4,9,16,25]
_defaults  :  ([0,1,4,0,1,4,9,16],)
[0,1,4,0,1,4,9,16,0,1,4,9,16,25]
_defaults  :  ([0,1,4,0,1,4,9,16,0,1,4,9,16,25],)
'''

#--------------------------------------------------------

#25.Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . _defaults_)  
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()
'''
Default Values  :  ('Hyd',[],)
a : HydSec
b : [1,2,3]
Default Values  :  ('Hyd',[1,2,3],)
a : HydSec
b : [1,2,3,1,2,3]
Default Values  :  ('Hyd',[1,2,3,1,2,3],)
a : HydSec
b : [1,2,3,1,2,3,1,2,3]
'''

#--------------------------------------------------------

# 26.Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30)) #   Error 
'''
(10 , 20 , 15 , 18)
<class 'tuple'>
4

()
<class 'tuple'>
0

([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
<class 'tuple'>
3

(''Hyd')
<class 'tuple'>
1

((100 , 200 , 150))
<class 'tuple'>
1
'''

#-------------------------------------------------------

# 27.Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):
	return sum(a)/len(a) # Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18
print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())    # Error
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))  # Error

#-------------------------------------------------------

#28.Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
def  concat(*a):
	s = ''
	for i in a: # Write  code  to  return  join  of  all  the  strings  passed  to  the  function  (1  line)
		s += i+' '
	return s
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))  # Error

#---------------------------------------------------------

#29.Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)             # a : 10	 b  : (20,30,40)
f1(50 , 60)                       # a : 50	 b  : (60)
f1(70)                            # a : 70	 b  : ()
f1(a = 80)                        # a : 80	 b  : ()
f1(b = (10 , 20 , 30) , a = 40)  # Error
f1()                              # a : 25	 b  : ()
f1(a = 10 , (20 , 30 , 40))      # Error
f1(25 , b = (10 , 20 , 30))      # Error
f1(25 , a = (10 , 20 , 30))      # Error
f1((10 , 20 , 30) , 10 , 20 , 30) # a : (10,20,30)	 b  : (10,20,30) 
f1(a = (10 , 20 , 30) , 10 , 20 , 30) # Error

#--------------------------------------------------------------

#30.Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)              # a : (10,20,30)		b  :  40
f1(50 , b = 60)                        # a : (50)		b  :  60
f1(b = 70)                             # a : ()		b  :  70
f1(b = 10 , a = (20 , 30 , 40))        # Error
f1(b = 10 , (20 , 30 , 40))            # Error
f1()                                   # Error
f1(10 , 20 , 30 , (10 , 20 , 30))      # Error
f1(10 , 20 , 30 , 40)                  # Error
f1(25)                                 # Error
f1(10 , 20 , 30 , b = (10 , 20 , 30))  # a : (10,20,30)		b  :  (10,20,30)

#----------------------------------------------------------------

#31.Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)         # a : 10		b : (20,30,40)		c : 50
f1(60 , 70 , c = 80)                   # a : 60  	b : (70)		    c : 80
f1(90 , c = 100)                       # a : 90		b : ()		        c : 100
f1(a = 1 , 2 , c = 3)                  # Error
f1(1 , 2 , 3)                          # Error
f1(a = 1 , b = 2 , c = 3)              # Error
f1(a = 25 , 100 , 200 , 300 , c = 35)  # Error

#----------------------------------------------------------------

#32.Which  of  the  following  are  valid  ?  (Home  work)
def f1(*a , *b):           # invalid
        pass
def f2(*a , b):            # valid
        pass
def f3(a , *b):            # valid
        pass
def f4(a , b):             # valid
        pass
def f5(a , *b , c):        # valid
        pass
def f6(* , a , *b , c):    # invalid
        pass
def f7(a , *b , c , /):    # invalid
        pass

#---------------------------------------------------------------

#33.Find  outputs  (Home  work)
def   f1(*a):
	print(a)       
	print(type(a)) 
	for  x  in  a:
		print(x)       
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
'''
([10 , 20] , {30 , 40} , (50 , 60))
# <class 'tuple'>
[10 , 20]
<class 'list'>
{30 , 40}
<class 'set'>
(50 , 60)
<class 'tuple'>
'''

#-----------------------------------------------------

#34.Variable  number  of  keyword  arguments  demo  program
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
'''
Results
<class 'dict'>
{RollNo : 10 , StudName : 'Rama  Rao'}

Results
<class 'dict'>
{EmpNo : 25 , EmpName : 'Sita' , Salary : 10000.0}

Results
<class 'dict'>
{AcNo : 30 , CustName : 'Kiran' , Balance : 20000.0 , Gender : 'm'}

Results
<class 'dict'>
{}
'''

#---------------------------------------------------

#35.Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
'''
Results
Empno...25
Empname...'Rama  Rao'
Salary...10000.0
Gender...'m'
Results
'''

#--------------------------------------------------

#36.Find  outputs (Home  work)
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
'''
<class 'tuple'>
(25 , 10.8 , 'Hyd' , True)

<class 'dict'>
{EmpNum : 25 , EmpName : 'Sita' , Salary : 10000.0}
'''

#----------------------------------------------------

#37.Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)    # Error
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
'''
Emp  Number : 25	Emp  Name : Sita	Salary : 10000.0
{'Emp  Number' : 25,'Emp  Name' : 'Sita','Salary' : 10000.0}
{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
'''

#-----------------------------------------------------

#38.Find  outputs   (Home  work)
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
'''
25

'Hyd'
(10,20,30)

10.8
(25,'Hyd',True)
{EmpNo : 12 , EmpName : 'Rama  Rao' , Salary : 10000.0}
'''

#------------------------------------------------------------------