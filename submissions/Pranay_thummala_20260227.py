# Write  a  program  to  print  fibonacci  series  upto   x

# Let  input  be   10
# What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

# 1) What  is  10th  term ?  --->  9th  term + 8th  term
#     What  is  3rd  term ?  ---> 2nd  term + 1st  term
#     What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

# 2) What  are  the  first  two  terms ?  --->  0  and  1

# 3) Hint:  Use  while  loop

x=int(input('enter a value : '))
a=0
b=1

print('fibonacci series')
while a<=x:
    print(a)
    c=a+b
    a=b
    b=c
    

# Find  outputs  (Home  work)
# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
l=[10,20,15,18]
for i in l:
    print(i)

# How  to  print  each  character  of   string  'Hyd'  with  for  loop
s='Hyd'
for i in s:
    print(i)
# How  to  print  each  element  of   range(5)  with  for  loop
for i in range(5):
    print(i)



# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10 ,30,50
print() 
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20 , 40 , 60
print() 
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10 , 20) , (30 , 40) , (50 , 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10 , 30 , 50
      


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20 , 30...40 , 50...60
for  x ,  y  in   a:
	print(x , y) # error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # error  
	

# Identify  error  (Home  work)
for  x  in   123:
        print(x) # error sequence  expected  but  int  found
		

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # no output
for  x   in  []:
        print(x) # no output
for  x   in   {}:
        print(x) # no output
for  x   in   set():
        print(x) # no output
for  x   in   '':
        print(x) # no output
for  x  in  range(10 , 10):
	print(x) # no output
for  x  in   range(): 
	print(x) # error
for  x  in   (25):
	print(x) # error sequence  expected  but  int  found
       


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  # (1 , 1) , (1 , 2) , (1 , 3) , (1 , 4) , (2 , 1) , (2 , 2) , (2 , 3) , (2 , 4) , (3 , 1) , (3 , 2) , (3 , 3) , (3 , 4)
	print('Hello') # Hello will be printed 3 times after each inner loop execution
print('Bye') # Bye will be printed once after all the loops execution


# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for  i  in  range(len(a)):
    print(i , a[i]) # 0 25 , 1 10.8 , 2 'Hyd' , 3 True
 
# How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
for  i  in  a:
    print(a.index(i) , i) # 0 25 , 1 10.8 , 2 'Hyd' , 3 True
# How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
print('For each loop with 1 variable')
for  i  in  a:
    print(a.index(i) , i) # 0 25 , 1 10.8 , 2 'Hyd' , 3 True



#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for  i  in  range(len(a)-1 , -1 , -1):
    print(i , a[i]) # 3 True , 2 'Hyd' , 1 10.8 , 0 25
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
a = [25, 10.8, 'Hyd', True]

print("Indexed for loop")

for i in range(len(a) - 1, -1, -1):
    print(a[i])
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
print("For each loop")

for x in reversed(a):
    print(x)




#Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
a = [10, 20, 30, 40]
b = [1, 2, 3, 4]

c = []

for i in range(len(a)):
    c.append(a[i] + b[i])

print("List A:", a)
print("List B:", b)
print("Result List C:", c)
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
a = [10, 20, 30, 40]
b = [1, 2, 3, 4]

c = []

for i in range(len(a)):
    c.append(a[i] + b[i])

print("Result list:", c)


#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
a = [10, 20, 30, 40]
b = [1, 2, 3, 4]

c = []

for x in a:
    c.append(x + b[a.index(x)])

print("Result List C:", c)


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
print("Indexed for loop")

for i in range(2, 5):   # 5 because range stops before 5
    print(a[i])
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
print("For each loop")

count = 0

for x in a:
    if count >= 2 and count <= 4:
        print(x)
    count += 1




#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a :  [11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # b :  [10 , 20 , 15 , 18]


'''
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
    print(" " * (n - i) + "*" * (2 * i - 1))


'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
count = 0
num = 2

while count < 20:
    print(num)
    num = num + 2
    count = count + 1



'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

n = int(input("Enter value of n: "))

i = 1

while i <= n:
    print(i)
    i = i + 1


'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
i = 10

while i >= 1:
    print(i)
    i = i - 1


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


