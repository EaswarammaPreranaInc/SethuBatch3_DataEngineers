 # Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_)#([],)
f1(3)
print('_defaults_  :  ' , f1._defaults_)#([3],)
f1(4 , [1 , 2 , 3])
print('_defaults_  :  ' , f1._defaults_)#([1,2,3,4])
f1(9)
print('_defaults_  :  ' , f1._defaults_)#[3,9]
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1._defaults_)#[10,20,30,40]
f1(5)
print('_defaults_  :  ' , f1._defaults_)
f1([6 , 7 , 8])
print('_defaults_  :  ' , f1._defaults_)
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_)#([],)
print(f1(3))
print('_defaults  :  ' , f1._defaults_)#([0,1,4],)
print(f1(4 , [10 , 20 , 15 , 18]))
print('_defaults  :  ' , f1._defaults_)#[10,20,15,18,0,1,4,9]
print(f1(5))
print('_defaults  :  ' , f1._defaults_)#[0,1,4,0,1,4,9,16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))
print('_defaults  :  ' , f1._defaults_)
print(f1(6))
print('_defaults  :  ' , f1._defaults_)
 # Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . _defaults_)#('hyd',[])
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()
#  Variable  number  of  arguments  demo  program
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
 #  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):
	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18#15.75
print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True#12.266
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))#14.26
print(avg())#0
print(avg(25))#25.0
print(avg(3 + 4j , 5 + 6j))#4+5j
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))#error
# Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
def  concat(*a):
	Write  code  to  return  join  of  all  the  strings  passed  to  the  function  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))#HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))
 #Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)
f1(50 , 60)
f1(70)
f1(a = 80)
f1(b = (10 , 20 , 30) , a = 40)
f1()
f1(a = 10 , (20 , 30 , 40))
f1(25 , b = (10 , 20 , 30))
f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)
[12:47 pm, 25/03/2026] SRINIVAS Sir Maths: # Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)
f1(b = 70)
f1(b = 10 , a = (20 , 30 , 40))
f1(b = 10 , (20 , 30 , 40))
f1()
f1(10 , 20 , 30 , (10 , 20 , 30))
f1(10 , 20 , 30 , 40)
f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))
[12:47 pm, 25/03/2026] SRINIVAS Sir Maths: #Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)
f1(60 , 70 , c = 80)
f1(90 , c = 100)
f1(a = 1 , 2 , c = 3)
f1(1 , 2 , 3)
f1(a = 1 , b = 2 , c = 3)
f1(a = 25 , 100 , 200 , 300 , c = 35)
[12:47 pm, 25/03/2026] SRINIVAS Sir Maths: # Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):
        pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
def   f6( * , a , *b , c):
       pass
def   f7(a , *b , c ,  /):
       pass
[12:51 pm, 25/03/2026] SRINIVAS Sir Maths: # Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
[12:53 pm, 25/03/2026] SRINIVAS Sir Maths: # Variable  number  of  keyword  arguments  demo  program
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
 #  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')# 25,'sita',10000.0
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)  
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
print()#25
f1('Hyd' , 10 , 20 , 30)
print()#hyd (10,20,30)
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)