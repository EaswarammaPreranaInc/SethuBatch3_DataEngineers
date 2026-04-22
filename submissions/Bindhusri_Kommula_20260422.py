'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
list = [10 , 20 , 15 , 18 , 5]
def f1(x):
    return x*x
m=map(f1,list)
print(type(m))
print(m)
for x in m:
    print(x)




# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m)) # 10 <nextline> 20 <nextline>  15 <nextline> 5 <nextline> 18
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
m1 = map(lambda  x  :  x['country'] , list) # empty object
print('Map   m1') # Map   m1
disp(m1) # India <nextline> China <nextline> USA <nextline> UK
m2 = map(lambda  x  :  x['sale']  , list)  # empty object
print('Map   m2')  # Map   m2
disp(m2) # 150.5 <nextline> 200.2 <nextline> 300.3 <nextline> 210.4


'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''

import  time
a =   [30 , 40 , 50 , 25]
m = map(lambda   x  :  1.8 *x + 32  ,  a)
while  True:
	try:
		print(next(m)) 
		time . sleep(1)
	except  StopIteration:
		break



# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)

import  time
nums=range(10)
m = map(lambda   x  :  2**x ,nums)
while  True:
	try:
		print(next(m)) 
		time . sleep(1)
	except  StopIteration:
		break


'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''

import  time
a=[3.5 , 2.8 , 4.2  , 1.9]
m = map(lambda   x  :  3.14159 * x*x ,a)
while  True:
	try:
		print(next(m)) 
		time . sleep(1)
	except  StopIteration:
		break


'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''

import  time
a=(10 , 20 , 30 , 40)
b=(1 , 2 , 3 , 4 ,  5  ,  6)
m = tuple(map(lambda   x ,y :  x+y,a,b))
print(m)


'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''

import  time
a=[10 , 20 , 15 , 18 , 19 , 17]
b=[1 , 5 , 3 , 2]
m = list(map(lambda   x ,y : x*y,a,b ))
print(m)


# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m)) # 40 <nextline> 30 <nextline> 36 <nextline> 50 <nextline> 34
		time . sleep(1)
	except:
		break


# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f)) # 100 <nextline> 400 <nextline> 144 <nextline> 324 <nextline> 196
		time . sleep(1)
	except:
		break




'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''

from functools import reduce
a=[10 , 20 , 15 , 30 , 25 , 40 , 35]
m = reduce(lambda  x,y: x if x>y else y,a )
print(m)


# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a))) 20 15 18 25   400  225 324 625
print(ans) # 1574


# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop') # While  loop
while   True:
        x = next(c1) 
        if   x > 9:
                break
        print(x) # 0 <nextline> 1 <nextline> 2 <nextline> 3 <nextline> 4 <nextline> 5 <nextline> 6 <nextline> 7 <nextline> 8 <nextline> 9
print('For  loop') # For  loop
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x) # 0 <nextline> 1 <nextline> .... <nextline> 20
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3)) # 0
c4 = count()
print(*c4) # memory error



#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t') 
        print()
# End  of  the  function
a = count(start = 10)
disp(a) # 10 \t  11 \t  12 \t 13
b = count(start = 10 , step = 5)
disp(b) # 10 \t 15 \t 20 \t  25
c = count(start = 10 , step = -2.5)
disp(c) # 10 \t  7.5 \t  5.5 \t  0.0
d = count()
disp(d) # 0 \t  1 \t  2 \t  3


#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop') # 'While  loop
while   True:
        try:
                print(next(z1)) # (10,0) <nextline> (20,1) <nextline> (15,2) <nextline> (18,3)
        except  StopIteration:
                break
z2 = zip(list , cnt)
print('for  loop') # for  loop
for  x   in    z2:
        print(x) # (10,4) <nextline> (20,5) <nextline> (15,6) <nextline> (18,7)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3)) # (10,8)
print('*z3 :  ' ,  *z3) # (20,9) <nextline> (15,10) <nextline> (18,11)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4)) # (10,12)


# Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')#while  loop
while   True:
        try:
                print(next(z1)) # (0,10) <nextline> (1,20) <nextline> (2,15) <nextline> (3,18)
        except:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x) # (10,5) <nextline> (20,6) <nextline> (15,7) <nextline> (18,8)
z3 = zip(cnt , list)
print(next(z3)) # (9,10)
print(*z3) # (10,20) <nextline> (11,15) <nextline> (12,18)
z4 = zip(list , cnt)
print(next(z4)) # (10,14)