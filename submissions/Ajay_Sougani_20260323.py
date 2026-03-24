#  Find  outputs
def  f1():
		print('f1  Function')
		f2() # Error f2 not defined
def  f2():
		print('f2  function')
f1() # f1 function


#  Find  outputs
def   add(a , b):
        return  a + b 
#End  of  the  function
print(add(10 , 20))  #  print(30)
print(add('Hyder' , 'abad')) # (Hyderabad)
print(add(10.8 , 20.6)) # (31.4)
print(add(True , False)) # (1)
print(add(3 + 4j , 5 + 6j)) # (8+10j)
print(add(25 , 10.8)) # (35.8)
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # ([25, 10.8, 'Hyd', True, None, 3+4j, 'Sec'])
# print(add(10 , '20')) # Error unsupported operands

# Find  outputs 
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three  argument  function : 10 20 30
f1(40 , 50)  # Error f1() missing 1 required positional argument: 'z'
f1(60)  # error f1() missing 2 required positional arguments: 'y' and 'z'
f1() # Error f1() missing 3 required positional arguments: 'x', 'y', and 'z'

from math import floor
def   prime(n):   
	if  n < 2:
		return False
	else:
		div = floor(n/2)
		for i in range(2,div):
			if n%i==0:
				return False
	return True
n = int(input('Enter  any  integer  number  :  '))  
res = prime(n)
print(res)

# Find  outputs  
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) # Emp  Number  :  25 \t  Emp Name  : Rama Rao  \t  Salary  :  10000.0
disp('Sita' , 20000.0 , 35) # Emp  Number  :  Sita \t  Emp Name  :  20000.0 \t  Salary  :  35

# Find  outputs  
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) # a  :  10    \t  b  :  20 \t  c :  30
f1(25 , 10.8 , 'Hyd') # a  :  25    \t  b  :  10.8  \t  c :  'Hyd'
f1(b = 40.7 , a = 50.2 , c = 60.5) # a  :  50.2    \t  b  :  40.7  \t  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a  :  'Cyb'    \t  b  :  'Sec'  \t  c :  'Hyd'
f1(c = 3 + 4j , a = True , b = None) # a  :  True    \t  b  :  None  \t  c :  3+4j
f1(25 , c = 10.8 , b = 'Hyd') # a  :  25    \t  b  :  'Hyd'  \t  c :  10.8
# f1(a = 100 , 200 , 300)  #   Error
# f1(True , None , b = 'Hyd') # Error f1() got multiple values for argument 'b'
# f1(10 , 20 , x = 30) # error f1() got an unexpected keyword argument 'x'
# f1(10 , 20) # error f1() missing 1 required positional argument: 'c'

def  words(n , units):
	a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" , "Eleven" , "Twelve" , 
	        "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" , "Eightteen" , "Nineteen"]
	b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
           # 0     1          2              3            4             5            6              7               8              9
	#Write  if  statement  to  print  two  digit  number  in  words
	if n>9:
		print(b[n // 10], a[n % 10], units, end=" ")
	# Write  if  statement  to  print  units
	elif n> 0:
		print(a[n], units, end=" ")

n = int(input('Enter any number (max : 999999999)  : '))
if n>99999999:
	print("number is too large")
	exit()
else:
	words(n//10000000, "Crore")
	words(n//100000%100, "Lakh")
	words(n//1000%100,"Thosand")
	words(n//100%10, "Hundred")
	words(n%100, "")

# Find  outputs 
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Emp  Number : 25  \t  Emp  Name : 'Rama Rao'  \t  Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp  Number : 35  \t  Emp  Name : 'Sita'  \t  Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) # Emp  Number : 20  \t  Emp  Name : 'Rama Rao'  \t  Salary : 30000.0

#  Tricky  program
# Find  outputs 
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8])) # 62 
print(f1([6 , 7 , 8])) # error 
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # 16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) # 14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # error
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) # {'c': 2, 'b':4, 'a': 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) # error unexpected keyword argument 'x

# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) # positional cannot  follow the keyword argument
print(sorted(a , rev = True)) # sorted function doesn't hqve argument rev
print(25 , 10.8 , 'Hyd' , separator = '\t') # seperator is not a valid argument for print function
print(25 , 10.8 , 'Hyd' , endofline = '\t') # endofline is not a calid argument for the print function
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #  positional arguments cannot follow the keyword arguments

