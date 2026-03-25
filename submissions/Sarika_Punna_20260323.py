#  Find  outputs
def  f1():
		print('f1  Function')
		f2()
def  f2():
		print('f2  function')
f1()
#output:
'''
f1 function
f2 function
'''


#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  print(30)
print(add('Hyder' , 'abad'))
print(add(10.8 , 20.6))
print(add(True , False))
print(add(3 + 4j , 5 + 6j))
print(add(25 , 10.8))
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))
print(add(10 , '20'))#error
'''
output
Hyderabad
31.4
1
8+10j
[25 , 10.8 , 'Hyd',True , None , 3+4j , 'Sec']
'''


# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
f1(40 , 50)  
f1(60)  
f1()
'''
Three  argument  function : 10 , 20 , 30
Two  argument  function :40 , 50
Single  argument  function  :60
No-argument  function
'''


#Write   a  function  to  test  a  number  is  prime  (or)  not.

def prime(a):
    if(a==2):
        return True
    elif(a==1):
        return False
    else:
        c=1
        for i in range(2,a//2):
            if(a%i==0):
                c=0
                return False
                break
        if(c==1):
            return True
a=int(input("Enter number"))
print(prime(a))


# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)
'''
Emp  Number  : 25 \t  Emp Name  : RamaRao \t  Salary  :  10000.0
Emp  Number  : Sita \t  Emp Name  : 20000.0 \t  Salary  :  25
'''

#Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)#a  :10    \t  b  :20\t  c :  30
f1(25 , 10.8 , 'Hyd')#a  : 25   \t  b  : 10.8  \t  c : Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)#a  :  50.2    \t  b  :  40.7  \t  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#a  :  Hyd    \t  b  :  "Sec"  \t  c :  'Cyb'
f1(c = 3 + 4j , a = True , b = None)#a  :  True    \t  b  :  Hyd  \t  c :  3+4j
f1(25 , c = 10.8 , b = 'Hyd')#a  :  25    \t  b  :  Hyd  \t  c :  10.8
f1(a = 100 , 200 , 300)  #   Error
f1(True , None , b = 'Hyd')#a  :  True \t  b  :  Hyd  \t  c : None
f1(10 , 20 , x = 30)#a  :  10   \t  b  :  20  \t  c :  30
f1(10 , 20)##a  :  10   \t  b  :  20  \t  c :  


#Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)#Emp  Number  : 25 \t  Emp Name  : RamaRao \t  Salary  :  10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#Emp  Number  : 35 \t  Emp Name  : Sita \t  Salary  :  20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)#Emp  Number  : RamaRao \t  Emp Name  : 30000.0 \t  Salary  :  20



#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#60
print(f1(*[6 , 7 , 8]))#62
print(f1([6 , 7 , 8]))#error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))#26
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})#{'c' : 2 , 'b' :  4 , 'a' : 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))#error


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))#error
print(sorted(a , rev = True))#[20, 15, 12, 10, 5]
print(25 , 10.8 , 'Hyd' , separator = '\t')#error
print(25 , 10.8 , 'Hyd' , endofline = '\t')#error
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')#error


'''
Write  a  function  to  print  number  in  words
Let  input  be  123456789
What  is  the  output ?  --->  Tweleve  crores  thirty  four  lakhs  fifty  six  thousand  seven  hundred  eighty  nine
'''

def  words(n , units):
    a = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine" ,"Ten","Eleven","Twelve" ,"Thirteen","Fourteen","Fifteen","Sixteen", "Seventeen","Eightteen","Nineteen"]
    b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
    p=a[n]+" "+units if n<=20 else b[n//10]+" "+a[n%10]+" "+units
    return p
n = int(input('Enter any number (max : 999999999)  : '))
s=""
if  n == 0:
	printf('Zero')
else:
    c=n//10000000
    if(c!=0):
        s=s+words(c,"crores")+" "
    d=n // 100000 % 100
    if(d!=0):
        s=s+words(d,"lakhs")+" "
    e=n // 1000 % 100
    if(e!=0):
        s=s+words(e,"thousand")+" "
    f=n// 100 % 10
    if(f!=0):
        s=s+words(f,"hundred")+" "
    g=n % 100 
    if(g!=0):
        s=s+words(g,"")
print(s)
