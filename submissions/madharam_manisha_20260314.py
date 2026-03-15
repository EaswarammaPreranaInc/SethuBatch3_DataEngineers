# Find  outputs  (Home  work)

s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } ( in random)
a , b , c , d = s
print(a) # Hyd
print(b) # 25
print(c) # True
print(d) # 10.8
#===============================================================================================================#
# Find  outputs  (Home  work)

s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a) # Hyd
print(b) # [25,  True,  10.8 ]
print(type(b)) # class list
#===============================================================================================================#
# Find  outputs  (Home  work)

s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a) # Hyd
print(b) # [ 25,  True ]
print(c) # 10.8
#===============================================================================================================#
# Find  outputs  (Home  work)

s = {20 , 10 , 20 , 10}
print(s) # {20 , 10 } random
x , y = s 
print(x) # 20
print(y) # 10
#===============================================================================================================#
# set()  function  demo  program  (Home  work)

a = range(100 , 151 , 10)
b = set(a) # { 100 , 110 , 120 , 130 , 140 , 150 }
print(b) # { 100 , 110 , 120 , 130 , 140 , 150 }
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10 , 15 , 18 , 50 , 20 , 12 } random
e = set('Rama  rAo')
print(e) # {'R','a','m',' ','r','A','o'}
print(set(25)) # error set does not allow non sequence
print(set()) # empty set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  --->  Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''
#===============================================================================================================#
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
print(a) # {True, 25, 10.8, 'Hyd', None} random
a . add(10 , 20 , 30) # error
a . add([10,20,30]) # error


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
#===============================================================================================================#
# Find  outputs  (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25, 10.8, 'Hyd', True}
print(id(a)) # address of set a 
a . add(tpl) # {25, 10.8, 'Hyd', True, (10, 20, 30)}
a . add('Sec') # {25, 10.8, 'Hyd', True, (10, 20, 30), 'Sec'}
print(a) # {25, 10.8, 'Hyd', True, (10, 20, 30), 'Sec'}
print(id(a)) # address of set a
print(len(a)) # 6
a . add([100 , 200 , 300]) # error
a . add(set()) # error
a . add({ }) # error
#===============================================================================================================#
# Find  outputs (Home  work)

s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) #{(10,20,15,18)}
print(len(s)) # 1
#===============================================================================================================#
# update()  method  demo program  (Home  work)

tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) #{10,20,15,18}
print(len(s)) #4
print(s) # {10,20,15,18} random
s . update(25) # error


'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  --->  Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                         (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  ---> One  (or)  more
'''
#===============================================================================================================#
# Find  outputs  (Home  work)

a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) # {10,20,30,40,50,70,60}
print(len(s)) # 7
s . add(a , b , c) # error
#===============================================================================================================#
# Find  outputs  (Home  work)

a = set()
a . update('Rama Rao')
print(a) # {'R','a','m',' ','o'}
print(len(a)) # 5
a . update(3 + 4j , 10.8 , True) # error update don't allows non sequence
#===============================================================================================================#
# copy()  method  demo  program  (Home  work)

a = {10 , 20 , 15 , 18}
print(a) # {10,20,15,18}
b = a . copy() 
print(b) # {10,20,15,18}
print(a  is  b) # false
print(a  ==  b) # true
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
#===============================================================================================================#
# pop()  method  demo  program  (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
print(a) #  {25 , 10.8 , 'Hyd' , True} random
print(a . pop())  # 25
print(a . pop())  # 10.8
print(a . pop())  # 'Hyd'
print(a . pop())  # True
print(a . pop())  # error
print(a) # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))  # error beacuse set does not allow indexing 


'''
pop()  method
----------------
1) What  does  pop(No-args)  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  ---> Zero
'''
#===============================================================================================================#
# remove()  method  demo  program  (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)  # {25 , 10.8 , True} random
a . remove('Sec')   # error 


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''
#===============================================================================================================#
# discard()  method  demo  program (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd') # {25 , 10.8 , True}
print(a) # {25 , 10.8 , True}
a . discard('Sec') # Nothing
print(a) # {25 , 10.8 , True}
a . remove('Sec') # error


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''
#===============================================================================================================#
# clear()  method  demo  program (Home  work)

a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear() # set()
print(a) # set()
print(len(a)) # 0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''
#===============================================================================================================#
# Find  outputs  (Home work)

a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {10,20,30,40,50,60}
print(a | b) # error
print(b . union(a)) # error
print(a + b) # error
#===============================================================================================================#
#  intersection()   method  demo  program (Home  work)

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) # {30,40}
print(type(c)) # class set
d = a & b
print(d) # {30,40}
print(type(d)) # class set
print(c  is  d) # false
print(c  ==  d) # true


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
#===============================================================================================================#
# difference()   method  demo  program  (Home  work)

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) # {10,20}
print(type(c)) # class set
d = a - b
print(d) # {10,20}
print(type(d)) # class set
print(c  is  d) # false
print(c  ==  d) # true


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->  
										Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''
#===============================================================================================================#
# symmetric_difference()   method  demo  program  (Home  work)

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) # {10,20,50,60}
print(type(c)) # class set
d = a ^ b
print(d) # {10,20,50,60}
print(type(d)) # class set
print(c   is   d) # False
print(c  ==   d) # true


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
#===============================================================================================================#
# Find  outputs  (Home  work)

a = {x * x  for   x   in   range(10)}
print(a) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a)) # class set 
#===============================================================================================================#
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

a = input("enter a string : ")
b = set(a)
c = "".join(b)
print("String without duplicates : ", c)
#===============================================================================================================#

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''

a = eval(input("enter a list with duplicates : "))
b = set(a)
c = list(b)
print(c)
#===============================================================================================================#
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
a = eval(input("enter a 1st list : "))
b = eval(input("enter a 2nd list : "))
c = set(a).intersection(set(b))
print("common elemnts from a and b : ", list(c))