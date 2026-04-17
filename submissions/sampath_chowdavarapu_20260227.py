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
units = int(input('Enter  units :   '))
if units>0:
#   175
  match  units // 100:
	case  0:   #   units  between  0  and  99
				cost = units * 3.00
	case  1:  #  units  between  100 and  199
				cost =  100 * 3.00 + (units - 100) * 3.50
	case  2:
				cost = 100*3.00+ 100*3.50+(units-200)*4.00
	case  3:
				cost = 100*3.00+ 100*3.50+200*4.00+(units-400)*4.50
	case _:
	    cost = 100*3.00+ 100*3.50+200*4.00+400*4.50+(units-700)*5.00
	    
    print('Bill  amount  :  ' ,cost)
else:
    print("input should be positive only ")
    
    
    
    
    
    


'''Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
x=int(input("Enter a positive integer number :"))
print("Fibonacci series")

if x==0:
    print("0")
else:

    a,b=0,1
    print(a)
    count=1
while count <= x:
    c=a+b
    a,b=b,c
    print(a)
    count=count+1
    
    
    
    # Find  outputs  (Home  work)
'''How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop'''


a = [10,20,15,18]
for x in a:
    print(x)
    
a = 'hyd'
for x in a:
    print(x)
    
a = range(5)
for i in a:
    print(a[i])
    
    
    
    
    
    # Find  outputs  (Home  work)
'''for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)'''
	
	
a = {10:20, 30:40, 50:60}
for x in a.keys():
    print(x)
for x in a.values():
    print(x)
for x in a.items():
    print(x)
    
    
    
    
    
    # Find outputs  (Home  work)
'''a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
for  x ,  y  in   a:
	print(x , y
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')'''
	
	
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a.items():
	print(x , y , sep = '...')
'''for  x , y  in   a:
	print(x , y , sep = '...')''' # error
    
    
    
    
    # Identify  error  (Home  work)
for  x  in   123:
        print(x)  # error int cannot be iterated
        
        
        
        

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) 
for  x   in  []:
        print(x)
for  x   in   {}:
        print(x)
for  x   in   set():
        print(x)
for  x   in   '':
        print(x)
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():
	print(x)  # error range() requires 1 argument, but 0 were given
for  x  in   (25):
	print(x) # error int object is not iterable
 
 
 #  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')  

'''output:
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
Bye'''






# How  to  print  each  element  and  the  corresponding  index
'''a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)'''


a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(i, a[i])
    
for x in a:
    print(a.index(x))
    
''' 
    output:
            0 25
            1 10.8
            2 Hyd
            3 True
            0
            1
            2
            3'''
            
            
            
            
            
            

#  How  to  print  list  elements  in  reverse  order   without  slice
'''a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)'''


a = [25 , 10.8 , 'Hyd' , True]

for x in a[::-1]:
    print(x)
    
for x in reversed(a):
    print(x)


'''output:

            True
            Hyd
            10.8
            25
            True
            Hyd
            10.8
            25      '''
            
            
            
            
            
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

for i in range(min(len(a),len(b))):
    c.append(a[i] + b[i])
'''How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop'''
print('3rd  list : ' , c)
'''How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)'''


'''
output:
Enter  1st  list  :  10,20,30
Enter  2nd  list  :  20,30,40,50,60
3rd  list :  [30, 50, 70]

'''




#  How  to  print  list  elements  from  indexes  2  to  4  without  slice

'''How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice'''

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

for x in range(len(a)):
    print(x)
    
for i in range(2,5):
    print(a[i])
    
for x in a:
    if a.index(x) >=2 and a.index(x) <=4:
         print(x)


'''
output:
            0
            1
            2
            3
            4
            5
            6
            'Hyd'
            True
            (3+4j)
            'hyd'
            True
            (3+4j)
            '''
            
            
            
        
#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)

'''
output:
a :   [11, 21, 16, 19]
b :   [10, 20, 15, 18]  '''




'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''

x = int(input("enter number:"))

for i in range(1,x+1):
    spaces = x-i
    stars = 2*i-1
    print(" " * spaces + "*" * stars)
    
'''
output:
enter number:5
    *
   ***
  *****
 *******
*********
'''


'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
print("even numbers")

i = 1
while i <= 20:
    print(2*i,)
    i += 1
    
'''output:
even numbers    
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
'''





'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

i = 1
while i <= 20:
    print(2*i-1)
    i += 1
    
'''output:  
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39'''




'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
n = (int(input("enter natural number:")))
i = 1
while i <= n:
    print(i)
    i += 1
    
'''output:
enter natural number:5
1
2
3
4
5
'''




'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

n = int(input("reverse numbering:"))

i = n
while i >= 1:
    print(i)
    i-=1
    
'''output:  
reverse numbering:5
5
4
3
2
1
'''



'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''


x = int(input("enter number:"))
total_sum = 0
for i in range(1,x+1):
    total_sum += 1.1*i
    
print("sum of the series:",total_sum)


'''output:
enter number:5
sum of the series: 16.5'''





'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''


x = int(input("enter number:"))

sum = 0
for i in range(1,x+1):
    sum += 2*i
    
print("sum of the even series:", sum)

'''output:
enter number:20
sum of the series: 420
'''




'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''


x = int(input("enter number:"))

sum = 0
for i in range(1,x+1):
    sum += (2*i-1)
    
print("sum of the odd series:", sum)

'''output:
enter number:20
sum of the series: 400
'''


'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''

x = int(input("enter number:"))

sum = 0
for i in range(1,x+1):
    sum += i
    
print("sum of the series:", sum)

'''output:
enter number:5
sum of the series: 15
'''



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

'''output:
1
Sec
Hello
2
Sec
Hello
3
Hello
4
Sec
Hello
5
Sec
Hello
6
Hello
7
Sec
Hello
Outside loop'''



# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')
 
 '''
 output:
 SyntaxError: 'continue' not properly in loop
 continue' statement can only be used inside a loop'''
 
 
 
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

'''output:  
1
Sec
Hello
2
Sec
Hello
3
Hello
Outside loop'''




# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
 
'''
output:
SyntaxError: 'break' outside loop
break' statement can only be used inside a loop
'''


