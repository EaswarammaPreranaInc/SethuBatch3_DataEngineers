# 1) Write  a  program  to  print  fibonacci  series  upto   x

x = int(input('Enter value of x : '))
print('Fibonacci Series')
a = 0
b = 1
while a < x:
    print(a)
    c = a + b
    a = b
    b = c
'''
2) Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
'''
list = [10 , 20 , 15 , 18]
for i in list:
    print(i)
'''
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
'''
Str = 'Hyd'
for i in Str:
    print(i)
# How  to  print  each  element  of   range(5)  with  for  loop
for i in range (5):
    print(i)

3) # Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10<next line>30<next line>50
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20<next line>40<next line>60
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) (10,20) <nextline> (30,40) <nextline> (50,60)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10<next line>30<next line>50
'''
4) # Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20 <next line> 30...40 <next line> 50...60
for  x ,  y  in   a:
	print(x , y # Error because brace is not closed
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # Error because cant use 2 variable for unpacking
'''
'''
5) # Identify  error  (Home  work)
for  x  in   123:
        print(x) # Error because integers cannot be iterated
'''
6) # Find  outputs  (Home  work)
for  x   in   ():
        print(x) # Empty tuple
for  x   in  []:
        print(x) # Empty list
for  x   in   {}:
        print(x) # Empty dict
for  x   in   set():
        print(x) # Empty set
for  x   in   '':
        print(x) # Empty set
for  x  in  range(10 , 10):
	print(x) # Empty
for  x  in   range():
	print(x) # Error because at least 1 element is to be there to iterarte the loop
for  x  in   (25):
	print(x) # Error because integer cannot be iterated
'''
7) How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
'''
print('Index  based  for  loop')
for i in range(len(a)):
    print(a[i])

print('For  each  loop')
for x in a:
    print(x)
'''
8) How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
'''
print('Indexed  for  loop')
for i in range(len(a)-1, -1, -1):
    print(a[i])
'''
9) Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
1st  list  --->  [10 , 20 , 15 , 18]
2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]
'''

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for i in range(len(a)):
    if i < len(b):
        c.append(a[i] + b[i])
print('3rd  list : ' , c)

'''
10) How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
'''
print('Indexed  for  loop')
for i in range(2, 5):
    print(a[i])

print('for each loop')
for i in range(2, 5):
    print(i)
'''
11)Tricky  program
  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a :  [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # b :    [10 , 20 , 15 , 18]
'''
'''
12)Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********
Input  is  number  of  lines
'''
n = int(input('How many lines ? : '))
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)

'''
13) Write  a  program  to  print  first  20  even  numbers 
Use  while  loop
'''
print('First 20 even numbers')
i = 1
while i <= 20:
    print(2 * i)
    i += 1
print('Bye')

'''
14) Write  a  program  to  print  first  20  odd  numbers
Use  while  loop
'''
print('First 20 odd numbers')
i = 1
while i <= 20:
    print(2 * i - 1)
    i += 1
print('Bye')

'''
15) Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'. Use  while  loop
'''
n = int(input('Enter value of n : '))
print('Natural Numbers')
i = 1
while i <= n:
    print(i)
    i += 1
'''
16) Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
Use  while  loop
'''
print('Numbers from 10 downto 1 in steps of -1')
i = 10
while i >= 1:
    print(i)
    i -= 1
'''
17) Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms.
Use  for  loop
'''
n = int(input('How many terms would you like to add : '))
total = 0
for i in range(1, n + 1):
    total += 1.1 * i
print('Sum  :  ', total)
'''
18) Write  a  program  to  determine  sum  of  first  20  even  numbers3) Use  for  loop
'''
print('Sum of first 20 even numbers')
total = 0
for i in range(1, 21):
    total += 2 * i
print('Sum  :  ', total)
'''
19) Write  a  program  to  determine  sum  of  first  20  odd  numbers
Use  for  loop
'''
print('Sum of first 20 odd numbers')
total = 0
for i in range(1, 21):
    total += 2 * i - 1
print('Sum  :  ', total)
'''
20)Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
'''
n = int(input('How many terms would you like to add : '))
total = 0
for i in range(1, n + 1):
    total += i
print('Sum  :  ', total)

'''
21) Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop') # 1 <nextline> Sec <nextline> Hello <nextline> 2 <nextline> Sec <nextline> Hello <nextline> 3 <nextline> 4 <nextline> Sec <nextline> Hello <nextline> 5 Sec <nextline> Hello <nextline> 6 <nextline> 7 <nextline> Sec <nextline> Hello <nextline>
'''
'''
22) Identify Error  (Home  work)
if ():
	print('Hyd')
	continue # Error because cant use continue without using for or while loop
	print('Sec')
'''
'''
23)  Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')  # 1 <nextline> Sec <nextline> Hello <nextline> 2 <nextline> Sec <nextline> Hello <nextline> 3<nextline> Outside loop
'''
'''
24) # Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break           # Error because cant use break without for or while loops
	print('Sec')
'''