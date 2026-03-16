# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } in any order
a , b , c , d = s
print(a) # 'Hyd'
print(b) # 25
print(c) # True
print(d) # 10.8

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } in any order
a , *b = s
print(a) # 'Hyd'
print(b) # [25 , True , 10.8]
print(type(b)) # <class'list'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } in any order
a , *b , c = s
print(a) # 'Hyd'
print(b) # [25 , True]
print(c) # 10.8

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {20 , 10} in any order
x , y = s
print(x) # 20
print(y) # 10

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a) 
print(b) # {100 , 110 , 120 , 130 , 140 , 150} in any order
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) 
print(d) # { 10 , 20 , 15 , 18 , 50 , 12} in any order
e = set('Rama  rAo')
print(e) # {'R' , 'a' , 'm' , 'r' , 'A' ,'o'} in any order
print(set(25)) # Error the argument should be a sequence
print(set()) # {} Empty set


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  --->  Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''

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
print(a) # { True, 25 , 10.8 , 'Hyd' , None} in any order
a . add(10 , 20 , 30) # Error add() method can only take one argument
a . add([10,20,30]) # Error because set cannot contain mutable objects


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

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25 , 10.8 , 'Hyd' , True} in any order
print(id(a)) # Address of set a
a . add(tpl) 
a . add('Sec')
print(a) # # {25 , 10.8 , 'Hyd' , True, (10 , 20 , 30) ,'Sec'} in any order
print(id(a)) # New address of set a
print(len(a)) # 6
a . add([100 , 200 , 300]) # Error because set cannot contain mutable objects in it
a . add(set()) # Error because set cannot contain mutable objects set in it
a . add({ }) # Error because set cannot contain mutable object dict in it

# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) 
print(s) # {(10 , 20 , 15 ,18)}
print(len(s)) # 1


# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s) # { 10 , 20 , 15, 18} in any order
s . update(25) # Error the update() method can only be sequence


'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  --->  Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
								(Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  ---> One  (or)  more
'''

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40, 50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c) 
print(s) # { 10 , 20 , 30 , 40 , 50 , 60, 70} in any order
print(len(s)) # 7
s . add(a , b , c) # Error set cannot contain mutable objects like list, set and dict and add() method takes only one argument

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) # { 'R' , 'a' , 'm' , 'o'} in any order
print(len(a)) # 4 
a . update(3 + 4j , 10.8 , True) # Error because update() method cannot have non sequences as arguments

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18} in any order
b = a . copy()
print(b) # {10 , 20 , 15 , 18} in any order
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is  c) # True


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

 # pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25 , 10.8 , 'Hyd' , True} in any order
print(a . pop()) # 25
print(a . pop()) # 10.8
print(a . pop()) # 'Hyd'
print(a . pop()) # True
print(a . pop()) # Error because set a is empty
print(a) # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2)) # Error because pop() method cannot have any arguments


'''
pop()  method
----------------
1) What  does  pop(No-args)  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  ---> Zero
'''

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25 , 10.8 , 'Hyd' , True} in any order
a . remove('Hyd')
print(a)  # {25 , 10.8 , True} in any order
a . remove('Sec') # Error because the element 'Sec' is not there in set


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True} in any order
a . discard('Hyd')
print(a) # {25 , 10.8 , True} in any order
a . discard('Sec')
print(a) # {25 , 10.8 , True} in any order
a . remove('Sec') # Error because the remove() method raises an error when invalid element is given


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18} in any order
a . clear()
print(a) # set()
print(len(a)) # 0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # { 10 , 20 , 30 , 40 , 50 , 60} in any order
print(a | b) # Error because a set and list cannot be concatenated
print(b . union(a)) # Error list class does not have union() method
print(a + b) # Error because set and list cannot be concatenated

#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) # { 30 , 40}
print(type(c)) # <class'set'>
d = a & b
print(d) # { 30 , 40}
print(type(d)) # <class'set'>
print(c  is  d) # False
print(c  ==  d) # True


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

# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) # {10 , 20}
print(type(c)) # <class'set'>
d = a - b
print(d) # {10 , 20}
print(type(d)) # <class'set'>
print(c  is  d) # False
print(c  ==  d) # True


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->  
				Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) # {10 , 20 , 50 , 60}
print(type(c)) # <class'set'>
d = a ^ b
print(d) # {10 , 20 , 50 , 60}
print(type(d)) # <class'set'>
print(c   is   d) # False
print(c  ==   d) #  True


'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
						                                                              without  common  elements																					  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_…

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # { 0 , 1, 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81} in any order
print(type(a)) # <class'set'>

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
# Code :
a = input("Enter input string : ")
s = set(a)
res = ''.join(s)
print("String without duplicates : ",res)

''' Output:
Enter input string : MISSISIPI
String without duplicates :  MISP
'''
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
# Code :
a = eval(input("Enter list with duplicates : "))
s = set(a)
res = list(s)
print("List without duplicates : ",res)

'''
Output:
Enter list with duplicates : [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
List without duplicates :  [False, 1, None, 10.8, 'Sec', 'Hyd', 25]
'''
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
# Code :
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
s = set(a) & set(b)
res = list(s)
print("Common elements between the 2 lists  : ",res)

'''
Output:
Enter 1st list : [10 , 20 , 30 , 40 , 50 , 60]
Enter 2nd list : [30 , 40 , 70 , 80 , 20]
Common elements between the 2 lists  :  [40, 20, 30]

'''