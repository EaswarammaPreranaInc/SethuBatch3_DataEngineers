''
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
units = int(input('Enter  units :   '))   #   175
match  units // 100:
	case  0:   #   units  between  0  and  99
				cost = units * 3.00
	case  1:  #  units  between  100 and  199
				cost =  100 * 3.00 + (units - 100) * 3.50
	case  2:
				cost =  100 * 3.00 + (units - 100) * 3.50+(units - 200)*4.00
	case  3:
				cost = 100 * 3.00 + (units - 100) * 3.50+(units - 200)*4.00+(units - 300)*4.50
	case  4:				
				cost = 100 * 3.00 + (units - 100) * 3.50+(units - 200)*4.00+(units - 300)*4.50+(units - 700)*4.50
print('Bill  amount  :  ' , cost)


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

i=int(input("enter value of x:"))
print("Fibonacci series")
a=0
b=1
while a<i:
	print(a)
	c=a+b
	a=b
	b=c


"""
OUt put
enter value of x:10
Fibonacci series
0
1
1
2
3
5
8
"""

# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
for list  in  [10 , 20 , 15 , 18]
print() 
How  to  print  each  character  of   string  'Hyd'  with  for  loop
for  x in 'Hyd'
print()
How  to  print  each  element  of   range(5)  with  for  loop



# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)#10 30 50 
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)#20 40 60 
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)#10 : 20 , 30 : 40 , 50 : 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)#10 : 20 , 30 : 40 , 50 : 60

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')#10 : 20 ... 30 : 40
for  x ,  y  in   a:
	print(x , y #error no )
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')#10 : 20 ... 30 : 40


# Identify  error  (Home  work)
for  x  in   123:
        print(x)#error due to no sequences in for loop


# Find  outputs  (Home  work)
for  x   in   ():
        print(x)#<emty>
for  x   in  []:
        print(x)#<emty>
for  x   in   {}:
        print(x)#<emty>
for  x   in   set():
        print(x)#<emty>
for  x   in   '':
        print(x)#<emty>
for  x  in  range(10 , 10):
	print(x)#<emty>
for  x  in   range():
	print(x)#<emty>
for  x  in   (25):
	print(x)#error due to it not sequences


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #(1,1) (2,2) (3,3) (0,4)
	print('Hello')#4 times hello
print('Bye')#Bye

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop') #print(len(a))                           
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')#for x in a:
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
#print(a[0],a[2],a[3],a[4])

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')# a[0:5:1]
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop # for x in a[-1:-4:1]  
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)##print(a[-4],a[-2],a[-1]))

'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
"""
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

"""
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for i in range(len(a)):
	c.append(a[i]+b[i])
	print(c)
'''
OUT PUT
Enter  1st  list  :  10 , 20 , 15 , 18
Enter  2nd  list  :  30 , 40 , 35 , 12 , 100 , 200 , 300
[40]
[40, 60]
[40, 60, 50]
[40, 60, 50, 30]
'''


#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)#10 , 20 , 15 , 18
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)#10 , 20 , 15 , 18

Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines
'''
n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    
    print(" " * spaces + "*" * stars)

""""
OUT PUT
Enter number of lines: 7
      *
     ***
    *****
   *******
  *********
 ***********
*************
""""

'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
print("first  20  even  numbers ")
i=1
while i<=20:
	print(2*i)
	i+=1
print('bye')

"""
OUT PUT
first  20  even  numbers
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
bye
"""

'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
print("first  20  odd  numbers ")
i=1
while(i<=20):
	print(2*i-1)
	i+=1
"""
OUT PUT
first  20  odd  numbers
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
"""
'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
a=int(input("enter value of n:"))
print('Natural Number')
i=1
while i<=a:
	print(i)
	i+=1
"""
OUTPUT
enter value of n:25
Natural Number
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

"""
'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
a=int(input("enter value of n:"))
print('Natural Number')
i=1
while i<=a:
	print(i)
	i+=1

"""
enter value of n:25
Natural Number
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
"""
'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
i=10
while i>=1:
	print(i)
	i-=1
"""
OUt put
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

"""



''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
	
a = int(input('how many terms would you like to add:'))
sum=0
sum=+1.1*i
for i in range(1,n):
	sum=+1.1*i
	print('sum',sum)


'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop

'''
sum = 0

for i in range(1, 21):
    sum = sum+ (2 * i - 1)
print("sum of first 20 even number: " sum)
'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop


n = int(input("Enter value of n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)


'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''


# Find  outputs  (Home  work)                             
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')

# End of loop
print('Outside loop')#Outside loop

OUT PUT
 Sec
                     Hello
                     2
                     Sec
                     ....  
                     7
                    Sec
                   Hello
                 Outside loop






# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')#ERROR ITS ONLY n loop

 # Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)#1,2,3,....
	if   i % 3 == 0:
		break
	else:
		print('Sec')#sec
	print('Hello')#hello


# End  of  the  loop
print('Outside loop')#Outside loop
# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')#error
	break
	print('Sec')