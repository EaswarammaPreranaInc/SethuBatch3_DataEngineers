# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)---> 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(type(a))---> <class string>
a[3] = 'Sec'--->  25 , 10.8 , 'Sec' , 'Hyd' , True , None , 'Hyd' , 25
a[3 : 6] = 60 , 70 , 80

#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))---> (1,2,3,(may be 1000))
a += b
print(a , id(a))---> (1,2,3,4,5,6, (may be 1000))

#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))---> (1,2,3, (may be 1000))
a = a + b
print(a , id(a))---> (1,2,3,4,5,6, (may be 1000))


#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)--->[10,20,30,40]
print(type(a))---><class list>
b = eval(a)--->[10,20,30,40]
print(b)--->[10,20,30,40]
print(type(b))---><class list>
print(len(b))--> 4

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)--> (10 , [[70],20 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]
print(a)--> (10 , [[70],[80 , 90 , 100],20 , 30 , 40] , 50 , 60)

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)--> (10 , ((70),20 , 30 , 40) , 50 , 60)
a[1] = [80 , 90]
print(a)--> (10 , ((70)[80,90],20 , 30 , 40) , 50 , 60)


# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)--->(25,10.8,'Hyd', True)
print(type(x))---> <class string>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)-->25
print(b)--->10.8
print(c)--->'Hyd'
print(d)--->True
p , q , r =  x
a , b , c , d  , e = x--> (25 , 10.8 , 'Hyd' , True)

# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)-->25
print(b)-->10.8
print(c)--->'Hyd'
print(type(c))--><class tuple>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)--> 25
print(b)---> 10.8
print(c)---> 'Hyd'

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)--->25
print(b)--->10.8
print(c)--->'Hyd'

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)--->25
print(b)--->10.8
print(c)--->'Hyd'
print(d)--->True
print(e)--->

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)-->25
print(b)--->10.8
print(_)--->'Hyd'
print(d)--->True
print(_)--->3+4j
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)--->(100,120,120,130,140,150)
print(type(b))--->Tuple
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)--->(10,20,15,18)
e = tuple('Vamsi')
print(e)--->('Vamsi')
print(tuple(25))--->(25)
print(tuple())--->()


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
print(a)-->(10,20,30,40,50)
print(id(a))---><class int>
How  to  modify  30  in  tuple  to  35
print(a)-->a[2]=35
print(id(a))---><class int>

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)
del  a[2]
a . pop(2)
print(a)--->(10,20,50)
print(id(a))---><class tuple>
How  to  remove  30  from  tuple  'a'l
print(a)--->a.remove[30]
print(id(a))---><class tuple>

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)--->( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))---><class str>
print(len(a))---> len(3)
print(How  to  print  1st  inner  tuple)---> [:1]
print(How  to  print  2nd  inner  tuple)--->[2:3]
print(How  to  print  3rd  inner  tuple)--->[-1:]
print(How  to  print  20)--->
print(How  to  print  50)
print(How  to  print  90)


# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)--->[:1]
print(How  to   print  inner  tuple  in  another  way)
print(How   to  print   10)
print(How   to  print   20)
print(How   to  print   30)
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)--->((10,20,30))
print(*a)--->(10,20,30)
b = (())
print(b)--->(())
print(*b)--->()

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)--->{10 , 15 , 18 , 20 , 12 }
print(type(a))---><class set>
b = eval(a)
print(b)--->(10 , 20 , 15 , 18 , 20 , 12 , 18)
print(type(b))---><class set>

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})--->(10 , 20 , 30)
print({[10 , 20 , 30]})--->(10 , 20 , 30)
print({{10 , 20 , 30}})--->{10 , 20 , 30}
print({{}})--->{}

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')---> print(a)
print(a)---> {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')--->
How  to  iterate  set  with  for  loop

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)--->{'Hyd',25,True}
print(len(s))--->len(3)
print(type(s))---><class set>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)---> {'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)--->{'Hyd'}
print(b)--->{25}
print(c)--->{True}
print(d)--->{10.8}

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) --->{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)-->{'Hyd'}
print(b)--->(25)
print(type(b))--><class str>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)--->{'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a)--->{'Hyd'}
print(b)--->{25}
print(c)--->{True}


# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)-->{10,20}
x , y = s
print(x)-->10
print(y)-->20


# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)--->{100,151,10}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)-->{10,20,15,12,18}
e = set('Rama  rAo')
print(e)--->{R,a,m, r,A,o}
print(set(25))-->{25}
print(set())--->{}


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
a . add(True)--->{True}
a . add(25)--->{True,25}
a . add(10.8)--->{True,25,10.8}
a . add(1)--->{True,25,10.8}
a . add('Hyd')--->{True,25,10.8,'Hyd'}
a . add(25)--->{True,25,10.8,'Hyd'}
a . add(None)--->{True,25,10.8,'Hyd',None}
a . add('Hyd')--->{True,25,10.8,'Hyd',None}
a . add(1.0)--->{True,25,10.8,'Hyd',None}
print(a)--->{True,25,10.8,'Hyd',None}
a . add(10 , 20 , 30)--->Error
a . add([10,20,30])--->Error

'''
add()   method
-----------------
1) What  does  add(x)  do ?  --->  Inserts   'x'  any  where  in  the  set  becoz  set  is  unordered

2) How  many  arguments  can  add()  method  take ?  --->  Single

3) Is  set . add(mutable-object)  valid ? --->  No  becoz  set  can  not  hold  mutable  element

4) In  other  words,  argument  of  add()  method  should  be  immutable  object  only

5) What  does  set .  add(sequence)  do  ?  --->Inserts  sequence  any  where  in  the  set  but  not  elements  of  sequence
(Like  append()  method  of  list  class)
'''

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)--->{25 , 10.8 , 'Hyd' , True}
print(id(a))---> may be 1000
a . add(tpl)--->{25 , 10.8 ,(10 , 20 , 30), 'Hyd' , True}
a . add('Sec')--->{25 ,'Sec', 10.8 ,(10 , 20 , 30), 'Hyd' , True}
print(a)--->{25 ,'Sec', 10.8 ,(10 , 20 , 30), 'Hyd' , True}
print(id(a))-->may be 10000
print(len(a))--->len(6)
a . add([100 , 200 , 300])--->{25 ,'Sec', 10.8 ,(10 , 20 , 30), 'Hyd' ,[100 , 200 , 300], True}
a . add(set())--->{25 ,'Sec', 10.8 ,(10 , 20 , 30), 'Hyd' ,[100 , 200 , 300], True}
a . add({ })--->{25 ,'Sec', 10.8 ,(10 , 20 , 30), 'Hyd' ,[100 , 200 , 300], True}


# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)--->{10 , 20 , 15 , 18}
print(s)--->{10 , 20 , 15 , 18}
print(len(s))--->4

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))--->6
print(s)--->{10 , 20 , 15, 18 , }
s . update(25)--->{10 , 20 , 15, 18  , 25}


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
s . update(a , b , c)--->{10 , 20 , 30, 40 , 50 , 60 , 70}
print(s)--->{10 , 20 , 30, 40 , 50 , 60 , 70}
print(len(s))--->len(7)
s . add(a , b , c)--->{10 , 20 , 30, 40 , 50 , 60 , 70}

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)--->{R,a,m,a, , R,a,o}
print(len(a))--->len(8)
a . update(3 + 4j , 10.8 , True)--->{R,a,m,a, ,3 + 4j , 10.8 , True , R,a,o}

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)---> {10 , 20 , 15 , 18}
b = a . copy()
print(b)---> {10 , 20 , 15 , 18}
print(a  is  b)---> True
print(a  ==  b)--->True
c = a
print(a  is  c)---> {10 , 20 , 15 , 18}


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
print(a)--->{25 , 10.8 , 'Hyd' , True}
print(a . pop()) ---> { 10.8 , 'Hyd' , True}
print(a . pop())  ---> { 'Hyd' , True}
print(a . pop())  ---> {True}
print(a . pop())  ---> { }
print(a . pop()) ---> { }
print(a) ---> { }
b = {10 , 20 , 30 , 40}
print(b . pop(2))  --->({30, 40})



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
print(a)  --->{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a) --->{25 , 10.8  , True}
a . remove('Sec')  --->{25 , 10.8  , True} 


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
print(a)--->{10 , 20 , 15 , 18}
a . clear()
print(a)--->{}
print(len(a))--->0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))--->{10 , 20 , 30 , 40, 50, 60}
print(a | b)--->{10 , 20 , 30 , 40, 50, 60}
print(b . union(a))--->{10 , 20 , 30 , 40, 50, 60}
print(a + b)---> Error

#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)--->{30,40}
print(type(c))---><class str>
d = a & b--->
print(d)---> {30,40}
print(type(d))---><class str>
print(c  is  d)---> True
print(c  ==  d)---> True


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
print(c)--->{50,60}
print(type(c))---><class str>
d = a - b
print(d)--->{50,60}
print(type(d))---><class str>
print(c  is  d)---> True
print(c  ==  d)---> True


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
print(c)--->{10 , 20 , 30 , 40,50,60}
print(type(c))---><class str>
d = a ^ b
print(d)--->{10 , 20 , 30 , 40,50,60}
print(type(d))---><class str>
print(c   is   d)--->True
print(c  ==   d)--->True


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
print(a)---> {1,2,6,9,16,25,36,49,64,81,100}
print(type(a))---><class str>

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

try:
x = input('enter any string: ')
y = ' '
for ch in x:
    if ch not in y:
        y += ch
print(y)
except:
print('Enter the string')

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
lst = [False , 25 , 10.8 , 1 , 25 , 0 , 'Hyd' , 10.8 , 1.0 , None , 'Sec' , 'Hyd' , True]

result = []
seen = set()

for x in lst:
    if x not in seen:
        result.append(x)
        seen.add(x)

print("Output:", result)



'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 70, 80, 20]
common = list(set(list1) & set(list2))
common.sort()

print("Common elements :", common)





















