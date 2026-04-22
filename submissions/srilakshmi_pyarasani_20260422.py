1) outputs
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
print('Map   m1')#Map m1
disp(m1)#India
	 China
	 USA
	 UK
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')#Map m2
disp(m2)#150.5
	 200.2
	 300.3
	 210.4

2) Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
#list = eval(input("Enter list of celsius temperatures : "))

print("Equivalent fahrenheit temperatures")

fahrenheit = list(map(lambda temp: 1.8 * temp + 32, celsius_list))

for x in fahrenheit:
    print(f)

3) Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator 
#print("Powers of 2")

powers = map(lambda x: 2 ** x, range(10))

for x in powers:
    print(x)

4) Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''
## Read input list
radii = eval(input("Enter list of radii : "))

print("Area of each radius in the list")

# Use map to calculate area
areas = map(lambda r: 3.14159 * r * r, radii)

# Print each area
for a in areas:
    print(round(a, 2))

5) Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
## Read tuples from user
t1 = eval(input("Enter first tuple : "))
t2 = eval(input("Enter second tuple : "))

# Add corresponding elements using map
t3 = tuple(map(lambda x, y: x + y, t1, t2))

print("Addition tuple :", t3)

6) Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
#list1 = eval(input("Enter first list : "))
list2 = eval(input("Enter second list : "))

result = list(map(lambda x, y: x * y, list1, list2))

print("Third list :", result)

7) filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))#40 <nextline> 30 <nextline> 36 <nextline> 50 <nextline> 34
		time . sleep(1)
	except:
		break

8) map  inside  filter 
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))#100 <nextline> 400 <nextline> 144 <nextline> 324 <nextline> 196
		time . sleep(1)
	except:
		break

9)Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''
#from functools import reduce

lst = [10, 20, 15, 30, 25, 40, 35]

largest = reduce(lambda x, y: x if x > y else y, lst)

print("Largest element:", largest)

10) outputs
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)#1574

11) from  itertools  import  count
c1 = count()
print('While  loop')#while loop
while   True:
        x = next(c1)
        if   x > 9:
                break
        print(x)#0 1 2 3 4 5 6 7 8 9 
print('For  loop')#for loop
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x)#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))#Element :   0
c4 = count()
print(*c4)


12) from  itertools  import  count
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
disp(c)#10 7.5 5.0 2.5
d = count()
disp(d)#0 1 2 3

13) from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop')#while loop
while   True:
        try:
                print(next(z1))#(10, 0)
				(20, 1)
				(15, 2)
				(18, 3)
        except  StopIteration:
                break
z2 = zip(list , cnt)
print('for  loop')#for loop
for  x   in    z2:
        print(x)#(10, 4)
		 (20, 5)
		 (15, 6)
		 (18, 7)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))#Next  element :   (10, 8)
print('*z3 :  ' ,  *z3)#*z3 :   (20, 9) (15, 10) (18, 11)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4))#Next  element  :  (10, 12)

14) Most  tricky  program
outputs
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')#while loop
while   True:
        try:
                print(next(z1))#(0, 10)
				(1, 20)
				(2, 15)
				(3, 18)
        except:
                break
z2 = zip(list , cnt)
print('for  loop')#for loop
for  x   in    z2:
        print(x)#(10, 5)
		 (20, 6)
		 (15, 7)
		 (18, 8)
z3 = zip(cnt , list)
print(next(z3))
print(*z3)#(10, 20) (11, 15) (12, 18)
z4 = zip(list , cnt)
print(next(z4))#(10, 14)