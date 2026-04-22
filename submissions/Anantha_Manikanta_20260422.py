'''
1) Modify following program such that
 Use regular function instead of lambda function
2) Use for loop instead of while loop

import  time
list = [10 , 20 , 15 , 18 , 5]
m = map(lambda  x :  x  *  x ,  list)
print(type(m))
print(m)
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
	time . sleep(1)
'''
import time
list = [10 , 20 , 15 , 18 , 5]
def sq(x):
	return x * x
m = map(sq , list)
print(type(m))
print(m)
for x in m:
	print(x)
	time.sleep(1)
'''
2) # Find outputs (Home work)
import time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda x : x[1] , a)
while True:
	try:
		print(next(m)) # 10 <nextline> 20 <nextline> 15 <nextline> 5 <nextline> 18
		time.sleep(1)
	except StopIteration:
		break
'''
'''
3) # Find outputs (Home work)
import time
def disp(m):
	while True:
		try:
			print(next(m))
			time.sleep(1)
		except StopIteration:
			break
# End of the function
list = [ { 'country' : 'India' , 'sale' : 150.5} ,
           { 'country' : 'China' , 'sale' : 200.2} ,
           { 'country' : 'USA' , 'sale' : 300.3} ,
           { 'country' : 'UK' , 'sale' : 210.4} ]
m1 = map(lambda x : x['country'] , list)
print('Map   m1')
disp(m1) # India <nextline> China <nextline> USA <nextline> UK <nextline>
m2 = map(lambda x : x['sale'] , list)
print('Map   m2')
disp(m2) # 150.5 <nextline> 200.2 <nextline> 300.3 <nextline> 210.4
'''
'''
4) Write a program to convert each celsius temperature of the list to farenheit temperature
1) What is the formula to convert celsius temperature to farenheit ? ---> 1.8 * celsius-temp + 32
2) Let input be list of celsius temperatures such as [30 , 40 , 50 , 25]
   What is the output ? ---> 1.8 * 30 + 32
                             1.8 * 40 + 32
                             1.8 * 50 + 32
                             1.8 * 25 + 32
'''
import time
ip = input('Enter list of celsius temperatures : ')
cs = ip.replace('[', '').replace(']', '')
clist = [float(x) for x in cs.split(',')]
print('Equivalent fahrenheit temperatures')
for c in clist:
    f = 1.8 * c + 32
    print(float(f))
    time.sleep(0.5)
# 5)  Write a program to print 2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9 using map iterator (Home work)
import time
a = range(10)
m = map(lambda x: 2 ** x, a)
b = list(m) 
print("Powers of 2: ")
for i in b:
    print(i)
    time.sleep(0.5)
'''
6) # Write a program to determine area of circle for each radius in the list
1) What is area of circle ? ---> 3.14159 * r * r
2) Let input be [3.5 , 2.8 , 4.2 , 1.9]
   What are the outputs ? ---> Area of radius 3.5
                               Area of radius 2.8
                               Area of radius 4.2
                               Area of radius 1.9
'''
import time
ip = input('Enter list of radii: ')
cs = ip.replace('[', '').replace(']', '')
radii = [float(r) for r in cs.split(',')]
areas = map(lambda r: round(3.14159 * r * r, 2), radii)
print('Area of each radius in the list: ')
for area in areas:
    print(area)
    time.sleep(0.5)
'''
7) Write a program to add two tuples of different sizes and store the results in 3rd tuple
Let 1st tuple be (10 , 20 , 30 , 40) and 2nd tuple be (1 , 2 , 3 , 4 , 5 , 6)
What is the 3rd tuple ? ---> (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4) and 5 and 6 are ignored
'''
def tupleadd(ip):
    cs = ip.replace('(', '').replace(')', '')
    return tuple(int(x) for x in cs.split(','))

t1 = tupleadd(input('Enter first tuple : '))
t2 = tupleadd(input('Enter second tuple : '))
result = tuple(map(lambda x, y: x + y, t1, t2))
print('Addition tuple : ', result)

'''
8) Write a program to multiply two lists and store results in 3rd list
Let 1st list be [10 , 20 , 15 , 18 , 19 , 17] and 2nd list be [1 , 5 , 3 , 2]
What is the 3rd list ? ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2] and ignores 19 and 17
'''
ip = input('Enter list of numbers (or) strings:')
cs = ip.replace('[', '').replace(']', '')
data = [int(x) for x in cs.split(',')]
largest = max(data, key=lambda x: x)
print('Largest element : ', largest)
'''
9) # filter inside map
import time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda y : y + y , filter(lambda x : x >= 15 , a))
while True:
	try:
		print(next(m)) # 30 <nextline> 36 <nextline> 50 <nextline> 34
		time.sleep(1)
	except:
		break
'''
'''
10) # map inside filter (Home work)
import time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda y : y % 2 == 0 , map(lambda x : x ** 2 , a))
while True:
	try:
		print(next(f))  # 100 <nextline> 400 <nextline> 144 <nextline> 324 <nextline> 196
		time.sleep(1)
	except:
		break
'''
'''
11) Write a program to determine largest element of the list with reduce() function
Let list be [10 , 20 , 15 , 30 , 25 , 40 , 35]
What is the largest element of list ? ---> 40
Hint: Use reduce() function
'''
from functools import reduce
a = []
n = int(input('How many elements ? : '))
for i in range(n):
	a.append(int(input('Enter element : ')))
ans = reduce(lambda x , y : x if x > y else y , a)
print(ans)
'''
12) # Find outputs (Home work)
from functools import reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce(lambda x , y : x + y , map(lambda y : y ** 2 , filter(lambda x : x >= 15 , a)))
print(ans) # 2218
'''
'''
13) # Find outputs (Home work)
from itertools import count
c1 = count()
print('While loop')
while True:
	x = next(c1)
	if x > 9:
		break
	print(x)
print('For loop')
c2 = count()
for x in c2:
	if x > 20:
		break
	print(x)
# End of for loop
c3 = count()
print('Element : ' , next(c3))
c4 = count()
print(*c4) # While loop <nextline> 0 <nextline> 1 <nextline> 2 <nextline> 3 <nextline> 4 <nextline> 5 <nextline> 6 <nextline> 7 <nextline> 8 <nextline> 9 <nextline> 
For loop <nextline> 0 <nextline> 1 <nextline> 2 <nextline> 3 <nextline> 4 <nextline> 5 <nextline> 6 <nextline> 7 <nextline> 8 <nextline> 9 <nextline> 10 <nextline> 11 <nextline> 12 <nextline> 13 <nextline> 14 <nextline> 15 <nextline> 16 <nextline> 17 <nextline> 18 <nextline> 19 <nextline> 20 <nextline> Element :  0 <nextline> Infinite.....
'''
'''
14) # Find outputs (Home work)
from itertools import count
def disp(cnt):
	for i in range(4):
		print(next(cnt) , end = '\t')
	print()
# End of the function
a = count(start = 10)
disp(a)
b = count(start = 10 , step = 5)
disp(b)
c = count(start = 10 , step = -2.5)
disp(c)
d = count()
disp(d) # 10	11	12	13 <nextline> 10	15	20	25 <nextline> 10	7.5	5.0	2.5 <nextline> 0	1	2	3
'''
'''
15) # Find outputs (Home work)
from itertools import count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While loop')
while True:
	try:
		print(next(z1)) # (10, 0) <nextline> (20, 1) <nextline> (15, 2) <nextline> (18, 3)
	except StopIteration:
		break
z2 = zip(list , cnt)
print('for loop')
for x in z2:
	print(x) # (10, 4) <nextline> (20, 5) <nextline> (15, 6) <nextline> (18, 7)
z3 = zip(list , cnt)
print('Next element : ' , next(z3)) # Next element :  (10, 8)
print('*z3 : ' , *z3) # *z3 :  (20, 9) (15, 10) (18, 11)
z4 = zip(list , cnt)
print('Next element : ' , next(z4)) # Next element :  (10, 12)
'''
'''
16) # Most tricky program
# Find outputs (Home work)
from itertools import count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while loop')
while True:
	try:
		print(next(z1))
	except:
		break
z2 = zip(list , cnt)
print('for loop')
for x in z2:
	print(x)
z3 = zip(cnt , list)
print(next(z3))
print(*z3)
z4 = zip(list , cnt)
print(next(z4)) # while loop <nextline> (0, 10) <nextline> (1, 20) <nextline> (2, 15) <nextline> (3, 18) <nextline> for loop <nextline> (10, 4) <nextline> (20, 5) <nextline> (15, 6) <nextline> (18, 7) <nextline> (8, 10) <nextline> (9, 20) <nextline> (10, 15) <nextline> (11, 18) <nextline> (10, 12)
'''