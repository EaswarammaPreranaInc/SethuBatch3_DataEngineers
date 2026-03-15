a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)        # (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))  # <class 'tuple'>
# a[3] = 'Sec'    # Error bcoz 'tuple' object does not support item assignment
a[3 : 6] = 60 , 70 , 80   # Not executed


a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))      # (1, 2, 3)  address of object 'a'
a += b
print(a , id(a))      # (1, 2, 3, 4, 5, 6) address of new object 'a'


# Find outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))   # (1, 2, 3)  address of 'a' 
a = a + b
print(a , id(a))   # (1, 2, 3, 4, 5, 6)  address of a with other reference


# What are the outputs if input is (10 , 20 , 30 , 40) ?
a = input('Enter Tuple : ')   # (10 , 20 , 30 , 40)
print(a)                      # (10 , 20 , 30 , 40)
print(type(a))                # <class 'str'>
b = eval(a)
print(b)                      # (10, 20, 30, 40)
print(type(b))                # <class 'tuple'>
print(len(b))                 # 4


# Find outputs (Home work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)                 # (10, [70, 30, 40], 50, 60)
# a[1] = [80 , 90 , 100]   # Error due to 'tuple' object does not support item
print(a)                 # Not execute but it will give (10,[70, 30, 40], 50, 60)


# Find outputs (Home work)
a = [10 , (20 , 30 , 40) , 50 , 60]
# a[1][0] = 70            # Error due to  'tuple' object does not support item
print(a)                # Not executed but it gives [10, (20, 30, 40), 50, 60]
a[1] = [80 , 90]
print(a)                # Not executed but it gives [10, [80, 90], 50, 60]


# Find outputs (Home work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)        # (25, 10.8, 'Hyd', True)
print(type(x))  # <class 'tuple'>



# Find outputs (Home work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)   # 25
print(b)   # 10.8
print(c)   # Hyd
print(d)   # True
p , q , r = x        # Error due to too many values to unpack (expected 3, got 4)
a , b , c , d , e = x   # Error due to not enough values to unpack (expected 5, got 4)


# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)        # 25
print(b)        # 10.8
print(c)        # ['Hyd', True]
print(type(c))  # <class 'list'>


# Find outputs (Home work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)   # 25
print(b)   # [10.8, 'Hyd']
print(c)   # True


# Find outputs (Home work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl   # Error due to not enough values to unpack (expected at least 5, got 4)
print(a)   # Not executed   25
print(b)   # Not executed   10.8
print(c)   # Not executed   []
print(d)   # Not executed   Hyd
print(e)   # Not executed   True


# Find outputs (Home work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _ = x
print(a)   # 25
print(b)   # 10.8
print(_)   # (3+4j)  
print(d)   # True
print(_)   # (3+4j)


# tuple() function demo program (Home work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)        # (100, 110, 120, 130, 140)
print(type(b))  # <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)        # (10, 20, 15, 18)
e = tuple('Vamsi')
print(e)        # ('V', 'a', 'm', 's', 'i')
print(tuple(25))    # Error due to 'int' object is not iterable
print(tuple())      # ()


#index() and count() methods demo program (Home work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
    i = a.index(15)
    while True:
        print('15 is found at index :', i)
        i = a.index(15, i + 1)
except:
    print(F'15 is found {a.count(15)} times')

# 15 is found at index : 2
# 15 is found at index : 5
# 15 is found at index : 8
# 15 is found 3 times


# How to modify an element of tuple? (Home work)
a = 10 , 20 , 30 , 40 , 50
#     0   1    2    3    4
a[2] = 35        # TypeError due to 'tuple' object does not support item
print(a)         # Not executed (10, 20, 30, 40, 50)
print(id(a))     # Not executed     address of a
a_list = list(a)  # [10, 20, 30, 40, 50]
a_list[2] = 35    # modify the element
a = tuple(a_list) # convert back to tuple
print(a)          # (10, 20, 35, 40, 50)
print(id(a))      # new id because a new tuple is created


# How to delete an element of tuple? (Home work)
a = 10 , 20 , 30 , 40 , 50
#    0    1    2    3    4
a.remove(30)   # Error due to 'tuple' object does not has attribute 'remove'
del a[2]       # Error due to 'tuple' object doesn't support deletion
a.pop(2)       # Error due to 'tuple' object does not have attribute 'pop'
print(a)       # Not executed   (10, 20, 30, 40, 50)
print(id(a))   # Not executed   address of a
a_list = list(a)  # [10, 20, 30, 40, 50]
a_list.remove(30) # remove element
a = tuple(a_list) # convert back to tuple
print(a)          # (10, 20, 40, 50)
print(id(a))      # new id because a new tuple is created



# Nested tuple (Home work)
a = ((10 , 20), (30 , 40 , 50), (60 , 70 , 80 , 90))
print(a)                 # ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a))           # <class 'tuple'>
print(len(a))            # 3
print(a[0])              # (10, 20)
print(a[1])              # (30, 40, 50
print(a[2])              # (60, 70, 80, 90)
print(a[0][1])           # 20
print(a[1][2])           # 50
print(a[2][3])           # 90


# Find outputs (Home work)
a = ((10 , 20 , 30),)
print(a[0])             # (10, 20, 30)
(inner,) = a
print(inner)            # (10, 20, 30)
print(a[0][0])          # 10
print(a[0][1])          # 20
print(a[0][2])          # 30
b = ((),)
print(b[0])             # ()
(inner_b,) = b
print(inner_b)          # ()


# Find outputs (Home work)
a = ((10 , 20 , 30))
print(a)        # (10, 20, 30)
print(*a)       # 10 20 30
b = (())
print(b)        # ()
print(*b)       # (prints nothing)


# What are the outputs if input is {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter Set : ')   # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a)                     # "{10 , 20 , 15 , 18 , 20 , 12 , 18}"
print(type(a))               # <class 'str'>
b = eval(a)
print(b)                     # {10, 12, 15, 18, 20}  duplicates are removed, order may vary
print(type(b))               # <class 'set'>


# Find outputs (Home work)
print({(10 , 20 , 30)})   # {(10, 20, 30)}   tuple is hashable, can be set element
print({[10 , 20 , 30]})   # Error due to unhashable type: 'list'  → list cannot be a set element
print({{10 , 20 , 30}})   # Error due to unhashable type: 'set'   → set cannot be a set element
print({{}})               # Error due to unhashable type: 'dict'  → empty dict cannot be a set element


# How to print set in different ways (Home work)
a = {25 , True , 'Hyd' , 10.8}
print('set with print function')
print(a)   # e.g., {True, 25, 10.8, 'Hyd'}  → order may vary
print('Iterate elements of set with for loop')
for element in a:
    print(element)   # prints each element in set, order may vary


# Find outputs (Home work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)       # {1, 25, 'Hyd'}     True and 1 are considered the same key in set so duplicates are removed
print(len(s))  # 3
print(type(s)) # <class 'set'>


# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8}
print(s)   # {True, 25, 10.8, 'Hyd'}  order may vary
a , b , c , d = s
print(a)   # first element from set iteration (order may vary)
print(b)   # second element
print(c)   # third element
print(d)   # fourth element


# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8}
print(s)      # {True, 25, 10.8, 'Hyd'} order sequence may vary
a , *b = s
print(a)      # first element from set iteration (order may vary)
print(b)      # list of remaining elements, [25, 10.8, 'Hyd']
print(type(b))# <class 'list'>


# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8}
print(s)       # {True, 25, 10.8, 'Hyd'} order may vary
a , *b , c = s
print(a)       # first element from set iteration (order may vary)
print(b)       # middle elements as a list, [25, 10.8] order amy vary
print(c)       # last element from set iteration (order may vary)


# Find outputs (Home work)
s = {20 , 10 , 20 , 10}
print(s)   # {10, 20}  duplicates are removed, order may vary
x , y = s
print(x)   # first element from set iteration (order may vary, could be 10 or 20)
print(y)   # second element from set iteration (order may vary, could be 10 or 20)


# set() function demo program (Home work)
a = range(100 , 151 , 10)
b = set(a)
print(b)        # {100, 110, 120, 130, 140, 150}  order may vary
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)        # {10, 12, 15, 18, 20, 50} duplicates are removed, order may vary
e = set('Rama  rAo')
print(e)        # {' ', 'A', 'm', 'a', 'r', 'R', 'o'} unique characters, order may vary
print(set(25))  # Error due to 'int' object is not iterable
print(set())    # set() empty set



# add() method demo program (Home work)
a = set()
a.add(True)
a.add(25)
a.add(10.8)
a.add(1)          # 1 is considered same as True so duplicate are removed
a.add('Hyd')
a.add(25)         # duplicates are removed
a.add(None)
a.add('Hyd')      # duplicate are removed
a.add(1.0)        # 1.0 is considered same as 1 so duplicates are removed
print(a)          # {True, 25, 10.8, 'Hyd', None}  order may vary
a.add(10 , 20 , 30)       # Error due to add() takes exactly one argument (3 given)
a.add([10,20,30])         # Error due to unhashable type: 'list'


# Find outputs (Home work)

a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)        # {True, 25, 10.8, 'Hyd'}  order may vary
print(id(a))    # memory address of the set
a.add(tpl)      # tuple is immutable so it will add
a.add('Sec')    # string is immutable so it will add
print(a)        # {True, 25, 10.8, 'Hyd', (10,20,30), 'Sec'} order may vary
print(id(a))    # same as before, set modified in-place
print(len(a))   # 6
a.add([100 , 200 , 300])   # Error due to unhashable type: 'list' cannot add mutable element
a.add(set())                # Error due to unhashable type: 'set' cannot add mutable element
a.add({})                   # Error due to unhashable type: 'dict' cannot add mutable element



# Find outputs (Home work)
s = set()
tpl = (10 , 20 , 15 , 18)
s.add(tpl)       # tuple is immutable so it will add
print(s)         # {(10, 20, 15, 18)}
print(len(s))    # 1


# update() method demo program (Home work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s.update(tpl)      # adds each element of tuple to set individually
print(len(s))      # 4 unique elements it will consider: 10, 15, 18, 20
print(s)           # {10, 20, 15, 18} order may vary
s.update(25)       # Error due to'int' object is not iterable so it cannot update with non-sequence


# Find outputs (Home work)
a = [10 , 20 , 30]
b = {30 , 40, 50}
c = (50 , 60 , 70)
s = set()
s.update(a, b, c)   # adds all elements from a, b, c individually
print(s)             # {10, 20, 30, 40, 50, 60, 70}  order may vary
print(len(s))        # 7
s.add(a, b, c)       # Error due to add() takes exactly one argument (3 given)



# Find outputs (Home work)
a = set()
a.update('Rama Rao')  
print(a)        # {' ', 'R', 'a', 'm', 'o'}  unique characters from string, order may vary
print(len(a))   # 5
a.update(3 + 4j, 10.8, True)    # Error due to 'complex' object is not iterable so it cannot update with non-sequence objects



# copy() method demo program (Home work)
a = {10 , 20 , 15 , 18}
print(a)           # {10, 20, 15, 18}  order may vary
b = a.copy()       # creates a new set object with same elements
print(b)           # {10, 20, 15, 18}  order may vary
print(a is b)      # False  different objects
print(a == b)      # True   same elements
c = a              # reference copy
print(a is c)      # True  both refer to same object



# pop() method demo program (Home work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)           # {True, 25, 10.8, 'Hyd'}  order may vary
print(a.pop())     # removes and returns an arbitrary element (order not guaranteed)
print(a.pop())     # removes next arbitrary element
print(a.pop())     # removes next arbitrary element
print(a.pop())     # removes last element
print(a.pop())     # KeyError  set is now empty
print(a)           # Not reached due to previous KeyError
b = {10 , 20 , 30 , 40}
print(b.pop(2))    # TypeError due to set.pop() takes no arguments (sets are unordered)



# remove() method demo program (Home work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)           # {True, 25, 10.8, 'Hyd'}order may vary
a.remove('Hyd')   
print(a)           # {True, 25, 10.8}  'Hyd' removed
a.remove('Sec')    # KeyError 'Sec' is not in the set



# discard() method demo program (Home work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)           # {True, 25, 10.8, 'Hyd'} order may vary
a.discard('Hyd')   
print(a)           # {True, 25, 10.8} 'Hyd' removed
a.discard('Sec')   
print(a)           # {True, 25, 10.8}  no error, set unchanged
a.remove('Sec')    # KeyError 'Sec' not in set



# clear() method demo program (Home work)
a = {10 , 20 , 15 , 18}
print(a)           # {10, 20, 15, 18}  order may vary
a.clear()          
print(a)           # set() empty set
print(len(a))      # 0



# Find outputs (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a.union(b))   # {10, 20, 30, 40, 50, 60} → union works with iterable
print(a | b)        # TypeError: unsupported operand type(s) for |: 'set' and 'list'
print(b.union(a))   # AttributeError: 'list' object has no attribute 'union'
print(a + b)        # TypeError: unsupported operand type(s) for +: 'set' and 'list'



# intersection() method demo program (Home work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.intersection(b)
print(c)          # {40, 30}  common elements, order may vary
print(type(c))    # <class 'set'>
d = a & b
print(d)          # {40, 30}  common elements, order may vary
print(type(d))    # <class 'set'>
print(c is d)     # False  different objects
print(c == d)     # True   same elements



# difference() method demo program (Home work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.difference(b)
print(c)          # {10, 20}  elements in 'a' but not in 'b', order may vary
print(type(c))    # <class 'set'>
d = a - b
print(d)          # {10, 20}  same as difference(), order may vary
print(type(d))    # <class 'set'>
print(c is d)     # False  different objects
print(c == d)     # True   same elements



# symmetric_difference() method demo program (Home work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.symmetric_difference(b)
print(c)          # {10, 20, 50, 60}  elements in a or b but not both, order may vary
print(type(c))    # <class 'set'>
d = a ^ b
print(d)          # {10, 20, 50, 60}  same as symmetric_difference, order may vary
print(type(d))    # <class 'set'>
print(c is d)     # False different objects
print(c == d)     # True  same elements


# Find outputs (Home work)
a = {x * x for x in range(10)}
print(a)        # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}  squares of 0–9, order may vary
print(type(a))  # <class 'set'>



# Remove duplicate characters of a string using set (Home work)
input_str = "Rama Rao"
unique_chars = set(input_str)
output_str = ''.join(unique_chars)
print(output_str)  # e.g., "Ram o" → order may vary because sets are unordered
print(type(output_str))  # <class 'str'>



# Remove duplicate elements from a list using set (Home work)
input_list = [False, 25, 10.8, 1, 25, 0, 'Hyd', 10.8, 1.0, None, 'Sec', 'Hyd', True]
unique_set = set(input_list)
output_list = list(unique_set)
print(output_list)  # e.g., [False, 25, 10.8, 1, 'Hyd', None



# Obtain common elements between two lists using sets
list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 70, 80, 20]
common_elements = set(list1).intersection(set(list2))
output_list = list(common_elements)
print(output_list)  # [20, 40, 30]  order may vary
print(type(output_list))  # <class 'list'>