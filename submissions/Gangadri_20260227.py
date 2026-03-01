# 1 . Write  a  program  to  determine  bill  amount  and  input  is  units

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
	case  ???:
				cost = 
	case  ???:
				cost = 
	case  ???:				
				cost = 
print('Bill  amount  :  ' , cost)


# output : 
units = int(input('Enter units : '))  

match units // 100:

    case 0:   # 0 - 99
        cost = units * 3.00

    case 1:   # 100 - 199
        cost = 100 * 3.00 + (units - 100) * 3.50

    case 2 | 3:   # 200 - 399
        cost = (
            100 * 3.00 +
            100 * 3.50 +
            (units - 200) * 4.00
        )

    case 4 | 5 | 6:   # 400 - 699
        cost = (
            100 * 3.00 +
            100 * 3.50 +
            200 * 4.00 +
            (units - 400) * 4.50
        )

    case _:   # 700 and above
        cost = (
            100 * 3.00 +
            100 * 3.50 +
            200 * 4.00 +
            300 * 4.50 +
            (units - 700) * 5.00
        )

print('Bill amount : ', cost)


# 2 . Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop

# output : 

x = int(input("Enter number of terms : "))

a = 0   
b = 1  

count = 1

while count <= x:
    print(a, end=" , ")
    c = a + b
    a = b
    b = c


# 3 . # Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop

# output : 1 : lst = [10, 20, 15, 18]

for x in lst:
    print(x)

# 2 . s = 'Hyd'

for ch in s:
    print(ch)

# 3 . for i in range(5):
    print(i)

# output : 1 . keys 

for x in {10:20, 30:40, 50:60}.keys():
    print(x)

# 2 . values . 

for x in {10:20, 30:40, 50:60}.values():
    print(x)

# 3 . items .

for x in {10:20, 30:40, 50:60}.items():
    print(x)
    count += 1


# 4 . # Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
for  x ,  y  in   a:
	print(x , y
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')

# Output : a = {10:20, 30:40, 50:60}

#  Using items()
for x, y in a.items():
    print(x, y, sep='...')

print()

for x, y in a:
    print(x, y)

print()

for x, y in {10:20, 30:40, 50:60}:
    print(x, y, sep='...')


# 5 . # Identify  error  (Home  work)
for  x  in   123:
        print(x)

# output : TypeError: 'int' object is not iterable


# 6 . # Find  outputs  (Home  work)
for  x   in   ():
        print(x) : no output

for  x   in  []:
        print(x) : no output

for  x   in   {}:
        print(x) : no output

for  x   in   set():
        print(x) : no output

for  x   in   '':
        print(x) : no output

for  x  in  range(10 , 10):
	print(x) : no output

for  x  in   range():
	print(x) : output : TypeError: range expected at least 1 argument, got 0

for  x  in   (25):
	print(x) : output : TypeError: 'int' object is not iterable


# 7 . #  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

# output : 
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

# 8 . # How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

a = [25, 10.8, 'Hyd', True]

print('Indexed based for loop')
for i in range(len(a)):
    print(i, a[i])

print('For each loop')
for x in a:
    print(a.index(x), x)

# output : Indexed based for loop
0 25
1 10.8
2 Hyd
3 True
For each loop
0 25
1 10.8
2 Hyd
3 True

# 9 . #  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

a = [25, 10.8, 'Hyd', True]

print('Indexed for loop')
for i in range(len(a)-1, -1, -1):
    print(a[i])

print('For each loop')
for x in reversed(a):
    print(x)

# output : Indexed for loop
True
Hyd
10.8
25
For each loop
True
Hyd
10.8
25

# 10 . '''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

# output : a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))

c = []

print('Indexed based for loop')

# Add using indexed based for loop
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])

print('3rd list :', c)


print('For each loop')

c = []

# Add using for each loop (no 2nd variable)
for x in a:
    if a.index(x) < len(b):
        c.append(x + b[a.index(x)])

print('3rd list :', c)


# 11 . #  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)

# output : a :  [11, 21, 16, 19]
b :  [10, 20, 15, 18]


# 12 . Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines

n = int(input("Enter number of lines : "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# output :     
    *
   ***
  *****
 *******
*********


# 13 . (Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

# output : i = 1

while i <= 20:
    print(2 * i, end=" ")
    i += 1

2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40

# 14 . Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

# output : i = 1

while i <= 20:
    print(2 * i - 1, end=" ")
    i += 1

# output : 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39


# 14 . Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop

# output :
 n = int(input("Enter value of n : "))

i = 1

while i <= n:
    print(i, end=" ")
    i += 1

1 2 3 4 5 6 7 8 9 10


# 15 . Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop

# output : i = 10

while i >= 1:
    print(i, end=" ")
    i -= 1

10 9 8 7 6 5 4 3 2 1

# 16 . Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop

# output : n = int(input("Enter number of terms : "))

sum = 0

for i in range(1, n + 1):
    sum += 1.1 * i

print("Sum :", sum)

1.1*1 + 1.1*2 + 1.1*3 + 1.1*4 + 1.1*5
= 1.1 + 2.2 + 3.3 + 4.4 + 5.5
= 16.5


# 17 . Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop

output : sum = 0

for i in range(1, 21):
    sum += 2 * i

print("Sum of first 20 even numbers :", sum)

2*1 + 2*2 + 2*3 + ... + 2*20
= 2 + 4 + 6 + ... + 40


# 18 .  Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

output : 1
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
Outside loop


# 19 . # Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')

output : SyntaxError: 'continue' not properly in loop

# output : 1
Sec
Hello
2
Sec
Hello
3
Outside loop


# 20 . # Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

output : 1
Sec
Hello
2
Sec
Hello
3
Hyd
Hello
4
Sec
Hello
5
Sec
Hello
6
Hyd
Hello
7
Sec
Hello
Outside loop


# 21 . # Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

output : 1
Sec
Hello
2
Sec
Hello
3