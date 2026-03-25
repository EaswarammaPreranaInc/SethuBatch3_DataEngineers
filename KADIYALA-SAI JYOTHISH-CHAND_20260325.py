# Keyword  only   arguments  demo  program
# def   f1(* , a , b):
#         print(F'a  :  {a}  \t  b :  {b}')
# # End  of  the  function
# f1(a = 10 , b = 20) # a : 10    b : 20
# f1(b = 30 , a = 40) # a : 30    b : 40
# #f1(50 , 60) # type Error: f1() takes 0 positional arguments but 2 were give 
# #f1(70 , b = 80) # TypeError
# f1(a = 15 , 25) # SyntaxError:positional arguments follows keyword arguments



2.
#Find  outputs (Home  work)
# def  f1(a , * , b , c):
#         print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# # End  of  function
# f1(10 , b = 20 , c = 30) # a : 10   b : 20  c : 30
# f1(a = 40 , b = 50 , c = 60)# a : 40    b : 50  c : 60
# f1(c = 100 , b = 90 , a = 80)#a : 80    b : 90  c : 100
# #f1(70 , 80 , c = 90)# TypeError: f1() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
# #f1(70 , 80 , 90) # TypeError: f1() takes 1 positional argument but 3 were given
# f1(c = 15 , b = 25 , 35) #SyntaxError : PA follows KA



3.
# Identify error (Home  work)
'''
#def   f1(a  , b , *): # kSyntaxError: becoz after * you must define at least one parameter
        pass
'''
# def f1(a, b , * , c):
#         pass



4.
#  Positional  only  arguments  demo  program
'''
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # a : 10    b : 20
#f1(a = 30 ,  b = 40) # TypeError : f1() Positional  only  arguments takes only positional arguments
#f1(50 , b = 60) # TypeError
f1(a = 70 , 80) # SyntaxError: PA follows KA
'''



5.
# Find  outputs (Home  work)
'''
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a : 10   b : 20  c : 30
f1(40 , 50 , c = 60) # a : 40   b : 50  c : 60
f1(a = 70 , b = 80 , c = 90) # TypeError
f1(a = 100 , b = 110 , 120) # SyntaxError
f1(a = 130 , 140 , c = 150) # SyntaxError
f1(160 , b = 170 , 180) # SyntaxError
f1(190 , b = 200 , c = 210)#TypeError
'''


6.
# Find outputs(Home  work)
'''
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#a  :  10    b  :  20    c  :  30    d  :  40    e  :  50    f  :  60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) #TypeError
#f1(1 , 2 , 3 , 4 , 5 , f = 6) #TypeError:f1() tkes 4 PA but 5 PA are were give
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#SyntaxError:PA follows KA
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#a  :  10    b  :  20    c  :  30    d  :  40    e  :  50    f  :  60
'''


7.
# Identify error (Home  work)
'''
def  f1(/ , a , b ,  c): # SyntaxError
        pass
def   f2(a , b , c , *): # SyntaxError
        pass
'''
# def f1(a,b,c,/):
#         pass
# def f2(*,a,b,c):
#         pass



8.
# Identify  error  (Home  work)
'''
def  f4(* , a , b , c , /): # SyntaxError: / must be before *
	        pass
'''
# def f4 (a , b , / , * , c):
#         pass




9.
# Find  outputs  (Home  work)
'''
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) # 3rd function: 10
f1(y = 20) #TypeError
f1(x = 30) #TypeError
'''



10.
# Default  arguments  demo  program
'''
def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))# 150
print(add(100 , 200)) # 330 
print(add(100 , 200 , 300))  # 600
print(add(100 , c = 200)) # 320
print(add(c = 100 , b = 200 , a = 300)) # 600
print(add(c = 100 , a = 200)) # 320
#print(add()) # TypeError: add() missing 1 required positional argument: 'a'
#print(add(a = 100 , 200)) # SysntaxError
#print(add(100 ,  , 300)) # SyntaxError:invalid syntax
print(add(100 ,  b , 300)) #NameError: name 'b' is not defined
'''




11.
# Identify  Error
'''
def   f1(a = 10 ,  b ,  c = 20 ,  d): # non-default argument follows default argument
	pass
'''
# def   f2(b , d , a = 10 , c = 20):
# 	pass




12.
#  Find  outputs (Home  work)
'''
def   f1(a = 10):
        print(a) 
# End  of  the  function
f1(20) # 20
f1() # 10
f1(a = 30) # 30
'''



13.
# Find  outputs (Home  work)
'''
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400)) # 1000
print(add(b = 100 , a = 200)) #330
print(add(100 , 200 , d = 300))# 610
print(add(d = 100 , a = 200 , b = 300))#610
#print(add(c = 100 , d = 200 , 300 , 400))#SyntaxError:PA follows KA
#print(add(100 , 200 , c = 300 , x = 400))# TypeError:add() got an unexpeted keyword argument 'x'
print(add())#TypeError: add() missing 2 required positional arguments: 'a' and 'b'
'''



14.
#  Find  outputs (Home  work)
'''
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))#10
print(f1())#25
print(f2(20))#20
print(f2())#TypeError: f2() missing 1 required positional argument: 'x'
'''


15.
# Find  outputs (Home  work)
'''
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)#----
disp('$')#$$$$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%
disp(7 , '@')#@@@@@@@
disp(7 , n = 6)#42
disp(ch = '!' ,  5)#SyntaxError
'''



16.
# Find  outputs (Home  work)
'''
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5))# 91.125
print(power(3 + 4j))#(-7+24j)
print(power(True))#1
def   power(b = 2 , a): # non-default  arguments follows default arguments
 	pass
'''



17.
'''
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
print(add(10 , 20 , 30 , 40))# 4-argument  function <next-line> 100                          
print(add(50 , 60 , 70))#4-argument  function <next-line> 184
print(add(80 , 90))#4-argument  function <next-line> 177
print(add(100))#4-argument  function <next-line> 109
print(add())#4-argument  function <next-line> 10
'''



18.
# Find outputs  (Home  work)
'''
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)# 3-argument function : 10 20 30
disp(40 , 50 , 60 , 70) # TypeError: disp() takes from 2 to 3 positional arguments but 4 were given 
disp(80 , 90) # 3-argument function : 80 90 25
'''


19.
# Find outputs(Home  work)
'''
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # 70
print(add()) # 30
print(add(a = 50)) # 70
print(add(b = 60 , a = 70)) # 130
print(add(80 , 90)) # TypeError:add() takes 0 positional arguments but 2 were given
'''



20.
# Find  outputs(Home  work)
'''
# def   add(a = 10 , b , c): # non-default arguments follows default arguments
#         pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))# 120
print(add(b = 60 , c = 70)) # 140
print(add(c = 80 , b = 90 , a = 100)) # 270
#print(add(c = 25 , a = 43)) # TypeError: add() missing 1 required keyword_only arguments: 'b'
#print(add(1 , 2 , 3)) # TypeError: add() takes 0 positional arguments but 3 were given
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):# SyntaxError: non-default srguments follows default arguments
		pass
'''



21.
# Find  output (Home  work)
'''
def   f1(a = []): 
        pass
print(f1 . _defaults_) # AttributeError: 'function' object has no attribute '_defaults_'
'''
# corrected code
# def f1(a = []):
#     pass
# print(f1.__defaults__)#([],)



22.
# Find  outputs (Home  work)
'''
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
#print('_defaults_  :  ' , f1._defaults_)
f1(3) # [3]
#print('_defaults_  :  ' , f1._defaults_)
f1(4 , [1 , 2 , 3]) # [1,2,3,4]
#print('_defaults_  :  ' , f1._defaults_)
f1(9) # [3,9]
#print('_defaults_  :  ' , f1._defaults_)
f1(40 , [10 , 20 , 30]) # [10, 20 , 30 , 40]
#print('_defaults_  :  ' , f1._defaults_)
f1(5) # [3,9,5]
#print('_defaults_  :  ' , f1._defaults_)
f1([6 , 7 , 8]) # [3,9,5.[6,7,8]]
#print('_defaults_  :  ' , f1._defaults_)
'''
# correct code
# def f1(x, a=[]):
#     a.append(x)
#     print('List : ', a)

# print('__defaults__ : ', f1.__defaults__) # ([],)
# f1(3) # [3]
# print('__defaults__ : ', f1.__defaults__) # ([3],)
# f1(4, [1, 2, 3]) # [1,2,3,4]
# print('__defaults__ : ', f1.__defaults__) # ([3],)
# f1(9) # [3,9]
# print('__defaults__ : ', f1.__defaults__) # ([3,9],)
# f1(40, [10, 20, 30]) # [10,20,30,40]
# print('__defaults__ : ', f1.__defaults__)# ([3,9],)
# f1(5)  # [3,9,5]
# print('__defaults__ : ', f1.__defaults__) # ([3,9,5],)
# f1([6, 7, 8]) # [3, 9, 5, [6, 7, 8]]
# print('__defaults__ : ', f1.__defaults__) # ([3, 9, 5, [6, 7, 8]],)



23.
# Find  outputs(Home  work)
'''
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_) # AttributeError: 'function' object has no attribute '_defaults_'. Did you mean: '__defaults__'?
print(f1(3)) # [0,1,4]
print('_defaults  :  ' , f1._defaults_) # AttributeError: 'function' object has no attribute '_defaults_'. Did you mean: '__defaults__'?
print(f1(4 , [10 , 20 , 15 , 18])) # [10, 20, 15, 18, 0, 1, 4, 9]
print('_defaults  :  ' , f1._defaults_) # AttributeError: 'function' object has no attribute '_defaults_'. Did you mean: '__defaults__'?
print(f1(5)) # [0, 1, 4, 0, 1, 4, 9, 16]
print('_defaults  :  ' , f1._defaults_) # AttributeError: 'function' object has no attribute '_defaults_'. Did you mean: '__defaults__'?
print(f1(a = [100 , 200 , 300],   x = 6 )) # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1._defaults_) # AttributeError: 'function' object has no attribute '_defaults_'. Did you mean: '__defaults__'?
print(f1(6)) # [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1._defaults_) # AttributeError: 'function' object has no attribute '_defaults_'. Did you mean: '__defaults__'?
'''
# correct code
# def f1(x, a=[]):
#     for i in range(x):
#         a.append(i * i)
#     return a

# print('__defaults__ : ', f1.__defaults__)
# print(f1(3))
# print('__defaults__ : ', f1.__defaults__)
# print(f1(4, [10, 20, 15, 18]))
# print('__defaults__ : ', f1.__defaults__)
# print(f1(5))
# print('__defaults__ : ', f1.__defaults__)
# print(f1(a=[100, 200, 300], x=6))
# print('__defaults__ : ', f1.__defaults__)
# print(f1(6))
# print('__defaults__ : ', f1.__defaults__)




24.
# Find  outputs
'''
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a) # HydSec
	print('b :  ' , b) # [1,2,3,1,2,3,1,2,3]
# End of the function
#print('Default Values  :  ' , f1 . _defaults_) # AttributeError: 'function' object has no attribute '_defaults_'. Did you mean: '__defaults__'?
f1() 
#print('Default Values  :  ' , f1 . _defaults_)# AttributeError: 'function' object has no attribute '_defaults_'. Did you mean: '__defaults__'?
f1()
#print('Default Values  :  ' , f1 . _defaults_) # AttributeError: 'function' object has no attribute '_defaults_'. Did you mean: '__defaults__'?
f1()
'''
# correct code
# def f1(a='Hyd', b=[]):
#     a += "Sec"
#     b += [1, 2, 3]
#     print('a : ', a)
#     print('b : ', b)

# print('Default Values : ', f1.__defaults__)
# f1()
# print('Default Values : ', f1.__defaults__)
# f1()
# print('Default Values : ', f1.__defaults__)
# f1()



25.
#  Variable  number  of  arguments  demo  program
'''
def   f1(*t):
	print(t) # ((100 , 200 , 150))
	print(type(t))# <class 'tuple'>
	print(len(t)) # 1
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18) # (10, 20 , 30 , 40)
f1() # Empty tuple
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) # ([10, 20], (30, 40, 50), {60, 70, 80, 90})
f1('Hyd') # ('Hyd',)
tpl = (100 , 200 , 150)
f1(tpl) ((100 , 200 , 150),)
#f1(t = (10 , 20 , 30)) #   Error
'''



26.
'''
#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):
	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18
print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))
# '''
# def avg(*a):
#     return sum(a) / len(a) if a else 0
# print(avg(10 , 20 , 15 , 18)) # 15.75
# print(avg(25 , 10.8 , True)) # 12.2666
# print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.26
# print(avg()) # 0
# print(avg(25)) # 25.0
# print(avg(3 + 4j , 5 + 6j))#(4 + 5j)
# tpl = (10 , 20 , 15 , 18)
# print(avg(tpl)) # TypeError:unsupported operand type for +: 'int' and 'tuple'

 



27.
# Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
'''
def  concat(*a):
	Write  code  to  return  join  of  all  the  strings  passed  to  the  function  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))
'''
# def concat(*a):
#     return ' '.join(a)
# print(concat('Sankar', 'Dayal', 'Sarma')) # Sankar Dayal Sarma
# print(concat('Hyd', 'Is', 'Green', 'City'))# Hyd Is Green City
# print(concat('Python', 'Is', 'A', 'Great', 'Language'))# Python Is A Greate language
# print(concat())# Empty space
# print(concat('Python'))#Python
# print(concat(1, 2, 3)) # TypeError:squence item 0: expected str instance, int found




28.
#Find  outputs (Home  work)
# def   f1(a = 25  , *b):
#         print(F'a : {a}  \t   b  :  {b} ')
# # End  of  the  function
# f1(10 , 20 , 30 , 40) # a : 10  b : (20, 30, 40)
# f1(50 , 60) # a : 50  b : (60,)
# f1(70) # a : 70  b : ()
# f1(a = 80) # a : 80  b : ()
# #f1(b = (10 , 20 , 30) , a = 40) # TypeError: f1() got an unexpeted KA 'b'
# f1() # a : 25   b : ()
# #f1(a = 10 , (20 , 30 , 40)) # SyntaxError: positional argument follows keyword argument
# #f1(25 , b = (10 , 20 , 30)) # TypeError: f1() got an unexpected keyword argument 'b'
# #f1(25 , a = (10 , 20 , 30)) # TypeError: f1() got multiple values for argument 'a'
# f1((10 , 20 , 30) , 10 , 20 , 30) # a : (10, 20, 30)           b  :  (10, 20, 30)
# #f1(a = (10 , 20 , 30) , 10 , 20 , 30) # SyntaxError: PA follows KA



29.
# Find  outputs (Home  work)
# def    f1(*a , b):
# 	print(F'a  :  {a}   \t   b  :  {b}')
# # End  of  the  function
# f1(10 , 20 , 30 , b = 40) # a  :  (10, 20, 30)         b  :  40
# f1(50 , b = 60) # a  :  (50,)        b  :  60
# f1(b = 70) # a  :  ()           b  :  70
# #f1(b = 10 , a = (20 , 30 , 40)) # TypeError: f1() got an unexpected keyword argument 'a'
# #f1(b = 10 , (20 , 30 , 40)) # SyntaxError
# #f1() # TypeError: f1() missing 1 required keyword-only argument: 'b'
# #f1(10 , 20 , 30 , (10 , 20 , 30)) # TypeError: f1() missing 1 required keyword-only argument: 'b'
# #f1(10 , 20 , 30 , 40)# TypeError: f1() missing 1 required keyword-only argument: 'b'
# #f1(25) # TypeError: f1() missing 1 required keyword-only argument: 'b'
# f1(10 , 20 , 30 , b = (10 , 20 , 30)) # a  :  (10, 20, 30)         b  :  (10, 20, 30)




30.
#Find  outputs (Home  work)
# def   f1(a , *b , c):
#         print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# # End  of  the  function
# f1(10 , 20 , 30 , 40 , c = 50) # a  :  10          b  :  (20, 30, 40)      c  :  50
# f1(60 , 70 , c = 80) # a  :  60          b  :  (70,)     c  :  80
# f1(90 , c = 100) # a  :  90          b  :  ()        c  :  100
#f1(a = 1 , 2 , c = 3) # SyntaxError
#f1(1 , 2 , 3) # TypeError: f1() missing 1 required keyword-only argument: 'c'
# f1(a = 1 , b = 2 , c = 3) # TypeError: f1() got an unexpected keyword argument 'b'
#f1(a = 25 , 100 , 200 , 300 , c = 35)# SyntaxError




31.
# Which  of  the  following  are  valid  ?  (Home  work)
'''
def   f1(*a , *b): # Invalid becoz two *args
        pass
def  f2(*a , b): # valid  b keyword-only
        pass
def  f3(a , *b): # valid 
        pass
def  f4(a , b): # valid
        pass
def    f5(a , *b , c): # valid
        pass
def   f6( * , a , *b , c): # invalid
       pass
def   f7(a , *b , c ,  /): # invalid
       pass
'''



32.
# Find  outputs  (Home  work)
# def   f1(*a):
# 	print(a)
# 	print(type(a))
# 	for  x  in  a:
# 		print(x)
# 		print(type(x))
# # End  of  the  function
# f1([10 , 20] , {30 , 40} , (50 , 60))
'''
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>
'''



33.
# Variable  number  of  keyword  arguments  demo  program
# def   disp(**a):
# 	print('Results')
# 	print(type(a))
# 	print(a)
# 	print()
# #End  of  the  function
# disp(RollNo = 10 , StudName = 'Rama  Rao')
# disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
# disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
# disp()
'''
Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}
'''



34.
# Find  outputs  (Home  work)
# def  f1(**a):
# 	print('Results')
# 	for  k , v   in   a . items():
# 		print(k , v , sep = ' ... ')
# # End  of  the  function
# f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
# f1()
'''
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results
'''


35.
# Find  outputs (Home  work)
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
'''
<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''



36.
#  Find  outputs (Home work)
# def   f1(empno , ename , sal):
# 	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
# def   f2(**a):
# 	print(a)
# # End  of  the  function
# f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # Emp  Number  :  25    Emp  Name  :  Sita  Salary  :   10000.0
# #f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # TypeError: f1() got an unexpected keyword argument 'eno'
# f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
# f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
