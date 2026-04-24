def rotate(a):  # 'a' is a list
    # shift right only once
    last = a[-1]
    for i in range(len(a) - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = last
    return a


# Read list 'a'
a = [10, 20, 15, 18, 12]

# Read 'k'
k = 3

# Call rotate() k times
for i in range(k):
    a = rotate(a)
    print(f"After {i+1} call --> {a}")

# Final result
print("Final result:", a)	





# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f))	#25 <next> 10.8 <next> (3+4j) <next> Hyd <next> False
		time . sleep(1)
	except:
		break




#  Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list)
while  True:
	try:
		print(next(f))  #error immediately raises stopiteration error
		time . sleep(1)
	except:
		break




# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda  x : x , list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#outputs:
25
10.8
(3+4j)
Hyd
(25,)





# Find outputs
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [10 , 0 ,  -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False]
f1 = filter(lambda  x : None  , list)
print('Filter  f1')	#filter f1
disp(f1)		#filter f2
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)	#10 -25 (25,) Hyd 10.8 [10,20] True




# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#outputs:
Rama Rao
Rajesh
Kiran
Manohar
Vamsi




# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda  x : x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
#outputs:
('B', 20)
('C', 15)
('E', 18)




# Find  outputs (Home  work)
import   time
list = [{'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75} ,
          {'Roll Num' :  20 , 'Stud Name' : 'Sita' , 'Marks' : 52} ,
          {'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65} ,
          {'Roll Num'  :  18 , 'Stud Name' : 'Amar' ,  'Marks' : 48} ,
          {'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}]  
f = filter(lambda  x :  x['Marks'] >= 60 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#outputs:
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}





# Find  outputs (Home  work)
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [{'country' : 'India' , 'sale' : 150.5} ,
          {'country' : 'china' , 'sale' : 200.2} ,
          {'country' : 'USA' , 'sale' : 300.3} ,
          {'country' : 'UK' , 'sale' : 210.4} ]
f1 = filter(lambda  x  :   x['country'] . startswith('U') , list)
print('Filter  f1')
disp(f1)
f2 = filter(lambda  x  :  x['sale']  >=  200  , list)
print('Filter  f2')
disp(f2)

#outputs:
Filter f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}




import time

a = [10, 15, 20, 17, 18, 19, 26]

# Filter even numbers
f1 = filter(lambda x: x % 2 == 0, a)

print('Iterate thru filter object with next function')

# Using next()
f2 = filter(lambda x: x % 2 == 0, a)
while True:
    try:
        print(next(f2))
        time.sleep(1)
    except StopIteration:
        break


print('Iterate thru filter object with for loop')

# Using for loop
f3 = filter(lambda x: x % 2 == 0, a)
for x in f3:
    print(x)
    time.sleep(1)


print('Unpack filter object :', *filter(lambda x: x % 2 == 0, a))


print('filter object converted to list :', list(filter(lambda x: x % 2 == 0, a)))







# List from 1 to 20
a = list(range(1, 21))

# Filter odd numbers
f = filter(lambda x: x % 2 != 0, a)

# Print using iterator
for num in f:
    print(num)





# Input string
s = input("Enter a string: ")

# Define vowels
vowels = 'aeiouAEIOU'

# Filter vowels from string
f = filter(lambda x: x in vowels, s)

# Convert to set for distinct vowels
result = set(f)

print("Distinct vowels:", result)






# Nested  filter  i.e.  filter  on  filter
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f))
		time .  sleep(1)
	except:
		break

#outputs:
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)