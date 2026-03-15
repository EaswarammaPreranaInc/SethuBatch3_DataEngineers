# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)		# (25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))		# <class 'tuple'>
#a[3] = 'Sec'		# error because tuple is immutable modifying elements is not possible
#a[3 : 6] = 60 , 70 , 80 # error because tuple is immutable modifying elements is not possible

#=======================================================================================================

#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))	# (1 , 2 , 3) address of an object 
a += b              # REFERENCE MODIFIED
print(a , id(a))	# (1 , 2 , 3 , 4 , 5, 6) different address

#=======================================================================================================

#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))    # (1 , 2 , 3) address of an object
a = a + b
print(a , id(a))    # (1 , 2 , 3 , 4 , 5 , 6) different address

#=======================================================================================================

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')	
print(a)		# (10 , 20 , 30 , 40)
print(type(a))		# <class 'str'>
b = eval(a)		# (10 , 20 , 30 , 40)
print(b)		# (10 , 20 , 30 , 40)
print(type(b))		# <class 'tuple'>
print(len(b))		# 4

#=======================================================================================================

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
#a[1][0] = 70       # error because tuple is immutable can't modified elements
print(a)
#a[1] = [80 , 90 , 100]      # error because tuple is immutable can't modified elements
print(a)

#=======================================================================================================

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70   # error because tuple is immutable can't change elements
print(a)	    #  [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)	    # [10 , [80 , 90] , 50 , 60]

#=======================================================================================================

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)	# (20 , 10.8 , 'Hyd' , True)
print(type(x))	# <class 'tuple'>

#=======================================================================================================

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)	# 25
print(b)	# 10.8
print(c)	# Hyd
print(d)	# True
#p , q , r =  x	# error because to many values to unpack 
#a , b , c , d  , e = x	# error because only 4 values are require got 5 objects

#=======================================================================================================

# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)	# 25
print(b)	# 10.8
print(c)	# [Hyd , True]
print(type(c))	# <class 'list'>

#=======================================================================================================

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)	# 25
print(b)	# [10.8 , Hyd]
print(c)	# True

#=======================================================================================================

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl	
print(a)	# 25
print(b)	# 10.8
print(c)	# []
print(d)    # Hyd
print(e)    # True

#=======================================================================================================

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)	# 25
print(b)	# 10.8
print(_)	# (3 + 4j) because last '_' points to last element 3+4j
print(d)	# True
print(_)	# (3 + 4j) because last '_' points to last element 3+4j

#=======================================================================================================

# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)		# (100 , 110 , 120 , 130 , 140)
print(b)		# (100 , 110 , 120 , 130 , 140)
print(type(b))		# <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)		# (10 , 20 , 15 , 18)
e = tuple('Vamsi')
print(e)		# ('V' , 'a' , 'm' , 's' , 'i')
#print(tuple(25))	# error it converts only sequence arguments
print(tuple())		# ()

'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  --->  Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''
#=======================================================================================================

#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1    2    3    4    5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')

# 15 is found at index : 2
# 15 is found at index : 5
# 15 is found at index : 8
# 15  is  found  3  times

#=======================================================================================================

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
# a[2] = 35	# error becoz tuple is immutable
print(a)	# ( 10 ,  20 ,  30 ,   40 ,  50)
print(id(a))	# address of an object
# how  to  modify  30  in  tuple  to  35
b = list(a)
b[2] = 35
a = tuple(b)
print(a)    # ( 10 ,  20 ,  35  ,   40 ,  50)
print(id(a))    # different address

#=======================================================================================================

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
# a . remove(30)	# error becoz remove method is not applicable tuple 
# del  a[2]	    # error
# a . pop(2)	# error becoz pop() is not applicable for tuple
print(a)	    # (10 , 20 , 30 , 40 , 50)
print(id(a))	# address of an object
# How  to  remove  30  from  tuple  'a'
b = list(a)
b.remove(30)
a = tuple(b)
print(a)        # (10 , 20 , 40 , 50)
print(id(a))    # different object

#===========================================================================================

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)	# ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))	# <class 'tuple'>
print(len(a))	# 3
print(a[0])	# How  to  print  1st  inner  tuple)
print(a[1])	# How  to  print  2nd  inner  tuple)
print(a[2])# How  to  print  3rd  inner  tuple)
print(a[0][1])	# How  to  print  20)
print(a[1][2])	# How  to  print  50)
print(a[2][3])	# How  to  print  90)

#===========================================================================================

# # Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])	     # How  to   print  inner  tuple)	
for i in a:      # How  to   print  inner  tuple  in  another  way)
    print(i)
print(a[0][0])	# How   to  print   10)
print(a[0][1])	# How   to  print   20)
print(a[0][2])  # How   to  print   30)
b = ((),)
print(b[0]) 	# How  to   print  inner  tuple  of  tuple  'b')
for i in b:     # How  to   print  inner  tuple  of  tuple  'b'  in  another  
    print(i)
	
#===========================================================================================

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)	# (10 , 20 , 30)
print(*a)	# 10 20 30
b = (())
print(b)	# ()
print(*b)	# nothing

#===========================================================================================

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)	#  {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))	# <class 'str'>
b = eval(a)	#  {10 , 20 , 15 , 18 , 12}
print(b)	#  {10 , 20 , 15 , 18 , 12}
print(type(b))	#  <class 'set'>

#===========================================================================================

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})		# {10 , 20 , 30}
# print({[10 , 20 , 30]})		# error becoz set elements must be immutable,  list is mutable
# print({{10 , 20 , 30}})		# error becoz set elements must be immutable,  set is mutable
# print({{}})			# error becoz set elements must be immutable,  dict is mutable

#===========================================================================================

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)	# {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
for i in a:	# How  to  iterate  set  with  for  loop
	print(i)

#===========================================================================================

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)	# {Hyd , True , 25}  # set doesn't allow duplicate elements so value of True is 1 so it give True
print(len(s))	# 3
print(type(s))	# <class 'set'>

#===========================================================================================

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)	# {Hyd , 25 , True , 10.8}
a , b , c , d = s
print(a)	# Hyd order may be changed becoz 'set' is unordered
print(b)    # 25  order may be changed becoz 'set' is unordered
print(c)    # True order may be changed becoz 'set' is unordered
print(d)    # 10.8 order may be changed becoz 'set' is unordered

#===========================================================================================

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) 	# {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)	# Hyd	order may be changed becoz set is unordered
print(b)	# {25 , True , 10.8}	order may be changed becoz set is unordered
print(type(b))	# <class 'set'>

#===========================================================================================

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)	# {'Hyd',  25,  True,  10.8 }
a , *b , c = s	
print(a)	# Hyd  order may be changed becoz set is unorder
print(b)	# {25 , True}  order may be changed becoz set is unorder
print(c)	# 10.8  order may be changed becoz set is unorder

#===========================================================================================

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)	# {20 , 10} because set doen't allow duplicate elements
x , y = s
print(x)	# 20
print(y)	# 10

#===========================================================================================

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)	# {100 , 110 , 120 , 130 , 140 , 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)	# {10 , 20 , 15 , 18 , 50 , 12}
e = set('Rama  rAo')
print(e)	# {'R' , 'a' , 'm' , ' ' , 'r' , 'A' , 'o'}
# print(set(25))	# error set arguments must be sequence
print(set())	# set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  --->  Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''
#============================================================================================

# add()  method  demo  program  (Home  work)
a = set()
a . add(True)	# {True}
a . add(25)	# {True , 25}
a . add(10.8)	# {True , 25 , 10.8}
a . add(1)	# {True , 25 , 10.8 , 1}
a . add('Hyd')	# {True , 25 , 10.8 , 1 , 'Hyd'}
a . add(25)	# {True , 25 , 10.8 , 1 , 'Hyd' , 25}
a . add(None)	# {True , 25 , 10.8 , 1 , 'Hyd' , 25 , None}
a . add('Hyd')	# {True , 25 , 10.8 , 1 , 'Hyd' , 25 , None , 'Hyd'}
a . add(1.0)	# {True , 25 , 10.8 , 1 , 'Hyd' , 25 , None , 'Hyd' , 1.0}
print(a)	# {True , 25 , 10.8 , 'Hyd' , None}
# a . add(10 , 20 , 30)	# error becoz only single argument will added at a time
# a . add([10,20,30])	# error becoz set allow immutable objects only , list is mutable


'''
add()   method
-----------------
1) What  does  add(x)  do ?  --->  Inserts   'x'  any  where  in  the  set  becoz  set  is  unordered

2) How  many  arguments  can  add()  method  take ?  --->  Single

3) Is  set . add(mutable-object)  valid ? --->  No  becoz  set  can  not  hold  mutable  element

4) In  other  words,  argument  of  add()  method  should  be  immutable  object  only

5) What  does  set .  add(sequence)  do  ?  ---> 	Inserts  sequence  any  where  in  the  set  but  not  elements  of  sequence
							(Like  append()  method  of  list  class)
'''

#============================================================================================

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)		# {25 , 10.8 , 'Hyd' , True}
print(id(a))		# address of an object
a . add(tpl)		# {25 , 10.8 , 'Hyd' , True , (10 , 20 , 30)}
a . add('Sec')		# {25 , 10.8 , 'Hyd' , True , (10 , 20 , 30) , 'Sec'}
print(a)		# {25 , 10.8 , 'Hyd' , True , (10 , 20 , 30) , 'Sec'}
print(id(a))		# same address because objects only modified
print(len(a))		# 6
# a . add([100 , 200 , 300]) # error set allows immutable elements only
# a . add(set())		# error becoz set is mutable
# a . add({ })	    	# error '{}' dict is a mutable but set is allows only immutable elements

#============================================================================================

# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)	# {(10 , 20 , 15 , 18)}
print(s)	# {(10 , 20 , 15 , 18)}
print(len(s))	# 1

#============================================================================================

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)		# {10 , 20 , 15, 18}
print(len(s))		# 4
print(s)		# {10 , 20 , 15, 18}
# s . update(25)		# error becoz it allows only sequence elements


'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  --->  Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                         (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  ---> One  (or)  more
'''

#============================================================================================

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40 , 50}
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)	# {10 , 20 , 30 , 40 , 50 , 60 , 70}    inserts elements of sequence to the set unordered
print(len(s))	# 7
# s . add(a , b , c)	# error becoz add() takes only one argument, there 3 arguments are given

#============================================================================================

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)	# {'R' , 'a' , 'm' , ' ' , 'o'}
print(len(a))	# 5
# a . update(3 + 4j , 10.8 , True)  errors becoz argument should be sequence only not non-sequence

#============================================================================================

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)		# {10 , 20 , 15 , 18}
b = a . copy()
print(b)		# {10 , 20 , 15 , 18}
print(a  is  b)		# False  becoz reference changed new set is created
print(a  ==  b)		# True   becoz a and b having same elements
c = a		
print(a  is  c)		# True   becoz a and c is points same set


'''
copy()  method
------------------
1) What  does  copy()  method  do ?  ---> Returns  a  new  set  with  same  elements

2) a = b
    What  does  the  statement  do ?  --->  Reference  copy
					    i.e.  id  is  copied

3)   What  is  shallow  clone ?  ---> Reference  copy
     What  is  deep  clone ?  --->  Object  copy
'''

#============================================================================================

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}     # pop() removes first element in set returns deleted element
print(a)  		# {25 , 10.8 , 'Hyd' , True}
print(a . pop())  	# 25
print(a . pop())  	# 10.8
print(a . pop())  	# 'Hyd'
print(a . pop())  	# True
# print(a . pop()) 	# error becoz set is empty
print(a) 		# empty set()
b = {10 , 20 , 30 , 40}
# print(b . pop(2))  	# error becoz indexing not possible in set , it is unordered 


'''
pop()  method
----------------
1) What  does  pop(No-args)  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  ---> Zero
'''

#============================================================================================

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  	# {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)  	# {25 , 10.8 ,  True}
# a . remove('Sec')   # error becoz 'sec' is not in set


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''

#============================================================================================

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)		# {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a)		# {25 , 10.8 , True}
a . discard('Sec')
print(a)		# {25 , 10.8 , True}  discard doesn't throw error if element not in set
# a . remove('Sec')	# error becoz remove(invalid-element) throws error


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''

#============================================================================================

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)	# {10 , 20 , 15 , 18}
a . clear()
print(a)	# set()
print(len(a))	# 0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''

#============================================================================================

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))	# {10 , 20 , 30 , 40 , 50 , 60}
# print(a | b)		# error '|' works between sets
# print(b . union(a)) # error becoz b is list, list don't have union method
# print(a + b)		# error becoz can't concatenate set and list

#============================================================================================

#  intersection()   method  demo  program (Home  work)  
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)	  # returns common elements from both sets
print(c)	# {30 , 40}
print(type(c))	# <class 'set'>
d = a & b
print(d)	# {30 , 40}
print(type(d))	# <class 'set'>
print(c  is  d)	# False reference is different
print(c  ==  d)	# True becoz elements are same


'''
intersection()  method
---------------------------
1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

2) Is  set . intersection(list)  valid  ?  --->	Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  another  way  to  obtain  common  elements ?  ---> a & b

4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

5) Is  list . intersection(set)  valid ?  --->  No  becoz  there  is  no  intersection()  method  in  list  class
'''

#============================================================================================

# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)	# {10 , 20}
print(type(c))	# <class 'set'>
d = a - b
print(d)	# {10 , 20}
print(type(d))	# <class 'set'>
print(c  is  d)	# False returns new set
print(c  ==  d)	# True becoz elements are same


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->  
										Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''

#============================================================================================

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)		# {10 , 20 , 50 , 60}
print(type(c))		# <class 'set'>
d = a ^ b
print(d)		# {10 , 20 , 50 , 60}
print(type(d))		# <class 'set'>
print(c   is   d)	# False becoz returns new set
print(c  ==   d)	# True becoz elements are same


'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but  without  common  elements										       i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b

4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only
'''

#============================================================================================

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)	# {0 , 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81}
print(type(a))	# <class 'set'>

#============================================================================================

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

a = input('Enter input string : ')       # missisipi 
set = set(a)
c = ''.join(set)
print('String without duplicates : ',c)  # imsp 

#============================================================================================

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''

a = eval(input('Enter list with duplicates : '))
b = set(a)
print('List without duplicates : ',list(b))

#============================================================================================

'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = set(a).intersection(set(b))
print('Common elements between the 2 lists : ',list(c))