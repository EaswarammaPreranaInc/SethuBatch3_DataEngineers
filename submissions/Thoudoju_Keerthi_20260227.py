
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term	
	
2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''

a = 0
b = 1
n =int(input('Enter n value : '))
while(n>=a):
	print(a)
	c=a+b
	a=b
	b=c


# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
for x in listt:
	print(x, end=", ")
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
for x in str:
	print(x, end=", ")
How  to  print  each  element  of   range(5)  with  for  loop
for x in range(5):
	print(x, end=", ")

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
#10
#30
#50

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
#20
#40
#60

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
#(10,20)
#(30,40)
#(50,60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
#10
#30
#50


 # Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
#10...20
#30...40
#50...60

for  x ,  y  in   a:
	print(x , y)
# Error

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
#error

 # Identify  error  (Home  work)
for  x  in   123:
        print(x)
#123 is not sequence


# Find  outputs  (Home  work)
for  x   in   ():
        print(x)
#empty

for  x   in  []:
        print(x)
# empty
for  x   in   {}:
        print(x)
#empty
for  x   in   set():
        print(x)
#empty

for  x   in   '':
        print(x)
#empty

for  x  in  range(10 , 10):
	print(x)
#empty

for  x  in   range():
	print(x)
#Error range should need a value
for  x  in   (25):
	print(x)
#error 25 is non -sequence

 #  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

#1 1
#1 2
#1 3
#1 4
#Hello
#2 1
#2 2
#2 3
#2 4
#Hello
#3 1
#3 2
#3 3
#3 4
#Hello
Bye

 # How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')

for i in range(len(a)):
	print(a[i])

How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)):
	print(i, a[i])

print('For each loop')
for x in a:
	print(x)

How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
for index,value in enumerate(a):
	print(index,value)

 #  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for i in range(-len(a),-1,-1):
	print(a[i])

How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(-len(a),-1,-1):
	print(a[i])

How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
for value in reversed(a):
	print(value)
 '''

Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
l1=len(a)
l2=len(b)
min = l1 if l1<l2 else l2
for i in range(min):
	c.append(a[i]+b[i])
	
print('3rd  list : ' , c)


How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for a, b in zip(a,b):
	c.append(a+b)
print('3rd  list : ' , c)


 #  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for i range(2,5):
	print(a[i])

How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i range(2,5):
	print(a[i])
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

for index,value in enumerate(a):
	if 2 <=index <=4:
		print(value)

 #  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
#a = [11 , 21 , 16 , 19]


b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)
#b = [11 , 21 , 16 , 19]


 '''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>****
<0  spaces>*****

Input  is  number  of  lines
'''

n=int(input("enter n value :"))
for i in range(1,n+1):
        print(" "*(n-i)+'*'*(2*i-1))


 '''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
for i in range(20):
	print(2*i)

 '''
 '''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
for i in range(20):
	print(2*i-1)

 '''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
i=1
n=int(input("enter n value :"))
while(i<=n):
	print(i)
	i+=1

'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
i=1
n=int(input("enter n value :"))
while(i<=n):
	print(n)
	n-=1

'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''

n=int(input("enter n value :"))
sum=0
for i in range(1,n+1):
	sum+=1.1*i
print('sum :' , sum )

'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

sum=0
for i in range(1,21):
	sum+=2*i
print('sum :' , sum )

 '''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
sum=0
for i in range(1,21):
	sum+=(2*i-1)
print('sum :' , sum )


 '''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
n=int(input("enter n value :"))
sum=0
for i in range(1,n):
	sum+=i
print('sum :' , sum )

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

#1
#Sec
#Hello
#2
#Sec
#Hello
#3
#Hello
#4
#Sec
#Hello
#5
#Sec
#Hello
#6
#Sec
#Hello
#7
#Sec
#Hello
Outside loop

 # Identify Error  (Home  work)
if ():
	print('Hyd')
	continue   # condition for continue not mentioned
	print('Sec')


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

#1
#Sec
#Hello
#2
#Sec
#Hello
#3
#Outside loop

 # Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break       # condition for break not mentioned

	print('Sec')

