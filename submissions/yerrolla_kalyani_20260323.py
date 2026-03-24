#  Find  outputs
def  f1():
		print('f1  Function')
		f2()
def  f2():
		print('f2  function')
f1()# f1  Function <nextline> f2  function <nextline> None
 #  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  print(30)
print(add('Hyder' , 'abad'))#Hyderabad
print(add(10.8 , 20.6))#31.2
print(add(True , False))#1
print(add(3 + 4j , 5 + 6j))#8+10j
print(add(25 , 10.8))#35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))#error no equal elements in  two positional parameters
print(add(10 , '20'))#error,cannot cancat  int and string




# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')# No-argument  function
def  f1(x):
	print('Single  argument  function  : ' , x)#Single  argument  function  :60
def  f1(x , y):
	print('Two  argument  function : ' , x , y)#Two  argument  function : 40 , 50
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)#Three  argument  function :10 , 20 , 30
f1(10 , 20 , 30)
f1(40 , 50)  
f1(60)  
f1()



''': Write   a  function  to  test  a  number  is  prime  (or)  not.
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
    prime=True 
    for i in range(2,n//2,1):
        if n%i!=0 :
            prime
        else:
            prime=False
    if prime:
        return "prime number"

    else:
        return"NOt a prime number"
x=prime(n=int(input("Enter a number:")))
print(x)

		
	#return  True  when 'n'  is  prime  number  and  False  otherwise
'''
1) prime(25)  --->  
    How  many  times  is  for  loop  executed ?  --->  4 times 

2) prime(11) --->  
    How  many  times  is  for  loop  executed ?  --->4  

3) prime(2) ---> 
    How  many  times  is  for  loop  executed ?  ---> 1

4) prime(49) ---> 
    How  many  times  is  for  loop  executed ?  ---> 6 
'''



# # Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)#Emp  Number  :  25 \t  Emp Name  :  Rama rao \t  Salary  : 10000.0
disp('Sita' , 20000.0 , 35)#Emp  Number  : Sita\t  Emp Name  :  20000.0 \t  Salary  : 35



# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)#a  :  10    \t  b  : 20  \t  c :  30
f1(25 , 10.8 , 'Hyd')#a  :  25    \t  b  :  10.8  \t  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)#a  :  50.2    \t  b  :  40.7  \t  c :  Cyb
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#a  :  Cyb    \t  b  :  Sec  \t  c : Hyd
f1(c = 3 + 4j , a = True , b = None)#a  :  True    \t  b  :  None  \t  c : 3+4j
f1(25 , c = 10.8 , b = 'Hyd')#a  :  25    \t  b  :  Hyd  \t  c :  10.8
f1(a = 100 , 200 , 300)  #   Error,positional parameters  are not valid after the keyword parameters  
f1(True , None , b = 'Hyd')#a  :  True    \t  b  :  Hyd  \t  c : None
f1(10 , 20 , x = 30)#error 
f1(10 , 20)#error 





# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)#Emp  Number : 25  \t  Emp  Name : Rama rao  \t  Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#Emp  Number :35  \t  Emp  Name : Sita  \t  Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)#Emp  Number : Rama rao  \t  Emp  Name : 30000.0  \t  Salary : 20


#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#23
print(f1(*[6 , 7 , 8]))##62
print(f1([6 , 7 , 8]))#62
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))#12
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#12
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})#{'c' : 2 , 'b' :  4 , 'a' : 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))#error c is not given
# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))#error the for mal aguments are not accepted after the  keyword argument
print(sorted(a , rev = True))#there is no rev keyword in it is reverse
print(25 , 10.8 , 'Hyd' , separator = '\t')# error  it should be sep not separator  
print(25 , 10.8 , 'Hyd' , endofline = '\t')# error it should be end no endofline
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')#error ,10.8  positional parameter  it should not defined aftr the keyword parameters 