'''
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

units = int(input('Enter units : '))

match units // 100:

    case 0:   
        cost = units * 3.00

    case 1:   
        cost = 100 * 3.00 + (units - 100) * 3.50

    case 2 | 3:   
        cost = (100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00)

    case 4 | 5 | 6:   
        cost = (100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50)

    case _:   
        cost = (100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00)

print('Bill amount :', cost)
'''
Output :=
Enter units : 582
Bill amount : 2269.0
'''
#----------------------------------------------------------------------------------------------------------------------------
'''
Q1
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
'''
ip = int(input("Enter the number : "))

a = 0
b = 1
print("Fibonaci Series")
while (a <= ip):
    
    print(a)
    c = a + b
    a = b
    b = c
'''

'''
Output :
Enter the number : 13
Fibonaci Series
0
1
1
2
3
5
8
13
'''
##----------------------------------------------------------------------------------------------------------

'''
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
a = [10 , 20 , 15 , 18]
for x in a :
    print(x)
    
Output :
10
20
15
18
'''

'''
#How  to  print  each  character  of   string  'Hyd'  with  for  loop
a = 'Hyd'
for x in a :
    print(x)
H
y
d
'''

'''
#How  to  print  each  element  of   range(5)  with  for  loop
a = range(5)
for x in a :
    print(x)

0
1
2
3
4
'''
#----------------------------------------------------------------------------------------------------------------------
'''
# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
10
30
50

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
20
40
60


for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
(10 , 20)
(30 , 40)
(50 , 60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
10 
30 
50 
'''
#-------------------------------------------------------------------------------------------------------------------

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')

10...20
30...40
50...60

for  x ,  y  in   a:
	print(x , y) # Error, 
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # Error
 
# Identify  error  (Home  work)
for  x  in   123:
        print(x) # Error, because 123 is non sequence , so it is not iterable
        
        
# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # Nothing, because there are no elements in tuple
for  x   in  []:
        print(x) # Nothing,  because there are no elements in tuple
for  x   in   {}:
        print(x) # Nothing, because there are no elements in dictionary
for  x   in   set(): 
        print(x)  # Nothing, because there are no elements in set
for  x   in   '':
        print(x) #Nothing, because there are no characters in string
for  x  in  range(10 , 10):
	print(x) # Nothing , because start and stop is same , so that are no elements are generated in range
for  x  in   range():
	print(x) # Error, because there are no arguments in range
for  x  in   (25):
	print(x) # Error, because (25) is non sequence , which is not iterable
 

#----------------------------------------------------------------------------------------------------------------

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

Output :-
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
Bye
 
#------------------------------------------------------------------------------------------------------------------

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('Indexed  based  for loop')
for i in range(len(a)) :
    print(i , a[i])

How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
print('For each loop')

#------------------------------------------------------------------------------------------------------------------------

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop

for i in range(len(a)-1 , -1, -1) :
    print(i , a[i])
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

#-----------------------------------------------------------------------------------------------------------------------------

'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''

How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []

for i in range(len(a)):
    if i < len(b):
        c.append(a[i] + b[j])
    
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

#------------------------------------------------------------------------------------------------------------------
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range([2:5]) :
    print(i , a[i])
    
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
#-----------------------------------------------------------------------------------------------------------------------

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a : [11 , 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # [10 , 20 , 15 , 18]

#---------------------------------------------------------------------------------------------------------------------------

'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines
'''
n = int(input('Enter number of lines: '))

for i in range(1, n + 1):
    sp = ' ' * (n - i)
    st = '*' * (2*i - 1)
    print(spaces + stars)
    
'''
Enter number of lines: 4
   *
  ***
 *****
*******
'''
#------------------------------------------------------------------------------------------------------------------
'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
n = int(input("Enter the number : "))

i = 1
print("First 20 even numbers ")

while (i <= n) :
    print(2 * i)
    i = i + 1

'''
Output :-
Enter the number : 20
First 20 even numbers
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
'''
#----------------------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

n = int(input("Enter the number : "))

i = 1
print("First 20 even numbers ")

while (i <= n) :
    print(2 *i - 1)
    i = i + 1

'''
Output :-
Enter the number : 20
First 20 odd numbers 
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
'''
#-----------------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
n = int(input("Enter the number : "))

i = 1
print("Natural Numbers ")

while (i <= n) :
    print(i)
    i = i + 1
'''
Output :
Enter the number : 20
Natural Numbers
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
'''
#-----------------------------------------------------------------------------------------------------------

'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
n = int(input("Enter the number : "))

i = 10
print("Numbers from 10 downto 1 in steps of -1")
while (i >= 1) :
    print(i)
    i = i - 1
'''
Output :-
Numbers from 10 downto 1 in steps of -1
10
9
8
7
6
5
4
3
2
1
'''
#-----------------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
n = int(input("Enter the number : "))

sum = 0

for i in range(1, n+1) :
    sum = sum + 1.1*i

print("Sum : ", sum)

'''
Output :-
Enter the number : 10
Sum : 60.50
'''
#---------------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

n = int(input("Enter the number : "))

sum = 0

for i in range(1, n+1) :
    sum = sum + 2*i

print("Sum of first 20 even numbers : ", sum)

'''
Output :=
Enter the number : 20
Sum of first 20 even numbers :  420
'''
#-------------------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
n = int(input("Enter the number : "))

sum = 0

for i in range(1, n+1) :
    sum = sum + (2*i - 1)

print("Sum of first 20 odd numbers : ", sum)

'''
Output :=
Enter the number : 20
Sum of first 20 odd numbers :  400
'''
#-------------------------------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''

n = int(input("Enter the number : "))

sum = 0

for i in range(1, n+1) :
    sum = sum + i

print("Sum of first 20  numbers : ", sum)

'''
Output :=
Enter the number : 20
Sum of first 20  numbers :  210
'''
#--------------------------------------------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside of Look
#----------------------------------------------------------------------------------------------------------------------------------
# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec') # Error, because continue only works inside loops such as for or while 
 #----------------------------------------------------------------------------------------------------------------------------------
 # Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

1
Sec
Hello
2
Sec
Hello
3
Outside loop

#----------------------------------------------------------------------------------------------------------------------------------
# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec') # Error, because break can be used only inside for or while loop

