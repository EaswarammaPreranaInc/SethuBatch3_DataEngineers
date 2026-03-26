# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # a  :  10  \t  b :  20
f1(b = 30 , a = 40) # a  :  40  \t  b :  30
f1(50 , 60) # Error since there is '*' in the header it will not allow positional args
f1(70 , b = 80) # Error since there is '*' in the header it will not allow positional args
f1(a = 15 , 25) # error positional is not allowed after keyword args


#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a  :  10  \t  b :  20  \t  c  :  30
f1(a = 40 , b = 50 , c = 60) # a  :  40  \t  b :  50  \t  c  :  60
f1(c = 100 , b = 90 , a = 80) # a  :  80  \t  b :  90  \t  c  :  100
f1(70 , 80 , c = 90) # Error f1() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
f1(70 , 80 , 90) # Error f1() takes only 1 positional args but 3 given 
f1(c = 15 , b = 25 , 35) # error positional is not allowed after the keyword args

# Identify error (Home  work)
def   f1(a  , b , *):
        pass
# Error there should atleast one arg after '*' / named arguments must follow bare *



 #  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # a  :  10 \t  b  :  20
f1(a = 30 ,  b = 40) # Error f1() allows only positional args
f1(50 , b = 60) # Error f1() allows only positional args
f1(a = 70 , 80) # error positional is not allowed after the keyword args
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a  :  10  \t  b :  20  \t  c  :  30 
f1(40 , 50 , c = 60) # a  :  40  \t  b :  50  \t  c  :  60 
f1(a = 70 , b = 80 , c = 90) # f1() got some positional-only arguments passed as keyword arguments: 'a, b'
f1(a = 100 , b = 110 , 120) # error positional is not allowed after the keyword args
f1(a = 130 , 140 , c = 150) # error positional is not allowed after the keyword args
f1(160 , b = 170 , 180) # error positional is not allowed after the keyword args
f1(190 , b = 200 , c = 210) # error f1() takes 2 positional but 1 given
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a  :  10  \t  b  :  20  \t  c  :  30  \t  d  :  40  \t  e  :  50  \t  f  :  60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # error f1() takes 2 positional but 1 given
f1(1 , 2 , 3 , 4 , 5 , f = 6) # error f1() takes 2 keyword args but 1 given
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # error positional is not allowed after the keyword args
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # a  :  10  \t  b  :  20  \t  c  :  30  \t  d  :  40  \t  e  :  50  \t  f  :  60
# Identify error (Home  work)
def  f1(/ , a , b ,  c): # preceeding '/' should have atleast one arg
        pass
def   f2(a , b , c , *): # succeeding '*' should have atleast one arg
        pass
#  Identify  error  (Home  work)
def  f4(* , a , b , c , /): # / must be ahead of *
	        pass
 # Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)
# f1(y = 20) # f1() got an unexpected keyword argument 'y'
f1(x = 30) # f1() got an unexpected keyword argument 'x'


# Default  arguments  demo  program
def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))   #  150
print(add(100 , 200))  #  330
print(add(100 , 200 , 300))  #   600
print(add(100 , c = 200)) # 320
print(add(c = 100 , b = 200 , a = 300)) # 600
print(add(c = 100 , a = 200)) # 320
print(add()) # add() missing 1 required positional argument: 'a'
print(add(a = 100 , 200)) # error positional is not allowed after the keyword args
print(add(100 ,  , 300)) # error invalid syntax
print(add(100 ,  b , 300)) # name 'b' is not defined

# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d): #  parameter without a default follows parameter with a default
	pass
def   f2(b , d , a = 10 , c = 20): 
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
print(add(c = 100 , d = 200 , 300 , 400)) # error positional follows keyword
print(add(100 , 200 , c = 300 , x = 400)) # error add() got an unexpected keyword argument 'x' 
print(add()) # error  add() missing 2 required positional arguments: 'a' and 'b'


#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) # 1o
print(f1()) # 25
print(f2(20)) # 20
print(f2()) # error missing one argument

# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # ------
disp('$') # $$$$
disp() # ****
disp(n = 5) # *****
disp(5) # 20
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # @@@@@@@
disp(7 , n = 6) # 42
# disp(ch = '!' ,  5) # positional argument after keyword argument

# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5)) # 91.125
print(power(3 + 4j)) # (-7+24j)
print(power(True)) # 1
# def   power(b = 2 , a): # non-default argument follows default argument
 	#  pass

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
print(add(10 , 20 , 30 , 40)) # 4-argument  function 100
print(add(50 , 60 , 70)) # 4-argument function 184
print(add(80 , 90)) # 4-argument function 177
print(add(100)) # 4-argument function 109
print(add()) # 4-argument function 10

# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :   10 20 30
# disp(40 , 50 , 60 , 70) # disp() takes from 2 to 3 positional arguments but 4 were given
disp(80 , 90) # 3-argument  function  : 80 90 25

# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # 70
print(add()) # 30
print(add(a = 50))# 70
print(add(b = 60 , a = 70)) # 130
print(add(80 , 90)) # add() takes 0 positional arguments but 2 were given

# Find  outputs(Home  work)
# def   add(a = 10 , b , c): # parameter without a default follows parameter with a default
        # pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) # 120
print(add(b = 60 , c = 70)) # 140
print(add(c = 80 , b = 90 , a = 100)) # 270
# print(add(c = 25 , a = 43)) # add() missing 1 required keyword-only argument: 'b'
# print(add(1 , 2 , 3)) # add() takes 0 positional arguments but 3 were given
# def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f): #parameter without a default follows parameter with a default
# 		pass

# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . __defaults__) # ([],)


# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__) # __defaults__  :   ([],)
f1(3) # List :   [3]
print('__defaults__  :  ' , f1.__defaults__) # __defaults__  :   ([3],)
f1(4 , [1 , 2 , 3]) # List :   [1, 2, 3, 4]
print('__defaults__  :  ' , f1.__defaults__) # __defaults__  :   ([3],)
f1(9) # List :   [3, 9]
print('__defaults__  :  ' , f1.__defaults__) # __defaults__  :   ([3, 9],)
f1(40 , [10 , 20 , 30]) # List :   [10, 20, 30, 40]
print('__defaults__  :  ' , f1.__defaults__) # __defaults__  :   ([3, 9],)
f1(5) # List :   [3, 9, 5]
print('__defaults__  :  ' , f1.__defaults__) # __defaults__  :   ([3, 9, 5],)
f1([6 , 7 , 8]) # List :   [3, 9, 5, [6, 7, 8]]
print('__defaults__  :  ' , f1.__defaults__) # __defaults__  :   ([3, 9, 5, [6, 7, 8]],)


# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('__defaults_  :  ' , f1.__defaults__) # __defaults_  :   ([],)
print(f1(3)) # [0, 1, 4]
print('__defaults_  :  ' , f1.__defaults__) # __defaults_  :   ([0, 1, 4],)
print(f1(4 , [10 , 20 , 15 , 18])) # [10, 20, 15, 18, 0, 1, 4, 9]
print('__defaults_  :  ' , f1.__defaults__) # __defaults_  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(5)) # [0, 1, 4, 0, 1, 4, 9, 16]
print('__defaults_  :  ' , f1.__defaults__) # __defaults_  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100 , 200 , 300],   x = 6 )) # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('__defaults_  :  ' , f1.__defaults__)
print(f1(6)) # [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('__defaults_  :  ' , f1.__defaults__) # __defaults_  :   ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)


#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):
    sum=0
    n = len(a)
    if n ==0:
        return 0
    for i in a:
        sum+=i
    avg = sum/n
    return avg
	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
#End  of  the  function
print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18 # 15.75
print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True # 12.6
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.26
print(avg()) # 0
print(avg(25)) # 25.0
print(avg(3 + 4j , 5 + 6j)) # 4+5j
tpl = (10 , 20 , 15 , 18) 
print(avg(tpl)) # 15.75


# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
# End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao') # Results
# <class 'dict'>
# {'RollNo': 10, 'StudName': 'Rama  Rao'}
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0) # Results
# <class 'dict'>
# {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm') # Results
# <class 'dict'>
# {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
disp() # Results
# <class 'dict'>
# {}





# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm') # Results
# Empno ... 25
# Empname ... Rama  Rao
# Salary ... 10000.0
# Gender ... m
f1() # Results



# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True) # <class 'tuple'>
# (25, 10.8, 'Hyd', True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0) # <class 'dict'>
 #{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}



#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
# f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # error f1() got an unexpected keyword argument 'eno' 
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
f1(25) # 25
print()
f1('Hyd' , 10 , 20 , 30) # ('Hyd', 10, 20, 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0) # 10.8 # (25, 'Hyd', True) # {'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}