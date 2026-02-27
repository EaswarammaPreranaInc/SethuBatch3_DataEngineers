1) Write  a  program  to  determine  bill  amount  and  input  is  units

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

output:
units = int(input('Enter units : '))

match units // 100:
    case 0:  # units between 0 and 99
        cost = units * 3.00

    case 1:  # units between 100 and 199
        cost = 100 * 3.00 + (units - 100) * 3.50

    case 2 | 3:  # units between 200 and 399
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00

    case 4 | 5 | 6:  # units between 400 and 699
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50

    case _:  # units >= 700
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print('Bill amount : ', cost)




2)  Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''

a = 0
b = 1
n = int(input())
i = 1
print('Fibonacci series')
while i < n:
     print(a)
     a, b = b , a + b
     i+=1




3)Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop

code:
for i in [10 , 20 , 15 , 18] :
	print(i)
for i in 'Hyd':
	print(i)
for i in range(5):
    print(i)
output:
10
20
15
18
H
y
d
0
1
2
3
4



4) Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)                                                
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)

Output:
10
30
50

20
40
60

(10 ,20 )
(30 ,40 )
(50 ,60 )

10
30
50





5)Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():               
	print(x , y , sep = '...')
for  x ,  y  in   a:                                # Error
	print(x , y)
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:      # Error
	print(x , y , sep = '...')
Output:
10...20
30...40
50...60





6)Identify  error  (Home  work)
for  x  in   123:                 # 123 is a non sequence(not iterable)
        print(x)   

             

7)Find  outputs  (Home  work)
for  x   in   (): 
        print(x)                          # empty tuple
for  x   in  []:
        print(x)                          # empty list
for  x   in   {}:
        print(x)                          # empty dict
for  x   in   set():
        print(x)                          # empty set
for  x   in   '':
        print(x)                          # empty str
for  x  in  range(10 , 10):             
	print(x)                          # no output
for  x  in   range():
	print(x)                          # Error range should have atleast 1 argument
for  x  in   (25):
	print(x)                          # Error int obj not iterable


8) Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):        
			print(i ,  j) 
	print('Hello')
print('Bye')

Output:
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




9)How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

output:  a = [25 , 10.8 , 'Hyd' , True]
         for i in range(len(a)):
           print(f'{i} : {a[i]}')



10) How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

output:  
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)-1,-1,-1):
  print(f'{i} : {a[i]}')



11) Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

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


output:
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])

print('list 3 :', c)



12) How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

output:

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(2, 5):
  print(a[i])


13)#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]     # output : a :   [11, 21, 16, 19]
                                       b :   [10, 20, 15, 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)



14) Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines

'''

output:a = 
int(input())
i = 1 
for i in range(1, a + 1):
  print(' '*(a-i)+'*'*(2*i-1))
 


15) (Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

output:
n = int(input())
i = 1
while i <= n:
  a = 2*i
  print(a)
  i+=1
print("Bye")



16)Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

output:
n = int(input())
i = 1
while i <= n:
  a = 2*i-1
  print(a)
  i+=1




17)Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

output:
n  = int(input())
i = 1 
while i <= n:
  print(i)
  i+=1




18)Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop


output:
i = int(input())
while i>=1:
  print(i)
  i=i-1


19)Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''



20)Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
output:
n  = int(input())
i = 1
s = 0
while i <= n:
  s = i+i*i
 # print(i)
  i+=1
print(f'Sum of first {n} numbers is : {s}')


or

n = int(input())
sum = 0
for i in range(1,n+1):
  sum = sum + 2*i
print(f'Sum of first {n} numbers : {sum}')


21)Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop

output:
n = int(input())
sum = 0
for i in range(1,n+1):
  sum = sum + 2*i-1
print(f'Sum of first {n} numbers : {sum}')





22)Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''

output:
n = int(input("Enter n: "))

sum = 0
for i in range(1, n + 1):
    sum = sum + i

print("Sum:", sum)





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


Output :
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




24)Identify Error  (Home  work)
if ():
	print('Hyd')
	continue                         #continue can be used within loops
	print('Sec')


25)Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:                            
		break
	else:                 
		print('Sec')
	print('Hello')
#End  of  the  loop
print('Outside loop')

Output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop



26)# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')                      
	break                      # works only with for loop and while loop
	print('Sec')