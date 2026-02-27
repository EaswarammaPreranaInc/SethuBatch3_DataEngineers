units = int(input('Enter  units :   '))   #   175
match  units // 100:
	case  0:   #   units  between  0  and  99
		cost = units * 3.00
	case  1:  #  units  between  100 and  199
		cost =  100 * 3.00 + (units - 100) * 3.50
	case  2 | 3: # units  between  200 and  399
		cost = 100*3.00 + 100*3.50 + (units - 200)*4.00
	case  4 | 5 | 6 : #units  between  400 and 699
		cost = 100*3.00 + 100*3.50 + 200*4.00 + (units - 400)*4.50
	case  _: #units  above 700				
		cost = 100*3.00 + 100*3.50 + 200*4.00 + 300*4.50 + (units -700)*5.00
print('Bill  amount  :  ' , cost)

'''
output
Enter  units :   1200
Bill  amount  :   5300.0
'''




x=int(input("Enter value of x : "))
print("Fibonacci  Series")
a,b=0,1
while a<=x:
    print(a)
    c=a+b
    a=b
    b=c
	
	
'''
output
Enter value of x : 10
Fibonacci  Series
0
1
1
2
3
5
8
Enter value of x : 0
Fibonacci  Series
0
Enter value of x : 1
Fibonacci  Series
0
1
1
'''




for  x in [10,20,15,18]:
    print(x)

'''
output
10
20
15
18
'''

for x in 'Hyd':
    print(x)

'''
output
H
y
d
'''


for num in range(5):
    print(num)
'''
output
0
1
2
3
4
'''




# Find  outputs  (Home  work)
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
	
'''
output
10
30
50

20
40
60

(10, 20)
(30, 40)
(50, 60)

10
30
50
'''




# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
'''
output
10...20
30...40
50...60
'''




for  x ,  y  in   a:
	print(x , y)

'''
output
error cannot unpack non-iterable int object
'''




for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
	
'''
output
error cannot unpack non-iterable int object
'''




# Identify  error  (Home  work)
for  x  in   123:
        print(x)
'''
output
123 is integer which is non-sequence which is not iterable
'''




# Find  outputs  (Home  work)
for  x   in   ():
        print(x)#empty prints nothing
for  x   in  []:
        print(x)#empty prints nothing
for  x   in   {}:
        print(x)#empty prints nothing
for  x   in   set():
        print(x)#empty prints nothing
for  x   in   '':
        print(x)#empty prints nothing
for  x  in  range(10 , 10):
	print(x)#empty prints nothing
for  x  in   range():
	print(x)#error atleast 1 argument is required in range()
for  x  in   (25):
	print(x)#(25) is int which is not iterable
	
	
	
	
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')
'''
output
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




a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(i,a[i])
print('Indexed  based  for loop')

'''
output
0 25
1 10.8
2 Hyd
3 True
Indexed  based  for loop
'''




a = [25,10.8,'Hyd', True]
for x in a:
    print(a.index(x),x)
print('For each loop')

'''
output
0 25
1 10.8
2 Hyd
3 True
For each loop
'''




a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for i in range(len(a)-1,-1,-1):
    print(i,a[i])

'''
output
Indexed for loop
3 True
2 Hyd
1 10.8
0 25
'''




a = [25, 10.8, 'Hyd', True]
print('For each loop')
for x in reversed(a):
    print(x)

'''
output
True
Hyd
10.8
25
'''




a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
print('Indexed for loop')
for i in range(min(len(a), len(b))):
    res = a[i] + b[i]
    c.append(res)
print('3rd list :', c)

'''
output
Enter  1st  list  :  [10,12,15,18]
Enter  2nd  list  :  [30 , 40 , 35 , 12 , 100 , 200 , 300]
Indexed for loop
3rd list : [40, 52, 50, 30]
'''




a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for i in range(2,5):
    print(a[i])

'''
output
Indexed for loop
Hyd
True
(3+4j)
'''




#Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1#change th copy of not orginal
print('b :  ' ,  b)

'''
output
a :   [11, 21, 16, 19]
b :   [10, 20, 15, 18]
'''




n = int(input("How many lines ? : "))
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
	
'''
output
How many lines ? : 7
      *
     ***
    *****
   *******
  *********
 ***********
*************
'''




print("First 20 even numbers")
i=1
while(i<=20):
    print(2*i)
    i=i+1
print("Bye")

'''
output
First 20 even numbers
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
Bye
'''




print("First 20 odd numbers")
i=1
while(i<=20):
    print(2*i-1)
    i=i+1
	
'''
output
First 20 even numbers
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
39
'''




n=int(input("Enter Value of n : "))
print("Natural Numbers")
i=1
while(i<=n):
    print(i)
    i=i+1

'''
output
Enter Value of n : 25
Natural NUmbers
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
'''




print("Numbers from 10 downto 1 in steps of -1")
i=10
while(0<i<=10):
    print(i)
    i=i-1
'''
output
Numbers from 10 downto 1 in steps of -1
10
9
8
7
6
5
4
3
2
1
'''




number=int(input("How many terms would you like to add : "))
total=0
for i in range(1,number+1):
    term=1.1*i
    total += term
print("Sum : ",total)

'''
output
How many terms would you like to add : 5
Sum : 16.5
'''




total=0
for i in range(1,21):
    even=2*i
    total += even
print("Sum of first 20 even numbers : ",total)

'''
output
Sum of first 20 even numbers : 420
'''




total=0
for i in range(1,21):
    odd=2*i-1
    total += odd
print("Sum of first 20 odd numbers :",total)

'''
output
Sum of first 20 odd numbers : 400
'''




n=int(input("How many terms would you like to add : "))
total=0
for i in range(1,n+1):
    term=i
    total += term
print(total)

'''
output
How many terms would you like to add : 10
55
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
'''
output
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
	continue
	print('Sec')

'''
output
cannot use continue inside an if statement unless that if statement is sitting inside a loop.
'''




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
output
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
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
	

'''
output
cannot use break inside an if statement unless that if statement is sitting inside a loop
'''
