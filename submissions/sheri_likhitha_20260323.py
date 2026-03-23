#  Find  outputs
def  f1():
		print('f1  Function')
		f2()	
def  f2():
		print('f2  function')
f1()		#f1 function
		#None



#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  print(30)
print(add('Hyder' , 'abad'))	#Hyderabad
print(add(10.8 , 20.6))		#31.4
print(add(True , False))	#1+0=1
print(add(3 + 4j , 5 + 6j))	#8+10j
print(add(25 , 10.8))		#35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))	#[25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))	#error




# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')	#skipped
def  f1(x):
	print('Single  argument  function  : ' , x)	#skipped
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)	#Three argument function : 10,20,30
f1(10 , 20 , 30)
f1(40 , 50)  
f1(60)  
f1()
#multiple functions with same name always excutes the last function 



# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)	#Emp  Number  : 25 \t  Emp Name  :  Rama Rao \t  Salary  : 10000.0
disp('Sita' , 20000.0 , 35)		#Emp  Number  :  Sita \t  Emp Name  :  20000.0 \t  Salary  :  35




# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)	#a  :  10    b  :  20   c :  30
f1(25 , 10.8 , 'Hyd')		#a  :  25    b  :  10.8 c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)	#a  :  50.2    b  :  40.7   c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')	#a  :  Cyb     b  :  Sec    c :  Hyd
f1(c = 3 + 4j , a = True , b = None)	#a  :  True    b  :  None   c :  (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')		#a  :  25      b  :  Hyd    c :  10.8
f1(a = 100 , 200 , 300)  #   Error
f1(True , None , b = 'Hyd')		#error
f1(10 , 20 , x = 30)			#error
f1(10 , 20)				#error




# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)		#Emp  Number : 25   Emp  Name :Rama Rao     Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)   #Emp  Number : 35   Emp  Name : Sita    Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)		#Emp  Number : Rama  Rao     Emp  Name :30000.0     Salary : 20




#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))	#23
print(f1(*[6 , 7 , 8]))	#62
print(f1([6 , 7 , 8]))	#error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))	#16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) #!4
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))	#error
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})	#{'c': 2, 'b': 4, 'a': 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))	#error





# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) #error
print(sorted(a , rev = True))	   #error
print(25 , 10.8 , 'Hyd' , separator = '\t') #error
print(25 , 10.8 , 'Hyd' , endofline = '\t')  #error
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #error




def words(n,units):
    a=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
       "Eleven","Tweleve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    b=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    if n==0:
        return
    if n<20:
        print(a[n],end=" ")
    else:
        print(b[n//10],a[n%10],end=" ")
    print(units,end=" ")
n=int(input("Enter any number: "))
if n==0:
    print("Zero")
else:
    words(n//10000000, "crores")
    words((n//100000)%100, "lakhs")
    words((n//1000)%100, "Thousand")
    words((n//100)%10, "Hundred")
    words((n%100), "")
print("\n")





def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=int(input("Enter a number: "))
if num<0:
    print("please enter a positive number")
elif prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is a composite number")

