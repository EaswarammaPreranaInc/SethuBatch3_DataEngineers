# Write  a  program  to  print  fibonacci  series  upto   x
x = int(input("Enter value of x : "))

a = 0
b = 1
count = 0

while count <= x:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1

# Find  outputs  (Home  work)
for x in list[10 , 20 , 15 , 18] :
	print(x)

for x in str('Hyd'):
    print(x)
	
for i in range(5):
	print(i)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10 30 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20 40 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # 10,20 30,40 50,60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # Error
	
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20 30...40 50...60
for  x ,  y  in   a:
	print(x , y # Error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # Error

# Identify  error  (Home  work)
for  x  in   123: # Error bcz it is a sequence
        print(x) 

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # empty
for  x   in  []:
        print(x) # empty
for  x   in   {}:
        print(x) # empty
for  x   in   set():
        print(x) # empty
for  x   in   '':
        print(x) # empty
for  x  in  range(10 , 10):
	print(x) # empty
for  x  in   range():
	print(x) # empty
for  x  in   (25):
	print(x) # Error
	
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  # 1,1 2,2 3,3
	print('Hello') # hello
print('Bye') # bye

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(a[i])
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for x in a:
    print(x)
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(a[-i])
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

# Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = []

for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])

print('3rd list :', c)

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range()
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # 20 15 18
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # 11 21 16 19

# Write  a  program  to  print  full  pyramid


# Write  a  program  to  print  first  20  even  numbers 
print("First 20 even numbers:")

cnt = 1

while cnt <= 20:
    print(2 * cnt)
    cnt += 1
	
# Write  a  program  to  print  first  20  odd  numbers 
print("First 20 odd numbers:")

cnt = 1

while cnt <= 20:
    print((2 * cnt)-1)
    cnt += 1
	
# Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'
n = int(input("Enter value of n : "))
print("Natural numbers :")

cnt = 1

while cnt <= n:
    print(cnt)
    cnt += 1
	
# Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
print("Numbers from 10 downto 1 isteps of -1")

cnt = 10

while cnt >= 1:
    print(cnt)
    cnt -= 1
	
