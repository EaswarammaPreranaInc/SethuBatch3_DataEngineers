 '''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
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
# Regular function instead of lambda
def square(x):
    return x * x
lst = [10, 20, 15, 18, 5]
m = map(square, lst)
print(type(m))
print(m)
for value in m:
    print(value)
    time.sleep(1)
    '''



	
 # Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m))#10<next line>20<next line>15<next line>5<next line>18
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
m1 = map(lambda  x  :  x['country'] , list)  #extracts country names
print('Map   m1')#Map m1
disp(m1)
m2 = map(lambda  x  :  x['sale']  , list)  #extracts sales values
print('Map   m2')#map m2
disp(m2)
'''
output
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
    What  is  the  output ?  --->   1.8 * 30 + 32=86.0
				    1.8 * 40 +32=104.0
				    1.8 * 50 + 32=122.0
				    1.8 * 25 + 32=77.0
				    
'''
def c_to_f(c):
    return 1.8 * c + 32

celsius = eval(intput("enter input"))

fahrenheit = map(c_to_f, celsius)

print(list(fahrenheit))


 
 # Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)

import time
# map iterator for powers of 2
m = map(lambda x: 2 ** x, range(10))
for value in m:
    print(value)
    time.sleep(1)


 '''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
				     Area  of  radius  2.8
				     Area  of  radius  4.2
				     Area  of  radius  1.9
'''

 radii = [3.5, 2.8, 4.2, 1.9]

for r in radii:
    area = 3.14159 * r * r
    print("Area of radius", r, "=", area)
 '''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple


Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''

t1 = (10, 20, 30, 40)
t2 = (1, 2, 3, 4, 5, 6)
t3 = tuple(a + b for a, b in zip(t1, t2))
print("Third tuple:", t3)

 '''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''

l1 = [10, 20, 15, 18, 19, 17]
l2 = [1, 5, 3, 2]

l3 = [a * b for a, b in zip(l1, l2)]

print("Third list:", l3)


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

# output : 

40
30
36
50
34



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

# output : 

100
400
144
324
196



'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''

# output :

from functools import reduce
lst = [10, 20, 15, 30, 25, 40, 35]
largest = reduce(lambda x, y: x if x > y else y, lst)
print("Largest element:", largest)



 # Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)#(20² = 400  15² = 225  18² = 324  25² = 625 ,400 + 225 = 625  625 + 324 = 949  949 + 625 = 1574 ) 
# output=1574




# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')#while loop
while   True:
        x = next(c1)
        if   x > 9:
                break
        print(x)#0 to 9
print('For  loop')#for loop
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x)#0 to 20
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))#Element:0
c4 = count()
print(*c4)#run infinitely





#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
# End  of  the  function
a = count(start = 10)
disp(a)#10<space>11<space>12<space>13
b = count(start = 10 , step = 5)
disp(b)#10 <space> 15<space>20<space>25
c = count(start = 10 , step = -2.5)
disp(c)  #10<space> 7.5<space>	 5.0<space>  2.5
d = count()
disp(d)  #0   <space>1	<space> 2 <space> 3




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

'''output

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
output
while  loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for  loop
(10, 5)
(20, 6)
(15, 7)
(18, 8)
(9, 10)
(10, 20) (11, 15) (12, 18)
(10, 14)
'''
