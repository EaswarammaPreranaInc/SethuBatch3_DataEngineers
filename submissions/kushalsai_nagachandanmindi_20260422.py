import  time
list = [10 , 20 , 15 , 18 , 5]
def f1(x):
    return x * x
m = map(f1 ,  list)
print(type(m))
print(m)
for x in m:
    print(x)
    time . sleep(1)

# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m)) # 10 <1sec> \n 20 <1sec> \n 15 <1sec> \n 5 <1sec> \n 18
		time . sleep(1)
	except  StopIteration:
		break

# Find  outputs (Home  work)
import   time
def  disp(m):
	while   True:
		try:
			print(next(m))
			time . sleep(1)
		except  StopIteration:
			break
#  End  of  the  function
list = [ { 'country' : 'India' , 'sale' : 150.5} ,
           { 'country' : 'China' , 'sale' : 200.2} ,
           { 'country' : 'USA' , 'sale' : 300.3} ,
           { 'country' : 'UK' , 'sale' : 210.4} ]
m1 = map(lambda  x  :  x['country'] , list)
print('Map   m1') # Map   m1
disp(m1) # India <1sec> \n China <1sec> \n USA <1sec> \n UK 
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2') # Map   m2
disp(m2) # 150.5 <1sec> \n 200.2 <1sec> \n 300.3 <1sec> \n  216

import time
a = eval(input("Enter the list: "))
m = map(lambda x: 1.8*x+32, a)
for x in m:
    print(x)
    time.sleep(1)

a = range(int(input("Enter no. of powers: ")))
m = map(lambda x : 2**x, a)
print('Powers of 2')
while True:
    try:
        print(next(m))
    except StopIteration:
        break

a = eval(input("enter the list: "))
def f1(x):
    return 3.14159 * x * x
m = map(f1, a)
print('Area of each radius in the list: ')
while True:
    try:
        print(next(m))
    except StopIteration:
        break
print('end')

a = eval(input("enter tuple: "))
b = eval(input("enter tuple: "))
def f1(x, y):
    return x+y
m = map(f1, a, b)
while True:
    try:
        print(next(m))
    except StopIteration:
        break
print('end')

a = eval(input("enter the list1: "))
b = eval(input("enter the list2: "))
m = map(lambda x,y: x*y, a,b)
cnt = 0
for x in m:
    print(F'product of {a[cnt]} and {b[cnt]} is {x}')
    cnt+=1
print('end')

# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m)) # 40 <1sec> \n 30 <1sec> \n 36 <1sec> \n 50 <1sec> \n 34
		time . sleep(1)
	except:
		break

# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f)) # 100 <1sec> \n 400 <1sec> \n 144 <1sec> \n 324 <1sec> \n 196
		time . sleep(1)
	except:
		break

from functools import reduce
a = eval(input("Enter the list: "))
r = reduce(lambda x, y: x if x>y else y, a)
print("Largest element of the list is: ", r)

# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans) #1574

'''
 reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 ,20,15,18,25 ))
 reduce( lambda  x , y  : x + y , 400,225,324,625 ))
 1574
'''





# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')
while   True:
        x = next(c1)
        if   x > 9:
                break
        print(x)
print('For  loop')
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x)
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))
c4 = count()
print(*c4)

'''
While  loop
0
1
2
3
4
5
6
7
8
9
For  loop
0
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
Element :  0
Waiting time and memory error
'''


#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
# End  of  the  function
a = count(start = 10)
disp(a)
b = count(start = 10 , step = 5)
disp(b)
c = count(start = 10 , step = -2.5)
disp(c)
d = count()
disp(d)

'''
10	11	12	13	
10	15	20	25	
10	7.5	5.0	2.5	
0	1	2	3
'''



#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop')
while   True:
        try:
                print(next(z1))
        except  StopIteration:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))
print('*z3 :  ' ,  *z3)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4))


'''
While  loop
(10,0)
(20,1)
(15,2)
(18,3)
for loop
(10,4)
(20,5)
(15,6)
(18,7)
Next  element :  (10,8)
*z3 :  (20,9) (15,10) (18,11)
Next  element  : (10,12)

'''


# Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')
while   True:
        try:
                print(next(z1))
        except:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(cnt , list)
print(next(z3))
print(*z3)
z4 = zip(list , cnt)
print(next(z4))

'''
while  loop
(0,10)
(1,20)
(2,15)
(3,18)
for  loop
(10,5)
(20,6)
(15,7)
(18,8)
(10,9)
(10,20) (11,15) (12,18)
(10,14)
'''