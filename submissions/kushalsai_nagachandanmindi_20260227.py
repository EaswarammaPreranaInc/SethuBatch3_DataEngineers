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
units = int(input('Enter  units :   '))   #   175
match  units // 100:
	case  0:   #   units  between  0  and  99
				cost = units * 3.00
	case  1:  #  units  between  100 and  199
				cost = 100 * 3.00 + (units - 100) * 3.50
	case  2:
				cost = 100 * 3.00 + (units - 100) * 3.50 + (units - 200) * 4.00
	case  3:
				cost = 100 * 3.00 + (units - 100) * 3.50 + (units - 200) * 4.00 + (units - 400) * 4.50
	case  4:				
				cost = 100 * 3.00 + (units - 100) * 3.50 + (units - 200) * 4.00 + (units - 400) * 4.50 + (units - 400) * 5.00
print('Bill  amount  :  ' , cost)

# Write  a  program  to  print  fibonacci  series  upto   x
a = int(input("Enter value of x : "))
x,y = 0,1
print("Fibonacci Series")
while x <= a:
    print (x)
    c = x + y
    x = y
    y = c
    
# Find  outputs  (Home  work)
for a in [10,20,15,18] :
	print(a) # How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
for a in 'Hyd':
	print(a)# How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
for a in range(5):
	print(a)# How  to  print  each  element  of   range(5)  with  for  loop

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10 <newline> 30 <newline> 50
print() # 
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20 <newline> 40 <newline> 60
print() #
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10, 20) <newline> (30, 40) <newline> (50, 60)
print() # 
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10 <newline> 30 <newline> 50

# Identify  error  (Home  work)
for  x  in   123:
        print(x) # In for loop non sequence cannot be iterated;

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # Nothing prints
for  x   in  []:
        print(x) # Nothing prints
for  x   in   {}:
        print(x) # Nothing prints
for  x   in   set():
        print(x) # Nothing prints
for  x   in   '':
        print(x) # Nothing prints
for  x  in  range(10 , 10):
	print(x) # Nothing prints
for  x  in   range():
	print(x) # Error range not specified
for  x  in   (25):
	print(x) # Error non sequence cannot be iterated in for loop

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  
	print('Hello')
print('Bye')

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Index based for loop')
for i in range(len(a)):
    print(i, a[i])
print('For each loop')
for x in a:
    print(a.index(x), x)
  
#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25, 10.8, 'Hyd', True]
print("Indexed for loop")
for i in range(len(a) - 1, -1, -1):
    print(a[i])

# Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2st list : "))
c = []
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])
print('3rd list :', c)

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print("Indexed based for loop")
for i in range(2, 5): 
    print(a[i])
print("For-each loop (without slice and without 2nd variable)")
count = 0
for x in a:
    if 2 <= count <= 4:
        print(x)
    count += 1
    
#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18] 
for  x  in   b:
	x += 1
print('b :  ' ,  b)		# a :   [11, 21, 16, 19] <Nextline> b :   [10, 20, 15, 18]

# Write  a  program  to  print  full  pyramid
n = int(input("Enter number of lines : "))
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
    
# Write  a  program  to  print  first  20  even  numbers 
print("First 20 even numbers")
i = 1
while i <= 20:
    print(2 * i)
    i += 1
print("Bye")

# Write  a  program  to  print  first  20  odd  numbers
print("First 20 odd numbers")

i = 1
while i <= 20:
    print(2 * i - 1)
    i += 1

# Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'
n = int(input("Enter value of n : "))
print("Natural Numbers")
i = 1
while i <= n:
    print(i)
    i += 1

# Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
print("Numbers from 10 downto 1")
i = 10
while i >= 1:
    print(i)
    i -= 1
    
# Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
n = int(input("How many terms would you like to add : "))
sum = 0
for i in range(1, n + 1):
    sum += 1.1 * i
print("Sum :", sum)

# Write  a  program  to  determine  sum  of  first  20  even  numbers
sum = 0
for i in range(1, 21):
    sum += 2 * i
print("Sum of first 20 even numbers :", sum)

# Write  a  program  to  determine  sum  of  first  20  odd  numbers
sum = 0
for i in range(1, 21):
    sum += (2 * i - 1)
print("Sum of first 20 odd numbers :", sum)


# Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
n = int(input("How many terms would you like to add : "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum :", sum) 

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop') # 1 <nxtli> Sec <nxtli> Hello <nxtli> 2 <nxtli> Sec <nxtli> Hello <nxtli> 3 <nxtli> 4 <nxtli> Sec <nxtli> Hello <nxtli> 5 Sec <nxtli> Hello
					  # 6 <nxtli> 7 <nxtli> Sec <nxtli> Hello <nxtli> Outside loop

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec') # continue outside loop