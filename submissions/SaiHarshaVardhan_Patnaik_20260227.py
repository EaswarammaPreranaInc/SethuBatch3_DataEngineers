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
units = int(input('Enter units: '))

match units // 100:
    case 0:   # 0–99
        cost = units * 3.00

    case 1:   # 100–199
        cost = (100 * 3.00) + (units - 100) * 3.50

    case 2:   # 200–299
        cost = (100 * 3.00) + (100 * 3.50) + (units - 200) * 4.00

    case 3:   # 300–399
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (units - 400) * 4.50

    case _:   # 400 and above
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + (units - 700) * 5.00

print('Bill amount:', cost)

"""
Output:
Enter units: 900
Bill amount: 3800.0
"""

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
x = int(input('Enter the limit: '))
a, b = 0, 1
print('Fibonacci series up to', x, ':', end=' ')
while a <= x:
    print(a, end='\n ')
    a, b = b, a + b

'''
 Output:
 Enter the limit: 10
 Fibonacci series up to 10 : 0
 1
 1
 2
 3
 5
 8

 Enter the limit: 1
 Fibonacci series up to 1 : 0
 1
 1

 Enter the limit: 0
 Fibonacci series up to 0 : 0
 
 '''

# Find  outputs  (Home  work)
'''How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop'''

a = [10, 20, 15, 18]
print('Elements of the list:')
for i in range(len(a)):
    print(a[i])

'''
Output:
Elements of the list:
10
20
15
18
'''

a = 'Hyd'
print('Characters of the string:')
for i in range(len(a)):
    print(a[i])

'''
Output:
Characters of the string:
H
y
d
'''

a = range(5)
print('Elements of the range:')
for i in range(len(a)):
    print(a[i])

'''
Output:
Elements of the range:
0
1
2
3
4
'''

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10 , 30 , 50
print() # 
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20 , 40 , 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10, 20) , (30, 40) , (50, 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10 , 30 , 50

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20 , 30...40 , 50...60
for  x ,  y  in   a:
	print(x , y) # Error 
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # Error

# Identify  error  (Home  work)
for  x  in   123:
        print(x) # Error '123' is non sequence number

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # Empty
for  x   in  []:
        print(x) # Empty
for  x   in   {}:
        print(x) # Empty
for  x   in   set():
        print(x) # Empty
for  x   in   '':
        print(x) # Empty
for  x  in  range(10 , 10):
	print(x) # Empty
for  x  in   range():
	print(x) # Error as range not has any argument
for  x  in   (25):
	print(x) #Error 
        
# Identify Error  (Home  work)
if(10 , 20 , 30): # Error 
	print('Hyd')
	break #Error
	print('Sec') 

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

'''
Output:
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
'''

'''
# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
'''
a = [25, 10.8, 'Hyd', True]
print('Indexed based for loop')
for i in range(len(a)):
    print(i, a[i])
'''
output:
Indexed based for loop
0 25
1 10.8
2 Hyd
3 True'''

a = [25, 10.8, 'Hyd', True]
print('For each loop')
for i, element in enumerate(a):
    print(i, element)

'''
output:
For each loop
0 25
1 10.8
2 Hyd
3 True
'''

'''#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)'''

a = [25, 10.8, 'Hyd', True]
print('Reverse Indexed for loop')
for i in range(len(a)-1,-1,-1):
    print(a[i])         

'''
output:
Reverse Indexed for loop
True
Hyd
10.8
25
'''
a = [25, 10.8, 'Hyd', True]
print('Reverse For each loop')
for element in reversed(a):
    print(element)

'''
output:
Reverse For each loop
True
Hyd
10.8
25
'''

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
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
for i in range(len(a)):
    c.append(a[i] + b[i])
print('3rd  list : ' , c)
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
for i, element in enumerate(a):
    c.append(element + b[i])
print('3rd  list : ' , c)

'''
Output:
Enter  1st  list  :  [10,20,15,18]
Enter  2nd  list  :  [30,40,35,12,100,200,300]
3rd  list :  [40, 60, 50, 30]
'''

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
print('Indexed for loop')
for i in range(2, 5):
    print(a[i])
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
print('For each loop')
for element in a[2:5]:
    print(element)

'''
Output:Indexed for loop
Hyd
True
(3+4j)

Output:For each loop
Hyd
True
(3+4j)
'''

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)

'''
Output:
a :   [11, 21, 16, 19]  '''

'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''
lines = int(input('Enter the number of lines: '))
for i in range(lines):
    spaces = ' ' * (lines - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)           

'''
Output:
Enter the number of lines: 5 
    *
   ***
  *****
 *******'''

'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
count = 1
num = 2
print('First 20 even numbers:')
while count <= 20:
    print(num, end=' ')
    num += 2
    count += 1

'''output:
First 20 even numbers:
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 '''

'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
count = 1
num = 1     
print('First 20 odd numbers:')
while count <= 20:
    print(num, end=' ')
    num += 2
    count += 1

'''output:First 20 odd numbers:
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 '''

'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
n = int(input('Enter the value of n: '))
i = 1
print('Natural numbers up to', n, ':', end=' ')
while i <= n:
    print(i, end=' ')
    i += 1
'''output:Enter the value of n: 10
Natural numbers up to 10 : 1 2 3 4 5 6 7 8 9 10 '''

'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
i = 10
print('Numbers from 10 to 1:', end=' ') 
while i >= 1:
    print(i, end=' ')
    i -= 1
'''output:Numbers from 10 to 1 : 10 9 8 7 6 5 4 3 2 1 '''

'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
n = int(input('Enter the number of terms: '))
total_sum = 0.0
for i in range(1, n + 1):
    total_sum += 1.1 * i
print('The sum of the series is:', total_sum)

'''output:Enter the number of terms: 5
The sum of the series is: 16.5'''

'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
a = 0
for i in range(1, 21):
    a += 2 * i  
print('The sum of the first 20 even numbers is:', a)

'''output:The sum of the first 20 even numbers is: 420'''

'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
a = 0
for i in range(1, 21):  
    a += 2 * i - 1  
print('The sum of the first 20 odd numbers is:', a)

'''output:The sum of the first 20 odd numbers is: 400'''

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
'''Output:
1'''

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')
'''Output:
Hyd'''

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
'''Output:
1'''