# Find outputs

def f1():
    print('f1 Function')
    f2()

def f2():
    print('f2 function')

f1() # f1 Function
     # f2 function

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home work)

def add(a , b):
        return a + b
# End of the function

print(add(10 , 20)) # 30
print(add('Hyder' , 'abad')) # Hyderabad
print(add(10.8 , 20.6)) # 31.4
print(add(True , False)) # 1
print(add(3 + 4j , 5 + 6j)) # (8+10j)
print(add(25 , 10.8)) # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
# print(add(10 , '20')) # Error because unsupported operand type(s) for +: 'int' and 'str'

# -----------------------------------------------------------------------------------------------------

'''
1) What are the three events in execution of add(10 , 20) ? --->
    a) Executes add() function and passes 10 and 20 to the function
    b) Copies 10 and 20 to formal parameters 'a' and 'b'
    c) Function returns 30 which is returned to the function call add(10 , 20)

2) Finally add(10 , 20) is 30

3) What is the drawback of 'c' language function ? ---> It can add only integers if 'a' and 'b' are defined as integers (Lack of generic typing).

4) What is the advantage of python function ? ---> It can add any type of objects as long as the '+' operator is defined for them (Polymorphism).
'''

# Find outputs (Home work)

def f1():
    print('No-argument function')
def f1(x):
    print('Single argument function : ' , x)
def f1(x , y):
    print('Two argument function : ' , x , y)
def f1(x , y , z):
    print('Three argument function : ' , x , y , z)

f1(10 , 20 , 30) # Three argument function : 10 20 30
# f1(40 , 50) # Error because f1() missing 1 required positional argument: 'z'
# f1(60) # Error because f1() missing 2 required positional arguments: 'y' and 'z'
# f1() # Error because f1() missing 3 required positional arguments: 'x', 'y', and 'z'

# -----------------------------------------------------------------------------------------------------

'''
Write a function to test a number is prime (or) not.
'''

def prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input('Enter any integer number : '))
if n <= 0:
    print('Invalid input')
elif prime(n):
    print('Prime number')
else:
    print('Composite number')

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home work)

def disp(empno , ename , sal):
        print(F'Emp Number : {empno} \t Emp Name : {ename} \t Salary : {sal}')

disp(25 , 'Rama Rao' , 10000.0) # Emp Number : 25 	 Emp Name : Rama Rao 	 Salary : 10000.0
disp('Sita' , 20000.0 , 35) # Emp Number : Sita 	 Emp Name : 20000.0 	 Salary : 35

# -----------------------------------------------------------------------------------------------------

'''
Write a function to print number in words
'''

def words(n, units):
    a = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", 
         "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    b = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    res = ""
    if n >= 20:
        res = b[n // 10] + " " + a[n % 10]
    else:
        res = a[n]
    
    if n > 0:
        print(res, units, end=" ")

n = int(input('Enter any number (max : 999999999) : '))
if n == 0:
    print('Zero')
else:
    words(n // 10000000, "Crores")
    words((n // 100000) % 100, "Lakhs")
    words((n // 1000) % 100, "Thousand")
    words((n // 100) % 10, "Hundred")
    words(n % 100, "")
    print()

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home work)

def f1(a , b , c):
          print(F'a : {a} \t b : {b} \t c : {c}')

f1(a = 10 , b = 20 , c = 30) # a : 10 	 b : 20 	 c : 30
f1(25 , 10.8 , 'Hyd') # a : 25 	 b : 10.8 	 c : Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5) # a : 50.2 	 b : 40.7 	 c : 60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a : Cyb 	 b : Sec 	 c : Hyd
f1(c = 3 + 4j , a = True , b = None) # a : True 	 b : None 	 c : (3+4j)
f1(25 , c = 10.8 , b = 'Hyd') # a : 25 	 b : Hyd 	 c : 10.8
# f1(a = 100 , 200 , 300) # Error because positional argument follows keyword argument
# f1(True , None , b = 'Hyd') # Error because f1() got multiple values for argument 'b'
# f1(10 , 20 , x = 30) # Error because f1() got an unexpected keyword argument 'x'
# f1(10 , 20) # Error because f1() missing 1 required positional argument: 'c'

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home work)

def disp(empno , ename , sal):
        print(F'Emp Number : {empno:4} \t Emp Name : {ename:15} \t Salary : {sal}')

disp(25 , 'Rama Rao' , 10000.0) # Emp Number :   25 	 Emp Name : Rama Rao       	 Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp Number :   35 	 Emp Name : Sita            	 Salary : 20000.0
x = 'Rama Rao'
y = 30000.0
z = 20
disp(x , y , z) # Emp Number : Rama Rao 	 Emp Name : 30000.0        	 Salary : 20

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home work)

def f1(a , b , c):
    return a + b * c

print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8])) # 62
# print(f1([6 , 7 , 8])) # Error because f1() missing 2 required positional arguments: 'b' and 'c'
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # 16
print(f1(**{'c' : 2 , 'b' : 4 , 'a' : 6})) # 14
# print(f1({'c' : 2 , 'b' : 4 , 'a' : 6})) # Error because f1() missing 2 required positional arguments: 'b' and 'c'
print({**{'c' : 2 , 'b' : 4 , 'a' : 6}}) # {'c': 2, 'b': 4, 'a': 6}
# print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) # Error because f1() got an unexpected keyword argument 'x'

# -----------------------------------------------------------------------------------------------------

# Identify Error (Home work)

a = [10 , 20 , 15 , 5 , 12]
# print(sorted(reverse = True , a)) # Error because positional argument follows keyword argument
# print(sorted(a , rev = True)) # Error because sorted() got an unexpected keyword argument 'rev'
# print(25 , 10.8 , 'Hyd' , separator = '\t') # Error because print() got an unexpected keyword argument 'separator'
# print(25 , 10.8 , 'Hyd' , endofline = '\t') # Error because print() got an unexpected keyword argument 'endofline'
# print(25 , sep = '\t' , 10.8 , end = '\t' , 'Hyd') # Error because positional argument follows keyword argument