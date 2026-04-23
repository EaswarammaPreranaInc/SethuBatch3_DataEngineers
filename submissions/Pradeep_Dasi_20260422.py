'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
list = [10 , 20 , 15 , 18 , 5]
m = map(lambda  x :  x  *  x ,  list)
print(type(m))              #<class 'map'>
print(m)                    #<map object at some address>
while   True:
	try:
		print(next(m))      #100    #400    #225    #324    #25
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
		print(next(m))      #10    #20    #15    #5    #18  
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
print('Map   m1')           #Map  m1
disp(m1)                    #India    #China    #USA    #UK
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')           #Map  m2
disp(m2)                    #150.5    #200.2    #300.3    #210.4




'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
def cel_to_far(cel):
    lst = []
    for i in range(len(cel)):
        lst.append(1.8 * cel[i] + 32)
    return lst
cel_list = eval(input('Enter  list  of  celsius  temperatures : '))   #[30 , 40 , 50 , 25]
far_list = cel_to_far(cel_list)
for i in far_list:
    print(i)                    #86.0    #104.0    #122.0    #77.0



# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
def power_of_two(n):
    return 2 ** n
n = int(input('Enter number of terms: '))
res = map(power_of_two, range(n))
print('Powers of 2:')
for i in res:
    print(i)                    #1    #2    #4    #8    #16    #32    #64    #128    #256    #512




'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''
def aoc(lst):
    pi = 3.14159
    ret_lst = []
    for i in range(len(lst)):
        ret_lst.append(pi * lst[i] * lst[i])
    return ret_lst
lst = eval(input('Enter list of radii: '))   #[3.5 , 2.8 , 4.2  , 1.9]
result = aoc(lst)
for x in result:
    print(f'{x:.2f}')




'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
def add_tuples(t1, t2):
    min_len = min(len(t1), len(t2))
    # res = (t1[i] + t2[i] for i in range(min_len))
    for i in range(min_len):
        yield t1[i] + t2[i]

t1 = eval(input('Enter first tuple: '))   #(10 , 20 , 30 , 40)
t2 = eval(input('Enter second tuple: '))  #(1 , 2 , 3 , 4 ,  5  ,  6)
result = add_tuples(t1, t2)
print('Addition tuple: ',tuple(result))   #(11, 22, 33, 44)



'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
def mul_lst(lst1, lst2):
    #m = map(lambda x,y: x*y, lst1,lst2)
    #return list(m)
    min_len = min(len(lst1), len(lst2))
    lst = []
    for i in range(min_len):
        lst.append(lst1[i] * lst2[i])
    return lst
lst1 = eval(input('Enter first list: '))   #[10 , 20 , 15 , 18 , 19 , 17]
lst2 = eval(input('Enter second list: '))  #[1 , 5 , 3 , 2]
result = mul_lst(lst1, lst2)
print('Multiplication: ',mul_lst(lst1, lst2))



# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))      #40    #30    #24    #36    #50    #34
		time . sleep(1)
	except:
		break




# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))      #100    #400    #144    #324    #196
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
def largest(lst):
    return reduce(lambda x,y: x if x>y else y,lst)
lst = eval(input('Enter list of numbers: '))   #[10 , 20 , 15 , 30 , 25 , 40 , 35]
print('Largest element: ',largest(lst))   #40



# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)      #1574



# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')    #While  loop
while   True:
        x = next(c1)
        if   x > 9:
                break
        print(x)        #0     1     2      3      4      5      6      7      8      9
print('For  loop')     #For  loop
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x)        #0     1     2      3      4      5      6      7      8      9      10     11     12     13     14     15     16     17     18     19     20
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3)) #Element :   0
c4 = count()
print(*c4)    #0    1   2   3..... memory error



#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
# End  of  the  function
a = count(start = 10)
disp(a)     #10    11    12    13
b = count(start = 10 , step = 5)
disp(b)     #10    15    20    25
c = count(start = 10 , step = -2.5)
disp(c)     #10    7.5   5.0   2.5
d = count()
disp(d)     #0    1    2    3



#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop')        #While  loop
while   True:
        try:
                print(next(z1))     #(10, 0)    #(20, 1)    #(15, 2)    #(18, 3)
        except  StopIteration:
                break
z2 = zip(list , cnt)
print('for  loop')      #for  loop
for  x   in    z2:
        print(x)        #(10, 4)    #(20, 5)    #(15, 6)    #(18, 7)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))   #Next  element :   (10, 8)
print('*z3 :  ' ,  *z3)                 #*z3 :   (20, 9) (15, 10) (18, 11)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4))  #Next  element  :  (10, 12)




# Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')        #while  loop
while   True:
        try:
                print(next(z1))     #(0, 10)    #(1, 20)    #(2, 15)    #(3, 18)
        except:
                break
z2 = zip(list , cnt)
print('for  loop')      #for  loop
for  x   in    z2:
        print(x)        #(10, 5)    #(20, 6)    #(15, 7)    #(18, 8)
z3 = zip(cnt , list)
print(next(z3))     #(9, 10)
print(*z3)    #(10, 20)    #(11, 15)    #(12, 18)
z4 = zip(list , cnt)
print(next(z4))     #(10, 14)