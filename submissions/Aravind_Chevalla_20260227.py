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

x=int(input("Enter value of x:"))
a=0
b=1
print("Fibonacci series")
while a<=x:
    print(a)
    c=a+b
    a=b
    b=c


'''
 # Find  outputs  (Home  work)
How  to  print  each  element  of  list a= [10 , 20 , 15 , 18]  with  for  loop
print() #for x in [10 , 20 , 15 , 18]:
           print(x)
How  to  print  each  character  of   string a= 'Hyd'  with  for  loop
print() #for x in 'Hyd':
           print(x)
How  to  print  each  element  of   range(5)  with  for  loop #for x in range(5):
          							 print(x)
'''

 # Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys(): # 10 <nextline>30 <nextline>50
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():# 20 <nextline> 40 <nextline> 60
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items(): #(10,20) <nextline>(30,40) <nextline>(50,60)
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:  #10 <nextline>30 <nextline>50
	print(x)

 # Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20<nextline>30...40<nextline>50...60

for  x ,  y  in   a:
	print(x , y #error

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')  #error


# Identify  error  (Home  work)
for  x  in   123: #Error non sequence
        print(x)

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) #Nothing
for  x   in  []:
        print(x) #Nothing
for  x   in   {}:
        print(x) #Nothing
for  x   in   set():
        print(x) #Nothing
for  x   in   '':
        print(x) #Nothing
for  x  in  range(10 , 10):
	print(x) #10
for  x  in   range():
	print(x) # nothing
for  x  in   (25):
	print(x) #error

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  # 1 1 <nextline>1 2<nextline>1 3<nextline> Hello <nextline>2 1 <nextline> 2 2 <nextline> 2 3 <nextline>Hello <nextline>3 1<nextline> 3 2<nextline> 3 3<nextline> Hello <nextline>Bye
	print('Hello')
print('Bye')

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
a=[25,10.8,'Hyd',True]
i=0
for x in a:
    print (x,i)
    i=i+1

How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
a=[25,10.8,'Hyd',True]
for i in range(len(a)):
    print (a[i],i)

How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
a=[25,10.8,'Hyd',True]
i=0
for x in a:
    print (x,i,sep="  ")
    i+=1

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
a=[25,10.8,'Hyd',True]
for i in range(-1,-len(a)-1,-1):
    print (a[i])

How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
a=[25,10.8,'Hyd',True]
for i in range(-1,-len(a)-1,-1):
    print (a[i],i)
-
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
a=[25,10.8,'Hyd',True]
for x in a:
    print (x)

 '''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a=eval(input('Enter 1st list:'))
b=eval(input('Enter 2st list:'))
c=[]
for i in range(len(a)):
    for j in range(len(b)):
      if i==j:
       c.append(a[i]+b[j])
print (c)


a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
a=eval(input('Enter 1st list:'))
b=eval(input('Enter 2st list:'))
c=[]
for x in a:
    for y in b:
        c.append(x+y)
print (c)


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(2,5):
    print(a[i])

#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice




 #  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)# [11  21  16  19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) #[10,20,15,18]



'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines
'''
a=int(input("How many line:"))
for i in range(1,a+1):
    print(" " *(a-i),end="")
    print('*'*(2*i-1))

'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

a=int(input("Number of even numbers required:"))
i=1
print("First",a,"Even number=")
while i<=a:
    print(2*i)
    i+=1
'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
a=int(input("Number of odd numbers required:"))
i=1
print("First",a,"odd number=")
while i<=a:
    print(2*i-1)
    i+=1


'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
a=int(input("Number of natural numbers required:"))
i=1
print("Natural numbers")
while i<=a:
    print(i)
    i+=1
 '''

Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
a=int(input("Number of natural numbers required:"))
i=a
print("Number from",a,"down to -1 in steps of 1")
while i>=1:
    print(i)
    i-=1
'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
a=int(input("How many terms would you like to add:"))
b=0
for i in range(a+1):
    b+=1.1*i
    i+=1
print(b)

 '''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop

'''

a=int(input("Number of even number should be added:"))
print("sum of 1st",a,"even number=")
b=0
for i in range(a+1):
    b+=2*i
    i+=1
print(b)

 '''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
a=int(input("Number of odd number should be added:"))
print("sum of 1st",a,"odd number=")
b=1
for i in range(a+1):
    b+=2*i-1
    i+=1
print(b)

'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
a=int(input("Number of Natural number should be added:"))
print("sum of 1st",a,"Natural number=")
b=0
for i in range(a+1):
    b+=i
    i+=1
print(b)


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
'''
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

#Identify Error  (Home  work)
if ():
	print('Hyd')
	continue  #eroor
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
print('Outside loop')
'''
1
sec
Hello
2
sec
Hello
3
Outside loop


'''


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break #error
	print('Sec')
