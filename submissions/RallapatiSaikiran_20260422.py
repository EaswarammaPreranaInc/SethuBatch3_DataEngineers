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

def f1(x):
	return x*x
m = map(f1,list)
for y in m:
	print(x)


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
#10
20
15
5
18


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
Map   m1
Map   m2
(country, India)
(country , China)
(country, USA)
(country, UK)


(sale,150.5)
(sale,200.2)
(sale,300.3)
(sale,210.4)




'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32

def f1(x):
    return x*1.8 +32
cel =[10,20,15,18]
m = map(f1,cel)
for x in m:
    print(x)


'''
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
'''
n = int(input("Enter range: "))
nums= range(n+1)
m = map(lambda x : 2**x,nums)
for x in m:
	print(x)

'''Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9'''
													  
def f1(r):
    return 3.14159 * r * r
a =list(input("Enterlist of radii: "))
m = map(f1,a)
print("Areas of each radius in the list.")
for x in m:
    print(f'{x:.2f}')



'''Write  a  program  to  add  two  tuples  of  different  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored'''

tup1=(10 , 20 , 30 , 40)
tup2 = (1 , 2 , 3 , 4 ,  5  ,  6)
m = map(lambda x,y:x + y,tup1,tup2)
print("Addition Tuple: "tuple(m))


'''Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17'''

list1 = list(input("Enter list1: "))
list2 = list(input("Enter list2: "))
m = map(lambda x,y:x * y,list1,list2)
print(list(m))

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
40
15
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
100
200
144
18*18
196
'''
'''Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function'''
from functools import reduce
a= [10 , 20 , 15 , 30 , 25 , 40 , 35]
result = reduce(lambda x, y: x if x>y else y ,a)
print(result)


'''
# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)
'''
#1574


# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')
while   True:
        x = next(c1)
        if   x > 9:
                break
        print(x)#0-9
print('For  loop')
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x)#0 to 20
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))#0
c4 = count()
print(*c4)#infinity



#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
# End  of  the  function
a = count(start = 10)
disp(a)#10 11 12 13
b = count(start = 10 , step = 5)
disp(b)#10 15 20 25
c = count(start = 10 , step = -2.5)
disp(c)#10 7.5 5.0 2.5 
d = count()
disp(d)#0 1 2 3




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
#While  loop
(10,0)
(20,1)
(15,2)
(18,3)

z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
(10,4)
(20,5)
(15,6)
(18,7)

z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))#(10,8)
print('*z3 :  ' ,  *z3)#(20,9) (15,10) (18,11)
z4 = zip(list , cnt)
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
                print(next(z1))
        except:
                break
(0,10)
(1,20)
(2,15)
(3,18)

z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
(10,5)
(20,6)
(15,7)
(18,8)


z3 = zip(cnt , list)
print(next(z3))#(9,10)
print(*z3)#(11,20) (12,15) (13,18)
z4 = zip(list , cnt)
print(next(z4))#(14,10)s