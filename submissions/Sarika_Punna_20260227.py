print("program  to  determine  bill  amount  and  input  is  units")
units=int(input("Enter units:"))
match units//100:
    case 0:
        cost=units*100
    case 1:
        cost=100*3+(units-100)*3.5
    case 2|3:
        cost=100*3+100*3.5+(units-200)*4
    case 4|5|6:
        cost=100*3+100*3.5+200*4+(units-400)*4.5
    case _:
        cost=100*3+100*3.5+200*4+300*4.5+(units-100)*5
print(f"cost:{cost}")



print("program  to  print  fibonacci  series  upto   x")
x=int(input("enter value of x"))
print("Fibonacci Series:")
a=0
b=1
c=0
while(a<x):
    print(a, end=" ")
    a,b=b,a+b



# Find  outputs  (Home  work)
#How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
for x in [10,20,15,18]:
    print(x)
#How  to  print  each  character  of   string  'Hyd'  with  for  loop
for x in "Hyd":
    print(x)
#How  to  print  each  element  of   range(5)  with  for  loop
for i in range(5):
    print(i)
    

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)#10 <nextline> 30 <nextline> 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)#20 <nextline> 40 <nextline> 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)#(10,20) <nextline> (30,40) <nextline> (50,60)

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)#10 <nextline> 30 <nextline> 50


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')#10...20 <nextline> 30...40 <nextline> 50...60
'''for  x ,  y  in   a:#Error cannot unpack
	print(x , y)
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:#Error cannot unpack
	print(x , y , sep = '...')'''


# Identify  error  (Home  work)
'''for  x  in   123:#Non -sequence are not permitted
        print(x)'''

# Find  outputs  (Home  work)
'''for  x   in   ():#Error 
        print(x)
for  x   in  []:
        print(x)
for  x   in   {}:
        print(x)
for  x   in   set():#error
        print(x)
for  x   in   '':
        print(x)
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():
	print(x)
for  x  in   (25):#Non sequence is not permitted
	print(x)'''

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')
'''Output:
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
for i in range(len(a)):
    print(f'{i} {a[i]})')
print('For each loop')
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)



#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for i in range(len(a)+1):
    print(a[i-1])
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)



print("program  to  add  two  lists  and  store  results  in  3rd  list")
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for i in range(len(a)):
   c.append(a[i]+b[i])
print(c)

print("print  list  elements  from  indexes  2  to  4  without  slice")
a = eval(input('Enter list  :  '))
for i in range(2,5):
    print(a[i])


#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)#[11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)#a = [10 , 20 , 15 , 18]

print("program  to  print  full  pyramid")
n=int(input("How many lines?"))
for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()


print("program  to  print  first  20  even  numbers ")
i=1
while(i<=20):
    print(f'{2*i}')
    i=i+1

print("program  to  print  first  20  odd  numbers ")
i=1
while(i<=20):
    print(f'{2*i-1}')
    i=i+1


print("program  to  print  first  n  natural  numbers ")
a=int(input("enter value of a:"))
i=1
print("Natural Numbers")
while(i<=a):
    print(f'{i}')
    i=i+1


print("program  to  print  10  ,  9  ,   8  ,  ..... 1")
print("Numbers from 10 down to 1 in step 1")
i=10
while(i>=1):
    print(i)
    i=i-1

print("program  to  determine  1.1 + 2.2 + 3.3 + .... n terms")
n=int(input("How many terms would you like to add"))
sum=0
for i in range(n):
    sum=sum+1.1*i
print(f'sum:{sum}')

print("Sum of first 20 even numbers")
sum=0
for i in range(20):
    sum=sum+2*i
print(f'sum:{sum}')

print("Sum of first 20 odd numbers")
sum=0
for i in range(n):
    sum=sum+2*i-1
print(f'sum:{sum}')

print("program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2)")
n=int(input("How many terms would you like to add"))
sum=0
for i in range(1,n):
    sum=sum+i
print(f'sum:{sum}')

#Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
'''Output:
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
'''if ():
	print('Hyd')
	continue#Indentation error
	print('Sec')'''


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
'''Output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop
'''


# Identify Error  (Home  work)
'''if(10 , 20 , 30):
	print('Hyd')
	break #Error break cannot be used without loops
	print('Sec')'''

