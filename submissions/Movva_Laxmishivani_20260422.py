'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
# Regular function
def f1(x):
    return x * x
list = [10 , 20 , 15 , 18 , 5]
m = map(f1, list)
print(type(m)) # <class 'map'>
print(m) # Type and address of map object 'm'
for value in m:
    print(value)
    time.sleep(1)
'''
100
400
225
324
25
'''
# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
'''
10
20
15
5
18
'''
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
print('Map   m1')
disp(m1)
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')
disp(m2)
'''
Map   m1
India
China
USA
UK
Map   m2
150.5
200.2
300.3
210.4
'''
'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature
1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32
2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
Sample output:
Enter list of celsius temperatures : [10,20,15,18]
Equivalent farenheit temperatures
50.0
68.0
59.0
64.4
'''
def temp(c):
    return 1.8 * c + 32
list = eval(input('Enter list of celsius temperatures : '))
m = map(temp, list)
print('Equivalent farenheit temperatures')
for x in m:
    print(x)
    
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
def f1(x):
    return 2 ** x
m = map(f1, range(10))
print('Powers of 2')
for x in m:
    print(x)
    
'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list
1) What  is  area  of  circle ?  --->  3.14159 * r * r
2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
Sample output:
Enter list of radii : [3.5 , 2.9 , 4.6 , 1.8]
Area of each radius in the list
38.48
26.42
66.48
10.18
'''
def f1(r):
    return 3.14159 * r * r
list = eval(input('Enter list of radii : '))
m = map(f1, list)
print('Area of each radius in the list')
for x in m:
    print(round(x, 2))
    
'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
Sample output:
Enter first tuple : (10,20,15,18,19,25)
Enter second tuple : (30,40,35,12)
Addition tuple : (40, 60, 50, 30)
'''
# Add two tuples of different sizes

def add(x, y):
    return x + y

t1 = eval(input('Enter first tuple : '))
t2 = eval(input('Enter second tuple : '))
m = map(add, t1, t2)
out = tuple(m)
print('Addition tuple :', out)
'''
Enter first tuple : (10,20,15,18,19,25)
Enter second tuple : (30,40,35,12)
Addition tuple : (40, 60, 50, 30)
'''

'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
# Multiply two lists and store result in 3rd list

def multiply(x, y):
    return x * y

l1 = eval(input('Enter first list : '))
l2 = eval(input('Enter second list : '))
m = map(multiply, l1, l2)
out = list(m)
print('3rd list:', out)
'''
Enter first list : [10 , 20 , 15 , 18 , 19 , 17]
Enter second list : [1 , 5 , 3 , 2]
3rd list : [10, 100, 45, 36]
'''

# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
40
30
36
50
34
'''
# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
100
400
144
324
196
'''
'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function
Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40
Hint:  Use  reduce()  function
Sample output:
Enter list of numbers (or) strings: [10 , 20 , 15 , 30 , 25 , 40 , 35]
Largest element : 40
'''
from functools import reduce
def f1(x, y):
    return x if x > y else y
list = eval(input('Enter list: '))
result = reduce(f1, list)
print('Largest element :', result)
'''
Enter list: [10 , 20 , 15 , 30 , 25 , 40 , 35]
Largest element : 40
'''
# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans) # 1574
'''
Filter
20, 15, 18, 25
Map
20 -- 400  
15 -- 225  
18 -- 324  
25 -- 625  
Reduce
400 + 225 =625
625 + 324 = 949
949 + 625 = 1574
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
print(*c4) # Error because c4 can't store infinite sequence
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
Element :   0
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
(10, 0)
(20, 1)
(15, 2)
(18, 3)
for  loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
Next  element :   (10, 8)
*z3 :   (20, 9) (15, 10) (18, 11)
Next  element  :  (10, 12)
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
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for  loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
next(z3)
(8, 10)
*z3
(9, 20) (10, 15) (11, 18)
next(z4)
(10, 12)
'''