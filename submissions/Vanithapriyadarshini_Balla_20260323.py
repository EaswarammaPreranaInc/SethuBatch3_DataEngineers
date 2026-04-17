'''#  Find  outputs
def  f1():
		print('f1  Function')
		f2()
def  f2():
		print('f2  function')
f1() # f1 function<nl> f2 function

#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  30
print(add('Hyder' , 'abad')) # Hyderabad
print(add(10.8 , 20.6)) # 31.4
print(add(True , False)) # 1
print(add(3 + 4j , 5 + 6j)) # 8+10j
print(add(25 , 10.8)) # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # [25 , 10.8 , 'Hyd', True , None , 3+4j , 'Sec'] 
print(add(10 , '20')) # Error

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three  argument  function : 10 20 30 
f1(40 , 50)  # Two  argument  function : 40 50
f1(60)  # Single  argument  function  : 60
f1() # No-argument  function

# Write   a  function  to  test  a  number  is  prime  (or)  not.
num=int(input("Enter number : "))
def prime(num):
	if num<=1:
		return 'Invalid input'
	elif num>1:
		for i in range(2,num//2):
			if num%i==0:
				return 'Composite Prime'
	return 'Prime Number'
print(prime(num))

# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) # Emp Number : 25      Emp Name : Rama Rao     Salary : 10000.0   
disp('Sita' , 20000.0 , 35) #  Emp Number : 'Sita'     Emp Name : 20000.0     Salary : 35

# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) # a : 10   b : 20  c : 30
f1(25 , 10.8 , 'Hyd') #  a : 25    b : 10.8    c : Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5) # a : 50.2   b : 40.7    c : 60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a : Cyb     b : Sec     c : Hyd
f1(c = 3 + 4j , a = True , b = None) # a : True     b : None    c : 3+4j
f1(25 , c = 10.8 , b = 'Hyd') # a : 25  b : Hyd     c : 10.8
#f1(a = 100 , 200 , 300)  #   Error, bca KA,PA is not valid 
#f1(True , None , b = 'Hyd') # a : True  , Error 
#f1(10 , 20 , x = 30) # Error, bcz no x formal parameter
#f1(10 , 20) # Error, actual parameters are 2 and formal are 3 unmatched

# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Emp Number : 25   Emp Name : 'Rama Rao    Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp  Number :   35        Emp  Name : Sita 
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) # Emp  Number : Rama  Rao           Emp  Name :         30000.0     Salary : 20

#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8])) # 62
#print(f1([6 , 7 , 8])) # Error,bcz args doesnt match
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # 16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) # 14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) #Error, unmatched args
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) # {'c' : 2 , 'b' :  4 , 'a' : 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) # Error, bcz there is no 'x' parameter

# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a)) # Error, (bcz KA,PK)) not supported
print(sorted(a , rev = True)) # Error, bcz there is no rev keyword arg for sorted func
print(25 , 10.8 , 'Hyd' , separator = '\t') # Error, bcz there is no separator keyword arg for print()
print(25 , 10.8 , 'Hyd' , endofline = '\t') # Error, bcz there is no endofline keyword arg for print()
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') # Erroe, bcz KA,PK are not supported, 10.8 and Hyd are culprits 
'''

# Write  a  function  to  print  number  in  words

n=eval(input("Enter numerical value : "))
units=input("Units")
def words(n, units):
    a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" ,   "Eleven" , "Twelve" ,
           "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" ,  "Eightteen" , "Nineteen"]
    b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
    if n==0:
       print("Zero")
    else:
        if n<20:
           print(a[n])
words(n,units)
          

    