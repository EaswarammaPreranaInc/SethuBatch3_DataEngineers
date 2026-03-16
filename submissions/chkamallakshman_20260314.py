# python Home work 14-03-2026
#1. Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)  # output : (25,10.8,3+4j,'Hyd',True,None,'Hyd',25)
print(type(a)) # output : <class 'tuple'>
a[3] = 'Sec' # output : Error : TypeError : tuple does not support item assignment
a[3 : 6] = 60 , 70 , 80 # TypeError : 'tuple' does not support for item assignment.


 # 2 . #  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # output : (1,2,3) <space> Adress of the tuple a.
a += b # output :  (1,2,3,4,5,6) 
print(a , id(a)) # output : (1,2,3,4,5,6)<space> reference is modifed.(new address)


  3 . #  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # output : (1,2,3)<space> Address of the tuple a .
a = a + b # (1, 2, 3, 4, 5, 6)
print(a , id(a)) # output : (1, 2, 3, 4, 5, 6)<space> address of the same reference.

 # 4 . #  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) # output : (10 , 20 , 30 , 40)
print(type(a)) # output : <class'str'>
b = eval(a) # 
print(b) # output : (10,20,30,40)
print(type(b)) # output : <class'tuple'>
print(len(b)) # output : 4


# 5 . # Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70 # output : (10 , [70, 30, 40],50,60)
print(a) # output : (10,[70,30,40],50,60)
a[1] = [80 , 90 , 100] # output : TypeError : 'tuple' object does not support item assignement.
print(a) # output : (10, [70, 30, 40], 50, 60)


# 6 . # Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70 # TypeError
print(a) # output : [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)  # output :[10, [80, 90], 50, 60]

#7 . # Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) # output : (25 ,10.8,'Hyd',True)
print(type(x)) # output : <class 'tuple'>


# 8 . # 8 . # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) # output : 25
print(b) # output : 10.8
print(c) # output : Hyd
print(d) # True
#p , q , r =  x # output : valueError: to many values to unpack(expected 3 , got 4)
a , b , c , d  , e = x # output : valueerror : (excpected 5 , got 4)


# 9 . # Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) # output : 25
print(b) # output : 10.8
print(c) # output : ['Hyd',True]
print(type(c)) # output : <class 'list'>


# 10 . # 10 . # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # output : 25
print(b) # [10.8 , 'Hyd']
print(c) # True


# 11 . # 11 .# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # output : 24
print(b) # output : 10.8
print(c) # output : []
print(d) # output : Hyd
print(e) # output : True


# 12 . # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) # output : 25
print(b)  # output : 10.8
print(_) # output : (3+4j)
print(d) # output : True
print(_) # output : (3+4j)


 # 13 . # tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a) 
print(b)  # output (100 , 110 , 120 , 130 , 140)
print(type(b)) # output : # <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c) #  (10 ,20 , 15 , 18)
print(d) # output : (10 20 , 15 ,18)
e = tuple('Vamsi')
print(e)# output :  ('v','a','m','s','i')
#print(tuple(25))  # output : TypeError beacuse 25 is int object
print(tuple()) # output : ()
'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  --->  Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''


# 14 . #index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
		
    # output : 15 is found at index :  2
	# output : 15 is found at index :  5
	# output : 15 is found at index :  8
	# output : 15  is  found  3  times


 # # 15 . #  How  to  modify  an  element  of  tuple ?    (Home  work)
# a  =  10 ,  20 ,  30 ,   40 ,  50
# #     0      1       2       3      4
# #a[2] = 35 # TypeError
# print(a) # (10,20,30,40,50)
# print(id(a)) # output : Address of the tuple a
# #How  to  modify  30  in  tuple  to  35
# print(a)
# print(id(a))  
# output :
a = (10 , 20 , 30 , 40, 50)
print(a)
print(id(a))

b=list(a)
b[2]=29
a=tuple(b)
print(a)
print(id(a))



# 16 . # # 16 . # How  to  delete  an  element  of  tuple ?   (Home  work)
# a  = 10 , 20 , 30 , 40 , 50
# #    0     1      2     3      4
# a . remove(30)
# del  a[2]
# a . pop(2)
# print(a)
# print(id(a))
# #How  to  remove  30  from  tuple  'a'
# print(a)
# print(id(a))

# output : 
a = (10,20,30,40,50)
print(a)
print(id(a))
b = list(a)
print(b)
b.remove(30)
#print(b)
a=tuple(b)
print(a)
print(id(a))


# # 17 .#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # output : ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a)) # output : <class 'tuple'>
print(len(a)) # output : 3
print(a[0])#(How  to  print  1st  inner  tuple) 
print(a[1])#(How  to  print  2nd  inner  tuple) 
print(a[2])#(How  to  print  3rd  inner  tuple)
print(a[0][1])#(How  to  print  20) 
print(a[1][2])#(How  to  print  50) 
print(a[2][3])#(How  to  print  90) 


 # 18 . # Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0]) #(How  to   print  inner  tuple)
#print(How  to   print  inner  tuple  in  another  way)
for i in a:
    print(i)
print(a[0][0]) #(How   to  print   10)
print(a[0][1]) #(How   to  print   20)
print(a[0][2]) #(How   to  print   30)
b = ((),)
print(b[0])
#print(How  to   print  inner  tuple  of  tuple  'b')
#print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)
for i in b:
    print(i)

# 19 . # 19 . #  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # output : (10 , 2 ,30)
print(*a) # 10,20,30
b = (())
print(b) # output : ()
print(*b)


 #20 . What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # output : {1,2,3,4,5,5,6,7}
print(type(a)) # output : <class 'str'>
b = eval(a) # output : {1,2,3,4,5,6,7}
print(b) # output : # output : {1,2,3,4,5,6,7}
print(type(b)) # output : <class 'set'>


# 21 . # 21 . #  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # output : {(10 , 20, 30)}
print({[10 , 20 , 30]}) # output : TypeError
print({{10 , 20 , 30}}) # output :TypeError : because set inside set 
print({{}}) # output : TypeError



# 22 .# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # output : {25, 10.8, 'Hyd', True}
print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop
for i in a:
    print(i)


 # 23 . # Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # output : {True, 'Hyd', 25}
print(len(s)) # output : 3
print(type(s)) # <class 'set'>


# 24 . # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # output : {'Hyd', 25, True, 10.8}
a , b , c , d = s
print(a) # output : Hyd
print(b) # output : 25
print(c) # output : True
print(d) # output : 10.8


 # 25 . # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  # output : {'Hyd' 25, True, 10.8}
a , *b = s
print(a) # output : Hyd
print(b) # output : [25 , True, 10.8]
print(type(b))  # output : <class 'list'>


# 26 . # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # output : {'Hyd' , 25, True, 10.8}
a , *b , c = s
print(a) # output : Hyd
print(b) # output : [25 , True]
print(c) # output : 10.8


# 27 . # 27 . # Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # output : {10 , 20}
x , y = s 
print(x) #  output :10
print(y) # output : 20


# 28 . # 28 . # set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) # output : {100 , 151 ,10}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # output : {10,20,15,18,50,12}
e = set('Rama  rAo')
print(e) # output : {'R','a','m',' ', 'r','A','o'}
#print(set(25)) # output : Error
print(set())  # output : set()

'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  --->  Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''


# 29 . # add()  method  demo  program  (Home  work)
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
print(a) #output : {None, True, 10.8, 'Hyd', 25}
#a . add(10 , 20 , 30)
#a . add([10,20,30])

# '''
# add()   method
# -----------------
# 1) What  does  add(x)  do ?  --->  Inserts   'x'  any  where  in  the  set  becoz  set  is  unordered

# 2) How  many  arguments  can  add()  method  take ?  --->  Single

# 3) Is  set . add(mutable-object)  valid ? --->  No  becoz  set  can  not  hold  mutable  element

# 4) In  other  words,  argument  of  add()  method  should  be  immutable  object  only

# 5) What  does  set .  add(sequence)  do  ?  --->
# 																Inserts  sequence  any  where  in  the  set  but  not  elements  of  sequence
# 																(Like  append()  method  of  list  class)



# 30 . # Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # output : {25 , 10.8, 'Hyd' True}
print(id(a)) # output : Address of the a
a . add(tpl)
a . add('Sec')
print(a) # output : {True, 'Sec', 10.8, (10, 20, 30), 'Hyd', 25}
print(id(a)) # output : Address of the a
print(len(a)) # output : 6
#a . add([100 , 200 , 300]) # output : TypeError
#a . add(set()) # output : TypeError
#a . add({ }) # output : TypeError


# 31 . # 31 . # Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # output : {(10,20,15,18)}
print(len(s)) # output : 1



# 32 . # update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # output : 4
print(s) # output : {10,20,15,18}
s . update(25) # output : TypeError
# '''
# update()  method
# --------------------
# 1) What  does  update(sequence)  do ?  --->  Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
# 											                         (Like  extend()  method  of  list  class)

# 2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

# 3) How  many  arguments  can  update()  method  take ?  ---> One  (or)  more


# 33 . # Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) # {10,20,30,40,50,60,70}
print(len(s)) # output : 7
#s . add(a , b , c)


 # 34 . # Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) # output : {'R','a','m',' ','o'}
print(len(a)) # output : 5
#a . update(3 + 4j , 10.8 , True)


# 35 . # copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # output : {10,20,15,18}
b = a . copy()
print(b) # output : {10,20,15,18}
print(a  is  b) # output : False
print(a  ==  b) # output : True
c = a
print(a  is  c) # output : True
# '''
# copy()  method
# ------------------
# 1) What  does  copy()  method  do ?  ---> Returns  a  new  set  with  same  elements

# 2) a = b
#     What  does  the  statement  do ?  --->  Reference  copy
# 																   i.e.  id  is  copied

# 3) What  is  shallow  clone ?  ---> Reference  copy
#      What  is  deep  clone ?  --->  Object  copy


# 36 . # pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)   # output : {25 , 10.8, 'Hyd',True}
print(a . pop())  # output : 25
print(a . pop())  # output :10.8
print(a . pop())   # output : Hyd
print(a . pop())  # output : True
#print(a . pop())  
print(a) # output: set()
b = {10 , 20 , 30 , 40}
#print(b . pop(2))  
# '''
# pop()  method
# ----------------
# 1) What  does  pop(No-args)  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

# 2) What  does  emptyset . pop()  do ?  --->  Throws  error

# 3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

# 4) How  many  arguments  can  pop()  method  take  ?  ---> Zero


## 37 . remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # output : {25,10.8,'Hyd',True}
a . remove('Hyd')
print(a)  # output : {25 , 10.8,True}
#a . remove('Sec') # output : KeyError
 

# '''
# remove()   method
# ----------------------
# 1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

# 2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

# 3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed




#38 . # discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # output : {25,10.8,'Hyd',True}
a . discard('Hyd')
print(a) # output : {25 , 10.8,True}
a . discard('Sec')
print(a) # output : KeyError
a . remove('Sec')

# '''
# discard()  method
# ---------------------
# 1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

# 2) What  does  discard(Invalid-element)  do ?  --->Nothing

# 3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion



# 39 . # clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # output : {10,20,15,18}
a . clear()
print(a) # output : set()
print(len(a)) # output : 0
# '''
# clear()  method
# ------------------
# What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty



# 40 . # Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))# output : {40, 10, 50, 20, 60, 30}
#print(a | b) #output : typeError
#print(b . union(a)) # output : TypeError
#print(a + b) # output : Typeerror


# 41 . #  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) # output : {30 , 40}
print(type(c)) # output : <class 'set'>
d = a & b 
print(d)# output : {30 , 40}
print(type(d)) # output  : <class 'set>
print(c  is  d) # output : False
print(c  ==  d) # output : True

# '''
# 1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

# 2) Is  set . intersection(list)  valid  ?  --->
# 							Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

# 3) What  is  another  way  to  obtain  common  elements ?  ---> a & b

# 4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

# 5) Is  list . intersection(set)  valid ?  --->  No  becoz  there  is  no  intersection()  method  in  list  class
# '''


# 42 . # difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) # output : {10 , 20}
print(type(c)) # output : <class 'set'>
d = a - b
print(d)# output : {10,20}
print(type(d)) # output : <class 'set'>
print(c  is  d) # output : False
print(c  ==  d) # output : True


# '''
# difference()  method
# ------------------------
# 1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

# 2) Is  set . difference(list)  valid  ?  --->  
# 										Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

# 3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

# 4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only


# 43 . # 43.symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) # {10 , 20 , 50 , 60}
print(type(c)) # output : <class 'set'>
d = a ^ b
print(d) # output : {10 , 50 , 20 , 60}
print(type(d)) # output : <class 'set'>
print(c   is   d) # output : False
print(c  ==   d) # output : True

# '''
# symmetric_difference()  method
# ---------------------------------------
# 1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
# 						                                                              without  common  elements
# 																					  i.e.  Union  -  Intersection

# 2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

# 3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b

# 4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only



# 44 . # 44 . # Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # output : {0,1,4,9,16,25,36,49,64,81}
print(type(a)) # output : <class 'set'>


# # 45 . (Home  work)
# Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

# 1) Let  input  be   Rama  Rao
#     What  is  the  output  ? ---> Ram<space>o

# 2) Both  input  and  output  are  strings

# 3) How  to  convert  string  to  set  ?  --->  set(string)
#     How  to  convert  set  to  string ?  --->  '' . join(set)

# 4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'

a = "Rama Rao"
s = set(a)
b = ''.join(s)
print(b)


# 46. Write  a  program  to  remove  duplicate  elements  of   list  using  set

# 1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
#     What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

# 2) Both  input  and  output  are  lists

a = [False , 25 , 10.8 , 1 , 25 , 0 , 'Hyd' , 10.8 , 1.0 , None , 'Sec' , 'Hyd' , True]

s = set(a)
b = list(s)

print(b)

