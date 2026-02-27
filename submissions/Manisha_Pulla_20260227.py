'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13 , 21 , 34 

1) What  is  10th  term ?  --->  9th  term + 8th  term #34
    What  is  3rd  term ?  ---> 2nd  term + 1st  term #1
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term 

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
# Output:
x = int(input('enter value of x: '))
# First two terms
a = 0
b = 1
count = 0
while count < x:
    print(a, end=" , ")
    c = a + b
    a = b
    b = c
    count += 1

# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop 
print()
#output:
a = [10 , 20 , 15 , 18]
for x in a:
    print(x)
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
#output:
a = 'Hyd'
for x in a:
    print(x)

How  to  print  each  element  of   range(5)  with  for  loop

#Output:
a = range(5)
for x in a:
    print(x)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)

#output:
10
30
50

20
40
60

(10, 20)
(30, 40)
(50, 60)

10
30
50

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') 
#ouput: 
10...20
30...40
50...60
for  x ,  y  in   a:
	print(x , y
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')

for  x  in   123:
        print(x)
#int object is not literable

# Find  outputs  (Home  work)
for  x   in   ():
        print(x)#empty
for  x   in  []:
        print(x)#empty
for  x   in   {}:
        print(x)#empty
for  x   in   set():
        print(x)#empty
for  x   in   '':
        print(x)#empty
for  x  in  range(10 , 10):
	print(x)#empty
for  x  in   range():
	print(x)#Error
for  x  in   (25):
	print(x)#Error

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
#Output:
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(a[i])

a = [25 , 10.8 , 'Hyd' , True]
for x in a:
    print(x)

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
#Output:
a = [25 , 10.8 , 'Hyd' , True]
a.reverse()
for x in a:
    print(x)

a = [25 , 10.8 , 'Hyd' , True]
a.reverse()
for i in range(len(a)):
    print(a[i])

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
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

#Output:
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
i=0
for x in a:
    c.append(a[i]+b[i])
    i+=1
print(c)

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
#Output:
a :   [11, 21, 16, 19]
b :   [10, 20, 15, 18]

'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines
'''
#Output:
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

i=1
print('first 20 even numbers:')
while i<=20:
    print(2*i)
    i+=1
    
'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

i=1
print('first 20 odd numbers:')
while i<=20:
    print(2*i-1)
    i+=1
    
'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

i=1
n=int(input('enter value of n: '))
print('Natural Numbers: ')
while i<=25:
    print(i*1)
    i+=1
    
'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
#Output:
i=10
while i>1:
    print(i-1)
    i-=1

'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
i=1
total=0
while i<=20:
    even=2*i
    total+=even
    i+=1
print('sum of first 20 even numbers: ',total)
    
'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
i=1
total=0
while i<=20:
    even=2*i-1
    total+=even
    i+=1
print('sum of first 20 even numbers: ',total)
    
 '''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''

a = 1.1
sum = 0
n= int(input('enter number: '))
for i in range(n):
  sum += a*i
  sum+=1
print(sum)


'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

n = int(input("Enter value of n:"))
sum = 0
for i in range(n+1):
 sum += 2*i
print("Sum of first 20 even numbers: ",sum)

'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

n = int(input("Enter value of n:"))
sum = 1
for i in range(n+1):
 sum += 2*i-1
print("Sum of first 20 odd numbers: ",sum)

'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
n = int(input("Enter value of n:"))
sum = 0
for i in range(1,n+1):
 sum += i
print("Sum: ",sum)


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
#output:
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
	continue
	print('Sec')
#_Error

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
#Output:
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
	break
	print('Sec')
  #Error 