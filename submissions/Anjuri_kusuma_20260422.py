 Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
def m1(x):
	return x*x
list = [10 , 20 , 15 , 18 , 5]
m = map(m1 ,  list)
print(type(m))  #class<map>
print(m)     #type and add
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
	time . sleep(1)
------------------------------------------------------------------------------
 # Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m))      #10  20  15  5  18
		time . sleep(1)
	except  StopIteration:
		break
-------------------------------------------------------------------------------
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
print('Map   m1') #Map m1
disp(m1)         #India  China  USA  UK
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')   #Map m2
disp(m2)     #150.5  200.2  300.3  210.4
---------------------------------------------------------------------------------
 '''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
import  time
def m1(x):
	return 1.8*x+32
list = eval(input("enter the celsius temperature  :  "))     #[10 , 20 , 15 , 18 , 5]
m = map(m1 , list)
print(type(m))  #class<map>
print(m)     #type and add
print("Equivalent farenhit temperatures are : ")
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
	time . sleep(1)
----------------------------------------------------------------------------------------
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
import  time
def m1(x):
	return 2**x
list = range(0,10)     
m = map(m1 , list)     
print("Powers of 2 : ")
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
	time . sleep(1)
-----------------------------------------------------------------------------------------------
'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9

import  time
def m1(x):
	return 3.14159*x*x
list = eval(input("Enter the list of radius : "))    
m = map(m1 , list)     
print("Area of each radius in the list : ")
while   True:
	try:
		print(f"{next(m):.2f}")
		time . sleep(1)
	except  StopIteration:
		break
	time . sleep(1)

------------------------------------------------------------------------------
'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
t1 = eval(input("Enter first tuple : "))  
t2=eval(input("Enter second tuple : "))  
t3=tuple(x+y for x,y in zip(t1,t2))
print(t3)
------------------------------------------------------------------------------
'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
t1 = eval(input("Enter first list : "))  
t2=eval(input("Enter second list : "))  
t3=tuple(x*y for x,y in zip(t1,t2))
print(t3)
--------------------------------------------------------------------------------
# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))   #40  30  36  50  34
		time . sleep(1)
	except:
		break
----------------------------------------------------------------------------------
# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))   100  400  144  324  196
		time . sleep(1)
	except:
		break
----------------------------------------------------------------------------------
'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''
from functools import reduce

lst = [10, 20, 15, 30, 25, 40, 35]

largest = reduce(lambda x, y: x if x > y else y, lst)

print("Largest element:", largest)
----------------------------------------------------------------------------------
# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)   #1894
----------------------------------------------------------------------------------
# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')
while   True:
        x = next(c1)   #0 1 2 3 4 5 6 7 8
        if   x > 9:
                break
        print(x)
print('For  loop')
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x)  #10 11 12 13 14 15 16 17 18 19 
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))  #21
c4 = count()
print(*c4)  #SIE
----------------------------------------------------------------------------------
#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
# End  of  the  function
a = count(start = 10)
disp(a)  #
b = count(start = 10 , step = 5)
disp(b)
c = count(start = 10 , step = -2.5)
disp(c)
d = count()
disp(d)