def prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def prime_divisors(n):
    divs = [i for i in range(1, n + 1) if n % i == 0 and prime(i)]
    print(f"Prime divisors : {divs}")
    print(f"Number of prime divisors : {len(divs)}")

prime_divisors(30) # Output: Prime divisors : [2, 3, 5] \n Number of prime divisors : 3
prime_divisors(84) # Output: Prime divisors : [2, 3, 7] \n Number of prime divisors : 3
prime_divisors(49) # Output: Prime divisors : [7] \n Number of prime divisors : 1

def f1(*, a, b):
    print(f'a : {a} \t b : {b}')

f1(a=10, b=20)   # Output: a : 10 	 b : 20
f1(b=30, a=40)   # Output: a : 40 	 b : 30
# f1(50, 60)     # TypeError: f1() takes 0 positional arguments but 2 were given
# f1(70, b=80)   # TypeError: f1() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given
# f1(a=15, 25)   # SyntaxError: positional argument follows keyword argument

def f1(a, *, b, c):
    print(f'a : {a} \t b : {b} \t c : {c} ')

f1(10, b=20, c=30)       # Output: a : 10 	 b : 20 	 c : 30 
f1(a=40, b=50, c=60)     # Output: a : 40 	 b : 50 	 c : 60 
f1(c=100, b=90, a=80)    # Output: a : 80 	 b : 90 	 c : 100 
# f1(70, 80, c=90)       # TypeError: f1() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
# f1(70, 80, 90)         # TypeError: f1() takes 1 positional argument but 3 were given
# f1(c=15, b=25, 35)     # SyntaxError: positional argument follows keyword argument

# def f1(a, b, *):       # SyntaxError: named arguments must follow bare *
#     pass

def f1(a, b, /):
    print(f'a : {a} \t b : {b}')

f1(10, 20)       # Output: a : 10 	 b : 20
# f1(a=30, b=40) # TypeError: f1() got some positional-only arguments passed as keyword arguments: 'a, b'
# f1(50, b=60)   # TypeError: f1() got some positional-only arguments passed as keyword arguments: 'b'
# f1(a=70, 80)   # SyntaxError: positional argument follows keyword argument

def f1(a, b, /, c):
    print(f'a : {a} \t b : {b} \t c : {c} ')

f1(10, 20, 30)           # Output: a : 10 	 b : 20 	 c : 30 
f1(40, 50, c=60)         # Output: a : 40 	 b : 50 	 c : 60 
# f1(a=70, b=80, c=90)   # TypeError: f1() got some positional-only arguments passed as keyword arguments: 'a, b'
# f1(a=100, b=110, 120)  # SyntaxError: positional argument follows keyword argument
# f1(a=130, 140, c=150)  # SyntaxError: positional argument follows keyword argument
# f1(160, b=170, 180)    # SyntaxError: positional argument follows keyword argument
# f1(190, b=200, c=210)  # TypeError: f1() got some positional-only arguments passed as keyword arguments: 'b'

def f1(a, b, /, c, d, *, e, f):
    print(f'a : {a} \t b : {b} \t c : {c} \t d : {d} \t e : {e} \t f : {f}')

f1(10, 20, 30, d=40, e=50, f=60)     # Output: a : 10 	 b : 20 	 c : 30 	 d : 40 	 e : 50 	 f : 60
# f1(1, b=2, c=3, d=4, e=5, f=6)     # TypeError: f1() got some positional-only arguments passed as keyword arguments: 'b'
# f1(1, 2, 3, 4, 5, f=6)             # TypeError: f1() takes 4 positional arguments but 5 positional arguments (and 1 keyword-only argument) were given
# f1(10, 20, c=30, 40, e=50, f=60)   # SyntaxError: positional argument follows keyword argument
f1(10, 20, 30, 40, e=50, f=60)       # Output: a : 10 	 b : 20 	 c : 30 	 d : 40 	 e : 50 	 f : 60

# def f1(/, a, b, c): # SyntaxError: expected 1 or more arguments before /
#     pass
# def f2(a, b, c, *): # SyntaxError: named arguments must follow bare *
#     pass

# def f4(*, a, b, c, /): # SyntaxError: / must be ahead of *
#     pass

def f1(x):
    print('1st function : ', x)
def f1(y):
    print('2nd function : ', y)
def f1(z):
    print('3rd function : ', z)

f1(z=10) # Output: 3rd function :  10
# f1(y=20) # TypeError: f1() got an unexpected keyword argument 'y'
# f1(x=30) # TypeError: f1() got an unexpected keyword argument 'x'

def add(a, b=20, c=30):
    return a + b + c

print(add(100))                 # Output: 150
print(add(100, 200))            # Output: 330
print(add(100, 200, 300))       # Output: 600
print(add(100, c=200))          # Output: 320
print(add(c=100, b=200, a=300)) # Output: 600
print(add(c=100, a=200))        # Output: 320
# print(add())                  # TypeError: add() missing 1 required positional argument: 'a'
# print(add(a=100, 200))        # SyntaxError: positional argument follows keyword argument
# print(add(100,  , 300))       # SyntaxError: invalid syntax
# print(add(100, b, 300))       # NameError: name 'b' is not defined (unless b is defined earlier)

# def f1(a=10, b, c=20, d):     # SyntaxError: non-default argument follows default argument
#     pass
def f2(b, d, a=10, c=20):       # Valid
    pass

def f1(a=10):
    print(a)

f1(20)      # Output: 20
f1()        # Output: 10
f1(a=30)    # Output: 30

def add(a, b, c=10, d=20):
    return a + b + c + d

print(add(100, 200))                   # Output: 330
print(add(100, 200, 300))              # Output: 620
print(add(100, 200, 300, 400))         # Output: 1000
print(add(b=100, a=200))               # Output: 330
print(add(100, 200, d=300))            # Output: 610
print(add(d=100, a=200, b=300))        # Output: 610
# print(add(c=100, d=200, 300, 400))   # SyntaxError: positional argument follows keyword argument
# print(add(100, 200, c=300, x=400))   # TypeError: add() got an unexpected keyword argument 'x'
# print(add())                         # TypeError: add() missing 2 required positional arguments: 'a' and 'b'

def f1(x=25):
    return x
def f2(x):
    return x

print(f1(10)) # Output: 10
print(f1())   # Output: 25
print(f2(20)) # Output: 20
# print(f2()) # TypeError: f2() missing 1 required positional argument: 'x'

def disp(ch='*', n=4):
    print(ch * n)

disp('-', 6)           # Output: ------
disp('$')              # Output: $$$$
disp()                 # Output: ****
disp(n=5)              # Output: *****
# disp(5)              # Output: 20 (Wait! Python handles 5 * 4 correctly, but logical error relative to string multiplication)
disp(n=7, ch='%')      # Output: %%%%%%%
# disp(7, '@')         # TypeError: unsupported operand type(s) for *: 'int' and 'str'
disp(7, n=6)           # Output: 42
# disp(ch='!', 5)      # SyntaxError: positional argument follows keyword argument

def power(a, b=2):
    return a ** b

print(power(2, 6))           # Output: 64
print(power(5))              # Output: 25
print(power(b=3, a=4.5))     # Output: 91.125
print(power(3 + 4j))         # Output: (-7+24j)
print(power(True))           # Output: 1

# def power(b=2, a):         # SyntaxError: non-default argument follows default argument
#     pass

def add(a, b):
    print('2-argument function')
    return a + b
def add(a, b, c):
    print('3-argument function')
    return a + b + c
def add(a=1, b=2, c=3, d=4):
    print('4-argument function')
    return a + b + c + d

print(add(10, 20, 30, 40)) # Output: 4-argument function \n 100
print(add(50, 60, 70))     # Output: 4-argument function \n 184
print(add(80, 90))         # Output: 4-argument function \n 177
print(add(100))            # Output: 4-argument function \n 109
print(add())               # Output: 4-argument function \n 10

def disp(a, b):
    print('2-argument function : ', a, b)
def disp(a, b, c, d):
    print('4-argument function : ', a, b, c, d)
def disp(a, b, c=25):
    print('3-argument function : ', a, b, c)

disp(10, 20, 30)         # Output: 3-argument function :  10 20 30
# disp(40, 50, 60, 70)   # TypeError: disp() takes from 2 to 3 positional arguments but 4 were given
disp(80, 90)             # Output: 3-argument function :  80 90 25

def add(*, a=10, b=20):
    return a + b

print(add(a=30, b=40))   # Output: 70
print(add())             # Output: 30
print(add(a=50))         # Output: 70
print(add(b=60, a=70))   # Output: 130
# print(add(80, 90))     # TypeError: add() takes 0 positional arguments but 2 were given

# def add(a=10, b, c):   # SyntaxError: non-default argument follows default argument
#     pass
def add(*, a=10, b, c):
    return a + b + c

print(add(a=30, b=40, c=50))    # Output: 120
print(add(b=60, c=70))          # Output: 140
print(add(c=80, b=90, a=100))   # Output: 270
# print(add(c=25, a=43))        # TypeError: add() missing 1 required keyword-only argument: 'b'
# print(add(1, 2, 3))           # TypeError: add() takes 0 positional arguments but 3 were given

# def add(a, b=10, c, *, d, e=20, f): # SyntaxError: non-default argument follows default argument
#     pass

def f1(x, a=[]):
    a.append(x)
    print('List : ', a)

# In Python, the attribute is __defaults__, not _defaults_. If run as written, it causes AttributeError.
# print('_defaults_ : ', f1._defaults_)   # AttributeError
print('__defaults__ : ', f1.__defaults__) # Output: __defaults__ :  ([],)
f1(3)                                     # Output: List :  [3]
print('__defaults__ : ', f1.__defaults__) # Output: __defaults__ :  ([3],)
f1(4, [1, 2, 3])                          # Output: List :  [1, 2, 3, 4]
print('__defaults__ : ', f1.__defaults__) # Output: __defaults__ :  ([3],)
f1(9)                                     # Output: List :  [3, 9]
print('__defaults__ : ', f1.__defaults__) # Output: __defaults__ :  ([3, 9],)
f1(40, [10, 20, 30])                      # Output: List :  [10, 20, 30, 40]
print('__defaults__ : ', f1.__defaults__) # Output: __defaults__ :  ([3, 9],)
f1(5)                                     # Output: List :  [3, 9, 5]
print('__defaults__ : ', f1.__defaults__) # Output: __defaults__ :  ([3, 9, 5],)
f1([6, 7, 8])                             # Output: List :  [3, 9, 5, [6, 7, 8]]
print('__defaults__ : ', f1.__defaults__) # Output: __defaults__ :  ([3, 9, 5, [6, 7, 8]],)

def f1(x, a=[]):
    for i in range(x):
        a.append(i * i)
    return a

print('__defaults__ : ', f1.__defaults__)           # Output: __defaults__ :  ([],)
print(f1(3))                                        # Output: [0, 1, 4]
print('__defaults__ : ', f1.__defaults__)           # Output: __defaults__ :  ([0, 1, 4],)
print(f1(4, [10, 20, 15, 18]))                      # Output: [10, 20, 15, 18, 0, 1, 4, 9]
print('__defaults__ : ', f1.__defaults__)           # Output: __defaults__ :  ([0, 1, 4],)
print(f1(5))                                        # Output: [0, 1, 4, 0, 1, 4, 9, 16]
print('__defaults__ : ', f1.__defaults__)           # Output: __defaults__ :  ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a=[100, 200, 300], x=6))                   # Output: [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('__defaults__ : ', f1.__defaults__)           # Output: __defaults__ :  ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6))                                        # Output: [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('__defaults__ : ', f1.__defaults__)           # Output: __defaults__ :  ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)

def f1(a='Hyd', b=[]):
    a += "Sec"
    b += [1, 2, 3]
    print('a : ', a)
    print('b : ', b)

print('Default Values : ', f1.__defaults__) # Output: Default Values :  ('Hyd', [])
f1()                                        # Output: a :  HydSec \n b :  [1, 2, 3]
print('Default Values : ', f1.__defaults__) # Output: Default Values :  ('Hyd', [1, 2, 3])
f1()                                        # Output: a :  HydSec \n b :  [1, 2, 3, 1, 2, 3]
print('Default Values : ', f1.__defaults__) # Output: Default Values :  ('Hyd', [1, 2, 3, 1, 2, 3])
f1()                                        # Output: a :  HydSec \n b :  [1, 2, 3, 1, 2, 3, 1, 2, 3]

def f1(*t):
    print(t)
    print(type(t))
    print(len(t))
    print()

f1(10, 20, 15, 18)  # Output: (10, 20, 15, 18) \n <class 'tuple'> \n 4 \n
f1()                # Output: () \n <class 'tuple'> \n 0 \n
f1([10, 20], (30, 40, 50), {60, 70, 80, 90}) # Output: ([10, 20], (30, 40, 50), {80, 90, 60, 70}) \n <class 'tuple'> \n 3 \n
f1('Hyd')           # Output: ('Hyd',) \n <class 'tuple'> \n 1 \n
tpl = (100, 200, 150)
f1(tpl)             # Output: ((100, 200, 150),) \n <class 'tuple'> \n 1 \n
# f1(t=(10, 20, 30)) # TypeError: f1() got an unexpected keyword argument 't'

def avg(*a):
    return sum(a) / len(a) if a else 0

print(avg(10, 20, 15, 18))                  # Output: 15.75
print(avg(25, 10.8, True))                  # Output: 12.266666666666667
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))     # Output: 14.26
print(avg())                                # Output: 0
print(avg(25))                              # Output: 25.0
print(avg(3 + 4j, 5 + 6j))                  # Output: (4+5j)
tpl = (10, 20, 15, 18)
# print(avg(tpl))                           # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

def concat(*a):
    return ' '.join(map(str, a))

print(concat('Sankar', 'Dayal', 'Sarma'))           # Output: Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))         # Output: Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Output: Python Is A Great Language
print(concat())                                     # Output: 
print(concat('Python'))                             # Output: Python
print(concat(1, 2, 3))                              # Output: 1 2 3

def f1(a=25, *b):
    print(f'a : {a} \t b : {b} ')

f1(10, 20, 30, 40)                   # Output: a : 10 	 b : (20, 30, 40) 
f1(50, 60)                           # Output: a : 50 	 b : (60,) 
f1(70)                               # Output: a : 70 	 b : () 
f1(a=80)                             # Output: a : 80 	 b : () 
# f1(b=(10, 20, 30), a=40)           # TypeError: f1() got an unexpected keyword argument 'b'
f1()                                 # Output: a : 25 	 b : () 
# f1(a=10, (20, 30, 40))             # SyntaxError: positional argument follows keyword argument
# f1(25, b=(10, 20, 30))             # TypeError: f1() got an unexpected keyword argument 'b'
# f1(25, a=(10, 20, 30))             # TypeError: f1() got multiple values for argument 'a'
f1((10, 20, 30), 10, 20, 30)         # Output: a : (10, 20, 30) 	 b : (10, 20, 30) 
# f1(a=(10, 20, 30), 10, 20, 30)     # SyntaxError: positional argument follows keyword argument

def f1(*a, b):
    print(f'a : {a} \t b : {b}')

f1(10, 20, 30, b=40)                 # Output: a : (10, 20, 30) 	 b : 40
f1(50, b=60)                         # Output: a : (50,) 	 b : 60
f1(b=70)                             # Output: a : () 	 b : 70
# f1(b=10, a=(20, 30, 40))           # TypeError: f1() got an unexpected keyword argument 'a'
# f1(b=10, (20, 30, 40))             # SyntaxError: positional argument follows keyword argument
# f1()                               # TypeError: f1() missing 1 required keyword-only argument: 'b'
# f1(10, 20, 30, (10, 20, 30))       # TypeError: f1() missing 1 required keyword-only argument: 'b'
# f1(10, 20, 30, 40)                 # TypeError: f1() missing 1 required keyword-only argument: 'b'
# f1(25)                             # TypeError: f1() missing 1 required keyword-only argument: 'b'
f1(10, 20, 30, b=(10, 20, 30))       # Output: a : (10, 20, 30) 	 b : (10, 20, 30)

def f1(a, *b, c):
    print(f'a : {a} \t b : {b} \t c : {c}')

f1(10, 20, 30, 40, c=50)             # Output: a : 10 	 b : (20, 30, 40) 	 c : 50
f1(60, 70, c=80)                     # Output: a : 60 	 b : (70,) 	 c : 80
f1(90, c=100)                        # Output: a : 90 	 b : () 	 c : 100
# f1(a=1, 2, c=3)                    # SyntaxError: positional argument follows keyword argument
# f1(1, 2, 3)                        # TypeError: f1() missing 1 required keyword-only argument: 'c'
# f1(a=1, b=2, c=3)                  # TypeError: f1() got an unexpected keyword argument 'b'
# f1(a=25, 100, 200, 300, c=35)      # SyntaxError: positional argument follows keyword argument

# def f1(*a, *b): # SyntaxError: invalid syntax (multiple * arguments)
#     pass
def f2(*a, b):    # Valid
    pass
def f3(a, *b):    # Valid
    pass
def f4(a, b):     # Valid
    pass
def f5(a, *b, c): # Valid
    pass
# def f6(*, a, *b, c): # SyntaxError: invalid syntax (multiple * arguments)
#    pass
# def f7(a, *b, c, /): # SyntaxError: / must be ahead of *
#    pass

def f1(*a):
    print(a)
    print(type(a))
    for x in a:
        print(x)
        print(type(x))

f1([10, 20], {30, 40}, (50, 60)) 
# Output:
# ([10, 20], {40, 30}, (50, 60))
# <class 'tuple'>
# [10, 20]
# <class 'list'>
# {40, 30}
# <class 'set'>
# (50, 60)
# <class 'tuple'>

def disp(**a):
    print('Results')
    print(type(a))
    print(a)
    print()

disp(RollNo=10, StudName='Rama Rao')
# Output: Results \n <class 'dict'> \n {'RollNo': 10, 'StudName': 'Rama Rao'} \n
disp(EmpNo=25, EmpName='Sita', Salary=10000.0)
# Output: Results \n <class 'dict'> \n {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0} \n
disp(AcNo=30, CustName='Kiran', Balance=20000.0, Gender='m')
# Output: Results \n <class 'dict'> \n {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'} \n
disp()
# Output: Results \n <class 'dict'> \n {} \n

def f1(**a):
    print('Results')
    for k, v in a.items():
        print(k, v, sep=' ... ')

f1(Empno=25, Empname='Rama Rao', Salary=10000.0, Gender='m')
# Output: Results \n Empno ... 25 \n Empname ... Rama Rao \n Salary ... 10000.0 \n Gender ... m
f1()
# Output: Results

def f1(*a):
    print(type(a))
    print(a)
def f2(**a):
    print(type(a))
    print(a)

f1(25, 10.8, 'Hyd', True)
# Output: <class 'tuple'> \n (25, 10.8, 'Hyd', True)
print()
f2(EmpNum=25, EmpName='Sita', Salary=10000.0)
# Output: <class 'dict'> \n {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

def f1(empno, ename, sal):
    print(f'Emp Number : {empno} \t Emp Name : {ename} \t Salary : {sal}')
def f2(**a):
    print(a)

f1(empno=25, ename='Sita', sal=10000.0)
# Output: Emp Number : 25 	 Emp Name : Sita 	 Salary : 10000.0
# f1(eno=25, empname='Sita', salary=10000.0) # TypeError: f1() got an unexpected keyword argument 'eno'
f2(empno=25, ename='Sita', sal=10000.0)
# Output: {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno=25, empname='Sita', salary=10000.0)
# Output: {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}

def f1(a, *b, **c):
    print(a)
    if b:
        print(b)
    if c:
        print(c)

f1(25)
# Output: 25
print()
f1('Hyd', 10, 20, 30)
# Output: Hyd \n (10, 20, 30)
print()
f1(10.8, 25, 'Hyd', True, EmpNo=12, EmpName='Rama Rao', Salary=10000.0)
# Output: 10.8 \n (25, 'Hyd', True) \n {'EmpNo': 12, 'EmpName': 'Rama Rao', 'Salary': 10000.0}