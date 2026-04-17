#1
#Find outputs
def f1():
    print('f1 Function') #fi function
    f2()
def f2():
    print('f2 function') #f2 function
f1() #This call initiates the execution of both print statements above



#2
#Find outputs (Homework)
def add(a, b):
    return a + b
print(add(10, 20)) # 30
print(add('Hyder', 'abad')) # 'Hyderabad'
print(add(10.8, 20.6)) # 31.4
print(add(True, False)) # 1 (True is 1, False is 0)
print(add(3 + 4j, 5 + 6j)) # (8+10j)
print(add(25, 10.8)) # 35.8
print(add([25, 10.8, 'Hyd'], [True, None, 3+4j, 'Sec'])) # [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
# print(add(10, '20')) # Error as a int object can't be added with a string object



#3
#Find outputs (Home work)
def f1():
    print('No-argument function')
def f1(x):
    print('Single argument function :', x)
def f1(x, y):
    print('Two argument function :', x, y)
def f1(x, y, z):
    print('Three argument function :', x, y, z)

f1(10, 20, 30) # Works: 'Three argument function : 10 20 30'
# f1(40, 50)   # Error as 1 required positional argument: 'z' is missing
# f1(60)       # Error as 2 required positional arguments: 'y' and 'z' are missing
# f1()         # Error as 3 required positional arguments: 'x', 'y', and 'z' are missing



#4
'''
Write a function to test a number is prime (or) not.
1) What is a prime number? ---> A number without divisors except 1 and itself

2)  Let input be 25
    What is the range of divisors? ---> i = 2 , 3 , 4 , 5 , 6 , ..... 12

3)  Let input be 11
    What is the range of divisors? ---> i = 2 , 3 , 4 , 5

4) What action to be made if 'i' is not a divisor of input number? ---> Move to the next element of range object

5) What action to be made if 'i' is a divisor of input number? ---> return False

6) What action to be made if there are no divisiors to input number? ---> return True outside the loop
'''
'''
def prime(n):   
    return True when 'n' is prime number and False otherwise
'''
'''
1)  prime(25) --->  
    How many times is for loop executed? ---> 4 times

2)  prime(11) --->  
    How many times is for loop executed? ---> 2 times

3)  prime(2) ---> 
    How many times is for loop executed? ---> 0 times

4)  prime(49) ---> 
    How many times is for loop executed? ---> 6 times 
'''
def prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input('Enter any integer number : '))
if n < 1:
    print('Invalid input')
elif prime(n):
    print('Prime number')
else:
    print('Composite number')



#5
#Find outputs (Home work)
def disp(empno, ename, sal):
    print(f'Emp Number : {empno} \t Emp Name : {ename} \t Salary : {sal}')
disp(25, 'Rama Rao', 10000.0) # Emp Number : 25 ... Rama Rao ... 10000.0
disp('Sita', 20000.0, 35)      # Emp Number : Sita ... 20000.0 ... 35 (Positional mismatch)



#6
'''
Write a function to print number in words

Let input be 123456789
What is the output? ---> Tweleve crores thirty four lakhs fifty six thousand seven hundred eighty nine

1) a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" ,   "Eleven" , "Twelve" ,
           "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" ,  "Eightteen" , "Nineteen"]

2) b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
        0     1       2          3          4         5         6          7          8           9

3)  How to print 92 in words? ---> b[92 // 10] and a[92 % 10] = b[9] and a[2]
    How to print 50 in words? ---> b[50 // 10] and a[50 % 10] = b[5] and a[0]

4)  How to print 14 in words? ---> a[14]
    How to print 4 in words? ---> a[4]

5)  How to obtain crores part from 123456789 ? ---> 123456789 // 10000000 = 12
    How to obtain lakhs part from 123456789 ? ---> 123456789 // 100000 % 100 = 1234 % 100 = 34
    How to obtain thousands part from 123456789 ? ---> 123456789 // 1000 % 100 = 123456 % 100 = 56
    How to obtain hundreds part from 123456789 ? ---> 123456789 // 100 % 10 = 1234567 % 10 = 7
    How to obtain last two digits of the number ? ---> 123456789 % 100 = 89
'''
'''
def words(n , units):
     a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" , "Eleven" , "Twelve" , 
            "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" , "Eightteen" , "Nineteen"]
     b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
            0     1          2              3            4             5            6              7               8              9
    Write if statement to print two digit number in words
    Write if statement to print units
'''
'''
1) words(92 , "Crores") ---> Ninety two crores

2) words(50 , "Lakhs") ---> Fifty Lakhs

3) words(14 , "Thousands") ---> Fourteen Thousand

4) words(7 , "Hundreds") ---> Seven Hundred

5) words(0 , "Crores") ---> Nothing becoz 1st argument is 0
'''
def words(n, units):
    if n == 0: return ""
    a = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", 
         "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    b = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    res = ""
    if n < 20:
        res = a[n]
    else:
        res = b[n // 10] + " " + a[n % 10]
    
    if res:
        print(f"{res.strip()} {units}", end=" ")

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



#7
#Find outputs (Home work)
def f1_7(a, b, c):
    print(f'a : {a} \t b : {b} \t c : {c}')
f1_7(a=10, b=20, c=30) # a:10 b:20 c:30
f1_7(25, 10.8, 'Hyd')  # a:25 b:10.8 c:Hyd
f1_7(b=40.7, a=50.2, c=60.5) # a:50.2 b:40.7 c:60.5
f1_7(c='Hyd', b='Sec', a='Cyb') # a:Cyb b:Sec c:Hyd
f1_7(c=3+4j, a=True, b=None) # a:True b:None c:(3+4j)
f1_7(25, c=10.8, b='Hyd') # a:25 b:Hyd c:10.8
# f1_7(a=100, 200, 300) # Error as positional argument follows keyword argument
f1_7(True, None, b='Hyd') # Error as f1_7() got multiple values for argument 'b'
# f1_7(10, 20, x=30) # Error as unexpected keyword argument 'x'
# f1_7(10, 20) # Error as there is one missing required positional argument: 'c'



#8
#Find outputs (Home work)
def disp_8(empno, ename, sal):
    print(f'Emp Number : {empno:4} \t Emp Name : {ename:15} \t Salary : {sal}')
disp_8(25, 'Rama Rao', 10000.0)
disp_8(ename='Sita', sal=20000.0, empno=35)
x, y, z = 'Rama Rao', 30000.0, 20
disp_8(x, y, z) # Output: Emp Number : Rama Rao (Note: formatting :4 might cause alignment shift for strings)



#9
#Tricky program
def f1_9(a, b, c):
    return a + b * c
print(f1_9(3, 4, 5)) # 3 + 20 = 23
print(f1_9(*[6, 7, 8])) # 6 + 56 = 62
# print(f1_9([6, 7, 8])) # Error as b and c are missing
print(f1_9(*{1: 2, 3: 4, 5: 6})) # a=1, b=3, c=5 -> 1 + 15 = 16
print(f1_9(**{'c': 2, 'b': 4, 'a': 6})) # 6 + 4*2 = 14
# print(f1_9({'c': 2, 'b': 4, 'a': 6})) # Error improper arguments given
print({**{'c': 2, 'b': 4, 'a': 6}}) # {'c': 2, 'b': 4, 'a': 6}
# print(f1_9(**{'c': 2, 'a': 4, 'x': 6})) # Error as no argument 'x' is defined earlier



#10
#Identify Error (Home work)
a = [10, 20, 15, 5, 12]
# print(sorted(reverse=True, a)) # Error as Positional arg 'a' after keyword arg
# print(sorted(a, rev=True)) # Error as 'rev' is not a valid argument (should be 'reverse')
# print(25, 10.8, 'Hyd', separator='\t') # Error as'separator' should be 'sep'
# print(25, 10.8, 'Hyd', endofline='\t') # Error as 'endofline' should be 'end'
# print(25, sep='\t', 10.8, end='\t', 'Hyd') # Error as Positional arg '10.8' after keyword arg 'sep'