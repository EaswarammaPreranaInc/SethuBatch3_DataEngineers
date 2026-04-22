import time

# Regular function instead of lambda
def square(x):
    return x * x

lst = [10, 20, 15, 18, 5]

m = map(square, lst)

print(type(m))
print(m)

# For loop instead of while loop
for value in m:
    print(value)
    time.sleep(1)






# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m))		#10 <next> 20 <next> 15 <next> 5 <next> 18 
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
m1 = map(lambda  x  :  x['country'] , list)      # creates empty map object m1  
print('Map   m1')				#Map m1
disp(m1)					#India <next> China  <next> USA <next> UK
m2 = map(lambda  x  :  x['sale']  , list)	#creates empty map object m2
print('Map   m2')				#Map m2
disp(m2)					#150.5  <next> 200.2  <next> 300.3 <next>  210.4






# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return 1.8 * c + 32

# Input list
celsius_list = eval(input("Enter the list:  "))

# Using map
m = map(celsius_to_fahrenheit, celsius_list)

# Output
for i in m:
   print(m)


#powers of two
def power_of_two(x):
    return 2 ** x
n = int(input("Enter the value of n: "))
numbers = range(n)
m = map(power_of_two, numbers)
for value in m:
    print(value) 






#area of circle
def area_of_circle(r):
    return 3.14159 * r * r
radii = eval(input("Enter the radius list: "))#[3.5, 2.8, 4.2, 1.9]
m = map(area_of_circle, radii)
for r, area in zip(radii, m):
    print("Area of radius", r, "=", area) 




# Function to add two numbers
def add(x, y):
    return x + y
t1 = eval(input("Enter the t1: "))  #(10, 20, 30, 40)
t2 = eval(input("Enter the t2: "))  #(1, 2, 3, 4, 5, 6)
m = map(add, t1, t2)
t3 = tuple(m)
print(t3)



# Function to multiply two numbers
def multiply(x, y):
    return x * y
list1 = eval(input("Enter the list1: "))    #[10, 20, 15, 18, 19, 17]
list2 = eval(input("Enter the list2: "))    #[1, 5, 3, 2]
m = map(multiply, list1, list2)
list3 = list(m)
print(list3)





# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))  #creates empty map object m
while   True:
	try:
		print(next(m))	#40 <next> 30 <next> 36 <next> 50 <next> 34 
		time . sleep(1)
	except:
		break




# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))      #creates empty filter object f
while   True:
	try:
		print(next(f))		#10^2, 20^2, 15^2, 12^2, 18^2, 5^2, 14^2, 25^2, 17^2  after filtering 10^2 <next> 20^2 <next> 12^2 <next> 18^2 <next> 14^2 

		time . sleep(1)
	except:
		break



# Function to find larger of two numbers
def largest(x, y):
    if x > y:
        return x
    else:
        return y
lst = eval(input("Enter the list: "))#[10, 20, 15, 30, 25, 40, 35]
result = reduce(largest, lst)
print(result)





# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)	#prints the single output after filter and map



# Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')
while   True:
        x = next(c1)
        if   x > 9:
                break
        print(x)
print('For  loop')
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x)
# End  of  for  loop
c3 = count()
print('Element :  ' , next(c3))		#Element : 0
c4 = count()
print(*c4)	#unpacks all the elements

#outputs:
While  loop
0
1
2
3
4
5
6
7
8
9

For  loop
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20




#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
# End  of  the  function
a = count(start = 10)
disp(a)		#starts from 10 upto infinite
b = count(start = 10 , step = 5)
disp(b)		#starts from 10 in steps of 5 upto infinite
c = count(start = 10 , step = -2.5)
disp(c)		#starts from 10 in steps of -2.5 upto infinite
d = count()
disp(d)		#starts from 0 upto infinite




#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)	#creates empty zip object z1
print('While  loop')	#while loop
while   True:
        try:
                print(next(z1))		#(0,10) <next> (1,20) <next> (2,15) <next> (3,18)
        except  StopIteration:
                break
z2 = zip(list , cnt)
print('for  loop')		#for loop
for  x   in    z2:
        print(x)		#(0,10) <next> (1,20) <next> (2,15) <next> (3,18)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))	#(0,10)
print('*z3 :  ' ,  *z3)		#unpacks the elements (1,20) (2,15) (3,18)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4))		#Next element:(10,4)




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

#outputs:
while  loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)

for  loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)

(8, 10)
(9, 20) (10, 15) (11, 18)
(10, 12)
  





