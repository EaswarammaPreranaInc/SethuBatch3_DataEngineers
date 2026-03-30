# Find outputs

def f1():
    print('f1 Function')
    f2()

def f2():
    print('f2 function')

f1()
# f1 Function
# f2 function


# Find outputs (Home work)

def add(a , b):
    return a + b
# End of the function

print(add(10 , 20))                      # 30
print(add('Hyder' , 'abad'))             # Hyderabad
print(add(10.8 , 20.6))                  # 31.4
print(add(True , False))                 # 1
print(add(3 + 4j , 5 + 6j))              # (8+10j)
print(add(25 , 10.8))                    # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))  
# [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']

print(add(10 , '20'))                    # error



# Find  outputs (Home  work)

def f1():
    print('No-argument function')

def f1(x):
    print('Single argument function : ', x)

def f1(x , y):
    print('Two argument function : ', x , y)

def f1(x , y , z):
    print('Three argument function : ', x , y , z)

f1(10 , 20 , 30)    # Three argument function :  10 20 30
f1(40 , 50)         # error
f1(60)              # error
f1()                # error


'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5 , 6 , .....  12

3) Let  input   be  11
    What  is   the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  --->  Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  ---> return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? --->  return  True  outside  the  loop
'''
def   prime(n):   
	return  True  when 'n'  is  prime  number  and  False  otherwise
'''
1) prime(25)  --->  
    How  many  times  is  for  loop  executed ?  --->  

2) prime(11) --->  
    How  many  times  is  for  loop  executed ?  --->  

3) prime(2) ---> 
    How  many  times  is  for  loop  executed ?  ---> 

4) prime(49) ---> 
    How  many  times  is  for  loop  executed ?  --->  
'''
n = int(input('Enter  any  integer  number  :  '))  
if  n<1:
	print('Invalid  input')
elif  prime(n):
	print('Prime  number')
else:
	print('Composite  number')

# Find  outputs  (Home  work)

def f1(a , b , c):
    print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function

f1(a = 10 , b = 20 , c = 30)             # a  :  10    	b  :  20  	c :  30
f1(25 , 10.8 , 'Hyd')                    # a  :  25    	b  :  10.8  	c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)       # a  :  50.2  	b  :  40.7  	c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')    # a  :  Cyb   	b  :  Sec  	c :  Hyd
f1(c = 3 + 4j , a = True , b = None)     # a  :  True  	b  :  None  	c :  (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')            # a  :  25    	b  :  Hyd  	c :  10.8
f1(a = 100 , 200 , 300)                  # error
f1(True , None , b = 'Hyd')              # error
f1(10 , 20 , x = 30)                     # error
f1(10 , 20)                              # error


# Find  outputs (Home  work)

def disp(empno , ename , sal):
    print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function

disp(25 , 'Rama Rao' , 10000.0)          
# Emp  Number :   25  	Emp  Name : Rama Rao       	Salary : 10000.0

disp(ename = 'Sita' , sal = 20000.0 , empno = 35)  
# Emp  Number :   35  	Emp  Name : Sita           	Salary : 20000.0

x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)                          
# Emp  Number : Rama  Rao  	Emp  Name : 30000.0       	Salary : 20


# Tricky  program
# Find  outputs (Home  work)

def f1(a , b , c):
    return a + b * c
#end  of  the  function

print(f1(3 , 4 , 5))                     # 23
print(f1(*[6 , 7 , 8]))                  # 62
print(f1([6 , 7 , 8]))                   # error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))      # 23
print(f1(**{'c' : 2 , 'b' : 4 , 'a' : 6}))  # 14
print(f1({'c' : 2 , 'b' : 4 , 'a' : 6}))    # error
print({**{'c' : 2 , 'b' : 4 , 'a' : 6}})    # {'c': 2, 'b': 4, 'a': 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))  # error


# Identify  Error (Home  work)

a = [10 , 20 , 15 , 5 , 12]

print(sorted(reverse = True , a))        # error
print(sorted(a , rev = True))            # error
print(25 , 10.8 , 'Hyd' , separator = '\t')  # error
print(25 , 10.8 , 'Hyd' , endofline = '\t')  # error
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')  # error