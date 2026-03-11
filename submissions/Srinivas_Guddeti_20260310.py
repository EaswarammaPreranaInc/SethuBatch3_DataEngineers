#  Find  outputs (Home  work)

a = [10, 20, 15, 18]
b = a
print(a  is  b)    # True
print(a  ==  b)    # True
b[2] = 12
print(a)           # [10, 20, 12, 18]

#----------------------------------------------------------------------------------------------------------------------

#  Find  outputs  (Home  work)

a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]

print(a + b)   # [10, 20, 15, 18, 100, 200, 150]
# print(a + 5)   # Error because list cannot be concatenated with int
# print(a + '5')   # Error because list cannot be concatenated with string
# print([10 , 20] + (30 , 40))   # Error because list cannot be concatenated with tuple

#----------------------------------------------------------------------------------------------------------------------

# Tricky  program
#  Find  outputs

a = [1 , 2 , 3]
b = [4 , 5 , 6]

print(a , id(a))
a += b
print(a , id(a))   # same id because += modifies same list

#----------------------------------------------------------------------------------------------------------------------

# Tricky  program
#  Find  outputs

a = [1 , 2 , 3]
b = [4 , 5 , 6]

print(a , id(a))
a  = a + b
print(a , id(a))   # new id because new list created

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs

list = [25 , 10.8 , 'Hyd' ,  True]

a , *b , c = list
print('a : ' , a)     # 25
print('b : ' , b)     # [10.8, 'Hyd']
print('c : ' , c)     # True
print(type(b))        # <class 'list'>

x , *y = list
print('x : ' , x)     # 25
print('y : ' , y)     # [10.8, 'Hyd', True]

*p , q = list
print('p : ' , p)     # [25, 10.8, 'Hyd']
print('q : ' , q)     # True

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

list = [25 , 10.8 , 'Hyd' , True]

# a , b , c , d , e = list   # Error because variables are more than list elements

a , b , *c , d , e = list
print('a : ' , a)   # 25
print('b : ' , b)   # 10.8
print('c : ' , c)   # []
print('d : ' , d)   # Hyd
print('e : ' , e)   # True

# a , b , *c , d , e , f = list   # Error because variables exceed elements

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list

print('a : ' , a)   # 25
print('b : ' , b)   # 10.8
print('_ :  ' , _)  # Hyd
print('d : ' , d)   # True

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]

a , b , a , d , a = list

print('a : ' , a)   # (3+4j)
print('b : ' , b)   # 10.8
print('d : ' , d)   # True

#----------------------------------------------------------------------------------------------------------------------

# Tricky  program
# Find  outputs (Home  work)

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]

a , b ,  _ , d , _  = list

print('a : ' , a)   # 25
print('b : ' , b)   # 10.8
print('_ : ' , _)   # (3+4j)
print('d : ' , d)   # True
print('_: ' , _)    # (3+4j)

#----------------------------------------------------------------------------------------------------------------------

# Identify  error (Home  work)

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]

# a , *b , c , *d , e  = list   # Error because Python allows only one starred variable

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

list = [[25 , 10.8] , 'Hyd' , True]

a , b , c = list

print('a :  ' , a)   # [25, 10.8]
print('b :  ' , b)   # Hyd
print('c :  ' , c)   # True

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

list = [[25 , 10.8] , 'Hyd' , True]

[a , b] , c , d = list

print('a : ' , a)   # 25
print('b : ' , b)   # 10.8
print('c : ' , c)   # Hyd
print('d : ' , d)   # True

# a , b , c , d = list   # Error because structure mismatch during unpacking

#----------------------------------------------------------------------------------------------------------------------

# Comparing  Lists

a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]

print(a == b)   # True
print(a  is   b)   # False
print(a < c)   # True
print(a > d)   # True
print(a >= c)   # False
print(a <= d)   # False
print(a != c)   # True
print(a != b)   # False
print(a == c)   # False

#----------------------------------------------------------------------------------------------------------------------

# Comparing  Lists  (Home  work)

a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]

print(a == b)   # False
print(a  is   b)   # False

#----------------------------------------------------------------------------------------------------------------------

#  len()  function demo   program  (Home  work)

a = [ 25, 10.8, 'Hyd', True]
print(len(a))   # 4

b = []
print(len(b))   # 0

c = [[10 , 20] , 30 , 40]
print(len(c))   # 3

#----------------------------------------------------------------------------------------------------------------------

# sum()  function  demo  program  (Home  work)

a = [25 , 10.8 , True]
print(sum(a))   # 36.8

b= [3 + 4j , 5 + 6j]
print(sum(b))   # (8+10j)

# c = [25 , 10.8 , True , 3 + 4j , False]   # Error because complex cannot mix with float in sum()

d = [10 , 20 , 15 , 18]
print(sum(d))   # 63

# e = [25 , 10.8 , 'Hyd' , True]   # Error because string cannot be added

#----------------------------------------------------------------------------------------------------------------------

#  Find  outputs

a = [[10 , 20 , 15 , 18]]

# print(sum(a))   # Error because inner list cannot be added directly

#----------------------------------------------------------------------------------------------------------------------

# max()  and  min()  functions  demo  program  (Home  work)

a = [10 , 20 , 15 , 18 , 30, 5 , 12]

print(max(a))   # 30
print(min(a))   # 5

b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']

print(max(b))   # Vamsi
print(min(b))   # Amar

# c = [25 , 10.8 ,  3 + 4j , True]   # Error because complex numbers cannot be compared

# d = [25 , '35']   # Error because int and string cannot be compared

# print(max([]))   # Error because max() cannot work on empty list
# print(min([]))   # Error because min() cannot work on empty list

#----------------------------------------------------------------------------------------------------------------------

# list()  function  demo  program

a = (10 , 20 , 15, 18)

b = list(a)

print(b)   # [10, 20, 15, 18]
print(type(b))   # <class 'list'>
print(a  is  b)   # False
print(a == b)   # False

#----------------------------------------------------------------------------------------------------------------------

#  Find  outputs (Home  work)

a = range(4 , 10 , 2)
b = list(a)

print(b)        # [4, 6, 8]
print(type(b))  # <class 'list'>

a = list('Vamsi')
print(a)        # ['V', 'a', 'm', 's', 'i']

a = list()
print(a)        # []

# print(list(25))     # Error because int object is not iterable
# print(list(10.8))   # Error because float object is not iterable
# print(list(True))   # Error because bool object is not iterable
# print(list(None))   # Error because NoneType object is not iterable

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)

a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))   # [(10,20),(30,40,50),(60,70,80,90)]

b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))   # order may change because set is unordered

c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))   # [[10,20], (30,40), {50,60}]

#----------------------------------------------------------------------------------------------------------------------

# sorted()  function   demo  program

a = [10 , 20 , 15 , 5 , 12]

b = sorted(a)
print(b)          # [5,10,12,15,20]
print(type(b))    # <class 'list'>

c = sorted(a , reverse = True)
print(c)          # [20,15,12,10,5]

print(a)          # [10,20,15,5,12]

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

b = sorted(a)
print(b)     # ['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']

c = sorted(a , reverse = True)
print(c)     # reverse order

print(a)     # original list unchanged

#----------------------------------------------------------------------------------------------------------------------

# all()  function demo  program

a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))   # True

b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))   # False

c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))   # False

d = [10 , 0 , 20]
print(all(d))   # False

e = []
print(all(e))   # True

#----------------------------------------------------------------------------------------------------------------------

# any()  function demo program  (Home  work)

a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))   # True

b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))   # False

c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))   # True

d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))   # False

e = []
print(any(e))   # False

#----------------------------------------------------------------------------------------------------------------------

# del  operator  demo  program (Home  work)

a = [10 , 20 , 15 , 18]

print(a)      # [10,20,15,18]

del a[2]
print(a)      # [10,20,18]

# del a[3]   # Error because index out of range

del a

# print(a)   # Error because variable deleted

#----------------------------------------------------------------------------------------------------------------------

#  append()  method  demo  program (Home  work)

list = [10 , 20 , 15 , 18]

print(list)        # [10,20,15,18]

list.append(19)

print(list)        # [10,20,15,18,19]

#----------------------------------------------------------------------------------------------------------------------

#  Find  outputs (Home  work)

list = []

print(list)    # []

list.append(25)
list.append(10.8)
list.append('Hyd')
list.append(True)

print(list)    # [25,10.8,'Hyd',True]

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

list = []

for x in range(0 , 50 , 10):
    list.append(x)

print(list)   # [0,10,20,30,40]

#----------------------------------------------------------------------------------------------------------------------

#  Find  outputs  (Home  work)

a = [10 , 20 , 30]

a.append('Hyd')

print(a)      # [10,20,30,'Hyd']

print(len(a)) # 4

print(a[3])   # Hyd
print(a[3][0]) # H
print(a[3][1]) # y
print(a[3][2]) # d

#----------------------------------------------------------------------------------------------------------------------

#  Find  outputs (Home  work)

a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]

a.insert(2 , b)

print(a)        # [10,20,[50,60,70],30,40]

print(len(a))   # 5

print(a[2])     # [50,60,70]
print(a[2][0])  # 50
print(a[2][1])  # 60
print(a[2][2])  # 70

#----------------------------------------------------------------------------------------------------------------------

# remove()  method  demo  program  (Home  work)

try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)          # [10, 20, 18, 15, 12, 15, 19]
	list . remove(25)
except:
	print('25  is   not  in  the  list')

#----------------------------------------------------------------------------------------------------------------------

'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''

a = [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
x = 15
b = []

for i in a:
	if i != x:
		b.append(i)

print(b)     # [10, 20, 18, 19, 17, 20, 14]

#----------------------------------------------------------------------------------------------------------------------

#  pop()  method  demo  program

a = [10 , 20 , 15 , 18 , 12]

print(a . pop(2))      # 15
print(a)               # [10,20,18,12]

# print(a . pop(len(a)))   # Error because index out of range

print(a . pop(-3))     # 20
print(a)

# print(a . pop(-4))   # Error because index out of range

print(a . pop())       # 12
print(a)

b = []

# b . pop()   # Error because pop from empty list

#----------------------------------------------------------------------------------------------------------------------

# clear() method  demo program  (Home  work)

list = [10 , 20 , 15 , 18]
print(list)          # [10,20,15,18]

list . clear()

print(list)          # []

#----------------------------------------------------------------------------------------------------------------------

# reverse()  method  demo  program (Home  work)

a = [10 , 20 , 15 , 18]
print(a)             # [10,20,15,18]

a . reverse()

print(a)             # [18,15,20,10]

#----------------------------------------------------------------------------------------------------------------------

#  sort()  method  demo  program (Home  work)

list = [10 , 20 , 15 , 18 , 5]
print(list)          # [10,20,15,18,5]

list . sort()
print(list)          # [5,10,15,18,20]

list . sort(reverse = True)
print(list)          # [20,18,15,10,5]

#----------------------------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)

a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']

print(a)

a . sort()
print(a)

a . sort(reverse = True)
print(a)

#----------------------------------------------------------------------------------------------------------------------

# Identify  error (Home  work)

a = [25 , 10.8 ,  'Hyd' ,  True]

# a . sort()   # Error because int, float, string and bool cannot be compared

#----------------------------------------------------------------------------------------------------------------------

#  count()  method  demo    program (Home  work)

a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]

print(a . count(15))   # 3
print(a . count(25))   # 0
print(len(a))          # 9

#----------------------------------------------------------------------------------------------------------------------

'''
Tricky  program

Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)

Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]

What  is  the  output ?  --->  [15 , 14 , 18 , 19]
'''

a = [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]

b = []

for i in a:
	if a.count(i) == 1:
		b.append(i)

print(b)     # [15, 14, 18, 19]

#----------------------------------------------------------------------------------------------------------------------

'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  --->  All  the  elements  are  identical

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->  All  the  elements  are  not  identical
'''

a = [25 , 25 , 25 , 25]

if len(a) == a.count(a[0]):
	print('All  the  elements  are  identical')
else:
	print('All  the  elements  are  not  identical')
