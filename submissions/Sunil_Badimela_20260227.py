'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''# Input


x = int(input("Enter number of terms: "))

# First two terms
a = 0
b = 1

count = 0

while count < x:
    print(a, end=" , ")
    
    # Update values
    c = a + b
    a = b
    b = c
    
    count += 1


output

0 , 1 , 1 , 2 , 3 , 5 , 8




# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop



lst = [10, 20, 15, 18]

for i in lst:
    print(i)

output
10
20
15
18





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

output
{10:20, 30:40, 50:60}

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
for  x ,  y  in   a:
	print(x , y
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')


output
10...20
30...40
50...60

ERROR

Same Error



# Find  outputs  (Home  work)
for  x   in   ():
        print(x)
for  x   in  []:
        print(x)
for  x   in   {}:
        print(x)
for  x   in   set():
        print(x)
for  x   in   '':
        print(x)
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():
	print(x)
for  x  in   (25):
	print(x)

output
() → empty tuple
[] → empty list
{} → empty dictionary
set() → empty set
'' → empty string
Nothing prints (No output)
ERROR
ERROR
ERROR




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
 


a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))

c = []

for i in range(len(a)):     # iterate based on first list length
    c.append(a[i] + b[i])

print('3rd list : ', c)

output
3rd list :  [40, 60, 50, 30]

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

print('Indexed for loop')

for i in range(2, 5):   # 2 to 4
    print(a[i])

output
Indexed for loop
Hyd
True
(3+4j)





#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

print('Indexed for loop')

for i in range(2, 5):   # 2 to 4
    print(a[i])


output
Indexed for loop
Hyd
True
(3+4j)



'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''


output

    *
   ***
  *****
 *******
*********




'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

i = 1

while i <= 20:
    print(2 * i, end=" ")
    i += 1

output
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40




'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''


i = 1

while i <= 20:
    print(2 * i - 1, end=" ")
    i += 1
 
output

1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39



'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

n = int(input("Enter value of n: "))

i = 1

while i <= n:
    print(i, end=" ")
    i += 1

output
1 2 3 4 5


'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
i = 10

while i >= 1:
    print(i, end=" ")
    i -= 1

output


10 9 8 7 6 5 4 3 2 1




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

output
Sum = 6.6




'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

total = 0

for i in range(1, 21):
    total = total + 2 * i

print("Sum of first 20 even numbers =", total)

output
Sum of first 20 even numbers = 420



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
output
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

output
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

output
error
error







