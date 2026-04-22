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
print('Map   m1') #map1
disp(m1)#india china usa uk
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')#map m2
disp(m2)# 150.5 200.2 300.3 210.4

Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32

c=[30 , 40 , 50 , 25]
f=list(map(lambdax:1.8*x+32,c))
for i in f:
   print(i)
'''
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)

a = list(map(lambda x: 2**x, range(10)))
print(*a)

Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list


1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9

r = [3.5, 2.8, 4.2, 1.9]
area = list(map(lambda x: 3.14159 * x * x, r))

for i in area:
    print(i)


Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored

t1 = (10, 20, 30, 40)
t2 = (1, 2, 3, 4, 5, 6)

t3 = tuple(map(lambda x, y: x + y, t1, t2))
print(t3)

Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
l1 = [10, 20, 15, 18, 19, 17]
l2 = [1, 5, 3, 2]

l3 = list(map(lambda x, y: x*y, l1, l2))
print(l3)

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
# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))#100 400 144 324 196
		time . sleep(1)
	except:
		break
 '''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function

from functools import reduce

a = [10, 20, 15, 30, 25, 40, 35]

ans = reduce(lambda x, y: x if x > y else y, a)
print(ans)
'''
 Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)
# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop') #while loop
while   True:
        x = next(c1)
        if   x > 9: 0 1 2 3 4 5 6 7 8 9
                break
        print(x)
print('For  loop')#for loop
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x)# 0 to 20
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))
c4 = count()
print(*c4)
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
disp(b)#10 15 20 25
c = count(start = 10 , step = -2.5)
disp(c)#10 7.5 5.0 2.3
d = count()
disp(d)# 0 1 2 3
 #  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)#[]
print('While  loop')#while loop
while   True:
        try:
                print(next(z1))#(0,10)(1,20)(2,15)(3,18)
        except  StopIteration:
                break
z2 = zip(list , cnt)
print('for  loop')#for loop
for  x   in    z2:
        print(x)(10,5)(20,6)(15,7)(18,8)(9,10)(10,20)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))
print('*z3 :  ' ,  *z3)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4))
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