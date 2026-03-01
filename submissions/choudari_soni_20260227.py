# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop #for x in list
print()	#10<\n>	20<\n>15<\n>18				
How  to  print  each  character  of   string  'Hyd'  with  for  loop  #for x in range(len(x))
print()
How  to  print  each  element  of   range(5)  with  for  loop	#for x in (0,1,2,3,4)

_______________________________________________________________

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)			#10<\n>30<\n>50
print()					#empty
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)			#20<\n>40<\n>60
print()					#empty
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)			#10 : 20<\n>30 : 40<\n>50 : 60
print()					#empty
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)  		#10<\n>30<\n>50

__________________________________________________________

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')#(10...20 , 30...40 , 50...60)
for  x ,  y  in   a:
	print(x , y)
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')# (10 ... 20 , 30 ... 40 , 50 ... 60)

____________________________________________________________

# Identify  error  (Home  work)
for  x  in   123:	#for loop contains only sequences it does not contains non-sequences
        print(x)

___________________________________________________________
# Find  outputs  (Home  work)
for  x   in   ():
        print(x)#empty tuple
for  x   in  []:
        print(x)#empty list
for  x   in   {}:
        print(x)#empty dictionary
for  x   in   set():
        print(x)#empty set
for  x   in   '':
        print(x)# nothing is printed
for  x  in  range(10 , 10):
	print(x)# 0
for  x  in   range():
	print(x)#empty
for  x  in   (25):
	print(x)#error because for loop contains only sequences

_________________________________________________________

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  # i=1,2,3,4  j=1,2,3,4,5
	print('Hello')			#Hello
print('Bye')				#Bye

_____________________________________________________

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)	#[11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)	#[11 , 21 , 16 , 19]

______________________________________________________

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):			#1</n>Sec<\n>Hello
	print(i)				#2</n>Sec<\n>Hello	
	if  i % 3  == 0:			#3
			continue		#4</n>Sec<\n>Hello
	else:					#5</n>Sec<\n>Hello
			print('Sec')		#6
	print('Hello')				#7</n>Sec<\n>Hello
# End of loop					#Outside loop
print('Outside loop')

_________________________________________________

# Identify Error  (Home  work)
if ():			#continue is used in loops only
	print('Hyd')
	continue
	print('Sec')

________________________________________

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)		#1 
	if   i % 3 == 0:	#2
		break		#3<\n>Sec<\n>Hello
	else:			#4
		print('Sec')	#5
	print('Hello')		#6<\n>Sec<\n>Hello		
# End  of  the  loop		#7
print('Outside loop')		#Outside loop

____________________________________________

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break		#break is used only loops
	print('Sec')

____________________________________________


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


x=int(input('Enter value of x:'))
a=0
b=1
c=a+b
print('Fibonacci series')
if((a==0 and b==1)and x!=0):
    print(a)
    print(b)
else:
    print(a)
while(c<x):
        print(c)
        a=b
        b=c
        c=a+b

____________________________________________________________
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

n=int(input('enter any number :'))

i=0
while i<=n:
    
    space=1
    while space<=n-i:
        print(' ', end='')
        space+=1
        
    star=1
    while star<=2*i-1:
        print('*', end='')
        star+=1
        
    print()       
    i+=1


________________________________________________________

Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

n=int(input('Numbers from 10 downto 1 is steps of -1:'))
n=10
while n>=1:
    print(n,'\n')
    n=n-1

______________________________________________________


Write  a  program  to  determine  sum  of  first  20  even  numbers

i=1
total=0
for I in range(1,21):
  total = total + (2 * i)
  i+=1
print("sum of first 20 even numbers :",total)

___________________________________________
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

n=int(input("How many terms would you like to add:"))

i=1
total=0
while i<=n:
    total = total + (1.1 * i)
    i+=1
print("sum=",total)

_____________________________________________________

Write  a  program  to  determine  sum  of  first  20  odd  numbers


i=1
total=0
for i in range(1,21):
    total = total + 2 * i-1
    i+=1
print("sum of first 20 odd numbers :",total)

______________________________________________________

Write  a  program  to  print  first  20  odd  numbers

print("First 20 odd numbers")
i=1
while i<=20:
    print(2*i-1)
    i+=1

_________________________________________________________

# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()#a[i]
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()#i
How  to  print  each  element  of   range(5)  with  for  loop#for x in  range(5):<next><tab>print(x)
# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)#10<nextline>30<nextline>50
print()#nothing is printed moves to next line 
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)#20<nextline>40<nextline>60
print()#nothing is printes moves to next line 
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)#(10 : 20)<nextline>(30 : 40 )<nextline>( 50 : 60)
print()#nothing is printes moves to next line
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)###
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')#(10...20)<nextline>(30...40 )<nextline>( 50...60)
for  x ,  y  in   a:
	print(x , y#syntax error 
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')#(10...20 ) (30...40)(50 : 60)
# Identify  error  (Home  work)
for  x  in   123:#error 25 it is not a sequence 
        print(x)
# Find  outputs  (Home  work)
for  x   in   ()# empty tuple so loop is skipped
        print(x)
for  x   in  []:# empty list so loop is skipped
        print(x)
for  x   in   {}:# empty dictionary so loop is skipped
        print(x)
for  x   in   set():# empty set so loop is skipped
        print(x)
for  x   in   '':# empty string so loop is skipped
        print(x)
for  x  in  range(10 , 10):# loop is skipped
	print(x)
for  x  in   range():# loop is skipped
	print(x)
for  x  in   (25):#error 25 it is not a sequence 
	print(x)
 #  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #1<nextline>1<nextline>1<nextline>2<nextline>1<nextline>3<nextline>4<nextline>1<nextline>5
	print('Hello')#Hello
print('Bye')#bye


________________________________________________________________________________________________---
 # How  to  print  each  element  and  the  corresponding  index #using index based for loop
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')#for x in range(len(a)):<nextline> <tab> print(a[i])
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop# print(a[i])
print('For each loop')#a[i]
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

___________________________________________________________________________

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
print('a :  ' , a)#a:10<nextline>a:20<nextline>a:15<nextline>a:18<nextline>
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)#b = [10 , 20 , 15 , 18]
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)#0,1,2,3,4,5,6,7
	if  i % 3  == 0:
			continue
	else:
			print('Sec')#Sec
	print('Hello')#Hello
# End of loop
print('Outside loop')#Outside loop'
# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
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
print('Outside loop')#Outside loop
 # Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')#Hyd
	break
	print('Sec')
_______________
#fibonacci series using while loop
x=int(input("enter value of x:"))
a=0
b=1
c=a+b
print("fibonacci series")
if(a==0 and b==1) and(x==0):
    print(a)
else:
    print(a,b,c,sep="\n")
while(c<x):
    print(c)
    a=b
    b=c
    c=a+b
__________________
'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)'''

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
n = min(len(a), len(b))

for i in range(n):
    c.append(a[i] + b[i])
print('3rd  list : ', c)
_______________
'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
a=(int(input("How many terms would you like to add :")))
sum=0
i=1
for i in range(1,a+1):
     sum=sum+i
print(f"sum:{sum}")
 
___________________________
'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 
1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40
2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20
3) Hint:  Do  not  use  range  object
4) Use  while  loop
'''
print("first 20 Even Numbers")
i=1
while(i<=20):
    n=2*i
    print(f"{n}")
    i=i+1
print("Bye")
_____________
'''
Write  a  program  to  print  first  20  odd  numbers
1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39
2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
3) Hint:  Do  not  use  range  object
4) Use  while  loop
'''
print("first 20 odd numbers")
i=1
while(i<=20):
    n=2*i-1
    print(f"{n}")
    i+=1
__________________________
'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'
What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n
1) Hint:  Do  not  use  range  object
2) Use  while  loop'''

print("Enter Value of n :")
print("Natural Numbers")
i=1
while(i<=20):
    print(f"{i}")
    i+=1
____________
'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1
1) Hint:  Do  not  use  range  object
2) Use  while  loop
'''
print("Numbers from 10 down 1 in steps of -1")
i=10
while(i>=1):
    print(f"{i}")
    i-=1

___________________________
'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......
2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n
3) Use  for  loop
'''
n=int(input("How many terms would you like to add:"))
sum=0
i=1
for i in range(1,n+1):
    sum=sum+1.1*i
    i+=1
print(f"{sum}")
____________________

'''
Write  a  program  to  determine  sum  of  first  20  even  numbers
1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20
2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20
3) Use  for  loop
'''
n=20
sum=0
i=1
print("sum of first 20 even numbers")
for i in range(1,n+1):
    sum=sum+2*i
    i+=1
print(f'{sum}')
_________________________________________________
 

'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers
1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)
2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20
3) Use  for  loop
'''
n=20
sum=0
i=1
for i in range(1,n+1):
    n=2*i-1
    sum=sum+n
    i+=1
print(f"Sum of first 20 odd numbers:{sum}")
___________
'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 
1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40
2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20
3) Hint:  Do  not  use  range  object
4) Use  while  loop
'''
n=int(input('enter any number :'))
i=0
while i<=n:
    space=1
    while space<=n-i:
        print(' ', end='')
        space+=1 
    star=1
    while star<=2*i-1:
        print('*', end='')
        star+=1 
    print()       
    i+=1
________________________________

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
				cost =  100 * 3.00 + (units - 100) * 3.50
	case  ???:
				cost = 
	case  ???:
				cost = 
	case  ???:				
				cost = 
print('Bill  amount  :  ' , cost)
units = int(input('Enter  units :   '))

match units//100:
    case 0:
         cost = 100*3.00
    case 1:
        cost = 100 * 3.00 + (units-100) * 3.50
    case 2:
        cost = 100 * 3.00 + 100 * 3.50 + (units-200) * 4.00
    case 3:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units-300) * 4.50
    case 4:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + (units-500) * 5.00
    case _:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50+units*700

    
print(f"Bill  amount  : {cost} ")

____________________________________________________________________________________________

'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)'''

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
n = min(len(a), len(b))

for i in range(n):
    c.append(a[i] + b[i])
print('3rd  list : ', c)

____________________________________________________________

Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)'''

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
n = min(len(a), len(b))

for i in range(n):
    c.append(a[i] + b[i])
print('3rd  list : ', c)

