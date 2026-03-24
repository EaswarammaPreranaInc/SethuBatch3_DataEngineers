#  Find  outputs
def f1():
    print('f1  Function')   # f1  Function
    f2()
def f2():
    print('f2  function')   # f2  function
f1()


#  Find  outputs
def add(a , b):
    return a + b
print(add(10 , 20))                 # 30
print(add('Hyder' , 'abad'))       # Hyderabad
print(add(10.8 , 20.6))            # 31.4
print(add(True , False))           # 1
print(add(3 + 4j , 5 + 6j))        # (8+10j)
print(add(25 , 10.8))              # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))  
# [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))              # TypeError



#  Find  outputs
def f1():
    print('No-argument function')
def f1(x):
    print('Single argument function : ', x)
def f1(x , y):
    print('Two argument function : ', x , y)
def f1(x , y , z):
    print('Three argument function : ', x , y , z)
f1(10 , 20 , 30)   # Three argument function :  10 20 30
f1(40 , 50)        # TypeError
f1(60)             # TypeError
f1()               # TypeError


Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5 , 6 , .....  12

3) Let  input   be  11
    What  is   the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5
#Program:

def prime(n):
    if n <= 1:
        return False
    for i in range(2 , n//2 + 1):
        if n % i == 0:
            return False
    return True


#  Find  outputs
def disp(empno , ename , sal):
    print(F'Emp Number : {empno} \t Emp Name : {ename} \t Salary : {sal}')
disp(25 , 'Rama Rao' , 10000.0)
# Emp Number : 25 	 Emp Name : Rama Rao 	 Salary : 10000.0
disp('Sita' , 20000.0 , 35)
# Emp Number : Sita 	 Emp Name : 20000.0 	 Salary : 35

''
Write  a  function  to  print  number  in  words

Let  input  be  123456789
What  is  the  output ?  --->  Tweleve  crores  thirty  four  lakhs  fifty  six  thousand  seven  hundred  eighty  nine
'''
#Program:

def words(n , units):
    a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" ,
         "Ten" , "Eleven" , "Twelve" , "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" ,
         "Seventeen" , "Eighteen" , "Nineteen"]
    b = ["" , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" ,
         "Seventy" , "Eighty" , "Ninety"]
    if n == 0:
        return
    if n < 20:
        print(a[n], units, end=" ")
    else:
        print(b[n // 10], a[n % 10], units, end=" ")
n = int(input('Enter any number (max : 999999999) : '))
if n == 0:
    print('Zero')
else:
    words(n // 10000000 , "Crores")      # Crores part
    words(n // 100000 % 100 , "Lakhs")   # Lakhs part
    words(n // 1000 % 100 , "Thousand")  # Thousands part
    words(n // 100 % 10 , "Hundred")     # Hundreds part
    words(n % 100 , "")                  # Last two digits
    print()



# Find  outputs  (Home  work)
def f1(a , b , c):
    print(F'a : {a} \t b : {b} \t c : {c}')
f1(a = 10 , b = 20 , c = 30)    # a : 10 	 b : 20 	 c : 30
f1(25 , 10.8 , 'Hyd')   # a : 25 	 b : 10.8 	 c : Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)      # a : 50.2 	 b : 40.7 	 c : 60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')       # a : Cyb 	 b : Sec 	 c : Hyd
f1(c = 3 + 4j , a = True , b = None)    # a : True 	 b : None 	 c : (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')       # a : 25 	 b : Hyd 	 c : 10.8
f1(a = 100 , 200 , 300)      # SyntaxError
f1(True , None , b = 'Hyd')  # TypeError
f1(10 , 20 , x = 30)         # TypeError
f1(10 , 20)                  # TypeError



# Find  outputs (Home  work)
def disp(empno , ename , sal):
    print(F'Emp Number : {empno:4} \t Emp Name : {ename:15} \t Salary : {sal}')
disp(25 , 'Rama Rao' , 10000.0)     # Emp Number :   25 	 Emp Name : Rama Rao      	Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)   # Emp Number :   35 	 Emp Name : Sita          	Salary : 20000.0
x = 'Rama Rao'
y = 30000.0
z = 20
disp(x , y , z)     # Emp Number : Rama Rao 	 Emp Name : 30000.0      	Salary : 20


# Find  outputs (Home  work)
def f1(a , b , c):
    return a + b * c
print(f1(3 , 4 , 5))                 # 23
print(f1(*[6 , 7 , 8]))              # 62
print(f1([6 , 7 , 8]))               # TypeError
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))  # 13
print(f1(**{'c' : 2 , 'b' : 4 , 'a' : 6}))  # 14
print(f1({'c' : 2 , 'b' : 4 , 'a' : 6}))    # TypeError
print({**{'c' : 2 , 'b' : 4 , 'a' : 6}})    # {'c': 2, 'b': 4, 'a': 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))  # TypeError



# Identify  Error (Home  work
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))        # SyntaxError
print(sorted(a , rev = True))            # TypeError
print(25 , 10.8 , 'Hyd' , separator = '\t')   # TypeError
print(25 , 10.8 , 'Hyd' , endofline = '\t')   # TypeError
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')  # SyntaxError