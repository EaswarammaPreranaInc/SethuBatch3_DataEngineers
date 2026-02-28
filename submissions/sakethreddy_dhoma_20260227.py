Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
# Fibonacci Series using only while loop

x = int(input("Enter value of x : "))

a = 0
b = 1
count = 0

print("Fibonacci Series")

while count < x:
    print(a)      # 0 1 1 2 3 5 8 13 ...
    c = a + b
    a = b
    b = c
    count += 1

    
# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
for x in [10, 20, 15, 18]:
    print(x)      # 10
                  # 20
                  # 15
                  # 18
print()           # (blank line)
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
for ch in 'Hyd':
    print(ch)     # H
                  # y
                  # d
print()           # (blank line)
How  to  print  each  element  of   range(5)  with  for  loop
for x in range(5):
    print(x)      # 0
                  # 1
                  # 2
                  # 3
                  # 4



# Find outputs (Home work)
for x in {10: 20, 30: 40, 50: 60}.keys():
    print(x)        # 10
                    # 30
                    # 50
print()             # (prints blank line)

for x in {10: 20, 30: 40, 50: 60}.values():
    print(x)        # 20
                    # 40
                    # 60
print()             # (prints blank line)

for x in {10: 20, 30: 40, 50: 60}.items():
    print(x)        # (10, 20)
                    # (30, 40)
                    # (50, 60)
print()             # (prints blank line)

for x in {10: 20, 30: 40, 50: 60}:
    print(x)        # 10
                    # 30
                    # 50
# Find outputs  (Home  work)
a = {10: 20, 30: 40, 50: 60}
for x, y in a.items():
    print(x, y, sep='...')      # 10...20
                                # 30...40
                                # 50...60


# Identify  error  (Home  work)
for  x  in   123: #'int' object is not iterable
        print(x)


# Find  outputs  (Home  work)
for x in ():
    print(x)        # No output Error

for x in []:
    print(x)        # No output

for x in {}:
    print(x)        # No output

for x in set():
    print(x)        # No output

for x in '':
    print(x)        # No output

for x in range(10, 10):
    print(x)        # No output

for x in range():
    print(x)        #  range expected at least 1 argument

for x in (25):
    print(x)        #'int' object is not iterable

#  Nested  Loop  demo  program
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)      # 1 1
                         # 1 2
                         # 1 3
                         # 1 4
                         #Hello
                         # 2 1
                         # 2 2
                         # 2 3
                         # 2 4
                         #Hello
                         # 3 1
                         # 3 2
                         # 3 3
                         # 3 4
    print('Hello')       # Hello
print('Bye')             # Bye






# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
    print(f'{i} {a[i]})')
print('For each loop')
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for i in range(len(a)+1):
    print(a[i-1])
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)



print("print  list  elements  from  indexes  2  to  4  without  slice")
a = eval(input('Enter list  :  '))
for i in range(2,5):
    print(a[i])


#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)#[11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)#a = [10 , 20 , 15 , 18]
'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''
n = int(input("Enter number of lines: "))
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
'''
a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))

c = []

for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])

print('3rd list :', c)
print("program  to  print  first  20  even  numbers ")
i=1
while(i<=20):
    print(f'{2*i}')
    i=i+1

print("program  to  print  first  20  odd  numbers ")
i=1
while(i<=20):
    print(f'{2*i-1}')
    i=i+1


print("program  to  print  first  n  natural  numbers ")
a=int(input("enter value of a:"))
i=1
print("Natural Numbers")
while(i<=a):
    print(f'{i}')
    i=i+1


print("program  to  print  10  ,  9  ,   8  ,  ..... 1")
print("Numbers from 10 down to 1 in step 1")
i=10
while(i>=1):
    print(i)
    i=i-1

print("program  to  determine  1.1 + 2.2 + 3.3 + .... n terms")
n=int(input("How many terms would you like to add"))
sum=0
for i in range(n):
    sum=sum+1.1*i
print(f'sum:{sum}')

print("Sum of first 20 even numbers")
sum=0
for i in range(20):
    sum=sum+2*i
print(f'sum:{sum}')

print("Sum of first 20 odd numbers")
sum=0
for i in range(n):
    sum=sum+2*i-1
print(f'sum:{sum}')

print("program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2)")
n=int(input("How many terms would you like to add"))
sum=0
for i in range(1,n):
    sum=sum+i
print(f'sum:{sum}')

#Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
'''Output:
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


# Identify Error  (Home  work)
'''if ():
	print('Hyd')
	continue#Indentation error
	print('Sec')'''


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
'''Output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop
'''


# Identify Error  (Home  work)
'''if(10 , 20 , 30):
	print('Hyd')
	break #Error break cannot be used without loops
	print('Sec')'''