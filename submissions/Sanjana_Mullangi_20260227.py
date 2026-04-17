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
#300+350+800+

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter  units :   '))   #   175
match  units // 100:
	case  0:   #   units  between  0  and  99
				cost = units * 3.00
				print(cost)
	case  1:  #  units  between  100 and  199
				cost =  (100 * 3.00) + (units - 100) * 3.50
				print(cost)
	case  2|3:  #  units  between  200 and  399
				cost = (100 * 3.00) +  (100 * 3.50) + (units-200)*4.00
				print(cost)
	case  4|5|6:   #  units  between  400 and  699
				cost = (100 * 3.00) +  (100 * 3.50) + (200*4.00) + (units-300)*4.50
				print(cost)
	case  _:	#  units  between  700 and above
				cost = (100 * 3.00) +  (100 * 3.50) + (200*4.00) + (300*4.50) +(units-700)*5.0
				print(cost)
print('Bill  amount  :  ' ,cost)


'''Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop

Sample output:
1)Enter the value of x:10
Fibonnaci series:
0
1
1
2
3
5
8
2)Enter the value of x:1
Fibonnaci series:
0
1
1
3)Enter the value of x:0
Fibonnaci series:
0'''

x=int(input("Enter the value of x:"))
a=0
b=1
print(f'Fibonnaci series:')
while(a<=x):
    print(a)
    c=a+b
    a=b
    b=c
    


'''# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()'''

a= [10,20,15,18]
for i in range(4):
    print(f'Elements of list: {i}')

How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
a="Hyd"
for i in range(3):
    print(f'Element of string: {a[i]}')
    
How  to  print  each  element  of   range(5)  with  for  loop
    for i in range(5):
        print(i)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
#10<next line>30<next line>50<next line>space
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
#20<next line>40<next line>60<next line>space
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
#(10,20)<next line>(30,40)<next line>(50,60)<next line>
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
#10<next line>30<next line>50'''
    
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') #[(10,20)...(30,40)...(50,60)]
for  x ,  y  in   a:
	print(x , y  #error-cannot unpack items
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') #error-cannot unpack items
    
# Identify  error  (Home  work)
for  x  in   123:
        print(x)#for loop only works for sequence not for single elements '''
        
# Find  outputs  (Home  work)
for  x   in   ():
        print(x)#error-for loop only works for sequence and tuple is empty 
for  x   in  []:
        print(x)#for loop only works for sequence and given list is empty
for  x   in   {}:
        print(x)#for loop only works for sequence and the given dictionary is empty
for  x   in   set():
        print(x) #for loop works for sequences and given set is empty
for  x   in   '':
        print(x)#for loop only works for sequence not for non sequence elements and given string is empty
for  x  in  range(10 , 10):
	print(x)#prints nothing
for  x  in   range():
	print(x)#the given range is empty
for  x  in   (25):
	print(x)#for loop only works for sequence not for non sequence elements'''
    
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')

#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop'''
a = [25 , 10.8 , 'Hyd' , True]
for i in range(4):
	print(f'Indexes are: {i}')
    print(f'Elements of list: {a[i]}')
print('For each loop')

#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
a = [25 , 10.8 , 'Hyd' , True]
for 

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method

list1 = [10 , 20 , 15 , 18]
list2 = [30 , 40 , 35 , 12 , 100 , 200 , 300]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print("3rd list :", list3)


a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
#Indexed Based For Loop'''
a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = []
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])
print('3rd list :', c)
#For-Each Loop
a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = []
for x in a:
    if a.index(x) < len(b):
        c.append(x + b[a.index(x)])
print('3rd list :', c)

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) #a :  [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) #b :  [10, 20, 15, 18]


Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines

Sample output:
    *
   ***
  *****
 *******
*********

n=int(input("enter the number of lines in which * should be printed:"))
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2*i - 1))



(Home  work)
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

print(f"First 20 even numbers: ") #y shouldn't we consider i value to be 2 because it is an even number
i=1
while (i<=20):
    print(f'{2 * i}')
    i=i+1



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

i=1
print(f"First 20 odd numbers:")
while(i<=20):
    print(f"{(2*i-1)}")
    i=i+1


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

n=int(input("Enter the value of n: "))
i=1
while (i<=n):
    print (i)
    i=i+1

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

a=10
while(a>=10):  #a<=10?
    for i in range (1,10):
        print(a)
        a=a-1
print(f"Numbers from 10 down to 1 in steps of -1: {a}")
        


Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
Sample outputs:
1)How many terms would you like to add: 5
Sum: 16.5

a=int(input("How many terms would you like to add:"))
sum=0
for i in range(1,a+1):
    sum=sum+1.1*i
print(f"Sum : {sum}")



Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop

Sample output:
1)Sum of first 20 even numbers : 420
a=20
sum=0
for i in range (1,2*a+1):
    if(i%2==0):
        sum=sum+i
print(f"Sum of first 20 even numbers: {sum}")


Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop

Sample output:
1)Sum of first 20 odd numbers: 400
a=20
sum=0
for i in range(1,2*a):
    if(i%2!=0):
        sum=sum+i
print(f'Sum of first 20 odd numbers : {sum}')


Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop

Sample output:
1)How many terms would you like to add: 10
Sum: 55

a=int(input("How many terms would you like to add:"))
sum=0
for i in range(1,a+1):
	sum=sum+i
print(f'Sum : {sum}')




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


# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')
#continue cannot be used when there is no for or else loop
    

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


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
#break cannot be used without for or while loop 








