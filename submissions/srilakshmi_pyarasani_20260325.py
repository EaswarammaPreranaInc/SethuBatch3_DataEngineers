1) Write  a  program  to  generate  all   prime  divisors  of  a  number  also  print  how  many  prime  divisors  are  existing

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
#Program
def prime_divisors(n):
	divisors =[]
	for i in range(2, n+1):
	   if n%i == 0:
		if prime(i):
		   divisors.append(i)
        return divisors

n = int(input("Enter a number:"))
res = prime_divisors(n)
print("Prime divisors :", res)
print("Number of prime divisors :", len(res))



2) Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#a:10	 b:20
f1(b = 30 , a = 40)#a:40	 b:30
f1(50 , 60)#Error because no PA after *
f1(70 , b = 80)#Error because no PA before KA
f1(a = 15 , 25)#Error because no PA after *

3) outputs
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)#a:10  	  b :  20  	  c  :  30 	
f1(a = 40 , b = 50 , c = 60)#a  :  40  	  b :  50  	  c  :  60 
f1(c = 100 , b = 90 , a = 80)#a  :  80  	  b :  90  	  c  :  100 
f1(70 , 80 , c = 90)#Error because no PA after *
f1(70 , 80 , 90)#Error because of *
f1(c = 15 , b = 25 , 35)#Error because of *

4) Identify error 
def   f1(a  , b , *):
        pass#Error because there should be atleast one arg after *

5) Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)#a  :  10  	  b  :  20
f1(a = 30 ,  b = 40)#Error because no KA before /
f1(50 , b = 60)#Error because no KA before /
f1(a = 70 , 80)#Error because no KA before /

6) outputs 
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)#a  :  10  	  b :  20  	  c  :  30 
f1(40 , 50 , c = 60)#a  :  40  	  b :  50  	  c  :  60 
f1(a = 70 , b = 80 , c = 90)#Error because no KA before /
f1(a = 100 , b = 110 , 120)#Error because no KA before /
f1(a = 130 , 140 , c = 150)#Error because no KA before /
f1(160 , b = 170 , 180)#Error because no KA before /
f1(190 , b = 200 , c = 210)#Error because no KA before /

7) outputs
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#a  :  10  	  b  :  20  	  c  :  30  	  d  :  40  	  e  :  50  	  f  :  60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)#Error because of * and /
f1(1 , 2 , 3 , 4 , 5 , f = 6)#Error because of * and /
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#Error because of * and /
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#a  :  10  	  b  :  20  	  c  :  30  	  d  :  40  	  e  :  50  	  f  :  60

8) Identify error 
def  f1(/ , a , b ,  c):
        pass #Error because there should be at least one arg before /
def   f2(a , b , c , *):
        pass #Error because there should be at least one arg after *

9) Identify  error  
def  f4(* , a , b , c , /):
	        pass ##Error because / and *

10)  outputs  
def  f1(x):
	print('1st  function : ' , x)#Error because function is already defined 
def  f1(y):
	print('2nd  function : ' , y)#Error because function is already defined
def  f1(z):
	print('3rd  function : ' , z)#3rd function : 10
f1(z = 10)
f1(y = 20)
f1(x = 30)

11) Default  arguments  demo  program
def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  function
print(add(100))   #  150
print(add(100 , 200))  #  330
print(add(100 , 200 , 300))  #   600
print(add(100 , c = 200))#320
print(add(c = 100 , b = 200 , a = 300))#600
print(add(c = 100 , a = 200))#320
print(add())#Error because no args
print(add(a = 100 , 200))#Error because of only 2 args
print(add(100 ,  , 300))#Error because of only 2 args
print(add(100 ,  b , 300))#Error because of only 2 args

12) Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):
	pass #Error because no non default arg after default arg
def   f2(b , d , a = 10 , c = 20):
	pass #Error because no non default arg after default arg

13) outputs
def   f1(a = 10):
        print(a)#20
                 10
                 30
# End  of  the  function
f1(20)
f1()
f1(a = 30)

14) outputs 
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))#330
print(add(100 , 200 , 300))#620
print(add(100 , 200 , 300 , 400))#1000
print(add(b = 100 , a = 200))#330
print(add(100 , 200 , d = 300))#610
print(add(d = 100 , a = 200 , b = 300))#610
print(add(c = 100 , d = 200 , 300 , 400))#Error because No KA before PA
print(add(100 , 200 , c = 300 , x = 400))#Error because x is not defined
print(add())#Error because no args

15) outputs
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))#10
print(f1())#25
print(f2(20))#20

16) outputs 
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)#------
disp('$')#$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%
disp(7 , '@')#@@@@@@
disp(7 , n = 6)#42
disp(ch = '!' ,  5)#Error because No KA before PA

17) outputs 
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))#91.12
print(power(3 + 4j))#-7+24j
print(power(True))#1
def   power(b = 2 , a):
 	 pass #Error because no non default after default

18) outputs  
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')#4-argument function
	return a + b  + c + d
# End  of  the  function
print(add(10 , 20 , 30 , 40))#100
print(add(50 , 60 , 70))#184
print(add(80 , 90))#177
print(add(100))#109
print(add())#10

19) outputs  
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)#3-argument function
#end
disp(10 , 20 , 30)#3-argument function : 10 20 30
disp(40 , 50 , 60 , 70)#Error because 4 args expected 3
disp(80 , 90)#3-argument function : 80 90 25

20) outputs
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))#70
print(add())#30
print(add(a = 50))#70
print(add(b = 60 , a = 70))#130
print(add(80 , 90))#Error because not permitted

21) outputs
def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#120
print(add(b = 60 , c = 70))#140
print(add(c = 80 , b = 90 , a = 100))#270
print(add(c = 25 , a = 43))#Error because only 2 args
print(add(1 , 2 , 3))##Error because no PA
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass

22) output 
def   f1(a = []):
        pass
print(f1 . __defaults__)#([],)

23) outputs 
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)#__defaults__  :   ([],)
f1(3)#List:[3]
print('__defaults__ :  ' , f1.__defaults__)#__defaults__  :   ([3],)
f1(4 , [1 , 2 , 3])#List :   [1, 2, 3, 4]
print('__defaults__ :  ' , f1.__defaults__)#__defaults__ :   ([3],)
f1(9)#List :   [3, 9]
print('__defaults__ :  ' , f1.__defaults__)#__defaults__ :   ([3, 9],)
f1(40 , [10 , 20 , 30])#List :   [10, 20, 30, 40]
print('__defaults__ :  ' , f1.__defaults__)#__defaults__ :   ([3, 9],)
f1(5)#List :   [3, 9, 5]
print('__defaults__  :  ' , f1.__defaults__)#__defaults__  :   ([3, 9, 5],)
f1([6 , 7 , 8])#List :   [3, 9, 5, [6, 7, 8]]
print('__defaults__ :  ' , f1.__defaults__)#__defaults__ :   ([3, 9, 5, [6, 7, 8]],)

24) outputs
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('__defaults  :  ' , f1.__defaults__)#__defaults  :   ([],)
print(f1(3))#[0, 1, 4]
print('__defaults  :  ' , f1.__defaults__)#__defaults  :   ([0, 1, 4],)
print(f1(4 , [10 , 20 , 15 , 18]))#[10, 20, 15, 18, 0, 1, 4, 9]
print('__defaults  :  ' , f1.__defaults__)#__defaults  :   ([0, 1, 4],)
print(f1(5))#[0, 1, 4, 0, 1, 4, 9, 16]
print('__defaults  :  ' , f1.__defaults__)#__defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100, 200, 300, 0, 1, 4, 9, 16, 25]
print('__defaults  :  ' , f1.__defaults__)#__defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6))#[0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('__defaults  :  ' , f1.__defaults__)#__defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)

25) outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)#Default Values  :   ('Hyd', [])
f1()#a :   HydSec
b :   [1, 2, 3]
print('Default Values  :  ' , f1 . __defaults__)#Default Values  :   ('Hyd', [1, 2, 3])
f1()#a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
print('Default Values  :  ' , f1 . __defaults__)#Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
f1()#a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]

26) Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)#(10, 20, 15, 18)
<class 'tuple'>
4
f1()#()
<class 'tuple'>
0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})#([10, 20], (30, 40, 50), {80, 90, 60, 70})
<class 'tuple'>
3
f1('Hyd')#('Hyd',)
<class 'tuple'>
1
tpl = (100 , 200 , 150)#((100, 200, 150),)
<class 'tuple'>
1
f1(tpl)#Error tpl is not defined
f1(t = (10 , 20 , 30)) #   Error

27) Write  a  function  to  determine  average  of  arguments  passed  to  the  function 
def  avg(*a):
	return sum(a)/len(a) if a else 0 #Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18 #15.75
print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True#12.2666
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))#14.26
print(avg())#0
print(avg(25))#25.0
print(avg(3 + 4j , 5 + 6j))#4 + 5j
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))#Error concatenation is not possible

28) Write  a  function  to  concatenate  strings  passed  to  the  function ? 
def  concat(*a):
	return ' '.join(str(x) for x in a) #(Write  code  to  return  join  of  all  the  strings  passed  to  the  function  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))#Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language'))#Python Is A Great Language
print(concat())#Empty
print(concat('Python'))#Python
print(concat(1, 2, 3))#1 2 3

29) outputs 
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10  	   b  :  (20, 30, 40) 
f1(50 , 60)#a : 50  	   b  :  (60,) 
f1(70)#a : 70  	   b  :  () 
f1(a = 80)#a : 80  	   b  :  () 
f1(b = (10 , 20 , 30) , a = 40))#Error because it is not permitted
f1()#a : 25  	   b  :  () 
f1(a = 10 , (20 , 30 , 40))#error because no ka before pa
f1(25 , b = (10 , 20 , 30))#Error because it is not permitted
f1(25 , a = (10 , 20 , 30))#Error because it is not permitted
f1((10 , 20 , 30) , 10 , 20 , 30)#a : (10, 20, 30)  	   b  :  (10, 20, 30) 
f1(a = (10 , 20 , 30) , 10 , 20 , 30)#Error because it is not permitted

30) outputs 
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#a  :  (10, 20, 30)   	   b  :  40
f1(50 , b = 60)#a  :  (50,)   	   b  :  60
f1(b = 70)#a  :  ()   	   b  :  70
f1(b = 10 , a = (20 , 30 , 40))#Error because it is not permitted
f1(b = 10 , (20 , 30 , 40))#error because no ka before pa
f1()#Error because it is not permitted
f1(10 , 20 , 30 , (10 , 20 , 30))#Error because it is not permitted
f1(10 , 20 , 30 , 40)#Error because it is not permitted
f1(25)#Error because it is not permitted
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a  :  (10, 20, 30)   	   b  :  (10, 20, 30)

31) outputs 
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a  :  10  	  b  :  (20, 30, 40)  	  c  :  50
f1(60 , 70 , c = 80)#a  :  60  	  b  :  (70,)  	  c  :  80
f1(90 , c = 100)#a  :  90  	  b  :  ()  	  c  :  100
f1(a = 1 , 2 , c = 3)#Error because it is not permitted
f1(1 , 2 , 3)#Error because it is not permitted
f1(a = 1 , b = 2 , c = 3)#Error because it is not permitted
f1(a = 25 , 100 , 200 , 300 , c = 35)#Error because it is not permitted

32) Which  of  the  following  are  valid  ?  
def   f1(*a , *b):
        pass #Invalid because of two *
def  f2(*a , b):
        pass #Valid
def  f3(a , *b):
        pass #Valid
def  f4(a , b):
        pass #Valid
def    f5(a , *b , c):
        pass #Valid
def   f6( * , a , *b , c):
       pass #Invalid because of two *
def   f7(a , *b , c ,  /):
       pass #Invalid because of * and /

33) outputs  
def   f1(*a):
	print(a)#([10, 20], {40, 30}, (50, 60))
	print(type(a))#<class 'tuple'>
	for  x  in  a:
		print(x)#[10, 20]
                        {40, 30}
                        (50, 60)
		print(type(x))#<class 'list'>
                               <class 'set'>
                               <class 'tuple'>
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

34) Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
# End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')#Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}
Empty
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)#Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
Empty
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')#Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
Empty
disp()#Results
<class 'dict'>
{}
Empty

35) outputs  
def  f1(**a):
	print('Results')#Results
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')#Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

35) outputs 
def   f1(*a):
	print(type(a))#<class 'tuple'>
	print(a)#(25 , 10.8 , 'Hyd' , True)
def   f2(**a):
	print(type(a))#<class 'dict'>
	print(a)#{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()#Empty
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

37) outputs 
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')#Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  :	10000.0
def   f2(**a):
	print(a)#{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)#Error because of eno  
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)

38) outputs  
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)#25
print()#Empty
f1('Hyd' , 10 , 20 , 30)#Hyd
(10, 20, 30)
print()#Empty
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)#10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}





