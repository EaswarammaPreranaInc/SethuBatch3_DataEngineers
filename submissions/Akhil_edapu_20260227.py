units = int(input("Enter units : "))

match units//100:
    case 0:
        print(f'cost : {100 *3.00}')
    case 1:
        print(f'cost : {100 *3.00+(units-100)*3.50}')
    case 2 |3:
        print(f'cost :{100*3.00+(units-100)*3.50 + (units-100)*4.00}')
    case 4 |5|6:
        print(f'cost :{100*3.00+(units-100)*3.50 + (units-100)*4.00 + (units-100)*4.50}')
    case _:
        print(f'cost :{100*3.00+(units-100)*3.50 + (units-100)*4.00 + (units-100)*4.50 + (units-100)*5.00}')
        
        
        
num = int(input("Enter a number :"))
x=0
fib1=0
fib2=1
print(fib1,fib2)
while(x<num):
    fib3=fib1+fib2
    print(fib3)
    fib1=fib2
    fib2=fib3
    x=x+1
  
  
  
# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(i,a[i])
    
    
    
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

for i in range(len(a)):
    z = a[i]+b[i]
    c.append(z)
print(c)
 

#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
#print('3rd  list : ' , c)
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)


'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''

a = int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)


'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

a = int(input("Enter a number :"))

sum = 0

for i in range(1,a+1,2):
    sum =sum+i
    print(i)
print(sum)

a = int(input("Enter a number :"))

sum = 0

for i in range(a):
    s = 2*i-1
    print(s)
    sum = sum+s
print(sum)


'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

a = int(input("Enter a number :"))

sum = 0

for i in range(a):
    s = 2*i
    print(s)
    sum = sum+s
print(sum)


'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''

a = int(input("Enter a number :"))
sum=0
for i in range(1,a):
   
    sum = sum +1.1*i
print(sum)


'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

i=10
while(i>0):
    print(i)
    i=i-1

'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

n = int(input("Enter a number :"))
i=1
while(i<=n):
    print(i)
    i=i+1

'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

i=1
while(i<40):
    print(i)
    i=i+2

#even

i=0
while(i<40):
    print(i)
    i=i+2
   
   
   
  '''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines
'''
n = int(input("Enter a number: "))

for i in range(1,n-1):
    print(' ' *i)
    for j in range(1,n):
        print('*' *j)
 
 
 # Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break # we cannot use break with if statment
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
print('Outside loop') #this is printed on screen
 
 
# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue #continue cannot be used with if statment Error
	print('Sec')
 
 
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) # i value index is printed
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')  # sec hello and outside loop both print function are printed on screen 


# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()

for x in list:
    print(x)
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()

How  to  print  each  element  of   range(5)  with  for  loop
for i in range(5):
    print(i)


# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) #10,30,50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20 40 60 
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) #10:20 30:40 50:60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) #10 30 50


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')  #10:20 ... 30:40 ... 50:60
for  x ,  y  in   a: 
	print(x , y) #10,20,30
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # 10:20 ... 30:40 ... 50:60


# Identify  error  (Home  work)
for  x  in   123:
        print(x) #Error because non squence can not be iterated


# Find  outputs  (Home  work)
for  x   in   ():#False
        print(x) #Empty
for  x   in  []: #false
        print(x) #empty
for  x   in   {}: #False
        print(x) #empty
for  x   in   set(): #False empty
        print(x)
for  x   in   '': #False
        print(x) #empty
for  x  in  range(10 , 10): # ) empty
	print(x)
for  x  in   range(): #empty
	print(x)
for  x  in   (25): #Error 
	print(x)
