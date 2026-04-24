
'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import time 
def f1(x):
       return x*x
list = [10 , 20 , 15 , 18 , 5]
m=map(f1,list)
print(type(m))
print(m)
for x in m:
    print(x)
    time.sleep(1)
	

import  time
list = [10 , 20 , 15 , 18 , 5]
m = map(lambda  x :  x  *  x ,  list)#empty map object is created 
print(type(m))#<class 'map'>
print(m)#type and address of object m
while   True:
	try:
		print(next(m))#10^2<nxt>20^2<nxt>15^2<nxt>18^2<nxt>5^2
		time . sleep(1)#1 sec delay for each yield
	except  StopIteration:
		break
	time . sleep(1)#1 sec delay for program termination
# 


# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m))#10<nxt>20<nxt>15<nxt>5<nxt>18
		time . sleep(1)#1 sec delay for each yield
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
m1 = map(lambda  x  :  x['country'] , list)#m1 map obj is created 
print('Map   m1')#Map   m1
disp(m1)#India<nxt>China<nxt>USA<nxt>UK
m2 = map(lambda  x  :  x['sale']  , list)#m2 map obj is created
print('Map   m2')#Map   m2
disp(m2)#150.5<nxt>200.2<nxt>300.3<nxt>210.4



'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature
1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32
2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
temp=[30 , 40 , 50 , 25]
m=map(lambda x:1.8*x+32 ,temp)
while True:
    try:
        print(next(m))
    except:
        break



'''Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
'''

r=range(10)
m=map(lambda x : 2 ** x , r)
while True:
    try:
            print(next(m))
    except:
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
from math import pi
import time 
lst=[3.5 , 2.8 , 4.2  , 1.9]
m=map(lambda x :f' {pi*x**2:.2f}' , lst)
while True :
    try:
        print(next(m))
        time.sleep (1)
    except:
        break



'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple
Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
import time 
t1=eval(input("enter first tuple :"))#(10 , 20 , 30 , 40)
t2=eval(input("enter first tuple :"))#(1 , 2 , 3 , 4 ,  5  ,  6)
m=map(lambda x,y :x+y ,t1,t2)
print('3rd  tuple sum of 2 tuples t1 and t2:')
print('addition tuple:',tuple(m))



        
'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be [10 , 20 , 15 , 18 , 19 , 17]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''

t1=eval(input("enter first list :"))#[10 , 20 , 15 , 18 , 19 , 17]
t2=eval(input("enter second list :"))#[1 , 5 , 3 , 2]
m=map(lambda x,y :x*y ,t1,t2)
print('3rd  list product of 2 list t1 and t2:')
print('product of t1 and t2 :',list(m))#[10, 100, 45, 36]



# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))#15 18 25 17
while   True:
	try:
		print(next(m))#30 <nxt> 32 <nxt> 625 <nxt> 34
		time . sleep(1)#1 sec delay for each yield
	except:
		break

# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))#10^2<nxt>20^2<nxt>12^2<nxt>18^2 <nxt>14^2 
		time . sleep(1)#1 sec delay for each yield
	
	except:
		break
       

#map not filters anything  : 10^2 , 20^2,   15^2 , 12^2 ,18^2  , 5^2  , 14^2  , 25^2  , 17^2 
#lambda filters map values :lambda  filters the even numbers of  map values whilch are yielded 



'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function
Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40
from  functools  import  reduce
list=eval(input("enter list:"))
m=max(list)
r=reduce(lambda x : x , filter (lambda x : x == max(list),list) )
print(r)

Hint:  Use  reduce()  function
'''
Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)#1574


#  filter(lambda  x  :  x  >= 15 , a)---> 20 , 15 , 18 , 25
# 	20 , 15 18 , 25---->iterator 

# map(lambda  y :  y ** 2 ,iterator )--> 400,225,324,625--->iterator 
# 400,225,324,625--->iterator 



# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')#While  loop
while   True:
        x = next(c1)#x values are 0,1,2,3,4,5,6,7,8,9
        if   x > 9:
                break
        print(x)#0,1,2,3,4,5,6,7,8
print('For  loop')#For  loop
c2 = count()
for  x  in  c2:
	if  x  >  20:#x values are 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
		break
	print(x)#0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))#0
c4 = count()
print(*c4)#memory error and waiting time 



#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
# End  of  the  function
a = count(start = 10)
disp(a)#10<\t>11<\t>12<\t>13<\t>nothing is printed by print()
b = count(start = 10 , step = 5)
disp(b)#10<\t>15<\t>20<\t>25<\t>nothing is printed by print()
c = count(start = 10 , step = -2.5)
disp(c)#10<\t>7.5<\t>5.0<\t>2.5<\t>nothing is printed by print()
d = count()
disp(d)#0<\t>1<\t>2<\t>3<\t>nothing is printed by print()



#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop')#While  loop
while   True:
        try:
                print(next(z1))#(10,0)<nxt>(20 ,1) <nxt>(15 , 2) <nxt> (18,3)
        except  StopIteration:
                break
z2 = zip(list , cnt)
print('for  loop')#for  loop
for  x   in    z2:
        print(x)##(10,4)<nxt>(20 ,5) <nxt>(15 , 6) <nxt> (18,7)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))#Next  element :(10,8)
print('*z3 :  ' ,  *z3)#*z3 :(20 ,9) <space> (15 , 10) <space> (18,11)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4))#(10,12)
# 


# Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)#count =0,1,2,3,4
print('while  loop')#while  loop
while   True:
        try:
                print(next(z1))#(0,10)<nxt>(1,20) <nxt>(2,15) <nxt> (3,18)
        except:
                break
z2 = zip(list , cnt)#cnt strts with 5
print('for  loop')#for  loop
for  x   in    z2:
        print(x)#(10,5)<nxt>(20 ,6) <nxt>(15 , 7) <nxt> (18,8)
z3 = zip(cnt , list)#c yields 9,10 ,11,12,13
print(next(z3))#(9,10)
print(*z3)#(10,20) <nxt>(11,15) <nxt> (12,18)
z4 = zip(list , cnt)
print(next(z4))#(10,14)