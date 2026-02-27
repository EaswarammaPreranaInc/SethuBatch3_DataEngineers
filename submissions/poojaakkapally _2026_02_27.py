1.'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)		    	Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(units >= 700)		Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter  units :   '))   #   175
match  units // 100:
	case  0:   #   units  between  0  and  99
				cost = units * 3.00
	case  1:  #  units  between  100 and  199
				cost =  100 * 3.00 + (units - 100) * 3.50
	case  2:#units  between  200 and  399
				cost = 100 * 3.00 + (units - 100) * 3.50 + (units - 100) * 4.00
	case  3:units  between  400 and  699
				cost = 100 * 3.00 + (units - 100) * 3.50 + (units - 100) * 4.00 + (units - 100) * 4.50
	case  4:units  between (units >= 700) 				
				cost = 100 * 3.00 + (units - 100) * 3.50 + (units - 100) * 4.00 + (units - 100) * 4.50 + (units - 100) * 5.00
print('Bill  amount  :  ' , cost)

match units//100:
    case 0:
        print(f'cost : {100 *3.00}')
    case 1:
        print(f'cost : {100 *3.00+(units-100)*3.50}')
    case 2 |3:
        print(f'cost :{100*3.00+(units-100)*3.50 + (units-100)*4.00}')
    case 4 |5|6:
        print(f'cost :{100*3.00+(units-100)*3.50 + (units-100)*4.00 + (units-100)*4.50}')
    case _:
        print(f'cost :{100*3.00+(units-100)*3.50 + (units-100)*4.00 + (units-100)*4.50 + (units-100)*5.00}')
        

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2.# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()

my_list = [10, 20, 15, 18]
for element in my_list:
    print(element)
OUTPUT:-10
20
15
18

How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()

my_string = 'Hyd'
for character in my_string:
    print(character)
OUTPUT:-H
y
d

How  to  print  each  element  of   range(5)  with  for  loop
for number in range(5):
    print(number)
OUTPUT:-0
1
2
3
4
-------------------------------------------------------------------------------------------------
3.# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
'''
10
30
50 
'''
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
'''
20
40
60
'''
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
'''
(10, 20)
(30, 40)
(50, 60)
'''
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
'''
10
30
50
'''
-----------------------------------------------------------------------------------------------------------------------------------
3.
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
'''
10...20
30...40
50...60
'''
for  x ,  y  in   a:
	print(x , y
#type error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
#type error
------------------------------------------------------------------------------------------------------------------------------------------
4.# Identify  error  (Home  work)
for  x  in   123:
        print(x)
#Type error
---------------------------------------------------------------------------------
5.# Find  outputs  (Home  work)
for  x   in   ():
        print(x)
#nothing prints
for  x   in  []:
        print(x)
#nothing prints
for  x   in   {}:
        print(x)
#nothing prints
for  x   in   set():
        print(x)
#nothing prints
for  x   in   '':
        print(x)
#nothing prints
for  x  in  range(10 , 10):
	print(x)
#nothing prints
for  x  in   range():
	print(x)
#error
for  x  in   (25):
	print(x)
#error
---------------------------------------------------------------------------------
6.#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')
'''
output:-
1 1
1 2
1 3
1 4(for i=1&j=1,2,3,4)
Hello
2 1
2 2
2 3
2 4(for i=2&j=1,2,3,4)
Hello
3 1
3 2
3 3
3 4(for i=3&j=1,2,3,4)
Hello
Bye
'''
---------------------------------------------------------------------------------
7.# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
'''
for i in range(len(a)):
    print('Index:', i, 'Element:', a[i])
'''
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
'''
for a in enumerate(a):
    print('Index:', a[0], 'Element:', a[1])
'''
------------------------------------------------------------------------------------------------------------------------
8.#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
'''
or i in range(len(a) - 1, -1, -1):
    print(a[i])
'''
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
'''
for x in reversed(a):
    print(x)
'''
'''
output:-
True
Hyd
10.8
25
'''
------------------------------------------------------------------------------------------------------------------------------
9.#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
'''
for i in range(2, 5):
    print(a[i])
'''
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
'''
for item in enumerate(a):
    if 2 <= item[0] <= 4:
        print(item[1])
'''
'''
output:-
Hyd
True
(3+4j)
'''
-----------------------------------------------------------------------------------------------------------------------
10.#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) #a :  [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) #b :  [10, 20, 15, 18]
-----------------------------------------------------------------
11.# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
------------------------------------------------------------
12# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue        #error,Continue should be used with loops
	print('Sec')
--------------------------------------------------------
13# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')#1<nl>Sec<nl>Hello<nl>2<nl>Sec<nl>Hello<nl>3<nl>Outside loop
------------------------------------------------------
14# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break        #error,break should be used with loops
	print('Sec')
------------------------------------------------
15.fibonacci  series 
num = int(input("Enter a number :"))
x=0
fib1=0
fib2=1
print(fib1,fib2)
while(x<num):
    fib3=fib1+fib2
    print(fib3)
    fib1=fib2
    fib2=fib3
    x=x+1
----------------------------------------------
16.Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []

for i in range(len(a)):
    z = a[i]+b[i]
    c.append(z)
print(c)
-----------------------------------------------------------
17.Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines'''

x=int(input("Enter How many lines : "))
for i in range(1,x+1):
     print((x-i)*' ' + ('*'* (2*i - 1)))
------------------------------------------------------
18.# Write  a  program  to  print  first  20  even  numbers 

x=int(input("Enter n number : "))
i=1
while i<=x:
    print(2*i)
    i += 1
print("Bye")
----------------------------------------
19. Write  a  program  to  print  first  20  odd  numbers

x=int(input("Enter n number : "))
i=1
while i<=x:
    print(2*i - 1)
    i += 1
print("Bye")
-------------------------------
20.# Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n

i=1
while i<=x:
    print(i)
    i += 1
print("Bye")
-------------------------------
21.# Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

x=int(input("Enter n number : "))
while x>0:
    print(x)
    x -= 1
print()
-------------------------------------
22.# Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

x=int(input("Enter n number you would like to add : "))
sum=0
for i in range(1,x+1):
    sum += 1.1 * i
    i+=1
print(sum)
--------------------------------------------
23.# Write  a  program  to  determine  sum  of  first  20  even numbers

x=int(input("Enter n number you would like to add : "))
sum=0
for i in range(1,x+1):
    sum += 2*(i)
    i+=1
print(f'sum of first {x} numbers is {sum}')
---------------------------------------------------------
24.# Write  a  program  to  determine  sum  of  first  20  odd numbers

x=int(input("Enter n number you would like to add : "))
sum=0
for i in range(1,x+1):
    sum += (2*i) - 1
    i+=1
print(f'sum of first {x} numbers is {sum}')
--------------------------------------------
25.# Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

x=int(input("Enter n number you would like to add : "))
sum=0
for i in range(1,x+1):
    sum += i
    i+=1
print(f'sum of first {x} numbers is {sum}')





















































