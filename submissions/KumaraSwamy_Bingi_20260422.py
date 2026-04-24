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
	
'''
modified program
'''
import time
def regular(x):
	return x*x
list = [10 , 20 , 15 , 18 , 5]
m=map(regular,list)
print(type(m))
print(m)
for i in m:
	print(i)
	time.sleep(1)
	

# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while  True:
	try:
		print(next(m))#10 <next iterator with 1 sec pause> 20 <next iterator with 1 sec pause> 15 <next iterator with 1 sec pause> 5 <next iterator with 1 sec pause> 18
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
m1 = map(lambda  x  :  x['country'] , list)#
print('Map   m1')
disp(m1)
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')
disp(m2)


'''
output
Map   m1
India
China
USA
UK
Map   m2
150.5
200.2
300.3
210.4
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
def to_fahrenheit(celsius):
    return (1.8 * celsius) + 32
celsius_temps = eval(input("Enter list of celsius-temp")
fahrenheit_temps = map(to_fahrenheit, celsius_temps)
print("Converting Celsius to Fahrenheit")
for f in fahrenheit_temps:
    print(f"{f}°F")
    time.sleep(1)

	
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
import time
def power(x):
    return 2**x
range(0,10)
power_2=map(power,range(0,10))
print("Powers of 2")
for i in power_2:
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
def aoc(r):
	return 3.14159*r*r
lt=eval(input("Enter list of radii : "))
m=map(aoc,lt)
print("Area of each radius in the list")
for i in m:
	print(F'{i:.2f}')
	time.sleep(1)
	

'''
Write  a  program  to  add  two  tuples  of  different  sizes  and  store  the  results  in  3rd  tuple
Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
def add(x1,x2):
	return x1+x2
t1=eval(input("Enter First tuple : "))
t2=eval(input("Enter Second tuple :"))
m1=map(add,t1,t2)
result=tuple(m1)
print("Addition tuple",result)


'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list
Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
def mul(x1,x2):
	return x1*x2
lt1=eval(input("Enter First list : "))
lt2=eval(input("Enter Second list :"))
m1=map(mul,lt1,lt2)
result=list(m1)
print("Multipied list",result)


# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))#40 <nextiteration with 1 sec pause> 30 <nextiteration with 1 sec pause> 36 <nextiteration with 1 sec pause> 50 <nextiteration with 1 sec pause> 34
		time . sleep(1)
	except:
		break
		
	
# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))#100 <nextiteration with 1 sec pause> 400 <nextiteration with 1 sec pause> 144 <nextiteration with 1 sec pause> 324 <nextiteration with 1 sec pause> 196
	except:
		break
		
		
'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function
Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40
Hint:  Use  reduce()  function
'''
from functools import reduce
def get_larger(a, b):
    if a > b:
        return a
    else:
        return b
lt = eval(input("Enter list of numbers or strings : "))
largest = reduce(get_larger,lt)
print("Largest element : ", largest)


