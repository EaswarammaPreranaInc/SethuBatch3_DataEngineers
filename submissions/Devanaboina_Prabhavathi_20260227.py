units = int(input('Enter units : ')) # Input Example: 1200
match units // 100:
    case 0: # 0 - 99
        cost = units * 3.00
    case 1: # 100 - 199
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 | 3: # 200 - 399
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6: # 400 - 699
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _: # 700 and above
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print('Bill amount : ', cost) # For 1200, output is 5300.0



x = int(input('enter value:' ))
a =  0
b = 1
while a+b < x:
    c = a+b
    a = b
    b = c
    print(c)


my_list = [10, 20, 15, 18]
for element in my_list:
    print(element)
    
my_string = 'Hyd'
for char in my_string:
    print(char)
    
my_range = range (5)
for element in my_range:
    print(range)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10 30 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) #20 40 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) #(10, 20) (30,40) (50, 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10 30 50


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20 30...40 50...60
for  x ,  y  in   a:
	print(x , y)#error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # error


# Identify  error  (Home  work)
for  x  in   123:
        print(x) # error


# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # No output
for  x   in  []:
        print(x) # No output
for  x   in   {}:
        print(x) # No output
for  x   in   set():
        print(x) # No output
for  x   in   '':
        print(x) # No output
for  x  in  range(10 , 10):
	print(x) # No output
for  x  in   range():
	print(x) # No output
for  x  in   (25):
	print(x) # No output


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j) # 1, 1,1,1  #1, 2, 3, 4
	print('Hello') #Hello Hello Hello
print('Bye')  #Bye


a = [25 , 10.8 , 'Hyd' , True]

print('Indexed based for loop')
# How to print each element and the corresponding index with index based for loop
for i in range(len(a)):
    print(f"Index: {i}, Element: {a[i]}") #Index: 0, Element: 25,Index: 1, Element: 10.8,Index: 2, Element: Hyd
Index: 3, Element: True

print('For each loop')
# How to print each element and the corresponding index with for ... each loop (Do not use 2nd variable)
for index, element in enumerate(a):
    print(f"Index: {index}, Element: {element}") #For each loop Index: 0, Element: 25,Index: 1, Element: 10.8
Index: 2, Element: Hyd ,Index: 3, Element: True


a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])

print('3rd  list : ', c)
# Example Output:
# Enter  1st  list  :  [10, 20, 15, 18]
# Enter  2nd  list  :  [30, 40, 35, 12, 100, 200, 300]
# 3rd  list :  [40, 60, 50, 30]

c = []  # reset list

for x in a:
    c.append(x + b[a.index(x)])

print('3rd  list : ', c) # 3rd  list :  [40, 60, 50, 30]

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')


How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']

print('Indexed for loop')
for i in range(2, 5):   # 2 to 4 (5 exclusive)
    print(a[i]) # Hyd # True # (3+4j)


print('For each loop')
for x in a:
    if 2 <= a.index(x) <= 4:
        print(x) # Hyd # True # (3+4j)


#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a: [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # [10, 20, 15, 18]


# Program to print the first 20 even numbers
i = 1
while i <= 20:
    print(i * 2)
    i += 1

'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
i = 1

while i <= 20:
    
    odd_number = 2 * i - 1
    print(odd_number)
    
    i += 1
'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

try:
    n = int(input("Please enter the value of 'n': "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()
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
    print(i) #10 9 8 7 6 5 4 3 2 1
    i -= 1

'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''

def calculate_series_sum(n):
    total_sum = 0.0
    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # 2) What is added to sum: 1.1 * i
        term = 1.1 * i
        total_sum += term
        print(f"Term {i} (1.1 * {i}): {term:.1f}, Current Sum: {total_sum:.1f}")
    
    return total_sum

# Example usage:
n_terms = 5
result = calculate_series_sum(n_terms)
print(f"\nFinal sum of first {n_terms} terms: {result:.1f}")


'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

sum_val = 0
for i in range(1, 21):
    sum_val += 2 * i
print(sum_val)


'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

sum = 0

for i in range(1, 21):
    sum += 2 * i - 1

print('Sum of first 20 odd numbers :', sum)
# Output:
# Sum of first 20 odd numbers : 400

'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
n = int(input('Enter n value : '))

sum = 0
for i in range(1, n + 1):
    sum += i

print('Sum =', sum)
# Example Output:
# Enter n value : 5
# Sum = 15

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) #1 Sec Hello 2 Sec Hello 3 Sec Hello
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello') #Hello
# End of loop
print('Outside loop') # Outside loop


# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec') #error

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i) # 1 Sec Hello
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')# Sec Hello
# End  of  the  loop
print('Outside loop') # Outside loop


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd') #error
	break
	print('Sec') #error


