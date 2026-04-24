Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
list = [10 , 20 , 15 , 18 , 5]
def sqr(x):
    return x*x
m = map(lambda  x :  sqr(x),  list)
print(type(m))
print(m)
for i in m:
    print(i)
#	time . sleep(1)




# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m))#10	20	15	5	18
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
print('Map   m1')
disp(m1)
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')
disp(m2)
##output##
'''
Map m1
'India'
'China'
'USA'
'UK'
Map m2
150.0
200.2
300.3
21.4
'''



'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
import time
a=[30 , 40 , 50 , 25]
m=map(lambda x:1.8*x+32,a)
for i in m:
    print(i)
    time.sleep(1)

    



# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
import time
m=map(lambda x:2**x,range(10))
for i in m:
    print(i)
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
import time
a= [3.5 , 2.8 , 4.2  , 1.9]
m=map(lambda x:3.14159*x*x,a)
for i in m:
    print(i)
    time.sleep(1)

    

Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
a=(10 , 20 , 30 , 40)
b=(1 , 2 , 3 , 4 ,  5  ,  6)
result = tuple(x + y for x, y in zip(a, b))
print(result)



Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
a=[10 , 20 , 15 , 18 , 19 , 17]
b=[1 , 5 , 3 , 2]
res=list(x*y for x,y in zip(a,b))
print(res)



# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))#20,15,18,25,17
while   True:
	try:
		print(next(m))#40 30 36 50 43
		time . sleep(1)
	except:
		break

                
                
# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))#100 400 225 144 324 25 196 125 289
while   True:
	try:
		print(next(f))#100	400	144	324		196	125	
		time . sleep(1)
	except:
		break
#
                


Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''
from functools import reduce
a=[10 , 20 , 15 , 30 , 25 , 40 , 35]
res=reduce(lambda x,y:x if x>y else y,a)
print(res)



# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))#1574<==400 300  324 625<==20 15  18 25
print(ans)#1574



# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')
while   True:
        x = next(c1)#0 1 2 3 4 5 6 7 8 9 10
        if   x > 9:#0 1 2 3 4 5 6 7 8 9
                break
        print(x)#0 1 2 3 4 5 6 7 8 9
print('For  loop')#fror loop
c2 = count()
for  x  in  c2:#0-21
	if  x  >  20:#0-20
		break
	print(x)#0-20
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))#0
c4 = count()
print(*c4)#nothing is printed


#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):#0 1 2 3
                print(next(cnt) , end = '\t')#10 11 12 13
        print()
# End  of  the  function
a = count(start = 10)
disp(a)#10 11 12 13
b = count(start = 10 , step = 5)
disp(b)#10 15 20 15
c = count(start = 10 , step = -2.5)
disp(c)#10 7.5 5 2.5
d = count()
disp(d)#0 1 2 3


#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)#(10,0) (20,1)(15,2)(18,3)
print('While  loop')
while   True:
        try:
                print(next(z1))#(10,0) (20,1)(15,2)(18,3)
        except  StopIteration:
                break
z2 = zip(list , cnt)##(10,4) (20,5)(15,6)(18,7)
print('for  loop')
for  x   in    z2:
        print(x)#(10,4) (20,5)(15,6)(18,7)
z3 = zip(list , cnt)#(10,8) (20,9)(15,10)(18,11)
print('Next  element :  ' , next(z3))#(10,8)
print('*z3 :  ' ,  *z3)#(20, 9) (15, 10) (18, 11)
z4 = zip(list , cnt)#(10, 12) (20, 13) (15, 14) (18,15)
print('Next  element  : ' ,  next(z4))#(10,12)


# Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')
while   True:
        try:
                print(next(z1))#
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
---output--
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