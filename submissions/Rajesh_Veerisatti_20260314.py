

# Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

s = input("Enter string : ")

a = set()
b = ""

for ch in s:# R
    if ch not in a:
        a.add(ch)
        b += ch

print(b)


# Write  a  program  to  remove  duplicate  elements  of   list  using  set
a = eval(input("Enter a list: "))

s = set()
b = []

for i in a:
    if i not in s:
        s.add(i)
        b.append(i)

print(b)

# Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

a =eval(input("Enter a 1st  list: "))
b = eval(input("Enter a 2nd list: "))

s1 = set(a)
s2 = set(b)

c = list(s1 & s2)

c.sort()   # optional (to display in order)

print(c)


# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) # (25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a)) # <class tuple>
# a[3] = 'Sec' error tuple is immutable
# a[3 : 6] = 60 , 70 , 80


#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # (1 , 2 , 3) id of a
a += b
print(a , id(a)) # (1,2,3,4,5,6) id is diff


#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # (1 , 2 , 3) id of a
a = a + b
print(a , id(a)) # (1,2,3,4,5,6) id is diff


#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) 
print(type(a)) # <class 'str'>
b = eval(a)
print(b)
print(type(b)) # <class 'tuple'>
print(len(b))



# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)
a[1] = [80 , 90 , 100]
# print(a) # error tuple is immutable


# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
# print(a)# error tuple is immutable
a[1] = [80 , 90]
print(a) #[10 , [80 , 90] , 50 , 60]



# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) # (25, 10.8, 'Hyd', True)
print(type(x))# <class 'tuple'>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) # 25
print(b) # 10.8
print(c) # Hyd
print(d) # True
# p , q , r =  x
# a , b , c , d  , e = x


# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) # 25
print(b) # 10.8
print(c) # ['Hyd', True]
print(type(c)) # <class 'list'>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)# 25
print(b) # [10.8, 'Hyd']
print(c) # True


# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
# a , b , *c , d , e = tpl
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) # 25
print(b) # 10.8
print(_) # (3+4j)
print(d) # True
print(_) # (3+4j)


# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b) # (100, 110, 120, 130, 140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)# (10, 20, 15, 18)
e = tuple('Vamsi')
print(e)# ('V', 'a', 'm', 's', 'i')
# print(tuple(25))# error
print(tuple()) #()


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
		


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a)
print(id(a))
How  to  modify  30  in  tuple  to  35
print(a)
print(id(a))
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)
del  a[2]
a . pop(2)
print(a)
print(id(a))
How  to  remove  30  from  tuple  'a'
print(a)
print(id(a))
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print(How  to  print  1st  inner  tuple)
print(How  to  print  2nd  inner  tuple)
print(How  to  print  3rd  inner  tuple)
print(How  to  print  20)
print(How  to  print  50)
print(How  to  print  90)
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)
print(How  to   print  inner  tuple  in  another  way)
print(How   to  print   10)
print(How   to  print   20)
print(How   to  print   30)
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)
print(*a)
b = (())
print(b)
print(*b)
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})
print({[10 , 20 , 30]})
print({{10 , 20 , 30}})
print({{}})
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)
print(len(s))
print(type(s))
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a)
print(b)
print(c)
print(d)
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) 
a , *b = s
print(a)
print(b)
print(type(b))
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s
print(a)
print(b)
print(c)
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)
x , y = s
print(x)
print(y)
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)
e = set('Rama  rAo')
print(e)
print(set(25))
print(set())


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
print(a)
a . add(10 , 20 , 30)
a . add([10,20,30])


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
print(a)
print(id(a))
a . add(tpl)
a . add('Sec')
print(a)
print(id(a))
print(len(a))
a . add([100 , 200 , 300])
a . add(set())
a . add({ })
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)
print(len(s))
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))
print(s)
s . update(25)


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
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)
print(len(s))
s . add(a , b , c)
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)
print(len(a))
a . update(3 + 4j , 10.8 , True)
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)
c = a
print(a  is  c)


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
print(a)  
print(a . pop())  
print(a . pop())  
print(a . pop())  
print(a . pop())  
print(a . pop()) 
print(a) 
b = {10 , 20 , 30 , 40}
print(b . pop(2))  


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
print(a)  
a . remove('Hyd')
print(a)  
a . remove('Sec')   


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . discard('Hyd')
print(a)
a . discard('Sec')
print(a)
a . remove('Sec')


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
a . clear()
print(a)
print(len(a))


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))
print(a | b)
print(b . union(a))
print(a + b)
#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)
print(type(c))
d = a & b
print(d)
print(type(d))
print(c  is  d)
print(c  ==  d)


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
print(c)
print(type(c))
d = a - b
print(d)
print(type(d))
print(c  is  d)
print(c  ==  d)


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
print(c)
print(type(c))
d = a ^ b
print(d)
print(type(d))
print(c   is   d)
print(c  ==   d)


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
# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)
print(type(a))
a[3] = 'Sec'
a[3 : 6] = 60 , 70 , 80
#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))
a += b
print(a , id(a))
#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))
a = a + b
print(a , id(a))
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
print(len(b))
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)
a[1] = [80 , 90 , 100]
print(a)
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)
a[1] = [80 , 90]
print(a)
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)
print(type(x))
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)
print(b)
print(c)
print(d)
p , q , r =  x
a , b , c , d  , e = x
# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)
print(b)
print(c)
print(type(c))
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)
print(b)
print(c)
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)
print(b)
print(c)
print(d)
print(e)
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)
print(b)
print(_)
print(d)
print(_)
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)
print(type(b))
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)
e = tuple('Vamsi')
print(e)
print(tuple(25))
print(tuple())


'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  --->  Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''
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
#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a)
print(id(a))
How  to  modify  30  in  tuple  to  35
print(a)
print(id(a))
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)
del  a[2]
a . pop(2)
print(a)
print(id(a))
How  to  remove  30  from  tuple  'a'
print(a)
print(id(a))
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print(How  to  print  1st  inner  tuple)
print(How  to  print  2nd  inner  tuple)
print(How  to  print  3rd  inner  tuple)
print(How  to  print  20)
print(How  to  print  50)
print(How  to  print  90)
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)
print(How  to   print  inner  tuple  in  another  way)
print(How   to  print   10)
print(How   to  print   20)
print(How   to  print   30)
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)
print(*a)
b = (())
print(b)
print(*b)
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})
print({[10 , 20 , 30]})
print({{10 , 20 , 30}})
print({{}})
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)
print(len(s))
print(type(s))
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a)
print(b)
print(c)
print(d)
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) 
a , *b = s
print(a)
print(b)
print(type(b))
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s
print(a)
print(b)
print(c)
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)
x , y = s
print(x)
print(y)
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)
e = set('Rama  rAo')
print(e)
print(set(25))
print(set())


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
print(a)
a . add(10 , 20 , 30)
a . add([10,20,30])


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
print(a)
print(id(a))
a . add(tpl)
a . add('Sec')
print(a)
print(id(a))
print(len(a))
a . add([100 , 200 , 300])
a . add(set())
a . add({ })
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)
print(len(s))
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))
print(s)
s . update(25)


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
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)
print(len(s))
s . add(a , b , c)
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)
print(len(a))
a . update(3 + 4j , 10.8 , True)
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)
c = a
print(a  is  c)


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
print(a)  
print(a . pop())  
print(a . pop())  
print(a . pop())  
print(a . pop())  
print(a . pop()) 
print(a) 
b = {10 , 20 , 30 , 40}
print(b . pop(2))  


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
print(a)  
a . remove('Hyd')
print(a)  
a . remove('Sec')   


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . discard('Hyd')
print(a)
a . discard('Sec')
print(a)
a . remove('Sec')


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
a . clear()
print(a)
print(len(a))


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))
print(a | b)
print(b . union(a))
print(a + b)
#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)
print(type(c))
d = a & b
print(d)
print(type(d))
print(c  is  d)
print(c  ==  d)


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
print(c)
print(type(c))
d = a - b
print(d)
print(type(d))
print(c  is  d)
print(c  ==  d)


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
print(c)
print(type(c))
d = a ^ b
print(d)
print(type(d))
print(c   is   d)
print(c  ==   d)


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
# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)
print(type(a))