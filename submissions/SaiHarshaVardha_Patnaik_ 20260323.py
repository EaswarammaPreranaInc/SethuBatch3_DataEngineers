# 1. FUNCTION CALLS
def f1():
    print('f1 Function')
    f2()
def f2():
    print('f2 function')
f1()
# OUTPUT:
# f1 Function
# f2 function

# 2. ADD FUNCTION WITH MULTIPLE DATA TYPES
def add(a, b):
    return a + b
print(add(10, 20))        # 30
print(add('Hyder', 'abad')) # Hyderabad
print(add(10.8, 20.6))     # 31.4
print(add(True, False))    # 1
print(add(3+4j, 5+6j))     # (8+10j)
print(add(25, 10.8))       # 35.8
print(add([25,10.8,'Hyd'], [True,None,3+4j,'Sec']))
                         # [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
# print(add(10, '20'))     # ERROR: TypeError

# 3. FUNCTION OVERLOADING (Last definition wins)
def f1():
    print('No-argument function')
def f1(x):
    print('Single argument function : ', x)
def f1(x, y):
    print('Two argument function : ', x, y)
def f1(x, y, z):
    print('Three argument function : ', x, y, z)
f1(10, 20, 30)  # Three argument function :  10 20 30
f1(40, 50)      # Two argument function :  40 50 None
f1(60)          # Single argument function :  60 None None
f1()            # No-argument function

# 4. PRIME NUMBER FUNCTION
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Analysis:
# prime(25): False, loop 4 times (2,3,4,5)
# prime(11): True,  loop 3 times (2,3,4) 
# prime(2):  True,  loop 0 times
# prime(49): False, loop 6 times (2,3,4,5,6,7)

# Main program:
n = int(input('Enter any integer number : '))
if n < 2:
    print('Invalid input')
elif prime(n):
    print('Prime number')
else:
    print('Composite number')

# 5. POSITIONAL ARGUMENTS disp()
def disp(empno, ename, sal):
    print(f'Emp Number : {empno}\tEmp Name : {ename}\tSalary : {sal}')
disp(25, 'Rama Rao', 10000.0)
disp('Sita', 20000.0, 35)

# 6. KEYWORD & FORMATTED disp()
def disp(empno, ename, sal):
    print(f'Emp Number : {empno:4}\tEmp Name : {ename:15}\tSalary : {sal}')
disp(25, 'Rama Rao', 10000.0)
disp(ename='Sita', sal=20000.0, empno=35)
x, y, z = 'Rama Rao', 30000.0, 20
disp(x, y, z)

# 7. KEYWORD ARGUMENTS f1()
def f1(a, b, c):
    print(f'a : {a}\tb : {b}\tc : {c}')
f1(a=10, b=20, c=30)
f1(25, 10.8, 'Hyd')
f1(b=40.7, a=50.2, c=60.5)
f1(c='Hyd', b='Sec', a='Cyb')
f1(c=3+4j, a=True, b=None)
f1(25, c=10.8, b='Hyd')
f1(a=100, 200, 300)
# f1(True, None, b='Hyd')  # ERROR: multiple value for b
# f1(10, 20, x=30)         # ERROR: unexpected keyword 'x'
# f1(10, 20)               # ERROR: missing c

# 8. TRICKY f1() WITH UNPACKING
def f1(a, b, c):
    return a + b * c
print(f1(3, 4, 5))           # 23 (3+4*5)
print(f1(*[6, 7, 8]))        # 27 (6+7*8)
# print(f1([6, 7, 8]))      # ERROR: list + int
# print(f1(*{1:2, 3:4, 5:6})) # ERROR: dict too long
print(f1(**{'c':2, 'b':4, 'a':6})) # 22 (6+4*2)
# print(f1({'c':2, 'b':4, 'a':6})) # ERROR: dict + int
print({**{'c':2, 'b':4, 'a':6}})   # {c:2, b:4, a:6}
# print(f1(**{'c':2, 'a':4, 'x':6})) # ERROR: unexpected 'x'

# 9. IDENTIFY ERRORS
a = [10, 20, 15, 5, 12]
# print(sorted(reverse=True, a))  # ERROR: reverse must be first
# print(sorted(a, rev=True))      # ERROR: no 'rev' parameter
print(25, 10.8, 'Hyd', sep='\t')  # 25	10.8	Hyd
# print(25, 10.8, 'Hyd', endofline='\t') # ERROR: no 'endofline'
print(25, sep='\t', 10.8, end='\t', 'Hyd') # 25	10.8	Hyd	
