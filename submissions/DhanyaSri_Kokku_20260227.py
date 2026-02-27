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
# Code:

units = int(input('Enter  units :   '))   #   175
match  units // 100:
	case  0:   #   units  between  0  and  99
		cost = units * 3.00
	case  1:  #  units  between  100 and  199
		cost =  100 * 3.00 + (units - 100) * 3.50
	case 2|3 : # units between 200 and 399
		cost = 100 * 3.00 + 100 * 3.50 + (units-200) *4.00
	case 4|5|6: # units between 400 to 699
		cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 +(units-400) * 4.50
	case  _: # units greater than 700				
		cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units-700) * 5.00
print('Bill  amount  :  ' , cost)

# Output:
Enter  units :   1200
Bill  amount  :   5300.0

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
# Code:

n = int(input("Enter value of x  : "))
try:
    if n >= 0:
        print("Fibonacci Series")
        if n == 0:
            print(n)
        else:
            a = 0
            b = 1
            print(a)
            print(b)
            while a + b <= n:
                c = a + b
                print(c)
                a = b
                b = c
    else:
        print("Enter the positive integer")
except:
    print("Enter the integer input")

#Output:
Enter value of x  : 10
Fibonacci Series
0
1
1
2
3
5
8

Enter value of x  : 1
Fibonacci Series
0
1
1

Enter value of x  : 0
Fibonacci Series
0

# Find  outputs  (Home  work)
# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
for x in [10 , 20 , 15 ,18]:
   print(x)
# How  to  print  each  character  of   string  'Hyd'  with  for  loop
for ch in 'Hyd':
   print(ch)
# How  to  print  each  element  of   range(5)  with  for  loop
for i in range(5):
   print(i)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
# Output:
10
30
50

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
# Output:
20
40
60

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
# Output:
(10,20)
(30,40)
(50,60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
# Output:
10
30
50

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
# Output:
10...20
30...40
50...60
for  x ,  y  in   a:
	print(x , y , sep = '...')
# Output:
Error cannot unpack non-sequence int object

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
# Output:
Error cannot unpack non-sequence int object

# Identify  error  (Home  work)
for  x  in   123: # Error
        print(x)

# Here for the for-each loop the loop should iterate sequence but not a non sequence

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # Nothing
for  x   in  []:
        print(x) # Nothing
for  x   in   {}:
        print(x) # Nothing
for  x   in   set():
        print(x) # Nothing
for  x   in   '': 
        print(x) # Nothing
for  x  in  range(10 , 10):
	print(x) # Nothing
for  x  in   range():
	print(x) # Error range object should have at least one argument
for  x  in   (25):
	print(x) # Error the for loop cannot iterate non sequences

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

# Output :
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

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
    print(a[i],i,sep='->')
# How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)):
    print(a[i],i,sep='->')
# How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
for x in enumerate(a):
    print(x[1],x[0],sep='->')

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
# How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(1,len(a)+1):
     print(a[-i])
# How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
for x in reversed(a):
     print(x)

''
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
min = len(a) if len(a)< len(b) else len(b)
for i in range(min):
    temp = a[i]+b[i]
    c.append(temp)
print('3rd  list : ' , c)
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
d = []
i = 0
for x in a[:min]:
   d.append(x+b[i])
   i+=1
print('3rd list : ', d)


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
# How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2,5):
    print(a[i])
# How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
for x in a:
    if a.index(x)>=2 and a.index(x)<=4:
         print(x)

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

# Output:
a :  [11 , 21 , 16 , 19]
b :  [10 , 20 , 15 , 18]

Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines
'''
# Code:
try:
    n = int(input("How many lines ?  : "))
    for i in range(n):
        print(' '*(n-i-1),'*'*(2*i+1),sep='')
except:
    print("Enter a integer input")

# Output:
How many lines ?  : 7
      *
     ***
    *****
   *******
  *********
 ***********
*************

'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
# Code:
print("First 20 even numbers")
i = 1 
while i<=20:
    print(2*i)
    i+=1
print('Bye')

'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
# Code:
print("First 20 odd numbers")
i = 1 
while i<=20:
    print(2*i-1)
    i+=1

'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
# Code:
try:
    n = int(input("Enter the value of n : "))
    print("Natural Numbers")
    i = 1
    while i<=n:
        print(i)
        i+=1
except:
    print("Enter a integer input")

# Output:
Enter the value of n : 5
Natural Numbers
1
2
3
4
5

'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
# Code:
print("Numbers from 10 down to 1 in steps of -1")
i = 10
while i > 0:
    print(i)
    i-=1

# Output:
Numbers from 10 down to 1 in steps of -1
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
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
# Code:
try:
    n = int(input("How many terms would you like to add  : "))
    sum = 0
    for i in range(1,n+1):
        sum+=(1.1*i)
    print(F'Sum  : {sum}')
except:
    print("Enter a integer input")

# Output:
How many terms would you like to add  : 5
Sum  : 16.5

'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
# Code:
sum = 0
for i in range(1,21):
    sum+=(2*i)-1
print(F"Sum of first 20 odd numbers :  {sum}")

# Output:
Sum of first 20 odd numbers :  400

'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
try:
    n = int(input("How many terms would you like to add  : "))
    sum = 0
    for i in range(1,n+1):
        sum+=i
    print("Sum  : ",sum)
except:
    print("Enter a integer input")

# Output:
How many terms would you like to add  : 10
Sum  :  55

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
# Output:
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

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue # Error
	print('Sec')
# The continue statement should be used in loops not in the conditions

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
# Output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break # Error
	print('Sec')
# The break statement should be used in loops not in conditions