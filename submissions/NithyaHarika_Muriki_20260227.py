
# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop

a=[10 , 20 , 15 , 18]
for x in a:
  print(x)
a = "Hyd"
for x in a:
  print(x)

for x in range(5):
  print(x)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)#output:10 <newline> 30 <newline> 50
print()<newline> 
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)#output:20 <newline> 40 <newline> 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)#output:(10,20) <newline> (30,40) <newline>(50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)#output:10 <newline> 30 <newline> 50



# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')[10...20<newline>30...40<newline>50...60
for  x ,  y  in   a:
	print(x , y)#output:error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')#output:error

# Identify  error  (Home  work)
for  x  in   123:
        print(x)#output:error


# Find  outputs  (Home  work)
for  x   in   ():
        print(x)#output:empty
for  x   in  []:
        print(x)#output:empty
for  x   in   {}:
        print(x)#output:empty
for  x   in   set():
        print(x)#output:empty
for  x   in   '':
        print(x)#output:empty
for  x  in  range(10 , 10):
	print(x)#output:error
for  x  in   range():
	print(x)#output:error
for  x  in   (25):
	print(x)#output:error


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


# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
 print("Element : " ,a[i], "Index: ", i)

for x in a:
  print(x, a.index(x),sep="\t ")




'''
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
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)


a= [10 , 20 , 15 , 18]

b= [30 , 40 , 35 , 12 , 100 , 200 , 300]

c =[]
for i in range(len(a)):
  sum = a[i]+b[i]
  c.append(sum)
print(c)


for x in a:
  c.append(x +b[a.index(x)])
print(c)


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

for i in range(len(a)):
  print(a[i])

'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines
'''

a = int(input("Enter any number : "))
for i in range(1,a+1):
   print("  "*(a-i)," * "*(2*i-1))
print()



'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
i = 1
while(i<=20):
  print(i*2)
  i +=1


'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
i = 1
while(i<=20):
print(i*2-1)
i +=1


'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''


i=1
n = int(input("Enter value of n:")
while(i <=n):
 print(i)
 i += 1

'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

i=10
n = int(input("Enter value of n:")
while(i >=n):
print(i)
i -= 1

'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
a = 1.1
n = int(input("Enter value of n:"))
sum = 0
for i in range(n+1):
  sum += a*i
 print(sum)


'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
n = int(input("Enter value of n:"))
sum = 0
for i in range(n+1):
 sum += 2*i
print("Sum of first 20 even numbers: ",sum)


'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
n = int(input("Enter value of n:"))
sum = 1
for i in range(n+1):
sum += (2*i-1)
print("Sum of first 20 odd numbers: ",sum)


'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
n = int(input("Enter value of n:"))
sum = 0
for i in range(n+1):
  sum += i
print("Sum of first n natural numbers: ",sum)



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

#OUTPUT
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
7
Sec
Hello
Outside loop



# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')

#Output: Error, continue cannot be used without loops

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
#Output:
1
Sec
Hello
2
Sec
Hello
3



# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')

#Output: Error, break cannot be used without loops


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice




#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1 
print('a :  ' , a)#output: 11 + 21+16+19
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)# Output: [10 , 20 , 15 , 18]



#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
#Output:
a = [25 , 10.8 , 'Hyd' , True]
a.reverse()
for x in a:
    print(x)

a = [25 , 10.8 , 'Hyd' , True]
a.reverse()
for i in range(len(a)):
    print(a[i])



















