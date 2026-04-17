#  Find  outputs
def  f1():
		print('f1  Function') #'f1 Function'
		f2()  #Error
def  f2():
		print('f2  function') #'f2 function'
f1() #Error


#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  print(30) #30
print(add('Hyder' , 'abad')) #Hyderabad
print(add(10.8 , 20.6)) #31.4
print(add(True , False)) #1
print(add(3 + 4j , 5 + 6j)) # 8 + 10j
print(add(25 , 10.8)) #35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) #[25 , 10.8 , 'Hyd' , True , None , 3+4j , 'Sec']
print(add(10 , '20')) #Error as operand 1 is non sequence operand 2 should be also non sequence only.

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z) 
f1(10 , 20 , 30) #Three argument function : 10 , 20 , 30
f1(40 , 50)  
f1(60)  
f1()

# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)

#outputs
Emp Number : 25  Emp Name : 'Rama Rao'  Salary : 10000.0
Emp Number : 'Sita'  Emp Name : 20000.0  Salary : 35







# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) # a  :  10  b  :  20  c  :  30
f1(25 , 10.8 , 'Hyd') #a  :  25  b  :  10.8   c  :  'Hyd'
f1(b = 40.7 , a = 50.2 , c = 60.5) #a  :  50.2  b  :  40.7  c  :  60.5Syntax 
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a  :  'Cyb'  b  :  'Sec'  c  :  'Hyd'
f1(c = 3 + 4j , a = True , b = None) #a  :  True   b  :  None   c  : (3+4j)
f1(25 , c = 10.8 , b = 'Hyd') # a  :  25  b  :  'Hyd'  c  :  10.8
f1(a = 100 , 200 , 300)  #   Error
f1(True , None , b = 'Hyd') #Type Error
f1(10 , 20 , x = 30) #Type Error
f1(10 , 20) #Type error


# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) #EMP Number : 25    Emp Name : Rama Rao    Salary : 10000.0   
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) #Emp Number :  35   Emp Name :  Sita   Salary :  20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) #Emp Number :  20   Emp Name  : Rama Rao  Salary :  30000.0



#  Tricky  program
# Find  outputs (Home  work)

# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8]) #
print(f1([6 , 7 , 8])) #Error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) #16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) #Error
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) #Error
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) #Error
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) #Error


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) #Error because positional argument is not permitted with key word argument.
print(sorted(a , rev = True)) # Error because sorted function has reverse argument but not rev.  
print(25 , 10.8 , 'Hyd' , separator = '\t') # print fuction does not have separator argument it is having sep argument.
print(25 , 10.8 , 'Hyd' , endofline = '\t') # print function does not have endofline argument it is having end argument
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #Syntax Error.



def   prime(n):   
	for i in range(2,(n+1//2)):
		if(n%i!=0):
			continue
		else:
			return False
	return True	
		
n = int(input('Enter  any  integer  number  :  '))  
if  (n<2):
	print('Invalid  input')
elif  prime(n):
	print('Prime  number')
else:
	print('Composite  number')













