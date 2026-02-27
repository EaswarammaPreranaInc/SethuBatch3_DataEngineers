#1
'''
Write a program to determine bill amount and input is units

Units                            Cost
---------------------------------------------------
First 100 units(0 - 99)          Rs. 3.00 / unit

Next 100 units(100 - 199)        Rs. 3.50 / unit

Next 200 units(200 - 399)        Rs. 4.00 / unit

Next 300 units(400 - 699)        Rs. 4.50 / unit

Above 700 units(units >= 700)    Rs. 5.00 / unit
---------------------------------------------------
Let units be 1200
What is the bill amount? ---> 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + 500 * 5.00

Hint: Use match ... case but not if...else
'''
units = int(input('Enter units : '))  # e.g., 1200
match units // 100:
    case 0: # 0-99
        cost = units * 3.00
    case 1: # 100-199
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 | 3: # 200-399
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6: # 400-699
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _: # 700+
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print('Bill amount: ', cost)



#2
'''
Write a program to print fibonacci series upto x

Let input be 10
What are the outputs? --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , 13

1) What is 10th term? ---> 9th term + 8th term
   What is 3rd term? ---> 2nd term + 1st term
   What is ith term? ---> (i - 1)th term + (i - 2) term

2) What are the first two terms? ---> 0 and 1

3) Hint: Use while loop
'''
x = int(input("Enter limit: "))
a, b = 0, 1
while a <= x:
    print(a, end=" ")
    a, b = b, a + b



#3
# Find outputs (Homework)
a = [10 , 20 , 15 , 18]
#How to print each element of list [10 , 20 , 15 , 18] with for loop
for x in a:
    print(x)
print()

a = 'Hyd'
#How to print each character of string 'Hyd' with for loop
for x in a:
    print(x)
print()

#How  to  print  each  element  of   range(5)  with  for  loop
for x in range(5):
    print(x)



#4
# Find outputs (Homework)
for x in {10 : 20 , 30 : 40 , 50 : 60} . keys():
    print(x) #10<next line>20<next line>30
print() #Empty
for x in {10 : 20 , 30 : 40 , 50 : 60} . values():
    print(x) #20<next line>40<next line>60
print() #Empty
for x in {10 : 20 , 30 : 40 , 50 : 60} . items():
    print(x) #(10,20)<nest line>(30,40)<next line>(50,60)
print() #Empty
for x in {10 : 20 , 30 : 40 , 50 : 60}:
    print(x) #10<next line>20<next line>30



#5
# Find outputs (Homework)
a = {10 : 20 , 30 : 40 , 50 : 60}
for x , y in a . items():
    print(x , y , sep = '...') # 10...20 <next line> 30...40 <next line> 50...60
for x , y in a:
    print(x , y) # Error as one can not unpack non-iterable int object
for x , y in {10 : 20 , 30 : 40 , 50 : 60}:
    print(x , y , sep = '...') #Error: cannot unpack non-iterable int object



#6
# Identify error (Homework)
for x in 123: #Error as a non-sequence object can't be iterated i.e. '123' can't be iterated
    print(x)



#7
# Find outputs (Homework)
for x in ():
    print(x) #Empty
for x in []:
    print(x) #Empty
for x in {}:
    print(x) #Empty
for x in set():
    print(x) #Empty
for x in '':
    print(x) #Empty
for x in range(10 , 10):
    print(x) #Empty
for x in range(): #Error as a range() object should at least have one argument
    print(x)
for x in (25): #Error as a non-sequence object can't be iterated i.e. '123' can't be iterated
    print(x)



#8
#  Nested  Loop  demo  program
for i in range(1 , 4):
    for j in range(1 , 5):
            print(i , j)  # 1 1 | 1 2 | 1 3 | 1 4 # 2 1 | 2 2 | 2 3 | 2 4 # 3 1 | 3 2 | 3 3 | 3 4
    print('Hello') # Hello | Hello | Hello (after each inner loop finishes)
print('Bye') #Bye



#9
# How to print each element and the corresponding index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed based for loop')
#How to print each element and the corresponding index with index based for loop
for i in range(len(a)):
    print(i, a[i])
print('For each loop')
#How to print each element and the corresponding index with for...each loop (Do not use 2nd variable)
for i, val in enumerate(a):
    print(i, val)



#10
# How to print list elements in reverse order without slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
#How  to print each element of list in reverse order with indexed based for loop
for i in range(len(a)-1, -1, -1):
    print(a[i])
#How to print each element of list in reverse order with for each loop (Do not use 2nd variable and slice)
for x in reversed(a):
    print(x)



#11
'''
Write a program to add two lists and store results in 3rd list

1st list ---> [10 , 20 , 15 , 18]

2nd list ---> [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd list ---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint: Use append() method
'''
a = eval(input('Enter 1st list:  '))
b = eval(input('Enter 2nd list:  '))
c = []
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])
print('3rd list: ' , c)
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
for x, y in zip(a, b):
    c.append(x + y) 



#12
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2, 5):
    print(a[i])
    
print('For each loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
for i, val in enumerate(a):
    if 2 <= i <= 4:
        print(val)



#13
#  Tricky program
#  Find outputs (Homework)
a = [10 , 20 , 15 , 18]
for i in range(len(a)):
    a[i] += 1
print('a : ' , a) #a :  [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for x in b:
    x += 1 
print('b : ' , b) #b :  [10, 20, 15, 18]



#14
'''
Write a program to print full pyramid
<4 spaces>*
<3 spaces>***
<2 spaces>*****
<1 space>*******
<0 spaces>*******

Input  is  number  of  lines
'''
n = int(input("How many lines: "))
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))



#15
'''
(Homework)
Write a program to print first 20 even numbers 

1) What are the first 20 even numbers? ---> 2 , 4 , 6 , 8 ,.... 40

2) What is printed in general? --->  2 * i where i varies from 1 to 20

3) Hint: Do not use range object

4) Use while loop
'''
i=1
while i<=20:
    print(2*i)
    i+=1



#16
'''
Write a program to print first 20 odd numbers

1) What are the first 20 odd numbers? ---> 1 , 3 , 5 , .... 39

2) What is printed in general? ---> 2 * i - 1  where i varies from 1 to 20

3) Hint: Do not use range  object

4) Use while loop
'''
i=1
while i<=20:
    print(2*i-1)
    i+=1



#17
'''
Write a program to print natural numbers 1 , 2 , 3 .... n and ask user to input value of 'n'

What is printed in general? ---> 'i' where 'i' varies from 1 to n

1) Hint: Do not use range object

2) Use while loop
'''
n = int(input("Enter the value of n: "))
i=1
while i<=n:
    print(i)
    i+=1



#18
'''
Write a program to print 10 , 9  , 8 , ..... 1

What is printed in general?  ---> 'i' where 'i' varies from 10 downto 1 in steps of -1

1) Hint: Do not use range object

2) Use while loop
'''
i=10
while i>=1:
    print(i)
    i-=1



#19
'''
Write a program to determine 1.1 + 2.2 + 3.3 + .... n terms

1) sum = 0 + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What is added to sum in general? ---> 1.1 * i  where 'i' varies from 1 to n

3) Use for loop
'''
n = int(input("Enter number of terms: "))
total_sum = 0.0

for i in range(1, n + 1):
    total_sum += 1.1 * i

print(f"Sum: {total_sum:.2f}")



#20
'''
Write a program to determine sum of first 20 even numbers

1) sum = 0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What is added to sum in general? --->  2 * i where 'i' varies from 1 to 20

3) Use for loop
'''
total_sum = 0

for i in range(1, 21):
    total_sum += 2 * i

print("Sum of first 20 even numbers:", total_sum)



#21
'''
Write a program to determine sum of first 20 odd numbers

1) sum =  0 + (2 * 1 - 1) + (2 * 2 - 1) + (2 * 3 - 1) + ... (2 * 20 - 1)

2) What is added to sum in general? ---> 2 * i - 1  where 'i' varies from 1 to 20

3) Use for loop
'''
total_sum = 0

for i in range(1, 21):
    total_sum += (2 * i - 1)

print("Sum of first 20 odd numbers:", total_sum)



#22
'''
Write a program to determine 1 + 2 + 3 + .... + n without using formula n * (n + 1) / 2

What is added to sum in general? --->  'i' where 'i' varies from 1 to n

Hint: Use for loop
'''
n = int(input("How many terms would you like to add: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"Sum: {total_sum}")



#23
# Find outputs (Homework)
for i in range(1 , 8):
    print(i) # 1 | 2 | 3 | 4 | 5 | 6 | 7
    if i % 3  == 0: # Skips 'Sec' and 'Hello' when i is 3 or 6
            continue
    else:
            print('Sec') # Sec | Sec | (skip) | Sec | Sec | (skip) | Sec
    print('Hello') # Hello | Hello | (skip) | Hello | Hello | (skip) | Hello
# End of loop
print('Outside loop') #Outside loop



#24
# Identify Error (Homework)
if ():
    print('Hyd')
    continue #Error as continue statement can't be used under if statement but can be used under only for and while loops
    print('Sec')



#25
# Find outputs (Homework)
for i in range(1 , 8):
    print(i) # 1 | 2 | 3
    if i % 3 == 0:
        break # Loop terminates here when i is 3
    else:
        print('Sec') # Sec | Sec
    print('Hello') # Hello | Hello
# End of the loop
print('Outside loop') #Outside loop



#26
# Identify Error (Homework)
if(10 , 20 , 30):
    print('Hyd')
    break #Error as break statement can't be used under if statement but can be used under only for and while loops
    print('Sec') 