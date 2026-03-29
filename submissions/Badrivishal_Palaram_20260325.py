# Find  outputs(Home  work)
def   add(a = 10 , b , c):
        pass			#error cause there should be no arguments after default arguments. 
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#30+40+50=120
print(add(b = 60 , c = 70))	    #10+60+70=140
print(add(c = 80 , b = 90 , a = 100))#100+90+80=270
print(add(c = 25 , a = 43))#error missing b
print(add(1 , 2 , 3))#error no positional args after *
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass



# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . _defaults_)#([],)



 # Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_)#([],)
f1(3)
print('_defaults_  :  ' , f1._defaults_)#([3],)
f1(4 , [1 , 2 , 3])
print('_defaults_  :  ' , f1._defaults_)#([1,2,3,4],)
f1(9)
print('_defaults_  :  ' , f1._defaults_)#([3,9],)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1._defaults_)#([3,9])
f1(5)
print('_defaults_  :  ' , f1._defaults_)#([3,9,5],)
f1([6 , 7 , 8])
print('_defaults_  :  ' , f1._defaults_)#([3,9,5,[6,7,8]],)





# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__)# ([],)
print(f1(3 # [0, 1, 4]
print('_defaults  :  ' , f1.__defaults__)  # ([0, 1, 4],)
print(f1(4 , [10 , 20 , 15 , 18 # [10, 20, 15, 18, 0, 1, 4, 9]
print('_defaults  :  ' , f1.__defaults__) # ([0, 1, 4],)
print(f1(5)) # [0, 1, 4, 0, 1, 4, 9, 16]
print('_defaults  :  ' , f1.__defaults__)# ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100 , 200 , 300], x = 6))# [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__)# ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6))# [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__)# ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)





# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . _defaults_)#('Hyd',[])
f1()
print('Default Values  :  ' , f1 . _defaults_)#('Hyd',[1,2,3])
f1()
print('Default Values  :  ' , f1 . _defaults_)#('Hyd'[1,2,3,1,2,3])
f1()





#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)
# (10, 20, 15, 18)
# <class 'tuple'>
# 4

f1()
# ()
# <class 'tuple'>
# 0

f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
# ([10, 20], (30, 40, 50), {60, 70, 80, 90})
# <class 'tuple'>
# 3

f1('Hyd')
# ('Hyd',)
# <class 'tuple'>
# 1

tpl = (100 , 200 , 150)
f1(tpl)
# ((100, 200, 150),)
# <class 'tuple'>
# 1

f1(t = (10 , 20 , 30))
# TypeError: f1() got an unexpected keyword argument 't'




#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):
	return sum(a)/len(a) if a else None
# End  of  the  function
print(avg(10 , 20 , 15 , 18))  # 15.75
print(avg(25 , 10.8 , True)) # 12.266666666666667
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))  # 14.26
print(avg())  # None
print(avg(25)) # 25.0
print(avg(3 + 4j , 5 + 6j))# (4+5j)

tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # TypeError




# Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
def  concat(*a):
    if len(a) == 0:
        return ''
    
    for x in a:
        if type(x) != str:
            return Noneresult = ''

    for x in a:
        result += x + ' '
    
    return result.strip()
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))# Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))# Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language'))# Python Is A Great Language
print(concat())# ''
print(concat('Python'))# Python
print(concat(1, 2, 3))
# None




#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 10 	   b  :  (20, 30, 40)
f1(50 , 60)# a : 50 	   b  :  (60,)
f1(70)# a : 70 	   b  :  ()
f1(a = 80)# a : 80 	   b  :  ()
f1(b = (10 , 20 , 30) , a = 40)# TypeError: f1() got an unexpected keyword argument 'b'
f1()# a : 25 	   b  :  ()
f1(a = 10 , (20 , 30 , 40))# SyntaxError
f1(25 , b = (10 , 20 , 30))# TypeError: f1() got an unexpected keyword argument 'b'
f1(25 , a = (10 , 20 , 30))# TypeError: f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30)# a : (10, 20, 30) 	   b  :  (10, 20, 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)# SyntaxError




# Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)# a  :  (10, 20, 30) 	   b  :  40
f1(50 , b = 60)# a  :  (50,) 	   b  :  60
f1(b = 70)# a  :  () 	   b  :  70
f1(b = 10 , a = (20 , 30 , 40))# TypeError: f1() got an unexpected keyword argument 'a'
f1(b = 10 , (20 , 30 , 40))# SyntaxError
f1()# TypeError: f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , (10 , 20 , 30))# TypeError: f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , 40)# TypeError: f1() missing 1 required keyword-only argument: 'b'
f1(25)# TypeError: f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30))# a  :  (10, 20, 30) 	   b  :  (10, 20, 30)





#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)# a  :  10 	  b  :  (20, 30, 40) 	  c  :  50
f1(60 , 70 , c = 80)# a  :  60 	  b  :  (70,) 	  c  :  80
f1(90 , c = 100)# a  :  90 	  b  :  () 	  c  :  100
f1(a = 1 , 2 , c = 3)# SyntaxError
f1(1 , 2 , 3)# TypeError: f1() missing 1 required keyword-only argument: 'c'
f1(a = 1 , b = 2 , c = 3)# TypeError: f1() got an unexpected keyword argument 'b'
f1(a = 25 , 100 , 200 , 300 , c = 35)# SyntaxError




# Which  of  the  following  are  valid  ?  (Home  work)
def f1(*a , *b):# SyntaxError (multiple * not allowed)
def f2(*a , b):# Valid
def f3(a , *b):# Valid
def f4(a , b):# Valid
def f5(a , *b , c):# Valid
def f6(* , a , *b , c):# SyntaxError (only one * allowed)
def f7(a , *b , c , /):# SyntaxError ( / cannot come after * )




# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
# ([10, 20], {30, 40}, (50, 60))
# <class 'tuple'>
# [10, 20]
# <class 'list'>
# {30, 40}
# <class 'set'>
# (50, 60)
# <class 'tuple'>




# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
# End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')
# Results
# <class 'dict'>
# {'RollNo': 10, 'StudName': 'Rama  Rao'}

disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
# Results
# <class 'dict'>
# {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
# Results
# <class 'dict'>
# {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

disp()
# Results
# <class 'dict'>
# {}





# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
# Results
# Empno ... 25
# Empname ... Rama  Rao
# Salary ... 10000.0
# Gender ... m

f1()
# Results





# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
# <class 'tuple'>
# (25, 10.8, 'Hyd', True)


f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
# <class 'dict'>
# {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}




#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)# Emp  Number  :  25 	  Emp  Name  :  Sita 	  Salary  : 10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)# TypeError: f1() got an unexpected keyword argument 'eno'
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)# {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)# {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}





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
print()
# Hyd
# (10, 20, 30)
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
# 10.8
# (25, 'Hyd', True)
# {'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}