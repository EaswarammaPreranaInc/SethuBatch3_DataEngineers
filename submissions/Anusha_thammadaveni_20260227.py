1)Write  a  program  to  print  fibonacci  series  upto   x
Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13
     1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term
      2) What  are  the  first  two  terms ?  --->  0  and  1
      3) Hint:  Use  while  loop



Program:
'''x = int(input("Enter value: "))
print("Fibonacci Series")
a = 0
b = 1
count = 0
while count < x:
    print(a, end=" , ")
    c = a + b
    a = b
    b = c
    count += 1



2)# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop




list1 = [10, 20, 15, 18]
for i in list1:
    print(i)

s = "Hyd"
for ch in s:
    print(ch)

for i in range(5):
    print(i)




3) # Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()

#10 30 50

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()

#20 40 60

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()

#(10, 20)
(30, 40)
(50, 60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)

#10
30
50



4) # Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')

#10...20
30...40
50...60

for  x ,  y  in   a:
	print(x , y)
 
# error, bcz  Keys are integers: 10, 30, 50

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')


#Error , bcz  cannot unpack non-iterable int object


5)# Identify  error  (Home  work)
for  x  in   123:
        print(x)


#int object is not iterable


6) # Find  outputs  (Home  work)
for  x   in   ():
        print(x)
    
#empty, due to empty tuple

for  x   in  []:
        print(x)

# empty, due to empty list


for  x   in   {}:
        print(x)


#empty, due to empty list


for  x   in   set():
        print(x)


#empty, due to empty set


for  x   in   '':
        print(x)


#empty, due to empty string


for  x  in  range(10 , 10):
	print(x)


#empty bcz start and stap at 10


for  x  in   range():
	print(x)


#error , range needs at least 1 argument


for  x  in   (25):
	print(x)


#Error, 'int' object is not iterable


7)Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')



output:

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






8)  # How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)






a = [25, 10.8, 'Hyd', True]
print('Index based for loop')
for i in range(len(a)):
    print("Index:", i, "Element:", a[i])
print('For each loop')
for x in a:
    print("Index:", a.index(x), "Element:", x)
for i, x in enumerate(a):
    print("Index:", i, "Element:", x)







9) #  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)






a = [25, 10.8, 'Hyd', True]
print('Indexed for loop')
for i in range(len(a)-1, -1, -1):
    print(a[i])
print('For each loop')
for x in reversed(a):
    print(x)






10) '''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
1st  list  --->  [10 , 20 , 15 , 18]
2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]
3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]
Hint:  Use  append()  method
'''






a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = []
# Find minimum length
min_len = min(len(a), len(b))
for i in range(min_len):
    c.append(a[i] + b[i])
print('3rd list :', c)
a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = []
for x in a:
    if a.index(x) < len(b):
        c.append(x + b[a.index(x)])
print('3rd list :', c)





11) How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice



print('Indexed for loop')
for i in range(2, 5):   # 5 because stop value is excluded
    print(a[i])
print('For each loop')
for x in a:
    if 2 <= a.index(x) <= 4:
        print(x)






12) Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)




#a :  [11, 21, 16, 19]
  b :  [10, 20, 15, 18]




13)  ''Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********
Input  is  number  of  lines

'''


n = int(input("How many lines? : "))
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()   # Move to next line





14) '''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 
1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40
2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20
3) Hint:  Do  not  use  range  object
4) Use  while  loop
'''




i = 1
while i <= 20:
    print(2 * i, end=" ")
    i += 1







15)  '''
Write  a  program  to  print  first  20  odd  numbers
1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39
2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
3) Hint:  Do  not  use  range  object
4) Use  while  loop




'i = 1
while i <= 20:
    print(2 * i - 1, end=" ")
    i += 1






16) '''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'
What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n
1) Hint:  Do  not  use  range  object
2) Use  while  loop
'''

# n = int(input("Enter value of n : "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 1







17)  '''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1
1) Hint:  Do  not  use  range  object
2) Use  while  loop
'''


#i = 10
while i >= 1:
    print(i, end=" ")
    i -= 1






18) '''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......
2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n
3) Use  for  loop
'''


n = int(input("Enter number of terms : "))
sum = 0
for i in range(1, n + 1):
    sum += 1.1 * i
print("Sum =", sum)




19)  '''
Write  a  program  to  determine  sum  of  first  20  even  numbers
1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20
2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20
3) Use  for  loop
'''




sum = 0
for i in range(1, 21):
    sum += 2 * i
print("Sum =", sum)




20) '''
Write  a  program  to  determine  sum  of  first  20  odd  numbers
1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)
2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20
3) Use  for  loop
'''




sum = 0
for i in range(1, 21):
    sum += (2 * i - 1)
print("Sum =", sum)




21) Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
Hint:  Use  for  loop




sum = 0
for i in range(1, 21):
    sum += (2 * i - 1)
print("Sum =", sum)




22) '''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
Hint:  Use  for  loop
'''


n = int(input("Enter value of n : "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum =", sum)





23)Find  outputs  (Home  work)
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





24) # Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')



# error bcz if is empty.




25) # Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')




1
Sec
Hello
2
Sec
Hello
3
Outside loop



26) # Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')



# error bcz. break can be used only inside a loop