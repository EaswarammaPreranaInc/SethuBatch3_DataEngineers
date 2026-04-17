
# Find outputs (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a)) #<class 'tuple'>
a[3] = 'Sec' #Error as 'tuple' object does not support item assignment
a[3 : 6] = 60 , 70 , 80  #TypeError: 'tuple' object does not support item assignment




#  Find outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1, 2, 3) <some id>
a += b
print(a , id(a)) #(1, 2, 3, 4, 5, 6) <different id> becoz += creates a new tuple object




#  Find outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1, 2, 3) <some id>
a = a + b
print(a , id(a)) #(1, 2, 3, 4, 5, 6) <different id> becoz + always creates a new tuple object



#  What are the outputs if input is (10 , 20 , 30 , 40)? (Homework)
a = input('Enter  Tuple:  ') #input: (10 , 20 , 30 , 40)
print(a) #(10 , 20 , 30 , 40)
print(type(a)) #<class 'str'>
b = eval(a)
print(b) #(10, 20, 30, 40)
print(type(b)) #<class 'tuple'>
print(len(b)) #4




# Find outputs (Homework)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) #(10, [70, 30, 40], 50, 60) becoz inner list is mutable so its element can be changed
a[1] = [80 , 90 , 100]  #Error as 'tuple' object does not support item assignment becoz tuple itself is immutable so its element (the list ref) cannot be replaced




# Find outputs (Homework)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70  #Error as 'tuple' object does not support item assignment becoz inner tuple is immutable so its element cannot be changed
a[1] = [80 , 90]
print(a) #[10, [80, 90], 50, 60] becoz outer list is mutable so its element can be replaced




# Find outputs (Homework)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25, 10.8, 'Hyd', True)
print(type(x)) #<class 'tuple'>




# Find outputs (Home work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25
print(b) #10.8
print(c) #Hyd
print(d) #True
p , q , r = x  #Error as too many values to unpack (expected 3)
a , b , c , d , e = x  #Error as not enough values to unpack (expected 5, got 4)




# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) #25
print(b) #10.8
print(c) #['Hyd', True]
print(type(c)) #<class 'list'>




# Find outputs (Homework)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) #25
print(b) #[10.8, 'Hyd']
print(c) #True




# Find outputs (Homework)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl  #Error as not enough values to unpack becoz 4 elements but 4 named vars + 1 starred = at least 4 needed with *c=[] *c would be [] and d='Hyd' e=True but a=25 b=10.8 works  --> actually it runs:
a , b , *c , d , e = (25 , 10.8 , 'Hyd' , True , 3 + 4j) #needs 5 elements; with 4 it raises ValueError
print(a) #25
print(b) #10.8
print(c) #[]
print(d) #'Hyd'
print(e) #True




# Find outputs (Homework)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) #25
print(b) #10.8
print(_) #(3+4j) becoz _ is reassigned to last matched value i.e. 3+4j
print(d) #True
print(_) #(3+4j)




# tuple() function demo program (Homework)
a = range(100 , 150 , 10)
b = tuple(a)
print(b) #(100, 110, 120, 130, 140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) #(10, 20, 15, 18)
e = tuple('Vamsi')
print(e) #('V', 'a', 'm', 's', 'i')
print(tuple(25))  #Error as 'int' object is not iterable
print(tuple()) #()




#index() and count() methods demo program (Homework)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1    2    3    4    5    6    7    8    9   10
try:
    i = a . index(15)
    while  True:
        print('15 is found at index : ' , i) #15 is found at index :  2
        i = a . index(15 , i + 1)            #15 is found at index :  5
except:                                      #15 is found at index :  8
        print(F'15  is  found  {a . count(15)}  times') #15 is found 3 times




# How to modify an element of tuple? (Homework)
a  =  10 , 20 , 30 , 40 , 50
#      0    1    2    3    4
a[2] = 35 #Error as 'tuple' object does not support item assignment so we convert to list , modify , then convert back to tuple
a = list(a)
a[2] = 35
a = tuple(a)
print(a) #(10, 20, 35, 40, 50)
print(id(a)) #<new id>  becoz a now points to a completely new tuple object




# How to delete an element of tuple? (Homework)
a = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)  #Error as 'tuple' object has no attribute 'remove'
del  a[2]       #Error as 'tuple' object doesn't support item deletion
a . pop(2)      #Error as 'tuple' object has no attribute 'pop' so we convert to list , delete , then convert back to tuple
a = list(a)
a . remove(30)
a = tuple(a)
print(a) #(10, 20, 40, 50)
print(id(a)) #<new id>  becoz a now points to a completely new tuple object




#  Nested tuple (Homework)
a = ( (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90) )
print(a) #((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a)) #<class 'tuple'>
print(len(a)) #3
print(a[0]) #(10, 20)        
print(a[1]) #(30, 40, 50)    
print(a[2]) #(60, 70, 80, 90)
print(a[0][1]) #20
print(a[1][2]) #50
print(a[2][3]) #90




# Find outputs (Homework)
a = ((10 , 20 , 30),)
print(a[0]) #(10, 20, 30)          
print(a[0][ : ]) #(10, 20, 30)     
print(a[0][0]) #10
print(a[0][1]) #20
print(a[0][2]) #30
b = ((),)
print(b[0]) #()   
print(b[0][ : ]) #()




#  Find outputs (Homework)
a = ((10 , 20 , 30))  
print(a) #(10, 20, 30)
print(*a) #10 20 30
b = (())  
print(b) #()
print(*b) #Error as print() argument after * must be an iterable but () is empty, actually prints nothing
print(*b) # (blank line)




# What are the outputs if input is {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter Set: ') #input: {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a) #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) #<class 'str'>
b = eval(a)
print(b) #{10, 12, 15, 18, 20} becoz set removes duplicates and order is not guaranteed
print(type(b)) #<class 'set'>




# Find outputs (Homework)
print({(10 , 20 , 30)}) #{(10, 20, 30)} becoz tuple is hashable so it can be a set element
print({[10 , 20 , 30]})  #Error as unhashable type: 'list' becoz list is not hashable
print({{10 , 20 , 30}})  #Error as unhashable type: 'set' becoz set is not hashable
print({{}})              #Error as unhashable type: 'dict' but {} is dict not set




# How to print set in differnet ways (Homework)
a = {25 , True , 'Hyd' , 10.8}
print('Set with print function')
print(a) #{25, 10.8, 'Hyd'} becoz True == 1 == 25 is False but True == 1 so 1 and True are same; 25 wins
print('Iterate  elements  of set with for loop')
for x in a:
    print(x)




# Find outputs (Homework)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) #{True, 25, 'Hyd'} order not guaranteed
print(len(s)) #3
print(type(s)) #<class 'set'>




# Find outputs (Homework)
s = {'Hyd',  25,  True,  10.8 }
print(s) #order not guaranteed e.g. {True, 25, 10.8, 'Hyd'} 
a , b , c , d = s #unpacking order follows internal iteration order (not guaranteed)
print(a) #<first element in iteration order>
print(b) #<second element in iteration order>
print(c) #<third element in iteration order>
print(d) #<fourth element in iteration order>




# Find outputs (Homework)
s = {'Hyd', 25, True, 10.8 }
print(s) #order not guaranteed
a , *b = s
print(a) #<first element in iteration order>
print(b) #<list of remaining elements>
print(type(b)) #<class 'list'>




# Find outputs (Homework)
s = {'Hyd', 25, True, 10.8 }
print(s) #order not guaranteed
a , *b , c = s
print(a) #<first element in iteration order>
print(b) #<list of middle elements>
print(c) #<last element in iteration order>




# Find outputs (Home  work)
s = {20 , 10 , 20 , 10}
print(s) #{10, 20} becoz set removes duplicates
x , y = s
print(x) #10
print(y) #20




# set() function demo program (Home work)
a = range(100 , 151 , 10)
b = set(a)
print(b) #{100, 110, 120, 130, 140, 150} order not guaranteed
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) #{10, 12, 15, 18, 20, 50} order not guaranteed
e = set('Rama  rAo')
print(e) #{'R', 'a', 'm', ' ', 'r', 'A', 'o'} order not guaranteed ; duplicates removed
print(set(25))  #Error as 'int' object is not iterable
print(set()) #set()




# add() method demo program (Homework)
a = set()
a . add(True)
a . add(25)
a . add(10.8)
a . add(1)     
a . add('Hyd')
a . add(25)    
a . add(None)
a . add('Hyd') 
a . add(1.0)   
print(a) #{True, 25, 10.8, 'Hyd', None}  order not guaranteed
a . add(10 , 20 , 30)  #Error as set.add() takes exactly one argument (3 given)
a . add([10,20,30])    #Error as unhashable type: 'list' becoz list is not hashable




# Find outputs (Homework)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) #order not guaranteed e.g. {True, 25, 10.8, 'Hyd'}
print(id(a)) #<some id>
a . add(tpl)
a . add('Sec')
print(a) #order not guaranteed e.g. {True, 25, 10.8, 'Hyd', (10, 20, 30), 'Sec'}
print(id(a)) #<same id> becoz set is mutable so add() modifies it in place
print(len(a)) #6
a . add([100 , 200 , 300])  #Error: unhashable type: 'list'
a . add(set())   #Error: unhashable type: 'set'
a . add({ })     #Error: unhashable type: 'dict'




# Find outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) #{(10, 20, 15, 18)} becoz tuple is hashable so added as single element
print(len(s)) #1



# update() method demo program (Homework)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) #4  becoz duplicates 10 and 20 are removed
print(s) #{10, 15, 18, 20}  order not guaranteed
s . update(25)  #Error as 'int' object is not iterable becoz update() expects iterable




# Find outputs (Homework)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) #{10, 20, 30, 40, 50, 60, 70} order not guaranteed
print(len(s)) #7
s . add(a , b , c)  Error as set.add() takes exactly one argument (3 given)




# Find outputs (Homework)
a = set()
a . update('Rama Rao')
print(a) #{'R', 'a', 'm', ' ', 'o'}  order not guaranteed ; duplicates removed ; iterates char by char
print(len(a)) #5
a . update(3 + 4j , 10.8 , True)  #Error: 'complex' object is not iterable becoz update() expects iterables and complex/float/bool are not iterable




# copy() method demo program (Homework)
a = {10 , 20 , 15 , 18}
print(a) #order not guaranteed e.g. {10, 15, 18, 20}
b = a . copy()
print(b) #order not guaranteed e.g. {10, 15, 18, 20}
print(a is b) #False becoz copy() creates a new set object
print(a == b) #True becoz both sets have same elements
c = a
print(a is c) #True becoz c is just another reference to the same set object




# pop() method demo program (Homework)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #order not guaranteed e.g. {True, 25, 10.8, 'Hyd'}
print(a . pop()) #removes and returns an arbitrary element
print(a . pop()) #removes and returns an arbitrary element
print(a . pop()) #removes and returns an arbitrary element
print(a . pop()) #removes and returns last remaining element, set is now empty
print(a . pop()) #Error as 'pop from an empty set'
print(a) #set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))  #Error as set.pop() takes no arguments (1 given) becoz pop() takes no index




# remove() method demo program (Homework)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #order not guaranteed e.g. {True, 25, 10.8, 'Hyd'}
a . remove('Hyd')
print(a) #e.g. {True, 25, 10.8}
a . remove('Sec') #Error as'Sec' becoz 'Sec' is not in the set




# discard() method demo program (Homework)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #order not guaranteed e.g. {True, 25, 10.8, 'Hyd'}
a . discard('Hyd')
print(a) #e.g. {True, 25, 10.8}
a . discard('Sec')
print(a) #e.g. {True, 25, 10.8}
a . remove('Sec')  #Error: 'Sec' becoz remove() raises error if element not found




# clear() method demo program (Homework)
a = {10 , 20 , 15 , 18}
print(a) #order not guaranteed e.g. {10, 15, 18, 20}
a . clear()
print(a) #set()
print(len(a)) #0




# Find outputs (Homework)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) #{10, 20, 30, 40, 50, 60}  order not guaranteed ; union() accepts any iterable
print(a | b)  #Error as unsupported operand type(s) for |: 'set' and 'list'  becoz | needs both operands to be sets
print(b . union(a))  #Error as 'list' object has no attribute 'union'  becoz union() is a set method
print(a + b)  #Error as unsupported operand type(s) for +: 'set' and 'list'  becoz + is not supported for sets




# intersection() method demo program (Homework)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) #{40, 30} order not guaranteed
print(type(c)) #<class 'set'>
d = a & b
print(d) #{40, 30} order not guaranteed
print(type(d)) #<class 'set'>
print(c  is  d) #False - becoz intersection() and & each create a new set object
print(c  ==  d) #True - becoz both sets have same elements




# difference() method demo program (Homework)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) #{10, 20} elements in a but not in b
print(type(c)) #<class 'set'>
d = a - b
print(d) #{10, 20}
print(type(d)) #<class 'set'>
print(c  is  d) #False - becoz difference() and - each create a new set object
print(c  ==  d) #True - becoz both sets have same elements




# symmetric_difference() method demo program (Homework)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) #{10, 20, 50, 60} elements in a or b but not in both
print(type(c)) #<class 'set'>
d = a ^ b
print(d) #{10, 20, 50, 60}
print(type(d)) #<class 'set'>
print(c   is   d) #False - becoz symmetric_difference() and ^ each create a new set object
print(c  ==   d) #True - becoz both sets have same elements




# Find outputs (Homework)
a = {x * x  for x in range(10)}
print(a) #{0, 1, 4, 9, 16, 25, 36, 49, 64, 81} order not guaranteed
print(type(a)) #<class 'set'>




'''
(Homework)
Write a program to remove duplicate characters of the string using set

1)  Let input be Rama Rao
    What is the output? Ram<space>o

2)  Both input and output are strings

3)  How to convert string to  set? -> set(string)
    How to convert set to string? -> '' . join(set)

4)  What is the result of str({'H' , 'y' , 'd'})? -> "{'H' , 'y' , 'd'}" but not 'Hyd'
'''
s = 'Rama  Rao'
result = '' . join(set(s))
print(result) #characters without duplicates order not guaranteed e.g.'Ram o'



7
'''
Write a program to remove duplicate elements of list using set

1)  Let input be [False , 25 , 10.8 , 1 , 25 , 0 , 'Hyd' , 10.8 , 1.0 , None , 'Sec' , 'Hyd' , True]
    What is the output? -> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2)  Both input and output are lists
'''
a = [False , 25 , 10.8 , 1 , 25 , 0 , 'Hyd' , 10.8 , 1.0 , None , 'Sec' , 'Hyd' , True]
b = list(set(a))
print(b) #[False, 25, 10.8, 'Hyd', None, 'Sec']  order not guaranteed ; duplicates removed




'''
Write a program to obtain common elements between two lists using sets

1)  Let 1st list be [10 , 20 , 30 , 40 , 50 , 60] and 2nd list be [30 , 40 , 70 , 80 , 20]
    What is the output? [20 , 30 , 40]

2)  Both input and output are lists
'''
a = [10 , 20 , 30 , 40 , 50 , 60]
b = [30 , 40 , 70 , 80 , 20]
c = list(set(a) & set(b))
print(c) #[20, 30, 40]  order not guaranteed