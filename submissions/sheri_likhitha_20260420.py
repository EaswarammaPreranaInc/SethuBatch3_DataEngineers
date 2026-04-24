import time

a = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'Tamilnadu']
b = ['Hyderabad', 'Amaravathi', 'Bangalore', 'Chennai']

z1 = zip(a, b)

print(type(z1))
print(z1)

print('\nIterate thru zip object with next() function')
z1 = zip(a, b)
while True:
    try:
        print(next(z1))
        time.sleep(0.5)
    except StopIteration:
        break

print('\nIterate thru zip object with __next__() method')
z1 = zip(a, b)
while True:
    try:
        print(z1.__next__())
        time.sleep(0.5)
    except StopIteration:
        break

print('\nIterate thru zip object with for loop')
z1 = zip(a, b)
for item in z1:
    print(item)
    time.sleep(0.5)

print('\nElements of each tuple in zip object')
z1 = zip(a, b)
for state, capital in z1:
    print('State:', state, '-> Capital:', capital)
    time.sleep(0.5)

print('\nUnpacks zip object with * operator:')
z1 = zip(a, b)
print(*z1)

print('\nzip object in the form of list:')
z1 = zip(a, b)
print(list(z1))

print('\nzip object in the form of dictionary:')
z1 = zip(a, b)
print(dict(z1))




#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z))
		time . sleep(1)
	except  StopIteration:
		break
outputs:
('Empno', 25)
('Emp Name', 'Rama Rao')
('Salary', 10000.0)




#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)

#outputs:
('Telangana', 'Hyderabad', 50000000)
('Andhra Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)




# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y) 	#5 <next> 7 <nexxt> 9 
	time . sleep(1)





# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
z1 = zip(a , b . keys())
disp(z1)	#(10,1) <next> (20,2) <next> (30,5)
z2 = zip(a , b . values())
disp(z2)	#(10,2) <next> (20,4) <next> (30,6)
z3 = zip(a , b . items())
disp(z3)	#(10,(1,2)) <next> (20,(3,4)) <next> (30,(5,6))
z4 = zip(a , b)
disp(z4)	#(10,1) <next> (20,3) <next> (30,5)
z5 = zip(a)
disp(z5)	#(10,) <next> (20,) <next> (30,)
z6 = zip(b)
disp(z6)	#(1,) <next> (3,) <next> (5,)
z7 = zip()
disp(z7)	#blank line


# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)	#[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]





import time

a = input('Enter any string: ')   # Assume input is HYD

r1 = reversed(a)

print(type(r1))
print(r1)

print('\nIterate thru reversed object with next() function')
r = reversed(a)
while True:
    try:
        print(next(r))
        time.sleep(0.5)
    except StopIteration:
        break

print('\nIterate thru reversed object with __next__() method')
r = reversed(a)
while True:
    try:
        print(r.__next__())
        time.sleep(0.5)
    except StopIteration:
        break

print('\nIterate thru reversed object with for loop')
r = reversed(a)
for ch in r:
    print(ch)
    time.sleep(0.5)

print('\nUnpack reversed object : ', end='')
r = reversed(a)
print(*r)

print('\nList of chars in reverse order : ', list(reversed(a)))

print('\nReverse string : ', ''.join(reversed(a)))





# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))
print(b)
print(id(b))
print(*b)
print(b[0])
print(b[1 : 3])
print(b * 2)
print(len(b))

#outputs:
<class 'reversed'>
<reversed object at 0x...>
(some integer)
D Y H
TypeError: 'reversed' object is not subscriptable




# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))		#<class 'reversed'>
for  x  in   b:
	print(x)	#True <next> Hyd <next> 10.8 <next> 25
	time . sleep(1)



import time

lst = [25, 10.8, 'Hyd', True]

r1 = reversed(lst)

print(type(r1))
print(r1)

# -------------------------------
print('\nnext() function iterates thru list_reverseiterator object')
r = reversed(lst)
while True:
    try:
        print(next(r))
        time.sleep(1)
    except StopIteration:
        break

# -------------------------------
print('\n__next__() method iterates thru list_reverseiterator object')
r = reversed(lst)
while True:
    try:
        print(r.__next__())
        time.sleep(1)
    except StopIteration:
        break

# -------------------------------
print('\nfor loop iterates thru list_reverseiterator object')
r = reversed(lst)
for x in r:
    print(x)
    time.sleep(1)

# -------------------------------
print('\nUnpack list_reverseiterator object :', *reversed(lst))

# -------------------------------
print('\nReverse list :', list(reversed(lst)))





#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)    #error set object is not reverssible because set is unordered



# Can  dictionary  be  reversed  ? (Home  work)
import   time
def   disp(r):
	while  True:
		try:
			print(next(r))
			time . sleep(0.5)
		except  StopIteration:
			break
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
r1 = reversed(a . keys())
disp(r1)	#18 15 20 10
r2 = reversed(a . values())
disp(r2)	#Amar Kiran Sita Rama
r3 = reversed(a . items())
disp(r3)	#(19,'Amar')  (15,'Kiran')  (20,'Sita')  (10,'Rama')
r4 = reversed(a)
disp(r4)	#error dict object is not directly reversible




# Reverse a dictionary (by order of items)

d = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}

rev_dict = dict(reversed(d.items()))

print(rev_dict)




import time

a = {10: 'Rama rao', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

# 1. Keys in reverse order
print('Keys in reverse order')
for k in reversed(a.keys()):
    print(k)
    time.sleep(0.5)

print()

# 2. Values in reverse order
print('Values in reverse order')
for v in reversed(a.values()):
    print(v)
    time.sleep(0.5)

print()

# 3. Tuples in reverse order
print('Tuples in reverse order')
for item in reversed(a.items()):
    print(item)
    time.sleep(0.5)

print()

# 4. Elements of each tuple in reverse order
print('Elements of each tuple in reverse order')
for k, v in reversed(a.items()):
    print(v, k)
    time.sleep(0.5)

print()

# 5. Keys and values in reverse order
print('Keys and values in reverse order')
for k, v in reversed(a.items()):
    print(k, v)
    time.sleep(0.5)




import time

lst = [10, 20, 15, 18]

# -------------------------------
print('Iterate list with for loop')

for x in lst:
    print(x)
    time.sleep(0.5)

print()

# -------------------------------
print('Create list iterator')
list_itr1 = iter(lst)

print(type(list_itr1))
print(list_itr1)

print()

# -------------------------------
print('Iterate thru list_iterator with next() function')

list_itr1 = iter(lst)
while True:
    try:
        print(next(list_itr1))
        time.sleep(0.5)
    except StopIteration:
        break

print()

# -------------------------------
print('Iterate thru list_iterator with __next__() method')

list_itr1 = iter(lst)
while True:
    try:
        print(list_itr1.__next__())
        time.sleep(0.5)
    except StopIteration:
        break

print()

# -------------------------------
print('Iterate thru list_iterator with for loop')

list_itr1 = iter(lst)
for x in list_itr1:
    print(x)
    time.sleep(0.5)

print()

# -------------------------------
print('Unpacks List_iterator :', *iter(lst))





# Find  outputs
a = 25
print(a)	#25
for  x   in   a:
	print(x)	#error int object is not iterable
print(iter(a))
print(next(a))


