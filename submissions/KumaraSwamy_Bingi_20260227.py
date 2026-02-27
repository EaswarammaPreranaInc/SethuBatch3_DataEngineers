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
units = int(input('Enter units : '))
match units // 100:
    case 0:
        cost = units * 3.00
    case 1:
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 | 3:
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
print('Bill amount : ', cost)
















'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''

x = int(input("Enter value of x :"))
print("Fibonacci Series")
if x == 0:
  print(0)
else:
    a,b=0,1
    while a<=x:
        print(a)
        a,b =b,a+b
  
  














# Find  outputs  (Home  work)
#How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
a=[10,20,15,18]
for i in a:
  print(i)
#How  to  print  each  character  of   string  'Hyd'  with  for  loop
s="hyd"
for i in s:
  print(i)

#How  to  print  each  element  of   range(5)  with  for  loop
for i in range(5):
  print(i)
  
  















# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)                                              # 10 <nextline> 30 <nextline> 50 <nextline>
print()                                                   # print nothing and move to <nextline>
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():      
	print(x)                                                # 20 <nextline> 40 <nextline> 60 <nextline>
print()                                                     # print nothing and move to <nextline>
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)                                                # (10,20) <nextline> (30,40) <nextline> (50,60) <nextline>
print()                                                     # print nothing and move to <nextline>
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)                                                # 10 <nextline> 30 <nextline> 50
     

















# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')       # 10...20 <nextline> 30...40 <nextline> 50...60 <nextline>
for  x ,  y  in   a:
	print(x , y)                 # error we should use items() and indexing is not supported in dictionary and if only 2 keypairs are there then its valid
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')   # error we should use items() and indexing is not supported in dictionary and if only 2 keypairs are there then its valid














# Identify  error  (Home  work)
for  x  in   123:
        print(x)   # Error 123 is not sequence its non sequence 











# Find  outputs  (Home  work)
for  x   in   ():
        print(x)    # prints nothing and move to <nextline>
for  x   in  []:
        print(x)    # prints nothing and move to <nextline>
for  x   in   {}:
        print(x)    # prints nothing and move to <nextline>
for  x   in   set():
        print(x)    # prints nothing and move to <nextline>
for  x   in   '':
        print(x)    # prints nothing and move to <nextline>
for  x  in  range(10 , 10):
	print(x)          # prints nothing and move to <nextline>
for  x  in   range():   # Error  range() should contain arguement inside it 
	print(x)          
for  x  in   (25):
	print(x)          # Error (25) its non sequence

















#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)                   #this inner loop is excute 4 times (1,2,3,4) for each i iterates from 1,2,3   
	print('Hello')
print('Bye')

'''
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

'''













# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)):
      print(a[i])

print('For each loop')
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

for i in a:
      print(i)


















#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(-1,-(len(a)+1),-1):
      print(a[i])


print("for each loop")
#ow   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
for i in reversed(a):
      print(i)














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
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
length= min(len(a),len(b))
for i in range(length):
  c.append(a[i]+b[i])
print('3rd  list : ' , c)
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

c = [x + y for x, y in zip(a, b)]

print('3rd  list : ' , c)




















#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2,5):
      print(a[i])
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
print('for each loop')
count=0

for i in a:
      if 2 <= count <= 4:
            print(i)
      count+=1





















#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1                 
print('a :  ' , a)               #a: [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)              #b: [10, 20, 15, 18]
















'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''


n = int(input("how many lines:"))

for i in range(1,n+1):
  print((n-i)* ' ' + i * '*'+ (i-1)* '*')


















'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

print("First 20 even numbers:")

i=1
while(i<=20):
  print(i*2)
  i+=1



















  '''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  3 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''


print("First 20 odd  numbers:")

i=1

while(i<=20):
  print(i*2-1)
  i+=1

















'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''


n = int(input("enter the value of n :"))
i=1
while(i<=n):
      print(i)
      i+=1














'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

n = int(input("enter the value of n :"))
print(n)
while n>1:
      n= n-1
      print(n)















'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''

n = int(input('hpw many terms you want to add:'))
sum =0
for i in range(1,n+1):
      sum = sum + 1.1*i
print('Sum:',sum)
















'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

n = int(input('hpw many terms you want to add:'))
sum =0
for i in range(1,n+1):
      sum = sum + 2*i
print('Sum:',sum)

















'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

n = int(input('hpw many terms you want to add:'))
sum =0
for i in range(1,n+1):
      sum = sum + 2*i-1
print('Sum:',sum)





















'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
n = int(input('hpw many terms you want to add:'))
sum =0
for i in range(1,n+1):
      sum =sum +i

print("sum is:",sum)

















# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:                   # its skips for loop at i = 3 , 6 
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')



'''
output:
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
if ():
	print('Hyd')
	continue                       # we cant use continue in if and we can use them in loops like for and while
	print('Sec')
      







# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')                    # we cant use break in if and we can use them in loops like for and while
	break
	print('Sec')