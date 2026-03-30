# Keyword only arguments demo program

def f1(*, a, b):
    print(f'a : {a} \t b : {b}')

f1(a=10, b=20)          # a : 10 	 b : 20
f1(b=30, a=40)          # a : 40 	 b : 30
f1(50, 60)              # error
f1(70, b=80)            # error
f1(a=15, 25)            # error


# Find outputs (Home work)

def f1(a, *, b, c):
    print(f'a : {a} \t b : {b} \t c : {c}')

f1(10, b=20, c=30)              # a : 10 	 b : 20 	 c : 30
f1(a=40, b=50, c=60)            # a : 40 	 b : 50 	 c : 60
f1(c=100, b=90, a=80)           # a : 80 	 b : 90 	 c : 100
f1(70, 80, c=90)                # a=70            b:80           c:90
f1(70, 80, 90)                  # error
f1(c=15, b=25, 35)              # error


# Identify error (Home work)

def f1(a, b, *):
    pass                         # error


# Positional only arguments demo program

def f1(a, b, /):
    print(f'a : {a} \t b : {b}')

f1(10, 20)              # a : 10 	 b : 20
f1(a=30, b=40)          # a:30      b:40
f1(50, b=60)            # error
f1(a=70, 80)            # error


# Find outputs (Home work)

def f1(a, b, /, c):
    print(f'a : {a} \t b : {b} \t c : {c}')

f1(10, 20, 30)                  # a : 10 	 b : 20 	 c : 30
f1(40, 50, c=60)                # a : 40 	 b : 50 	 c : 60
f1(a=70, b=80, c=90)            # a : 70 	 b : 20 	  c : 90
f1(a=100, b=110, 120)           # a : 100 	 b : 110	 c : 120
f1(a=130, 140, c=150)           # a:130          b:140           c:150
f1(160, b=170, 180)             # error
f1(190, b=200, c=210)           # error


# Find outputs (Home work)

def f1(a, b, /, c, d, *, e, f):
    print(f'a : {a} \t b : {b} \t c : {c} \t d : {d} \t e : {e} \t f : {f}')

f1(10, 20, 30, d=40, e=50, f=60)      # a : 10 	 b : 20 	 c : 30 	 d : 40 	 e : 50 	 f : 60
f1(1, b=2, c=3, d=4, e=5, f=6)        # error
f1(1, 2, 3, 4, 5, f=6)                # error
f1(10, 20, c=30, 40, e=50, f=60)      # error
f1(10, 20, 30, 40, e=50, f=60)        # a : 10 	 b : 20 	 c : 30 	 d : 40 	 e : 50 	 f : 60


# Identify error (Home work)

def f1(/, a, b, c):
    pass                         # error

def f2(a, b, c, *):
    pass                         # error

def f4(*, a, b, c, /):
    pass                         # error


# Find outputs (Home work)

def f1(x):
    print('1st function :', x)

def f1(y):
    print('2nd function :', y)

def f1(z):
    print('3rd function :', z)

f1(z=10)     # 3rd function : 10
f1(y=20)     # 2st function 
f1(x=30)     # 1st function 


# Default arguments demo program

def add(a, b=20, c=30):
    return a + b + c

print(add(100))                     # 150
print(add(100, 200))                # 330
print(add(100, 200, 300))           # 600
print(add(100, c=200))              # 320
print(add(c=100, b=200, a=300))     # 600
print(add(c=100, a=200))            # 320
print(add())                        # error
print(add(a=100, 200))              # error
print(add(100, , 300))              #420
print(add(100, b, 300))             # error


# Identify Error

def f1(a = 10, b, c = 20, d):
    pass                    # error

def f2(b, d, a = 10, c = 20):
    pass                    # correct


# Find outputs (Home work)

def f1(a = 10):
    print(a)

f1(20)            # 20
f1()              # 10
f1(a = 30)        # 30


# Find outputs (Home work)

def add(a, b, c = 10, d = 20):
    return a + b + c + d

print(add(100, 200))                    # 330
print(add(100, 200, 300))               # 620
print(add(100, 200, 300, 400))          # 1000
print(add(b = 100, a = 200))            # 330
print(add(100, 200, d = 300))           # 610
print(add(d = 100, a = 200, b = 300))   # 610
print(add(c = 100, d = 200, 300, 400))  # error
print(add(100, 200, c = 300, x = 400))  # error
print(add())                            # error


# Find outputs (Home work)

def f1(x = 25):
    return x

def f2(x):
    return x

print(f1(10))       # 10
print(f1())         # 25
print(f2(20))       # 20
print(f2())         # error


# Find outputs (Home work)

def disp(ch = '*', n = 4):
    print(ch * n)

disp('-', 6)              # ------
disp('$')                 # $$$$
disp()                    # ****
disp(n = 5)               # *****
disp(5)                   # error
disp(n = 7, ch = '%')     # %%%%%%%
disp(7, '@')              # error
disp(7, n = 6)            # error
disp(ch = '!', 5)         # error


# Find outputs (Home work)

def power(a, b = 2):
    return a ** b

print(power(2, 6))                # 64
print(power(5))                   # 25
print(power(b = 3, a = 4.5))      # 91.125
print(power(3 + 4j))              # (-7+24j)
print(power(True))                # 1

def power(b = 2, a):
    pass                          # error


# Find outputs (Home work)

def add(a, b):
    print('2-argument function')
    return a + b

def add(a, b, c):
    print('3-argument function')
    return a + b + c

def add(a = 1, b = 2, c = 3, d = 4):
    print('4-argument function')
    return a + b + c + d

print(add(10, 20, 30, 40))    # 4-argument function / 100
print(add(50, 60, 70))        # 4-argument function / 184
print(add(80, 90))            # 4-argument function / 177
print(add(100))               # 4-argument function / 109
print(add())                  # 4-argument function / 10


# Find outputs (Home work)

def disp(a, b):
    print('2-argument function :', a, b)

def disp(a, b, c, d):
    print('4-argument function :', a, b, c, d)

def disp(a, b, c = 25):
    print('3-argument function :', a, b, c)

disp(10, 20, 30)          # 3-argument function : 10 20 30
disp(40, 50, 60, 70)      # error
disp(80, 90)              # 3-argument function : 80 90 25


# Find outputs (Home work)

def add(*, a = 10, b = 20):
    return a + b

print(add(a = 30, b = 40))     # 70
print(add())                   # 30
print(add(a = 50))             # 70
print(add(b = 60, a = 70))     # 130
print(add(80, 90))             # error


# Find outputs (Home work)

def add(a = 10, b, c):
    pass                        # error

def add(*, a = 10, b, c):
    return a + b + c

print(add(a = 30, b = 40, c = 50))     # 120
print(add(b = 60, c = 70))             # 140
print(add(c = 80, b = 90, a = 100))    # 270
print(add(c = 25, a = 43))             # error
print(add(1, 2, 3))                    # error


def add(a, b = 10, c, *, d, e = 20, f):
    pass                                # error