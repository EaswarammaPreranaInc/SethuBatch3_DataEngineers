'''Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
list = [10 , 20 , 15 , 18 , 5]
def f1(x):
	return x*x
m = map(f1,  list)
print(type(m))# <class 'map'>
print(m)# type and address
while   True:
	try:
		print(next(m))#100 200 225 324 25
		time . sleep(1)
	except  StopIteration:
		break
	time . sleep(1)


# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m))# 10 20 15 5 18
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
print('Map   m1')# Map m1
disp(m1)# # India China USA UK
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')# Map m2
disp(m2)# 150.5 200.2 300.3 210.4


#Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature
import time
list=eval(input("Enter list : "))
m=map(lambda x: 1.8 * x + 32, list)
for y in m:
    print(y)
    time.sleep(0.5)

# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
import time 
m1=map(lambda x: 2**x,range(10))
for y in m1:
    print(y)
    time.sleep(1)

#Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list
import time , math
list=eval(input("Enter list : "))
m2=map(lambda x: math.pi * x * x,list)
for y in m2:
    print(y)
    time.sleep(0.5)

import time
tpl1=eval(input("Enter 1st tuple : "))
tpl2=eval(input("Enter 2nd tuple : "))
m3=map(lambda x,y: x+y,tpl1,tpl2)
tpl=tuple(m3)
print(tpl)


#Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

import time
l1=eval(input("Enter 1st list : "))
l2=eval(input("Enter 2nd list : "))
m4=map(lambda x,y: x*y,l1,l2)
l=list(m4)
print(l)

# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:                   # 20 15 18 25 17
	try:
		print(next(m))# 40 30 36 50 34
		time . sleep(1)
	except:
		break

# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:                         # 100 400 225 144 324 25 196 625 289
	try:
		print(next(f))# 100 400 144 324 196
		time . sleep(1)
	except:
		break

#Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function
from functools import reduce
list=eval(input("Enter list : "))
res=reduce(lambda x,y : max(x,y),list)
print(res)


# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14] # 1574    #400 225 324 625    # 20 15 18 25
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans) 

# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')# While loop
while   True:
        x = next(c1)
        if   x > 9: # x is # 0 1 2 3 4 5 6 7 8 9 10
                break
        print(x)# 0 1 2 3 4 5 6 7 8 9 
print('For  loop')# For loop
c2 = count()
for  x  in  c2:
	if  x  >  20:# 0 1 2 3 4 ........... 20 21
		break
	print(x)# 0 1 2 3 4 ........... 20
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))# 0
c4 = count()
print(*c4)# waiting time and memory

#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
# End  of  the  function
a = count(start = 10)
disp(a)# 10 11 12 13
b = count(start = 10 , step = 5)
disp(b)# 10 15 20 25
c = count(start = 10 , step = -2.5)
disp(c)# 10 7.5 5.0 2.5 
d = count()
disp(d)# 0 1 2 3  

#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop')
while   True: # cnt is 0 1 2 3 
        try:
                print(next(z1))## (10,0) (20,1) (15,2) (18,3)
        except  StopIteration:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2: # x is 4 5 6 7 
        print(x)# (10,4) (20,5) (15,6) (18,7)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))# (10,8) cnt is 8
print('*z3 :  ' ,  *z3)# (20,9) (15,10) (18,11) cnt is 9 10 11 
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4)) # (16,12)


# Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')# While loop
while   True: # cnt is 0 1 2 3 4
        try:
                print(next(z1)) # (0,10) (1,20) (2,15) (3,18) si
        except:
                break
z2 = zip(list , cnt)
print('for  loop')# for loop
for  x   in    z2: # 5 6 7 8
        print(x)# (10,5) (20,6) (15,7) (18,8)
z3 = zip(cnt , list)
print(next(z3))# cnt is 9 (9,10)
print(*z3)# cnt is 10 11 12 13  (10,20)(11,15)(12,18)
z4 = zip(list , cnt)
print(next(z4))# (10,14)