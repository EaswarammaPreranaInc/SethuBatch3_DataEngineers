#1
'''
Write a program to generate all prime divisors of a number also print how many prime divisors are existing

1) What are the outputs if input is 30? ---> Prime divisors : [2, 3, 5]
                                             Number of prime divisors : 3

2) What are the outputs if input is 84? ---> Prime divisors : [2, 3, 7]
                                             Number of prime divisors : 3

3) What are the outputs if input is 49? ---> Prime divisors : [7]
                                             Number of prime divisors : 1
'''
def prime_divisors(n):
    divs = [i for i in range(2, n + 1) if n % i == 0 and prime(i)]
    return divs

n = int(input())
res = prime_divisors(n)
print(f"Prime divisors : {res}") 
print(f"Number of prime divisors : {len(res)}")



#2
# Keyword only arguments demo program
def f1(*, a, b):
    print(f'a : {a} \t b : {b}')
#End of the function
f1(a=10, b=20)   # a : 10   b : 20
f1(b=30, a=40)   # a : 40   b : 30
# f1(50, 60)     # ERROR as f1() takes 0 positional arguments but 2 were given (* forces keyword-only)
# f1(70, b=80)   # ERROR as f1() takes 0 positional arguments but 1 was given
# f1(a=15, 25)   # ERROR as positional argument follows keyword argument



#3
# Find Outputs (Home work)
def f1(a, *, b, c):
    print(f'a : {a} \t b : {b} \t c : {c}')
#End of the function
f1(10, b=20, c=30)            # a : 10   b : 20   c : 30
f1(a=40, b=50, c=60)          # a : 40   b : 50   c : 60
f1(c=100, b=90, a=80)         # a : 80   b : 90   c : 100
# f1(70, 80, c=90)            # ERROR as b must be a keyword argument
# f1(70, 80, 90)              # ERROR as b and c must be keyword arguments
# f1(c=15, b=25, 35)          # ERROR as positional argument follows keyword argument



#4
# Identify Error (Home work)
# def f1(a, b, *): # ERROR as Named arguments must follow bare *
      pass



#5
# Positional Arguments only demo program
def f1(a, b, /):
    print(f'a : {a} \t b : {b}')
#End of the function
f1(10, 20)          # a : 10   b : 20
# f1(a=30, b=40)    # ERROR as f1() got some positional-only arguments passed as keyword arguments
# f1(50, b=60)      # ERROR as b is positional-only
# f1(a=70, 80)      # ERROR as a is positional-only and positional must come before keyword



#6
# Find outputs (Home work)
def f1(a, b, /, c):
    print(f'a : {a} \t b : {b} \t c : {c}')
#End of the function
f1(10, 20, 30)                # a : 10   b : 20   c : 30
f1(40, 50, c=60)              # a : 40   b : 50   c : 60
# f1(a=70, b=80, c=90)        # ERROR as a and b are positional-only
# f1(a=100, b=110, 120)       # ERROR as a and b are positional-only
# f1(a=130, 140, c=150)       # ERROR as a is positional-only
# f1(160, b=170, 180)         # ERROR as b is positional-only
f1(190, 200, c=210)           # a : 190  b : 200  c : 210



#7
# Find outputs (Home work)
def f1(a, b, /, c, d, *, e, f):
    print(f'a : {a} \t b : {b} \t c : {c} \t d : {d} \t e : {e} \t f : {f}')
#End of the function
f1(10, 20, 30, d=40, e=50, f=60) # a : 10  b : 20  c : 30  d : 40  e : 50  f : 60
# f1(1, b=2, c=3, d=4, e=5, f=6) # ERROR as b is positional-only
# f1(1, 2, 3, 4, 5, f=6)         # ERROR as e must be keyword-only
# f1(10, 20, c=30, 40, e=50, f=60)# ERROR as positional argument (40) follows keyword (c=30)
f1(10, 20, 30, 40, e=50, f=60)   # a : 10  b : 20  c : 30  d : 40  e : 50  f : 60



#8
# Identify errors (Home work)
# def f1(/, a, b, c):       # ERROR as / cannot be at the start without parameters before it
      pass
# def f2(a, b, c, *):       # ERROR as * must be followed by keyword-only arguments
      pass



#9
#Identify error (Home work)
# def f4(*, a, b, c, /):    # ERROR as / must appear before *
      pass



#10
# Find outputs (Home work)
def f1(x):
    print('1st function :', x)
def f1(y):
    print('2nd function :', y)
def f1(z):
    print('3rd function :', z)
f1(z=10) # 3rd function : 10 (Last definition overwrites previous ones)
f1(y=20) # 3rd function : 20 (y becomes the value for parameter z)
f1(x=30) # 3rd function : 30 (x becomes the value for parameter z)



#11
# Default arguments demo program
def add(a, b=20, c=30):
    return a + b + c
#End of the function
print(add(100))               # 150
print(add(100, 200))          # 330
print(add(100, 200, 300))     # 600
print(add(100, c=200))        # 320
print(add(c=100, b=200, a=300)) # 600
print(add(c=100, a=200))      # 320
# print(add())                # ERROR as missing required positional argument 'a'
# print(add(a=100, 200))      # ERROR as positional argument follows keyword argument
# print(add(100, , 300))      # ERROR as Invalid syntax (empty comma)
# print(add(100, b, 300))     # ERROR as NameError: 'b' is not defined



#12
#Identify Error
# def f1(a=10, b, c=20, d): # ERROR as non-default argument follows default argument
      pass
def f2(b, d, a=10, c=20):   # Valid
    pass


#13
# Find outputs (Home work)
def f1(a=10):
    print(a)
#End of the function
f1(20)   # 20
f1()     # 10
f1(a=30) # 30



#14
# Find outputs (Home work)
def add(a, b, c=10, d=20):
    return a + b + c + d
#End of the function
print(add(100, 200))             # 330
print(add(100, 200, 300))        # 630
print(add(100, 200, 300, 400))   # 1000
print(add(b=100, a=200))         # 330
print(add(100, 200, d=300))      # 610
print(add(d=100, a=200, b=300))  # 610
# print(add(c=100, d=200, 300, 400)) # ERROR as positional argument follows keyword argument
# print(add(100, 200, c=300, x=400)) # ERROR as unexpected keyword argument 'x'
# print(add())                       # ERROR as missing required positional arguments 'a', 'b'



#15
# Find outputs (Home work)
def f1(x=25):
    return x
def f2(x):
    return x
#End of the function
print(f1(10)) # 10
print(f1())   # 25
print(f2(20)) # 20
# print(f2()) # ERROR as at least one argument has to be given which is assigned to 'x' i.e. no default argument



#16
# Find outputs (Home work)
def disp(ch='*', n=4):
    print(ch * n)
#End of the function
disp('-', 6)      # ------
disp('$')         # $$$$
disp()            # ****
disp(n=5)         # *****
disp(5)           # ERROR as if 5 is passed to 'ch', you can't multiply int by int like this (TypeError)
disp(n=7, ch='%') # %%%%%%%
disp(7, '@')      # ERROR as Trying to repeat int 7, '@' times (TypeError)
# disp(7, n=6)    # ERROR as 7 assigned to ch, results in TypeError: unsupported operand
# disp(ch='!', 5) # ERROR as positional argument follows keyword argument



#17
# Find outputs (Home work)
def power(a, b=2):
    return a ** b
#End of the fucntion
print(power(2, 6))           # 64
print(power(5))              # 25
print(power(b=3, a=4.5))     # 91.125
print(power(3 + 4j))         # (-7+24j) -> (3+4j)^2
print(power(True))           # 1 (True is 1, 1^2 = 1)
# def power(b=2, a):         # ERROR as non-default argument follows default argument
      pass



#18
# Find outputs (Home work)
def add(a , b):
    print('2-argument  function')
    return a + b
def add(a , b , c):
    print('3-argument  function')
    return a + b + c
def add(a=1, b=2, c=3, d=4):
    print('4-argument function')
    return a + b + c + d
#End of the function
print(add(10, 20, 30, 40)) # 4-argument function \n 100
print(add(50, 60, 70))     # 4-argument function \n 184
print(add(80, 90))         # 4-argument function \n 177
print(add(100))            # 4-argument function \n 109
print(add())               # 4-argument function \n 10



#19
# Find outputs (Home work)
def disp(a , b):
    print('2-argument function : ' , a , b)
def disp(a , b , c , d):
    print('4-argument function : ' , a , b , c , d)
def disp(a, b, c=25):
    print('3-argument function : ', a, b, c)
#End of the function
disp(10, 20, 30)   # 3-argument function : 10 20 30
# disp(40, 50, 60, 70) # ERROR as f1() takes from 2 to 3 positional arguments but 4 were given
disp(80, 90)       # 3-argument function : 80 90 25



#20
# Find outputs (Home work)
def add(*, a=10, b=20):
    return a + b
#End of the function
print(add(a=30, b=40)) # 70
print(add())           # 30
print(add(a=50))       # 70
print(add(b=60, a=70)) # 130
# print(add(80, 90))   # ERROR as takes 0 positional arguments



#21
## Find outputs (Home work)
# def add(a=10, b, c):  # ERROR as non-default argument follows default argument
      pass
def add(*, a=10, b, c):
    return a + b + c
#End of the function
print(add(a=30, b=40, c=50)) # 120
print(add(b=60, c=70))       # 140
print(add(c=80, b=90, a=100))# 270
# print(add(c=25, a=43))     # ERROR as missing required argument 'b'
# print(add(1, 2, 3))        # ERROR as takes 0 positional arguments
# def add(a, b=10, c, *, d, e=20, f): # ERROR: non-default 'c' follows default 'b'
      pass



#22
# Find outputs (Home work)
def f1(a=[]):
    pass
print(f1.__defaults__) # ([],)



#23
# Find outputs (Home work)
def f1(x, a=[]):
    a.append(x)
    print('List : ', a)
#End of the function
print('_defaults_ : ', f1.__defaults__) # _defaults_ : ([],)
f1(3)                                   # List : [3]
print('_defaults_ : ', f1.__defaults__) # _defaults_ : ([3],)
f1(4, [1, 2, 3])                        # List : [1, 2, 3, 4] (New list passed, default untouched)
print('_defaults_ : ', f1.__defaults__) # _defaults_ : ([3],)
f1(9)                                   # List : [3, 9] (Default list updated)
print('_defaults_ : ', f1.__defaults__) # _defaults_ : ([3, 9],)
f1(40, [10, 20, 30])                    # List : [10, 20, 30, 40]
print('_defaults_ : ', f1.__defaults__) # _defaults_ : ([3, 9],)
f1(5)                                   # List : [3, 9, 5]
print('_defaults_ : ', f1.__defaults__) # _defaults_ : ([3, 9, 5],)
f1([6, 7, 8])                           # List : [3, 9, 5, [6, 7, 8]]
print('_defaults_ : ', f1.__defaults__) # _defaults_ : ([3, 9, 5, [6, 7, 8]],)



#24
# Find outputs (Home work)
def f1(x, a=[]):
    for i in range(x):
        a.append(i * i)
    return a
#End of the function
print('__defaults__ :', f1.__defaults__)      # ([],)
print(f1(3))                                  # [0, 1, 4]
print('__defaults__ :', f1.__defaults__)      # ([0, 1, 4],)
print(f1(4, [10, 20, 15, 18]))                # [10, 20, 15, 18, 0, 1, 4, 9] (New list used, default unchanged)
print('__defaults__ :', f1.__defaults__)      # ([0, 1, 4],)
print(f1(5))                                  # [0, 1, 4, 0, 1, 4, 9, 16] (Appended to existing default)
print('__defaults__ :', f1.__defaults__)      # ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100, 200, 300], x = 6))         # [100, 200, 300, 0, 1, 4, 9, 16, 25] (Default unchanged)
print('__defaults__ :', f1.__defaults__)      # ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6))                                  # [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('__defaults__ :', f1.__defaults__)      # ([0, 1, 4, ..., 25],)



#25
# Find outputs (Home work)
def f1(a = 'Hyd', b = []):
    a += "Sec"
    b += [1, 2, 3]
    print('a : ', a)
    print('b : ', b)
#End of the function
print('Default Values : ', f1.__defaults__)   # ('Hyd', [])
f1()                                          # a : HydSec  b : [1, 2, 3]
print('Default Values : ', f1.__defaults__)   # ('Hyd', [1, 2, 3])
f1()                                          # a : HydSec  b : [1, 2, 3, 1, 2, 3]
print('Default Values : ', f1.__defaults__)   # ('Hyd', [1, 2, 3, 1, 2, 3])
f1()                                          # a : HydSec  b : [1, 2, 3, 1, 2, 3, 1, 2, 3]



#26
# Find outputs (Home work)
def f1(*t):
    print(t)
    print(type(t))
    print(len(t))
    print()
#End of the function
f1(10, 20, 15, 18)                  # (10, 20, 15, 18), <class 'tuple'>, 4
f1()                                # (), <class 'tuple'>, 0
f1([10, 20], (30, 40), {60, 70})    # ([10, 20], (30, 40), {60, 70}), <class 'tuple'>, 3
f1('Hyd')                           # ('Hyd',), <class 'tuple'>, 1
tpl = (100, 200, 150)
f1(tpl)                             # ((100, 200, 150),), <class 'tuple'>, 1 (The tuple itself is the 1st element)
# f1(t = (10, 20, 30))              # ERROR due to an unexpected keyword argument 't' (*args doesn't accept keywords)



#27
# Write a function to determine average of arguments passed to the function (Home work)
def avg(*a):
    return sum(a) / len(a) if a else 0        
#End of the function
print(avg(10, 20, 15, 18))                    # 15.75
print(avg(25, 10.8, True))                    # 12.266... (True is treated as 1)
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))       # 14.26
print(avg())                                  # 0
print(avg(25))                                # 25.0
print(avg(3 + 4j, 5 + 6j))                    # (4+5j)
tpl = (10, 20, 15, 18)
# print(avg(tpl))                             # ERROR as sum() fails because it tries to add a tuple to an int



#28
# Write a function to concatenate strings passed to the function? (Home work)
def concat(*a):
    return " ".join(map(str, a))
#End of the function
print(concat('Sankar', 'Dayal', 'Sarma')) # Sankar Dayal
print(concat('Hyd', 'Is', 'Green', 'City')) # Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Python Is A Great Language
print(concat()) #Empty string
print(concat('Python')) # Python
print(concat(1, 2, 3))  # 1 2 3



#29
# Find outputs (Home work)
def f1(a=25, *b):
    print(f'a : {a} \t b : {b}')
#End of the function
f1(10, 20, 30, 40)               # a : 10<tab>b : (20, 30, 40)
f1(50, 60)                       # a : 50<tab>b : (60,)
f1(70)                           # a : 70<tab>b : ()
f1(a=80)                         # a : 80<tab>b : ()
f1(b=(10, 20, 30), a=40)         # ERROR as unexpected keyword argument 'b' (*b cannot be used as a keyword)
f1()                             # a : 25<tab>b : ()
f1(a=10, (20, 30, 40))           # ERROR as positional argument follows keyword argument
f1(25, b=(10, 20, 30))           # ERROR as unexpected keyword argument 'b'
f1(25, a=(10, 20, 30))           # ERROR as multiple values for argument 'a' (25 is 1st pos, a=... is keyword)
f1((10, 20, 30), 10, 20, 30)     # a : (10, 20, 30)<tab>b : (10, 20, 30)
f1(a=(10, 20, 30), 10, 20, 30)   # ERROR as positional argument follows keyword argument



#30
# Find outputs (Home work)
def f1(*a, b):
    print(f'a : {a} \t b : {b}')
#End of the function
f1(10, 20, 30, b=40)             # a : (10, 20, 30)<tab>b : 40
f1(50, b=60)                     # a : (50,)<tab>b : 60
f1(b=70)                         # a : ()<tab>b : 70
f1(b=10, a=(20, 30, 40))         # ERROR as unexpected keyword argument 'a' (parameter 'a' is a collector, not a name)
f1(b=10, (20, 30, 40))           # ERROR as positional argument follows keyword argument
f1()                             # ERROR as missing 1 required keyword-only argument: 'b'
f1(10, 20, 30, (10, 20, 30))     # ERROR as missing 1 required keyword-only argument: 'b' (last tuple is swallowed by *a)
f1(10, 20, 30, 40)               # ERROR as missing 1 required keyword-only argument: 'b'
f1(25)                           # ERROR as missing 1 required keyword-only argument: 'b'
f1(10, 20, 30, b=(10, 20, 30))   # a : (10, 20, 30)<tab>b : (10, 20, 30)



#31
# Find outputs (Home work)
def f1(a, *b, c):
    print(f'a : {a} \t b : {b} \t c : {c}')
#End of the function
f1(10, 20, 30, 40, c=50)         # a : 10<tab>b : (20, 30, 40)<tab>c : 50
f1(60, 70, c=80)                 # a : 60<tab>b : (70,)<tab>c : 80
f1(90, c=100)                    # a : 90<tab>b : ()<tab>c : 100
# f1(a=1, 2, c=3)                # ERROR as positional argument follows keyword argument
f1(1, 2, 3)                      # ERROR as missing 1 required keyword-only argument: 'c' (3 is swallowed by *b)
f1(a=1, b=2, c=3)                # ERROR as unexpected keyword argument 'b'
f1(a=25, 100, 200, 300, c=35)    # ERROR as positional argument follows keyword argument



#32
# Which of the following are valid? (Home work)
def f1(*a , *b): # f1 is Invalid (multiple *args)
    pass
def f2(*a , b): # f2() is Valid
    pass
def f3(a , *b): # f3() is Valid
    pass
def f4(a , b): # f4() is Valid
    pass
def f5(a , *b , c): # f5() is Valid
    pass
def f6( * , a , *b , c): # f6() is Invalid (multiple *args)
    pass
def f7(a , *b , c ,  /): # f7() is Invalid (*b after / not allowed in this combo)
    pass



#33
# Find outputs (Home work)
def f1(*a):
    print(a)
    print(type(a))
    for x in a:
        print(x)
        print(type(x))
#End of the function
f1([10, 20], {30, 40}, (50, 60))
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



#34
# Variable number of keyword arguments demo program
def disp(**a):
    print("Results")
    print(type(a))
    print(a)
    print()
#End of the function
disp(RollNo = 10 , StudName = 'Rama Rao') # Results <next line> <class 'dict'> <next line> {'RollNo': 10, 'StudName': 'Rama Rao'}
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0) # Results <next line> <class 'dict'> <next line> {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm') # Results <next line> <class 'dict'> <next line> {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
disp() # Results <next line> <class 'dict'> <next line> {}



#35
# Find outputs (Home work)
def f1(**a):
    print("Results")
    for k, v in a.items():
        print(k, v, sep=' ... ')
#End of the function
f1(Empno = 25 , Empname = 'Rama Rao' , Salary = 10000.0 , Gender = 'm')
'''
Results
Empno ... 25
Empname ... Rama Rao
Salary ... 10000.0
Gender ... m
'''



#36
# Find outputs (Home work)
def f1(*a):
    print(type(a))
    print(a)
def f2(**a):
    print(type(a))
    print(a)
#End of the function
f1(25 , 10.8 , 'Hyd' , True) #<class 'tuple'> <next line> (25, 10.8, 'Hyd', True)
print() #/n i.e. empty 
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0) #<class 'dict'> <next line> {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}



#37
# Find outputs (Home work)
def f1(empno , ename , sal):
    print(F'Emp Number: {empno} \t Emp Name: {ename} \t Salary: {sal}')
def f2(**a):
    print(a)
#End of the function
f1(empno=25, ename='Sita', sal=10000.0) #Emp Number: 25<tab>Emp Name: Sita<tab>Salary: 10000.0
# f1(eno=25, empname='Sita', salary=10000.0) # ERROR as unexpected keyword argument
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) #{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno=25, salary=10000.0) # {'eno': 25, 'salary': 10000.0}



#38
# Find outputs (Home work)
def f1(a, *b, **c):
    print(a)
    if b:
        print(b)
    if c:
        print(c)
#End of the function
f1(25)                    # 25
f1('Hyd', 10, 20)         # Hyd \n (10, 20)
f1(10.8, 25, EmpNo=12)    # 10.8 \n (25,) \n {'EmpNo': 12}
