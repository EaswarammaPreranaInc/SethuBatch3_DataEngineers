
1.Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost

First  100  units(0 - 99)		Rs. 3.00 / unit

Next  100  units(100 - 199)		Rs. 3.50 / unit

Next  200  units(200 - 399)		Rs. 4.00 / unit

Next  300  units(400 - 699)		Rs. 4.50 / unit

Above  700  units(units >= 700)		Rs. 5.00 / unit

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

code:-
units = int(input('Enter units : '))

match units // 100:
    
    case 0:   # 0 – 99
        cost = units * 3.00

    case 1:   # 100 – 199
        cost = 100 * 3.00 + (units - 100) * 3.50

    case 2 | 3:   # 200 – 399
        cost = (
            100 * 3.00 +
            100 * 3.50 +
            (units - 200) * 4.00
        )

    case 4 | 5 | 6:   # 400 – 699
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

print('Bill amount :', cost)




2.Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop

code:--
x = int(input("Enter value of x : "))

a = 0
b = 1
 count = 0
 while count < x:
	print(a, end=',')
	c = a + b
	a = b
	b = c
 	count +=1




3.# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop

1.
list = [10,20,15,18]
for x in list:
	print(x)

2.
s = 'Hyd'
for ch in s:
	print(s)
3.
for i in range(5):
        print(i)




4.# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10, 30, 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20, 40, 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10,20)
		(30,40)
		(50,60)
print()`	
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10
		30
		50



5.# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20
			  # 30...40
			   #50...60

for  x ,  y  in   a:
	print(x , y
		#Missing closing brackets ) in print(x,y
		# cannot unpack non-iterable int object
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # cannot unpack non-iterable int object




6.# Identify  error  (Home  work)
for  x  in   123:
        print(x) # 'int' object is not iterable # for loop works only on iterable objects




7.# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # Empty tuple # No output
for  x   in  []:
        print(x) # Empty list # No output
for  x   in   {}:
        print(x) # empty dictionary # No keys
for  x   in   set():
        print(x) # Empty set # No output
for  x   in   '':
        print(x) # No output due to empty string
for  x  in  range(10 , 10):
	print(x) # No numbers between 10 and 10
for  x  in   range():
	print(x) # range() needs at least one argument
for  x  in   (25):
	print(x) # 'int' object is not iterable




8.#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')
output:--
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




9.# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)


1.
using range(len(a))
a = [25, 10.8, 'Hyd',True]
print('Indexed based for loop')
for i in range(len(a)):
	print(i, a[i])

output:
Indexed based for loop
0 25
1 10.8
2 Hyd
3 True

2.
# Using enumerate()
print('For each loop')

for index, value in enumerate(a):
    	print(index, value)




10.#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

1.
# Use range() with negative step
print('Indexed for loop')

for i in range(len(a) - 1, -1, -1):
   	 print(a[i])

output:
Indexed for loop
True
Hyd
10.8
25

2.
#Use reversed() function
print('For each loop')
for x in reversed(a):
	print(x)

output:
For each loop
True
Hyd
10.8
25




11.Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

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

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))

c = []

# 1️.Indexed Based For Loop
min_len = min(len(a), len(b))

for i in range(min_len):
    c.append(a[i] + b[i])

print('3rd list (Indexed loop) :', c)

 2️.For Each Loop (Do NOT use 2nd variable)
c = []

for x in a:
    if a.index(x) < len(b):
        c.append(x + b[a.index(x)])

print('3rd list (For each loop) :', c)



12.#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

1.index based for loop
print('indexed  for loop')
for i in range(2,5):
	print(a[i])
o/p:--
Indexed for loop
Hyd
True
(3+4j)
 
2. for each loop
print('For each loop')

for x in a:
 if 2 <= a.index(x) <= 4:
        	print(x)

output:
For each loop
Hyd
True
(3+4j)



13#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a :  [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # b :  [10, 20, 15, 18]



14.Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines

n = int(input("Enter number of lines : "))
for i in range(1, n+1):
	print(" " * (n - i), end="")
    	print("*" * (2 * i - 1))



15.(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

i = 1
while i <=20:
	print(2 * i, end=" ")
	i += 1 




16.Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

i = 1
while i <= 20:
	print(2 * i-1, end=" ")
	i +=1



17.Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop

n = int(input("Enter value of n : "))
i=1
while i <=n:
	print(i, end= " ")
	i += 1



18.Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop

i = 10
while i>= 1:
	print(i, end=" ")
	i -= 1



19.Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''

n = int(input("Enter number of terms : "))
total = 0
for i in range(1, n+1):
	total +=1.1 * i
print("Sum =", total)



20.Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop

total = 0
for i in range(1,21):
	total +=2*i
print("Sum =", total)




21.Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop

total = 0
for i in range(1,21):
	total += 2 * i -1
print("Sum =", total)



22.Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop

n = int(input("Enter value of n : "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)




23.# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
		continue
	else:
		print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

output:
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
Outside loop




24.# Identify Error  (Home  work)
if ():  
	print('Hyd')
	continue # 'continue' not properly in loop
	print('Sec')



25.# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop



26.# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break # 'break' outside loop
	print('Sec')