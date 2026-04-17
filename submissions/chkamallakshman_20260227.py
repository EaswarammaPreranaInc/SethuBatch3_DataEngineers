'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
x= int(input("Enter the value of x:"))
print("Fabonaci series:")
if x==0:
   print(0)
elif x==1:
       print(0)
       print(1)
else:
       a=0
       b=1
       c=a+b
       print(a)
       print(b)
       print(c)
       while(c<x):
           
           a=b
           b=c
           c=a+b
           print(c)
--------------------------------------------------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
'''How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print() '''

l=[10,20,15,18]
for x in l:
  print(x) 
'''
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()'''
str='HYD'
for x in str:
  print(x) 
'''
How  to  print  each  element  of   range(5)  with  for  loop
'''
x=5
for i in range(x):
  print(i) 
--------------------------------------------------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) #10 30 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) #20 40 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) #(10,20) (30,40) (50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10 30 50
--------------------------------------------------------------------------------------------------------------------------------------------------
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') 
  #10...20
   30...40
   50...60
for  x ,  y  in   a:
	print(x , y) # Error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') #Error

--------------------------------------------------------------------------------------------------------------------------------------------------

# Identify  error  (Home  work)
for  x  in   123:
        print(x)  #TypeError: 'int' object is not iterable

--------------------------------------------------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
for  x   in   ():
        print(x)   # empty
for  x   in  []:
        print(x)   # empty
for  x   in   {}:
        print(x)   # empty
for  x   in   set():
        print(x)   #empty
for  x   in   '':
        print(x)   #empty
for  x  in  range(10 , 10):
	print(x)   #empty
for  x  in   range():
	print(x)   #Error
for  x  in   (25):
	print(x)   #error
--------------------------------------------------------------------------------------------------------------------------------------------------
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

''' output:
1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye   '''
--------------------------------------------------------------------------------------------------------------------------------------------------
# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
   print(i,a[i])
#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop print('For each loop')
for i in range a:
   print(a)
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
a = [25, 10.8, 'Hyd', True]
for index, value in enumerate(a):
    print("Index =", index, "Value =", value)
--------------------------------------------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])
print("3rd list :", c)

How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

a = [10, 20, 15, 18]
b = [30, 40, 35, 12, 100, 200, 300]
c = []
for x in a:
    c.append(x + b[a.index(x)])
print("3rd list :", c)
--------------------------------------------------------------------------------------------------------------------------------------------------
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2,5):
    print(a[i])
     
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
for x in a:
  if a.index(x) >= 2 and a.index(x) <= 4:
   print(x)
--------------------------------------------------------------------------------------------------------------------------------------------------
#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)   # a :   [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)   #b :   [10, 20, 15, 18]
--------------------------------------------------------------------------------------------------------------------------------------------------

'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''
n=int(input("Enter number of lines:"))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
--------------------------------------------------------------------------------------------------------------------------------------------------
'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
n=int(input("Enter first n even numbers:"))
i = 1
while i <= n:
    print(2 * i)
    i += 1
print("Bye")
--------------------------------------------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
n=int(input("Enter first n odd numbers:"))
i = 1
while i <= n:
    print(2 * i-1)
    i += 1
print("Bye")
--------------------------------------------------------------------------------------------------------------------------------------------------

'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
n=int(input("Enter first n natural numbers:"))
i = 1
while i <= n:
    print(i)
    i += 1
print("Bye")

--------------------------------------------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
n=int(input("numbers from n down to 1 :"))
while n >= 1:
    print(n)
    n -= 1
--------------------------------------------------------------------------------------------------------------------------------------------------

'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
n = int(input("Enter number of terms: "))

total = 0

for i in range(1, n + 1):
    total = total + 1.1 * i

print("Sum =", total)









































