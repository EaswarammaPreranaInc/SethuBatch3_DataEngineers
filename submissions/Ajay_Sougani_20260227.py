n = int(input("Enter the n value: "))
a = 0
b = 1
next=b
count = 0
while(count <=n):
	print(a, end = ' ')
	a=b;
	b=next;
	next=a+b;
	count += 1;

How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print() 
# a = [10, 20, 15, 18]
  for i in list: 
	print(i)
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print() 
# str = 'Hyd'
  for i in 'Hyd': 
	print(i)
How  to  print  each  element  of   range(5)  with  for  loop 
# for i in range(5):
	 print(i)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10 30 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20 40 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10, 20) (30, 40) (50, 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10 30 50

a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')  #(10...20) (30...40) (50...60)
for  x ,  y  in   a:
	print(x , y) # cannot unpack non-iterable int object
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # Error

# Identify  error  
for  x  in   123:
        print(x)  # non-sequence objects are not iterable

for  x   in   ():
        print(x) # Nothing
for  x   in  []:
        print(x) # Nothing
for  x   in   {}:
        print(x) # Error
for  x   in   set():
        print(x) # Nothing
for  x   in   '':
        print(x) # Nothing
for  x  in  range(10 , 10):
	print(x) # Nothing
for  x  in   range():
	print(x) # range object expects atleast one object
for  x  in   (25):
	print(x) # 'int' object is not iterable

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  # 
	print('Hello')                    
print('Bye')                             
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

program:
a = [25, 10.8, 'Hyd', True]
for i in range(len(a)):
   print(i, a[i])

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
program:
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)-1,-1,-1):
	print(a[i])
a = [25 , 10.8 , 'Hyd' , True]
for i in reversed(a):
	print(i)

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = []

# iterate using index (till smaller list length)
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])

print('3rd list :', c)	


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
program:
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(2,len(a)):
	print(a[i])
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in a[2:]:
	print(i)


a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a :   [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # b :   [10, 20, 15, 18]

Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines
program:
n = int(input("Enter the n value: "))
for i in range(1, n+1):
     print(" " * (n - i) + "*" * (2 * i - 1))

Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

program:
n = 2;
a =1

while(a<=20):
	print(n)
	n+=2
	a+=1

Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

program:
n=1;
a=1;
while(a<=20):
	print(n)
	n+=2;
	a+=1

Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop

program:
n = int(input("enter n value : "))
a=1
while(a<=n):
	print(a);
	a+=1

Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop

program:
n = int(input("enter n value : "))
a=1
while(n>=a):
	print(n);
	n-=1
'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
n = int(input("Enter number of terms: "))

total = 0

for i in range(1, n + 1):
    total = total + (1.1 * i)

print("Sum =", total)


'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
total = 0

for i in range(1, 21):
    total = total + (2 * i)

print("Sum  of first 20 even numbers =", total)

'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
total = 0

for i in range(1, 21):
    total = total + (2 * i - 1)

print("Sum  of first 20 odd numbers =", total)


'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''

n = int(input("Enter value of n: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)

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

# outputs  ---> 1 Sec Hello 2 Sec Hello 3 Hello 4 Sec Hello 5 Sec Hello 6 Hello 7 Sec Hello Outside loop


# Identify Error  (Home  work)
if ():
	print('Hyd') #
	continue # error 'continue' outside loop
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
print('Outside loop') # 1 sec Hello 2 sec Hello 3 Hello Outside loop


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd') # 
	break # error 'break' outside loop
	print('Sec')


