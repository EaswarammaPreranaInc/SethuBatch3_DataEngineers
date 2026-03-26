from poojaakkapally _2026_03_23.py import prime
from poojaakkapally _2026_03_24.py import prime_num
def prime_divisors(num):
    l=[]
    for i in range(2,num//2+1):
        if prime(i):
                if num%i==0:
                        l.append(i)
        return True
num=int(input("Enter num value n:"))
print(prime_divisors(num))
#----------------------------------------------------------------------
# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # a : 10    b : 20
f1(b = 30 , a = 40) # a : 40    b : 30
f1(50 , 60) # error, bcz default args should be keyword args
f1(70 , b = 80) # Error, bcz default args should be keyword args
#f1(a = 15 , 25) # Error, bcz no PA after KA
#----------------------------------------------------------------------
#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a : 10   b : 20  c: 30
f1(a = 40 , b = 50 , c = 60) # a : 40    b : 50  c: 60
f1(c = 100 , b = 90 , a = 80) # a : 80  b : 90  c : 100
f1(70 , 80 , c = 90) # error, bcz b should be KA
f1(70 , 80 , 90) # error, bcz b and c should be KA
#f1(c = 15 , b = 25 , 35) # Error, bcz PA after KA not valid
#----------------------------------------------------------------------
# Identify error (Home  work)
# def   f1(a  , b , *): # Error, bcz after '*'(keyword only argument) there should be atleast one argument
#         pass
#----------------------------------------------------------------------
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # a : 10    b: 20
f1(a = 30 ,  b = 40) # Error ,bcz a, b should be only PA
f1(50 , b = 60) # Error, bcz b should be only PA
#f1(a = 70 , 80) # Error, bcz PA is not valid after KA
#----------------------------------------------------------------------
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a : 10   b : 20  c : 30
f1(40 , 50 , c = 60) # a : 10   b : 20  c : 60
f1(a = 70 , b = 80 , c = 90) # Error, bcz a and b should be PA only
#f1(a = 100 , b = 110 , 120) # Error, bcz PA is not valid after KA
#f1(a = 130 , 140 , c = 150) # Error, bcz PA is not valid after KA
#f1(160 , b = 170 , 180) # Error, bcz PA is not valid after KA
f1(190 , b = 200 , c = 210) # Error ,bcz b should be PA
#----------------------------------------------------------------------
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a : 10    b : 20  c : 30  d : 40  e : 50  f : 60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error, bcz b should be PA only
f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error, bcz e should be KA only
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error, bcz PA is not valid after KA
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # # a : 10    b : 20  c : 30  d : 40  e : 50  f : 60
#----------------------------------------------------------------------
# Identify error (Home  work)
#def  f1(/ , a , b ,  c): # Atleast one arg should be there before '/'
   #     pass
#def   f2(a , b , c , *): # Atleast one arg should be there after '*'
      #  pass
#----------------------------------------------------------------------
# Identify  error  (Home  work)
#def  f4(* , a , b , c , /): # Atleast one arg should be there before '/'
	       # pass
#----------------------------------------------------------------------               
# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) # 3rd function
f1(y = 20) # Error
f1(x = 30) # Error
#----------------------------------------------------------------------
# Default  arguments  demo  program
def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))   #  150 
print(add(100 , 200))  #  330
print(add(100 , 200 , 300))  #   600
print(add(100 , c = 200)) # 220
print(add(c = 100 , b = 200 , a = 300)) # 600
print(add(c = 100 , a = 200)) # 320
print(add()) # Error
#print(add(a = 100 , 200)) # Error, bcz PA not allowed after KA
#print(add(100 ,  , 300)) # there should be value before ','
#print(add(100 ,  b , 300)) # arg should be value or keyword arg
#----------------------------------------------------------------------
# Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d): # Error, bcz non-default args are not permitted after default arg
	#pass
def   f2(b , d , a = 10 , c = 20): # Passes args
	pass
#----------------------------------------------------------------------
#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20) # 20
f1() # 10
f1(a = 30) # 30
#----------------------------------------------------------------------
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400)) # 1000
print(add(b = 100 , a = 200)) # 330
print(add(100 , 200 , d = 300)) # 610
print(add(d = 100 , a = 200 , b = 300)) #610
#print(add(c = 100 , d = 200 , 300 , 400)) # Error, bcz PA not valid after KA
print(add(100 , 200 , c = 300 , x = 400)) # Error, bcz no x
print(add()) # Error, bcz a and b values are req
#----------------------------------------------------------------------
# find outputs
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) # 10
print(f1()) # 25
print(f2(20)) # 20
print(f2()) # Error, bcz 1 arg is req
#----------------------------------------------------------------------
# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # '----'
disp('$') # $$$$
disp() # ****
disp(n = 5) # *****
disp(5) # *****
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # error, bcz 1st arg is string but not integer
disp(7 , n = 6) # error, bcz 1st arg is string but not integer
#disp(ch = '!' ,  5) # Error ,bcz PA not valid after KA
#----------------------------------------------------------------------
# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5)) # (4.5)^3
print(power(3 + 4j)) # (3+4j)^2
print(power(True)) # 1
#def   power(b = 2 , a): # Error, bcz non def arg is not valid after def arg
 	# pass
 #----------------------------------------------------------------------       
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
print(add(80 , 90)) # 177
print(add(100)) # 109
print(add()) # 10
#----------------------------------------------------------------------
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :  10 20 30
disp(40 , 50 , 60 , 70) # Error, bcz exceeded args, only 3 req, got 4
disp(80 , 90) # 3-argument  function  : 80 90 25
#----------------------------------------------------------------------
# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # 70
print(add()) # 30
print(add(a = 50)) #70
print(add(b = 60 , a = 70)) # 130
print(add(80 , 90)) # error, bcz arg should be KA only
#----------------------------------------------------------------------
# Find  outputs(Home  work)
# def   add(a = 10 , b , c): # Error, bcz no def-arg are not valid after def-args
#         pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) # 120
print(add(b = 60 , c = 70)) # 140
print(add(c = 80 , b = 90 , a = 100)) # 270
print(add(c = 25 , a = 43)) # error, bcz b is expected in KA
print(add(1 , 2 , 3)) # Error, bcz a,b,c should be KA
# def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f): ## Error, bcz no def-arg are not valid after def-args
# 		pass
#----------------------------------------------------------------------
# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . _defaults_) # ([],)
#----------------------------------------------------------------------
# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_) # ([],)
f1(3) # [3]
print('_defaults_  :  ' , f1._defaults_) # ([3],)
f1(4 , [1 , 2 , 3]) # [1,2,3,4]
print('_defaults_  :  ' , f1._defaults_) # ([3,])
f1(9)# [3,9]
print('_defaults_  :  ' , f1._defaults_) # ([3,9],)
f1(40 , [10 , 20 , 30]) # [10,20,30,40]
print('_defaults_  :  ' , f1._defaults_) # ([3,9],)
f1(5) # [3,9,5]
print('_defaults_  :  ' , f1._defaults_) # ([3,9,5])
f1([6 , 7 , 8]) # [3,9,5,[6,7,8]]
print('_defaults_  :  ' , f1._defaults_) # ([3,9,5,[6,7,8]],)
#----------------------------------------------------------------------
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_) # ([],)
print(f1(3)) # [0,1,2]
print('_defaults  :  ' , f1._defaults_) # ([0,1,2],)
print(f1(4 , [10 , 20 , 15 , 18])) # [10,20,15,18,0,1,2,3]
print('_defaults  :  ' , f1._defaults_) # ([0,1,2],)
print(f1(5)) # [0,1,2,0,1,2,3,4]
print('_defaults  :  ' , f1._defaults_) # ([0,1,2,0,1,2,3,4],)
print(f1(a = [100 , 200 , 300],   x = 6 )) # [100,200,300,0,1,2,3,4,5]
print('_defaults  :  ' , f1._defaults_) # ([0,1,2,0,1,2,3,4],)
print(f1(6)) # [0,1,2,0,1,2,3,4,0,1,2,3,4,5]
print('_defaults  :  ' , f1._defaults_) # ([0,1,2,0,1,2,3,4,0,1,2,3,4,5],)
#----------------------------------------------------------------------
# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 .__defaults__) # ('Hyd',[])
f1() # 'HydSec'<nl>[1,2,3]
print('Default Values  :  ' , f1 .__defaults__) # ('Hyd',[1,2,3])
f1() # 'HydSec'<nl>[1,2,3,1,2,3]
print('Default Values  :  ' , f1 .__defaults__) # ('Hyd',[1,2,3,1,2,3])
f1() # 'HydSec'<nl>[1,2,3,1,2,3,1,2,3]
#----------------------------------------------------------------------
#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18) # (10,20,15,18)<nl><class 'tuple'><nl>4
f1() #()<nl><class 'tuple'><nl>0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) # ([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})<nl><class 'tuple'><nl>3
f1('Hyd') # ('Hyd',)<nl><class 'tuple'><nl>1
tpl = (100 , 200 , 150)
f1(tpl) # ((100 , 200 , 150),)<class 'tuple'><nl>1
f1(t = (10 , 20 , 30)) #   Error
#----------------------------------------------------------------------
# #  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)

def avg(*t):
        s=0
        for x in t:
                s+=x
        return s/len(t)
print(avg(10,20,30))
print(avg(10.8,20.6,30.4))
print(avg(3+4j,5+6j,7+8j))
tpl=(10,20,30)
print(avg(tpl))
#----------------------------------------------------------------------
# Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)

def concat(*s):
        ns=''
        for x in s:
                ns+=x+' '
        return ns
print(concat())
print(concat('Sankar','Dayal','Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat('Python'))
#----------------------------------------------------------------------
#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 10  b : (20 , 30 , 40)
f1(50 , 60) # a : 50    b : (60,)
f1(70) # a : 70 b :()
f1(a = 80) # a : 80     b : ()
f1(b = (10 , 20 , 30) , a = 40) # KA cant be send to var-arg 
f1() # a : 25   b: ()
#f1(a = 10 , (20 , 30 , 40)) # PA not valid after KA
f1(25 , b = (10 , 20 , 30)) # KA cant be send to var-arg 
f1(25 , a = (10 , 20 , 30)) # Erroe, bcz a got multiple values
f1((10 , 20 , 30) , 10 , 20 , 30) # a : (10,20,30)       b: (10,20,30)
f1#(a = (10 , 20 , 30) , 10 , 20 , 30) #  # PA not valid after KA
#----------------------------------------------------------------------
# Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a : (10,20,30)      b : 40
f1(50 , b = 60) # a : (50,)     b :60
f1(b = 70) # a : ()      b : 70
f1(b = 10 , a = (20 , 30 , 40)) # Error, bcz KW are invalid for var-arg func
#f1(b = 10 , (20 , 30 , 40)) # Error, bcz PA is not valid after KA
f1() # Error, bcz b value is expected
f1(10 , 20 , 30 , (10 , 20 , 30)) # Error, bcz b is req
f1(10 , 20 , 30 , 40) # Error, bcz b is req
f1(25) # Error, bcz b is req
f1(10 , 20 , 30 , b = (10 , 20 , 30)) # Error
#----------------------------------------------------------------------
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a:10   b:(20,30,40)    c :50
f1(60 , 70 , c = 80) # a:60     b :(70,)        c:80
f1(90 , c = 100) # a : 90       b : ()  c :100
#f1(a = 1 , 2 , c = 3) # Error, bcz PA is not valid after KA
f1(1 , 2 , 3) # Error, bcz c is missing
f1(a = 1 , b = 2 , c = 3) # Error, bcz for var -arg arg, KA is not valid
#f1(a = 25 , 100 , 200 , 300 , c = 35) # Error, bcz PA is not valid after KA
#----------------------------------------------------------------------

# Which  of  the  following  are  valid  ?  (Home  work)
# def   f1(*a , *b): # Error, bcz only one var-arg is valid
#         pass
def  f2(*a , b): # valid
        pass
def  f3(a , *b): # valid
        pass
def  f4(a , b): # valid
        pass
def    f5(a , *b , c): # valid
        pass
# def   f6( * , a , *b , c): # Error, bcz var-arg arg cannot be a KA
#        pass
# def   f7(a , *b , c ,  /): # '/' is not allowed  after '*' bcz, after '*' everything must be KA only, but not PA
#        pass
 #----------------------------------------------------------------------        
# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))# ([10 , 20] , {30 , 40} , (50 , 60))<nl><class 'tuple'<nl>[10,20]<nl><class 'list'><nl>{30,40}<nl><class 'set'><nl>(50,60)<nl><class 'tuple'>
#----------------------------------------------------------------------
# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
# End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')# Results<nl><class 'dict'><nl>{RollNo : 10 , StudName : 'Rama  Rao'}<nl>
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0) # Results<class 'dict'>{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')# Results<class 'dict'>{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
disp()# Results<nl><class 'dict'><nl>{}
#----------------------------------------------------------------------
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')# Results<nl>Empno...25<nl>Empname...Rama Rao<nl>Salary...10000.0<nl>Gender...m
f1() # Results
#----------------------------------------------------------------------
# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True) # <class 'tuple'><nl>(25 , 10.8 , 'Hyd' , True)
print()#<nl>
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)# <class 'dict'><nl>{EmpNum : 25 , EmpName :  'Sita' , Salary :10000.0}
#----------------------------------------------------------------------
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)# Emp  Number  :  25  \t  Emp  Name  :  Sita  \t  Salary  :	10000.0'
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)  # Error
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # {Emp  Number  :  25  \t  Emp  Name  :  Sita  \t  Salary  :	10000.0'}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) #{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
#----------------------------------------------------------------------
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25) # 25<nl>
print()# <nl>
f1('Hyd' , 10 , 20 , 30) # Hyd<nl>(10,20,30)<nl>
print()# <nl>
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0) # 10.8<nl>(25,'Hyd',True)<nl>{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}