# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)#25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(type(a))#<class 'tuple'>
a[3] = 'Sec'#error because tuple is immutable because does not modifie the original tuple
a[3 : 6] = 60 , 70 , 80#error because tuple is immutable
#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))#(1 , 2 , 3),address of object tuple a
a += b#(1,2,3,4,5,6)
print(a , id(a))#(1,2,3,4,5,6),address of object tuple a
#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))#(1 , 2 , 3),address of object a
a = a + b#(1,2,3,4,5,6)
print(a , id(a))#(1,2,3,4,5,6),new address
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)#'(10,20,65)'
print(type(a))#<class 'str'>
b = eval(a)#a='(1,2,3)'
print(b)#(1,2,3)
print(type(b))#<class 'tuple'>
print(len(b))#3
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)#(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]
print(a)#(10 , [80 , 90 , 100] , 50 , 60)
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)# [10 , (70 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)#[10 ,[80 , 90] , 50 , 60]
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#25,10.8,'Hyd',True
print(type(x))#<class'tuple'>
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#'Hyd'
print(d)#True
p , q , r =  x
a , b , c , d  , e = x
# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)#25
print(b)#10.8
print(c)#('Hyd',True)
print(type(c))#<class 'tuple'>
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#(10.8 , 'Hyd')
print(c)#True
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)#Hyd
print(e)#True
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#3+4j
print(d)#True
print(_)#3+4j
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)#(100,110,120,130,140)
b = tuple(a)
print(b)#(100,110,120,130,140)
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)#(10 , 20 , 15, 18)
print(d)#(10 , 20 , 15, 18)
e = tuple('Vamsi')
print(e)#('V','a','m','s','i')
print(tuple(25))#error because tuple doesn't support single element
print(tuple())#empty tuple


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
		print('15 is found at index : ' , i)#2,5,8
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')#3
  
  #  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35#error because tuple is immutable so tuple cannot the change the original tuple
print(a)# (10 ,  20 ,  30 ,   40 ,  50)
print(id(a))#address of object a
# How  to  modify  30  in  tuple  to  35#tuple(list(a[2]=35))
print(a)#(10 ,  20 ,  35 ,   40 ,  50)
print(id(a))#new address
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)#error
del  a[2]#a[:2]+a[3:]
a . pop(2)#error
print(a)#(10 , 20 , 40 , 50)
print(id(a))#new address
# How  to  remove  30  from  tuple  'a'
print(a)#a[:2]+a[3:]
print(id(a))#new address

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))#<class 'tuple'>
print(len(a))#3
print(How  to  print  1st  inner  tuple)#a[0]
print(How  to  print  2nd  inner  tuple)#a[1]
print(How  to  print  3rd  inner  tuple)#a[2]
print(How  to  print  20)#a[0][1]
print(How  to  print  50)#a[1][2]
print(How  to  print  90)#a[2][3]
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)#a[0]
print(How  to   print  inner  tuple  in  another  way)#a[:]
print(How   to  print   10)#a[0][0]
print(How   to  print   20)#a[0][1]
print(How   to  print   30)#a[0][2]
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')#b[0]
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)#b[:]

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)#(10 , 20 , 30)
print(*a)#10 20 30
b = (())
print(b)#((),)
print(*b)#()
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)# '{10 , 20 , 15 , 12 , 18}'
print(type(a))#<class str>
b = eval(a)
print(b)#{10 , 20 , 15 , 12 , 18}
print(type(b))#<class 'set'>
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})#{(10 , 20 , 30)}
print({[10 , 20 , 30]})#error because set cannot have list
print({{10 , 20 , 30}})#error because set cannot have set
print({{}})#empty dictionary
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')#print(a)
print(a)#{25 , True , 'Hyd' , 10.8} in any order
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop#for x in set(a):
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{'Hyd',True,25}
print(len(s))#3
print(type(s))#<class 'set'>
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)#Hyd
print(b)#25
print(c)#True
print(d)#10.8
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)# {'Hyd',  25,  True,  10.8 } in any order
a , *b = s
print(a)#Hyd
print(b)#[25,  True,  10.8]
print(type(b))#<class 'list'>
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 } in any order
a , *b , c = s
print(a)#Hyd
print(b)#[True,25,]
print(c)#10.8
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)# {20 , 10} in order
x , y = s
print(x)#20 or 10
print(y)#10 or 20
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)#100,110,120,130,140,150
b = set(a)#{100,110,120,130,140,150}
print(b)#{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)#{10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18}
print(d)#{10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18}
e = set('Rama  rAo')
print(e)#{Rama  rAo}
print(set(25))#error because set cannot take non-sequence elements
print(set())#empty set


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
a . add(True)#{True}
a . add(25)#{True,25}
a . add(10.8)#{True,25,10.8}
a . add(1)#duplicate not allowed
a . add('Hyd')#{True,25,10.8,'Hyd'}
a . add(25)#error because duplicates not allowed
a . add(None)#{True,25,10.8,'Hyd',None}
a . add('Hyd')#duplicates not allowed
a . add(1.0)#{True,25,10.8,'Hyd',None,1.0}
print(a)#{True,25,10.8,'Hyd',None,1.0} in any order
a . add(10 , 20 , 30)#{True,25,10.8,'Hyd',None,1.0,(10 , 20 , 30)}
a . add([10,20,30])#No  becoz  set  can  not  hold  mutable  elements 


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
print(a)#{25 , 10.8 , 'Hyd' , True}
print(id(a))#address of an object a
a . add(tpl)#{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30)}
a . add('Sec')#{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30),'Sec'}
print(a)#{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30),'Sec'}
print(id(a))#same address because set is mutable so set is modified
print(len(a))#6
a . add([100 , 200 , 300])#error because mutable elements are not allowed in the set
a . add(set())#error because nested set is not possible
a . add({ })#error

# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)#{(10 , 20 , 15 , 18)}
print(s)#{(10 , 20 , 15 , 18)}
print(len(s))#1
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)#{10 , 20 , 15, 18}
print(len(s))#4
print(s)#{10 , 20 , 15, 18 }
s . update(25)#error because argument should be sequence


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
print(s)#{10,20,30,40,50,60,70}
print(len(s))#7
s . add(a , b , c)#error
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')#{'R','a','m,'a',' ','R','a','o'}
print(a)#{'R','a','m,'a',' ','R','a','o'}
print(len(a))#8
a . update(3 + 4j , 10.8 , True)#{'R','a','m,'a',' ','R','a','o',3 + 4j , 10.8 , True}
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
b = a . copy()
print(b)#{10 , 20 , 15 , 18}
print(a  is  b)#False
print(a  ==  b)#True
c = a
print(a  is  c)#c={10 , 20 , 15 , 18}


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
print(a)  #
print(a . pop()) #25 
print(a . pop()) #10.8 
print(a . pop())#Hyd  
print(a . pop()) #True 
print(a . pop()) #error because empty set
print(a) #error arguments
b = {10 , 20 , 30 , 40}
print(b . pop(2))# error because no index method in set 


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
print(a) #  {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)#{25 , 10.8, True}  
a . remove('Sec') #error because  invalid element 


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a)#{25 , 10.8 ,True}
a . discard('Sec')
print(a)#
a . remove('Sec')#error because invalid element


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()
print(a)#{}
print(len(a))#0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))#{10 , 20 , 30 , 40,50,60}
print(a | b)#error because |operator does not support set to list
print(b . union(a))#{10 , 20 , 30 , 40,50,60}
print(a + b)#error set operator does not support + operator
#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)#{30 , 40}
print(c)#{30 , 40}
print(type(c))#<class 'set'>
d = a & b#{30 , 40}
print(d)#{30 , 40}
print(type(d))#<class 'set'>
print(c  is  d)#False
print(c  ==  d)#True


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
c = a . difference(b)#{10 , 20}
print(c)#{10 , 20}
print(type(c))#<class 'set'>
d = a - b
print(d)#{10 , 20}
print(type(d))#<class 'set'>
print(c  is  d)#False
print(c  ==  d)#True


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
c = a . symmetric_difference(b)#{10 , 20 , 50 , 60}
print(c)#{10 , 20 , 50 , 60}
print(type(c))#<class 'set'>
d = a ^ b
print(d)#{10 , 20 , 50 , 60}
print(type(d))#<class 'set'>
print(c   is   d)#False
print(c  ==   d)#True


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
print(a)#{0,1,4,9,16,25,36,49,64,81}
print(type(a))#<class 'set'>

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
a=input('Enter a string =')
s=set(a)
b=''.join(s)
print(b)
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a=eval(input('list with duplicates ='))
s=set(a)
b=list(s)
print('list without duplicates =',b)
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
a=eval(input('Enter 1st list ='))
b=eval(input('Enter 2nd list ='))
s1=set(a)
s2=set(b)
c=s1.intersection(s2)
d=list(c)
print(d)

