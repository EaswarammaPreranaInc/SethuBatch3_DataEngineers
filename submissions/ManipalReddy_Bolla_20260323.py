#  Find  outputs
def  f1():
		print('f1  Function')#f1 function
		f2()
def  f2():
		print('f2  function')#f3 function
f1()


#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  print(30)
print(add('Hyder' , 'abad'))#print(Hyderabad)
print(add(10.8 , 20.6))#print(31.4)
print(add(True , False))#print(1)
print(add(3 + 4j , 5 + 6j))#print(8+10j)
print(add(25 , 10.8))#print(35.8)
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))#print([25 , 10.8 , 'Hyd',True , None , 3+4j , 'Sec'])
print(add(10 , '20'))#error


# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)#Three argument fuction : 10 20 30
f1(40 , 50) #error
f1(60)  #error
f1()#error


def prime(n):
    if n < 2:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False 
    return True 

n = int(input('Enter any integer number: '))
if n < 1:
    print('Invalid input')
elif prime(n):
    print('Prime number')
else:
    print('Composite number')
	
'''
output
Enter any integer number: 9
Composite number
Enter any integer number: 5
Prime number
Enter any integer number: 0
Invalid input
'''


# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)#Emp Number : 25 <tab> Emp Name : Rama Rao <tab> Salary : 10000.0 
disp('Sita' , 20000.0 , 35)#Emp Number : Sita <tab> Emp Name : 20000.0 <tab> Salary : 35


def words(n, units):
    a = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
         "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    b = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n == 0:
        return ""

    res = ""

    if n < 20:
        res = a[n]
    else:
        res = b[n // 10] + (" " + a[n % 10] if n % 10 != 0 else "")

    return res + " " + units + " "


n = int(input('Enter any number (max : 999999999): '))

if n == 0:
    print('Zero')
else:
    output = ""
    output += words(n // 10000000, "Crores")
    output += words((n // 100000) % 100, "Lakhs")
    output += words((n // 1000) % 100, "Thousand")
    output += words((n // 100) % 10, "Hundred")

    output += words(n % 100, "")

    print(output.strip())


# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)#a : 10 <tab> b : 20 <tab> c : 30 
f1(25 , 10.8 , 'Hyd')#a : 25 <tab> b : 10.8 <tab> c : Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)#a  :  50.2        b  :  40.7      c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#a  :  Cyb         b  :  Sec       c :  Hyd
f1(c = 3 + 4j , a = True , b = None)#a  :  True        b  :  None      c :  3+4j
f1(25 , c = 10.8 , b = 'Hyd')#a  :  25          b  :  Hyd       c :  10.8
f1(a = 100 , 200 , 300)  #   Error
f1(True , None , b = 'Hyd')#error
f1(10 , 20 , x = 30)#error due to x 
f1(10 , 20)#error


# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)#Emp  Number :   25        Emp  Name : Rama Rao            Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#Emp  Number :   35        Emp  Name : Sita                Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)#Emp  Number : Rama  Rao           Emp  Name :         30000.0     Salary : 20


#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#23
print(f1(*[6 , 7 , 8]))#62
print(f1([6 , 7 , 8]))#error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))#14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#error
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})#{'c': 2, 'b': 4, 'a': 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))#error due to x


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))#error
print(sorted(a , rev = True))#error
print(25 , 10.8 , 'Hyd' , separator = '\t')#error
print(25 , 10.8 , 'Hyd' , endofline = '\t')#error
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')#error 

