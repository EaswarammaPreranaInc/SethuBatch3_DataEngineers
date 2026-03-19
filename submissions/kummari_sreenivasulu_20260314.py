1.
# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
 
print(a) # 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(type(a)) # <class 'tuple'>
a[3] = 'Sec' # TypeError: 'tuple' object does not support item assignment
a[3 : 6] = 60 , 70 , 80 # TypeError: 'tuple' object does not support item assignment


# 2.
# #  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # (1 , 2 , 3) <id_of_a>
a += b
print(a , id(a)) #(1 2, 3 , 4 , 5 , 6) <new_id_of_a>



# 3.
# #  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # (1 , 2 , 3) <id_of_a>
a = a + b
print(a , id(a)) # (1,2,3,4,5,6) <new_id_of_a>


4.
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)  # 10 ,20, 30, 40
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # (10 , 20 , 30 , 40)
print(type(b)) # <class 'tuple'>
print(len(b)) # 4


5.
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) # (10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]
print(a) # (10 , [80 , 90 , 100] , 50 , 60)


6.
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a) # [10, (70 ,30, 40), 50 , 60]
a[1] = [80 , 90]
print(a) # [10, [80 , 90], 50 , 60]


7.
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) # (25, 10.8, 'Hyd' , True) 
print(type(x)) # <class 'tuple'>



8.
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) # 25
print(b) # 10.8
print(c) # 'Hyd
print(d) # True
p , q , r =  x # valueError: too many values to unpack
a , b , c , d  , e = x # ValueError: not enough values to unpack


9.
# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) # 25
print(b) # 10.8
print(c) # ['Hyd' , True]
print(type(c)) # <class 'list'>


10.
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # 25
print(b) # [10.8 , 'Hyd']
print(c) # True


11.
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) # 10.8
print(c) # []
print(d) # ['Hyd']
print(e) # True


12.
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)  # 25
print(b) # 10.8
print(_) # (3 + 4j)
print(d) # 'Hyd'
print(_) # (3 + 4j)



13.
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b) # (100 , 150 , 10)
print(type(b)) # <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) # (10 ,20 , 15, 18)
e = tuple('Vamsi')
print(e) # ('V', 'a' , 'm' , 's' , 'i')
print(tuple(25)) # TypeError: 'int' object is not iterable
print(tuple()) # ()
'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  --->  Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''


14.
#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
		
'''
15 is found at index: 2
15 is found at index: 5
15 is found at index: 8

15 is found 3 times
'''


16.
#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a) # TypeError: 'tupe' object does not support item assingment
print(id(a)) # address_of_a
#How  to  modify  30  in  tuple  to  35
print(a) # (10 , 20 , 30 , 40 , 50)
print(id(a)) # address_of_a



17.
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)
del  a[2]
a . pop(2)
print(a) # TypeError: 'tuple' object has no attribute 'remove'
print(id(a)) # address_of_a
How  to  remove  30  from  tuple  'a'
print(a) # (10 , 20, 30, 40, 50)
print(id(a)) # address_of_a


18.
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ((10, 20) , (30, 40, 50) , (60, 70, 80, 90))
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(How  to  print  1st  inner  tuple)
# print(a[0]) # (10,20)
print(How  to  print  2nd  inner  tuple)
# print(a[1]) # (30,40,50)
print(How  to  print  3rd  inner  tuple)
# print(a[2]) # (60, 70, 80, 90)
print(How  to  print  20)
# print(a[0][1]) # 20
print(How  to  print  50)
# print(a[1][2]) # 50
print(How  to  print  90)
# print(a[2][3]) # 90



19.
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple) 
# print(a[0]) # (10, 20, 30)
print(How  to   print  inner  tuple  in  another  way)
# print(*a) # (10, 20 ,30)
print(How   to  print   10)
# print(a[0][0]) # 10
print(How   to  print   20)
# print(a[0][1]) # 20
print(How   to  print   30)

# print(a[0][2]) # 30
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b') 
# print(b[0]) # ()
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)
# print(*b) # ()


20.
#  Find  outputs (Home  work)
# a = ((10 , 20 , 30))
# print(a) # (10, 20, 30)
# print(*a) # 10, 20, 30
# b = (()) 
# print(b) # ()
# print(*b) # Nothing will be printed because the inner tuple is empty


21.
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18} 
print(type(a)) # < class 'str'>
b = eval(a)
print(b) # {10, 12, 15, 18, 20}
print(type(b)) # <class 'set'>



22.
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10 , 20 , 30)}
print({[10 , 20 , 30]}) # TypeError: unhashable type: 'list'
print({{10 , 20 , 30}}) # TypeError: unhashable type: 'set'
print({{}}) # TypeError: unhashable type: 'dict'


23.
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop
    
for  i in a:
    print(a)


24.
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {True , 25 , 'Hyd'}
print(len(s)) # 3
print(type(s)) # <class 'set



25.
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {True , 25 , 'Hyd' , 10.8}
a , b , c , d = s
print(a) # True
print(b) # 25
print(c) # 'Hyd'
print(d) # 10.8


26.
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {True , 25 , 'Hyd' , 10.8} 
a , *b = s
print(a) # True
print(b) # [25 , 'Hyd' , 10.8]
print(type(b)) # <class 'list'>


27.
#Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s
print(a) # True
print(b) # [25 , 'Hyd']
print(c) # 10.8


28.
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {10 , 20}
x , y = s
print(x) # 10
print(y) # 20


29.
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) # {100, 110, 120 , 130 , 140 , 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10 , 12 , 15 , 18 , 20 , 50}
e = set('Rama  rAo')
print(e) # {' ', 'R', 'a', 'm', 'r', 'A', 'o'}
print(set(25)) # TypeError: 'int' object is not iterable
print(set()) # set() function with no arguments returns an empty set
'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  --->  Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''


30.
# add()  method  demo  program  (Home  work)
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
print(a) # {True , 25 , 10.8, 'Hyd' , None}
a . add(10 , 20 , 30) # TypeError: add() takes exactly one argument (3 given)
a . add([10,20,30]) # TypeError: unhashable type: 'list'

'''
add()   method
-----------------
1) What  does  add(x)  do ?  --->  Inserts   'x'  any  where  in  the  set  becoz  set  is  unordered

2) How  many  arguments  can  add()  method  take ?  --->  Single

3) Is  set . add(mutable-object)  valid ? --->  No  becoz  set  can  not  hold  mutable  element

4) In  other  words,  argument  of  add()  method  should  be  immutable  object  only

5) What  does  set .  add(sequence)  do  ?  --->
																Inserts  sequence  any  where  in  the  set  but  not  elements  of  sequence
																(Like  append()  method  of  list  class)
'''


31.
# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {True, 25 , 10.8 , 'Hyd}
print(id(a)) # address_of_a
a . add(tpl)
a . add('Sec')
print(a) # {True , 25 , 10.8 , 'Hyd' , (10 , 20 , 30) , 'Sec'}
print(id(a)) # address_of_a (same as before becoz  set  is  mutable)
print(len(a)) # 6
a . add([100 , 200 , 300]) # TypeError: unhashable type: 'list'
a . add(set()) # TypeError: unhashable type: 'set'
a . add({ }) # TypeError: unhashable type: 'dict'


32.
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10, 20, 15, 18)}
print(len(s)) # 1


33.
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) # Inserts  elements  of  'tpl'  anywhere  in  the  set  but  not  'tpl'  itself
print(len(s)) # 4
print(s) # {10 , 15 , 18 , 20}
s . update(25) # TypeError: 'int' object is not iterable
'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  --->  Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                         (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  ---> One  (or)  more
'''


34.
# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) # {50, 20, 70, 40, 10, 60, 30}
print(len(s)) # 7
s . add(a , b , c) # TypeError: add() takes exactly one  argument 


35.
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) # {' ', 'R', 'a', 'm', 'r', 'A', 'o'}
print(len(a)) # 7
a . update(3 + 4j , 10.8 , True) # TypeError: 'complex' object is not iterable


36.
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
b = a . copy()
print(b) # {10 , 20 , 15 , 18}
print(a  is  b) # False  becoz  'a'  and  'b'  are  different  objects
print(a  ==  b) # True  becoz  'a'  and  'b'  have  same  elements
c = a
print(a  is  c) # True becoz 'a' and  'c' are same objects
'''
copy()  method
------------------
1) What  does  copy()  method  do ?  ---> Returns  a  new  set  with  same  elements

2) a = b
    What  does  the  statement  do ?  --->  Reference  copy
																   i.e.  id  is  copied

3) What  is  shallow  clone ?  ---> Reference  copy
     What  is  deep  clone ?  --->  Object  copy
'''


37.
# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {True , 25 , 10.8 , 'Hyd'}
print(a . pop()) # True (or) 25 (or) 10.8 (or) 'Hyd'  
print(a . pop()) # 25 (or) 10.8 (or) 'Hyd' (or) True
print(a . pop())  # 10.8 (or) 'Hyd' (or) True (or) 25
print(a . pop())  # 'Hyd' (or) True (or) 25 (or) 10.8
print(a . pop()) # KeyError: 'pop from an empty set'
print(a)  # set() empty set
b = {10 , 20 , 30 , 40}
print(b . pop(2))   # TypeError: pop() takes no arguments
'''
pop()  method
----------------
1) What  does  pop(No-args)  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  ---> Zero
'''

38.
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {True , 25 , 10.8 , 'Hyd'}
a . remove('Hyd') # Removes 'Hyd' from the set
print(a)  # {True , 25 , 10.8}
a . remove('Sec')   # Error becoz 'Sec' is not present in the list
'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''


39.
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {True , 10.8 , 25 , 'Hyd'}
a . discard('Hyd') # Removes 'Hyd' from the set
print(a) # {True , 10.8 , 25}
a . discard('Sec') # NOthing will happen becoz 'Sec' is not present in the set
print(a) # {True , 10.8 , 25}
a . remove('Sec') # Error becoz 'Sec' is not present in the set
'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''


40.
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear() # Removes all the elements of set 'a' and set becomes empty
print(a) # set() empty set
print(len(a)) # 0
'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''


41.
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {10 , 20 , 30 , 40 , 50 , 60}
print(a | b) # unsupported operand type(s) for |: 'set' and 'list'
print(b . union(a)) # list object has no attribute 'union'
print(a + b) # TypeError: unsupported operand type(s) for +: 'set' and 'list'


42.
#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) # {30 , 40}
print(type(c)) # <class 'set'>
d = a & b
print(d) # {40 , 30}
print(type(d)) # <class 'set'>
print(c  is  d) # False becoz 'c' and 'd' are different objects
print(c  ==  d) # True becoz 'c' and 'd' have same elements
'''
intersection()  method
---------------------------
1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

2) Is  set . intersection(list)  valid  ?  --->
							Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  another  way  to  obtain  common  elements ?  ---> a & b

4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

5) Is  list . intersection(set)  valid ?  --->  No  becoz  there  is  no  intersection()  method  in  list  class
'''


43.
# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) 
print(c) # {10, 20}
print(type(c)) # <class 'set'>
d = a - b
print(d) # {10, 20}
print(type(d)) # <class 'set'>
print(c  is  d) # False becoz 'c' and 'd' are different objects
print(c  ==  d) # True becoz 'c' and 'd' have same elements
'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->  
										Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''


44.
# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) # {10 20 , 50 , 60}
print(type(c)) # <clqss 'set'>
d = a ^ b
print(d) # {10 , 20 , 50 , 60}
print(type(d)) # <class 'ste'>
print(c   is   d) # False becoz 'c' and 'd' are different objects
print(c  ==   d) # True becoz 'c' and 'd' have same elements
'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
						                                                              without  common  elements
																					  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b

4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only
'''


45.
# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # {0 , 1, 2 ,3 ,4, 5, 6, 7, 8, 9}
print(type(a)) # <class 'set'>


46.
'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''

# a = input('Enter  a String: ')
# s = set(a)
# result = ''.join(s)
# for ch in a:
#     if ch not in a:
#         s.add(ch)
#         result+=ch
# print(result)


47.
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a = [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
s = set(a)
result = []
for i in a:
    if i not in result:
        s.add(i)
        result.append(i)
        print(result)


48.
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

a = [10 , 20 , 30 , 40 , 50 ,60]
b = [30 , 40 , 70 , 80 , 20]

s1 = set(a)
s2 = set(b)
c = s1 . intersection(s2)
result = []
for i in a:
    if i in c:
        result.append(i)
        print(result)