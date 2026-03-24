#  Find  outputs
def  f1():
		print('f1  Function') #f1 function 
		f2()
def  f2():
		print('f2  function') #f2 function
f1()


#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  print(30)
print(add('Hyder' , 'abad')) #Hyderabad
print(add(10.8 , 20.6)) #31.400
print(add(True , False)) #1
print(add(3 + 4j , 5 + 6j)) #8+10j
print(add(25 , 10.8)) #35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec' #[25, 10.8, 'Hyd', True, None, (3+4j), 'Sec'] 
print(add(10 , '20')) #error


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
 #Three  argument  function :  10 20 30

def prime(n):
    if n <= 1:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


n = int(input('Enter any integer number: '))

if n <= 1:
    print('Invalid input')
elif prime(n):
    print('Prime number')
else:
    print('Composite number')


# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)

#Emp  Number  :  25 	  Emp Name  :  Rama  Rao 	  Salary  :  10000.0
#Emp  Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35


a = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
     "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
     "Seventeen", "Eighteen", "Nineteen"]

b = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
     "Sixty", "Seventy", "Eighty", "Ninety"]

def words(n, units):
    if n == 0:
        return

    if n < 20:
        print(a[n], units, end=" ")
    else:
        print(b[n // 10], a[n % 10], units, end=" ")


n = int(input('Enter any number : '))

if n == 0:
    print("Zero")
else:
    words(n // 10000000, "Crores")
    words((n // 100000) % 100, "Lakhs")
    words((n // 1000) % 100, "Thousand")
    words((n // 100) % 10, "Hundred")

    last = n % 100
    if last:
        if last < 20:
            print(a[last], end=" ")
        else:
            print(b[last // 10], a[last % 10], end=" ")

    print()


Write  a  function  to  print  number  in  words

Let  input  be  123456789
What  is  the  output ?  --->  Tweleve  crores  thirty  four  lakhs  fifty  six  thousand  seven  hundred  eighty  nine

1) a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" ,   "Eleven" , "Twelve" ,
           "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" ,  "Eightteen" , "Nineteen"]

2) b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
            0     1          2              3            4             5           6              7               8               9

3) How  to  print  92  in  words ?  --->  b[92 // 10]  and  a[92 % 10]  = b[9]  and  a[2]
    How  to  print  50  in  words ?  --->   b[50 // 10]  and  a[50 % 10]  = b[5]  and  a[0]

4) How  to  print  14  in  words ?  --->  a[14]
    How  to  print  4  in  words ?  --->  a[4]

5) How  to  obtain  crores  part  from  123456789 ?  --->  123456789 // 10000000 = 12
    How  to  obtain  lakhs  part  from  123456789 ?  --->  123456789 // 100000 % 100 = 1234 % 100 = 34
    How  to  obtain  thousands  part  from  123456789 ?  --->  123456789 // 1000 % 100 = 123456 % 100 = 56
    How  to  obtain  hundreds  part  from  123456789 ?  ---> 123456789 // 100 % 10 = 1234567 % 10 = 7
    How  to  obtain  last  two  digits  of  the  number ?  ---> 123456789 % 100 = 89
'''
def  words(n , units):
	 a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" , "Eleven" , "Twelve" , 
	        "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" , "Eightteen" , "Nineteen"]
	 b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
            0     1          2              3            4             5            6              7               8              9
	Write  if  statement  to  print  two  digit  number  in  words
	Write  if  statement  to  print  units
'''
1) words(92 , "Crores")  --->  Ninety  two  crores

2) words(50 ,  "Lakhs")  --->  Fifty  Lakhs

3) words(14 , "Thousand")  --->  Fourteen  Thousand

4) words(7 , "Hundred")  ---> Seven  Hundred

5) words(0 , "Crores")   --->  Nothing  becoz  1st  argument  is  0
'''
n = int(input('Enter any number (max : 999999999)  : '))
if  n == 0:
	printf('Zero')
else:
        How  to  obtain  crores  part  from  the  number  and  call  words()  function
        How  to  obtain  lakhs  part  from  the  number  and  call  words()  function
        How  to  obtain  thousands  part  from  the  number  and  call  words()  function
        How  to  obtain  hundreds  part  from  the  number  and  call  words()  function
        How  to  obtain  last  two  digits  of  the  number  and  call  words()  function
		printf("\n");

a = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
     "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
     "Seventeen", "Eighteen", "Nineteen"]

b = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
     "Sixty", "Seventy", "Eighty", "Ninety"]

def words(n, units):
    if n == 0:
        return

    if n < 20:
        print(a[n], units, end=" ")
    else:
        print(b[n // 10], a[n % 10], units, end=" ")


n = int(input('Enter any number : '))

if n == 0:
    print("Zero")
else:
    words(n // 10000000, "Crores")
    words((n // 100000) % 100, "Lakhs")
    words((n // 1000) % 100, "Thousand")
    words((n // 100) % 10, "Hundred")

    last = n % 100
    if last:
        if last < 20:
            print(a[last], end=" ")
        else:
            print(b[last // 10], a[last % 10], end=" ")

    print()

# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) #a  :  10    	  b  :  20  	  c :  30
f1(25 , 10.8 , 'Hyd') #a  :  25    	  b  :  10.8  	  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5) #a  :  50.2    	  b  :  40.7  	  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') #  Cyb    	  b  :  Sec  	  c :  Hyd
f1(c = 3 + 4j , a = True , b = None) #a  :  True    	  b  :  None  	  c : (3+4j)
f1(25 , c = 10.8 , b = 'Hyd') #a  :  25    	  b  :  Hyd  	  c :  10.8
f1(a = 100 , 200 , 300)  #Error
f1(True , None , b = 'Hyd') #Eerror
f1(10 , 20 , x = 30) #Error
f1(10 , 20) #Error


# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)

#Emp  Number :   25  	  Emp  Name : Rama Rao         	  Salary : 10000.0
Emp  Number :   35  	  Emp  Name : Sita             	  Salary : 20000.0
Emp  Number : Rama  Rao  	  Emp  Name :         30000.0  	  Salary : 20


#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) #23
print(f1(*[6 , 7 , 8])) #62
print(f1([6 , 7 , 8]))#Error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) #16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) #14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) #Error
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) #{'c': 2, 'b': 4, 'a': 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) #Error

# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) #Error
print(sorted(a , rev = True)) #Error
print(25 , 10.8 , 'Hyd' , separator = '\t') #Error
print(25 , 10.8 , 'Hyd' , endofline = '\t') #Error
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #Error

