
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
units = int(input('Enter units : '))   # 175
cost = 0

match units // 100:
    case 0:   # units between 0 and 99
        cost = units * 3.00
    case 1:   # units between 100 and 199
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2:
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 3:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case 4:				
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
    case _:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print('Bill amount : ', cost)


n=int(input("enter value of x"))
a=0
b=1
s=0
print(a)
while(s<=n):
    s=a+b
    print(b)
    a,b=b,s
    
a=eval(input("enter value excluding string "))
for i in a:
    print(i)
a=input("enter value string ")
for i in a:
    print(i)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10 30 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) #20,40,60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)#(10,20),(30,40),(50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) #10,30,50

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')# 10...20, 30...40, 50...60
for  x ,  y  in   a:
	print(x , y)#10,20,30,40,50,60
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')# 10...20, 30...40, 50...60
 
 # Identify  error  (Home  work)
for  x  in   123:#error it cant iterate int 
        print(x)
        
# Find  outputs  (Home  work)
for  x   in   ():
    print(x)# it will not print anything because it is empty tuple
for  x   in  []:
    print(x)# it will not print any thing
for  x   in   {}:
    print(x)#it will print nothing
for  x   in   set():
    print(x)#error
for  x   in   '':
    print(x)#nothing is printed
for  x  in  range(10 , 10):
	print(x)#nothing is printec
for  x  in   range():
	print(x)#error because range 
for  x  in   (25):
	print(x)#error
 
 #  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  ## 1 1, 1 2, 1 3, 1 4, 2 1, 2 2, 2 3, 2 4, 3 1, 3 2, 3 3, 3 4
	print('Hello')#hello hello hello
print('Bye')#bye
 
 
a = [25 , 10.8 , 'Hyd' , True]
for i  in  a:
    print(i) #25,10.8,Hyd,True  
print('Indexed  based  for loop')

#index and there elemetnt with for loop
a=[10 , 20 , 30]
for i in range(len(a)):
    print(i,a[i])


#index and there elemetnt with for each loop
a = [25 , 10.8 , 'Hyd' , True]
for i  in  a:
    print(i,a.index(i))


#reverse the list with for  loop  
a=[10 , 20 , 30]
for i in range(-1,-len(a)-1,-1):
    print(a[i])
    
#reverse the list with for  each loop 
a=[10 , 20 , 30]
for i in a:
    print(a[a.index(i)-1])
    
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
le=len(a) if len(a) < len(b) else len(b)
for i in range(le):
    c.append(a[i] + b[i])
print('3rd  list  :  ' , c)
c = []
for i in range(len(a) if len(a) < len(b) else len(b)):
    c.append(a[i] + b[i])
print('3rd  list  :  ' , c)

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for i in range(len(a)):
    if(i>=2):
        print(a[i])


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('for each loop')
for i in a:
    if(a.index(i)>=2):
        print(i)
    
    
    
#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)#11,21,16,19
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)#10,20,15,18

#print pyramid
n=int(input("enter number of lines"))
star=1
for i in range(1,n+1):
    print(" "*(n-i)+"*"*star)
    star+=2
    
'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''


i=1;
print("first 20  even numbers are")
while(i<21):
    print(i*2)
    i+=1
    
i=1;
print("first 20  even numbers print are")
while(i<21):
    print(i)
    i+=1

'''
    Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop'''
i=1;
print("first 20  odd numbers are")
while(i<21):
    print(i*2-1)
    i+=1

i=1;
print("first 20  odd numbers  with i are")
while(i<21):
    print(i*2-1,i)
    i+=1
    
    '''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
    
a=int(input("enter a number :"))
f=1
while(f!=a+1):
    print(f)
    f+=1
    
'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

a=int(input("enter a number :"))

while(a!=0):
    print(a)
    a-=1
    
'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''

n=int(input("how many terms would you like to add"))
sum=0
f=1.1
for i in range(n+1):
    sum+=f*i
print(sum)

sum=0
f=1
for i in range(0,41,2):
    sum+=f*i
print(f'sum of 20 even number:{sum}')
sum=0
f=1
for i in range(1,41,2):
    sum+=f*i
print(f'sum of 20 odd number:{sum}')

n=int(input("how many terms would you like to add"))
sum=0
for i in range(n+1):
    sum+=i
print("sum :",sum)



# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)#1,2,3,4,5,6,7
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
'''1
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
Outside loop'''


# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue#it should be in loop
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

'''1
Sec
Hello
2
Sec
Hello
3'''

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break#break should be in loop
	print('Sec')
 




    




    





    






