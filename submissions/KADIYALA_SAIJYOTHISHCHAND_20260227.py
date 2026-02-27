# Write  a  program  to  determine  bill  amount  and  input  is  units

unit = int(input('Enter  units :   ')) 
a= unit//100 
match  unit:
	case  0:
				cost = unit * 3.00
	case  1:
				cost = 100*3.00 + (unit - 100)*3.50
	case  2:
				cost = 100*3.00 + 100*3.50 + (unit - 200)*4.00
	case  3:
				cost = 100*3.00 + 100*3.50 + 200*4.00 + (unit - 400)*4.50
	case  _:				
				cost = 100*3.00 + 100*3.50 + 200*4.00 + 300*4.5 + (unit - 700)*5.0
print('Bill  amount  :  ' , cost)

# Write  a  program  to  print  fibonacci  series  upto   x

x=int(input("Enter x value : "))
f1=0
f2=1
if x<0:
    print("Enter a positive number")
else: 
    print("Fibonacci series")
    while f1<=x:
        print(f1)
        f3=f1+f2
        f1=f2
        f2=f3
print()

# Find  outputs  (Home  work)
# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
lt=[10 , 20 , 15 , 18]
for i in lt:
    print(i)

# How  to  print  each  character  of   string  'Hyd'  with  for  loop
st='Hyd'
for ch in st:
  print(ch)
# How  to  print  each  element  of   range(5)  with  for  loop
r=range(5)
for i in r:
 print(i)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)                               #10<nl>30<nl>50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)                               #20<nl>40<nl>60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)                               #(10,20)<nl>(30,40)<nl>(50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)                          #10<nl>30<nl>50

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')   # 10...20<nl>30...40<nl>50...60
for  x ,  y  in   a:
	print(x , y)                 # Error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')   # Error
# Identify  error  (Home  work)
for  x  in   123:
        print(x)   # Error, bcz 123 is non sequence

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # nothing
for  x   in  []:
        print(x) # nothing
for  x   in   {}:
        print(x) # nothing
for  x   in   set():
        print(x) # nothing
for  x   in   '':
        print(x) # nothing
for  x  in  range(10 , 10):
	print(x) # nothing
for  x  in   range():
	print(x) # Error, bcz there should be an arg for range 
for  x  in   (25):
	print(x) # error bcz it is not tuple

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  
	print('Hello')
print('Bye')

'''1 1
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
for i in range(len(a)):
 print('Indexed  based  for loop')
 print(a[i] , i)
for i in a:
 print('For each loop')
 print(i)

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
 print(a[i] , i)
print('For each loop')
for i in a:
 print(i)

# Write  a  program  to  add  two  lists  and  store  results  in  3rd  list


list1=  eval(input("Enter 1st list : "))
list2=  eval(input("Enter 2nd list : "))
list3 = []
c=0
for x in list1:
    if c < len(list2):
        v=x+list2[c]
        list3.append(v)
        c=c+1
print(list3)


# How  to  print  list  elements  from  indexes  2  to  4  without  slice

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for x in range(2,5):
    print(a[x])

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
c=0
for x in a:
    if c>=2 and c<=4:
     print(x)
    c=c+1

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)   # a :   [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # b :   [10, 20, 15, 18]

'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines'''

x=int(input("Enter How many lines : "))
for i in range(1,x+1):
     print((x-i)*' ' + ('*'* (2*i - 1)))

# Write  a  program  to  print  first  20  even  numbers 

x=int(input("Enter n number : "))
i=1
while i<=x:
    print(2*i)
    i += 1
print("Bye")

# Write  a  program  to  print  first  20  odd  numbers

x=int(input("Enter n number : "))
i=1
while i<=x:
    print(2*i - 1)
    i += 1
print("Bye")

# Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n

i=1
while i<=x:
    print(i)
    i += 1
print("Bye")

# Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

x=int(input("Enter n number : "))
while x>0:
    print(x)
    x -= 1
print()

# Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

x=int(input("Enter n number you would like to add : "))
sum=0
for i in range(1,x+1):
    sum += 1.1 * i
    i+=1
print(sum)

# Write  a  program  to  determine  sum  of  first  20  even numbers

x=int(input("Enter n number you would like to add : "))
sum=0
for i in range(1,x+1):
    sum += 2*(i)
    i+=1
print(f'sum of first {x} numbers is {sum}')

# Write  a  program  to  determine  sum  of  first  20  odd numbers

x=int(input("Enter n number you would like to add : "))
sum=0
for i in range(1,x+1):
    sum += (2*i) - 1
    i+=1
print(f'sum of first {x} numbers is {sum}')

# Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

x=int(input("Enter n number you would like to add : "))
sum=0
for i in range(1,x+1):
    sum += i
    i+=1
print(f'sum of first {x} numbers is {sum}')
