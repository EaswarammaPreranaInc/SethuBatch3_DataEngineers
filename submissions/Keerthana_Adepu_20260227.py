#Outputs Homework #1
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
'''
for x in [10 , 20 , 15 , 18]:
        print(x)
'''
print() # prints nothing and moves to the next line
How  to  print  each  character  of   string  'Hyd'  with  for  loop
'''
for x in 'Hyd':
        print(x)
'''
print() # prints nothing and moves to the next line
How  to  print  each  element  of   range(5)  with  for  loop
'''
for x in range(5):
        print(x)
'''


#Outputs Homework #2
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10 <> 30 <> 50
print() # prints nothing and moves to the next line
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20 <> 40 <> 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10 , 20) <> (30 , 40) <> (50 , 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10 <> 30 <> 50
	

#Outputs Homework #3
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20 <> 30...40 <> 50...60
for  x ,  y  in   a:
	print(x , y) # error 
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') 
              

#Identify Error Homework #1
for  x  in   123:
        print(x) # error because for loops cannot be used for non-sequence objects
              

#Outputs Homework #4
for  x   in   ():
        print(x) # prints nothing
for  x   in  []:
        print(x) # prints nothing
for  x   in   {}:
        print(x) # prints nothing
for  x   in   set():
        print(x) # prints nothing
for  x   in   '':
        print(x) # prints nothing
for  x  in  range(10 , 10):
	print(x) # prints nothing
for  x  in   range():
	print(x) # error because range object cannot be empty
for  x  in   (25):
	print(x) # error because for loop can't iterate a non-sequence
              

#Nested Loop
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  
	print('Hello')
print('Bye')

'''
1 1
1 2
1 3
1 4
Hello
Bye
2 1
2 2
2 3
2 4
Hello
Bye
3 1
3 2
3 3
3 4
Hello
Bye
'''

#How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
'''
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(a[i])
'''
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
'''
for x in a:
        print(x)
'''
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)


#How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
'''
for i in range(len(a)):
        print(a[-i])
'''
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
'''for x in a:
'''

#How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
'''
for i in range(2 , 5):
        print(a[i])
'''
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
'''for x in a:
'''

#Tricky Program
##Outputs Homework #5
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # [11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # [10 , 20 , 15 , 18]


#Outputs Homework #6
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
'''
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
'''


#Identify Error Homework #2
if ():
	print('Hyd')
	continue
	print('Sec') # error because continue is not used in a loop
	

#Outputs Homework #7
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
'''
1
Sec
Hello

2
Sec
Hello

3

Outside loop
'''


#Identify Error Homework #3
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec') # error because break is not used inside a loop



#Programming Homework #1
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

units = int(input('Enter  the number of units:'))   #   175
match  units // 100:
        case  0:   #   units  between  0  and  99
				cost = units * 3.00
	case  1:  #  units  between  100 and  199
				cost =  100 * 3.00 + (units - 100) * 3.50
	case  2 | 3:
				cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
	case  4 | 5 | 6:
				cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
	case  _:				
				cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
print('Bill  amount  :  ' , cost)



#Programming Homework #2
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
'''
Sample Output 1:

Enter the value of x:10
Fibonnaci series:
0
1
1
2
3
5
8
Press any key to continue...


Sample Output 2:

Enter the value of x:1
Fibonnaci series:
0
1
1
Press any key to continue...


Sample Output 3:
Enter the value of x:0
Fibonnaci series:
0
Press any key to continue...
'''
x = int(input('Enter the value of x:'))
a = 0
b = 1
print('Fibonacci Series until {x}:')
while a <= x:
    print(a)
    c = a + b
    a = b
    b = c


#Programming Homework #4
'''Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
list1 = [10 , 20 , 15 , 18]
list2 = [30 , 40 , 35 , 12 , 100 , 200 , 300]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print("3rd list :", list3)

'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
'''
#Indexed Based For Loop
a = eval(input('Enter the 1st List:'))
b = eval(input('Enter the 2nd List:'))
c = []
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])
print('The 3rd List is:', c)


#Programming Homework #5
'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  spaces>***
<0  spaces>***

Input  is  number  of  lines
'''
n = int(input('Enter the number of lines:'))

for i in range(1 , n + 1):
    print(' ' * (n - i), end='')      # spaces
    print('*' * (2 * i - 1))          # stars



#Programming Homework #6
'''
Write  a  program  to  print  first  20  even  numbers 
1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40
2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20
3) Hint:  Do  not  use  range  object
4) Use  while  loop
Sample output:
1)First 20 even numbers:
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
Bye
'''

print('First 20 Even Numbers:')

i = 1
while i <= 20:
    print(2 * i)
    i += 1



#Programming Homework #7
'''
Write  a  program  to  print  first  20  odd  numbers
1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39
2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
3) Hint:  Do  not  use  range  object
4) Use  while  loop
Sample output:
1)First 20 odd numbers
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
print('First 20 Odd Numbers:')

i = 1
while i <= 20:
    print(2 * i - 1)
    i += 1



#Programming Homework #8
'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'
What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n
1) Hint:  Do  not  use  range  object
2) Use  while  loop
Sample output:
1)Enter the value of n: 25
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
21
22
23
24
25
'''
n = int(input("Enter the value of n: "))

print(f'Natural Numbers until {n}:')

i = 1
while i <= n:
    print(i)
    i += 1



#Programming Homework #9
'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1
1) Hint:  Do  not  use  range  object
2) Use  while  loop
Sample output:
1)Numbers from 10 downto 1 in steps of -1
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

print('Numbers from 10 downto 1 in steps of -1')

i = 10

while i >= 1:
    print(i)
    i -= 1



#Programming Homework #10
'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......
2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n
3) Use  for  loop
Sample outputs:
1)How many terms would you like to add: 5
Sum: 16.5
'''
n = int(input('Enter the number of terms you would like to add:'))

total = 0

for i in range(1 , n + 1):
print(f'Sum: {total += 1.1 * i}')



#Programming Homework #11
'''
Write  a  program  to  determine  sum  of  first  20  even  numbers
1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20
2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20
3) Use  for  loop
Sample output:
Sum of first 20 even numbers : 420
'''
total = 0

for i in range(1 , 21):
        print(f'The sum of first 20 Even Numbers is: {total += 2 * i}')



#Programming Homework #12
'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers
1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)
2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20
3) Use  for  loop
Sample output:
1)Sum of first 20 odd numbers: 400
'''
total = 0

for i in range(1 , 21):
        print(f'The sum of first 20 Odd Numbers: {total += 2 * i - 1}')



#Programming Homework #13
'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
Hint:  Use  for  loop
Sample output:
1)How many terms would you like to add: 10
Sum: 55
'''

n = int(input('Enter the number of terms you would like to add:'))

total = 0

for i in range(1 , n + 1):
        print(f'Sum: {total += i}')





            
