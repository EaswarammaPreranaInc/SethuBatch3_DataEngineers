Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop

x = int(input("Enter value of x: "))
a = 0
b = 1
while a<= x:
    print(a, "\n ")
    c = a + b
    a = b
    b = c

# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print() #a= [10 , 20 , 15 , 18] 
for element in a:
    print(element)

How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()#a="Hyd"
for element in a:
    print(element)
How  to  print  each  element  of   range(5)  with  for  loop #for i in range(5):
    print(i)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()  #10 20 30
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print() #20 40 60
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print() #(10, 20)
(30, 40)
(50, 60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) #10
30
50

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') 
#10...20
30...40
50...60
for  x ,  y  in   a:
	print(x , y)#error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')#error

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
	print(x)#error
for  x  in   (25):

	print(x)#error

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

a = [25, 10.8, 'Hyd', True]
for i in range(len(a)):
    print(a[i])
print("Index based for loop")

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

a = [25, 10.8, 'Hyd', True]
for i in range(len(a)-1,-1,-1):
    print(a[i])
a = [25, 10.8, 'Hyd', True]
for element in reversed(a):
    print(element)

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

a = eval(input('Enter 1st list: '))
b = eval(input('Enter 2nd list: '))
c = []

len = min(len(a), len(b))

for i in range(len):
    c.append(a[i] + b[i])

print('3rd list:', c)


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

a :   [11, 21, 16, 19]
b :   [10, 20, 15, 18]

Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines

a = int(input("Enter number of lines: "))
for i in range(1, a + 1):
    for j in range(a - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

count = 1       
num = 2
print("First 20 Even Numbers")
while count <= 20:
    print(num,"\n")
    num += 2    
    count += 1

'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

num=1
count=1
print("first 20 odd numbers")
while count <= 20:
    print(num)
    num += 2    
    count += 1  

Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop

n = int(input("Enter the value of n: "))

i = 1

while i <= n:
    print(i)
    i += 1

Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop

i = 10 
print("numbers from 10 downto 1 in steps of -1")

while i >= 1:
    print(i)
    i -= 1  

Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop

n = int(input("How many terms would like to add: "))

sum_total = 0

for i in range(1, n + 1):
    sum_total += 1.1 * i

print("Sum:", sum_total)


Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop

a = 0

for i in range(1, 21): 
    a += 2 * i 
print("Sum of first 20 even numbers:", a)

Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop

a = 0
for i in range(1, 21):  
    a += (2 * i - 1) 
print("Sum of first 20 odd numbers:", a)

Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop

n = int(input("How many terms would you like to add : "))
a = 0
for i in range(1, n + 1):
    a += i  
print("Sum :", a )

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

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')
hyd
sec

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

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
    break
	print('Sec')
sec
 
                                                           
