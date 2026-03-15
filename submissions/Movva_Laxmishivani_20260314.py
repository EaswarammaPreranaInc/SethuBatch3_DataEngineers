# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) # (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a)) # <class 'tuple'>
a[3] = 'Sec' # ERROR because we can't insert element into tuple
a[3 : 6] = 60 , 70 , 80 # ERROR because we can't insert element into tuple

 #  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # (1, 2, 3) address of tuple a
a += b
print(a , id(a)) # (1, 2, 3, 4, 5, 6) address of new tuple a

 #  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # (1, 2, 3) address of tuple a
a = a + b
print(a , id(a)) # (1, 2, 3, 4, 5, 6) address of new tuple a

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) # (10 , 20 , 30 , 40)
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # (10, 20, 30, 40)
print(type(b)) # <class 'tuple'>
print(len(b)) # 4

 # Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) # (10, [70, 30, 40], 50, 60)
a[1] = [80 , 90 , 100]
print(a) # ERROR because tuple doesn't allow another sequence insertion

 # Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a) #  ERROR because tuple doesn't allow another sequence insertion
a[1] = [80 , 90]
print(a) #  ERROR because tuple doesn't allow another sequence insertion

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) # (25, 10.8, 'Hyd', True)
print(type(x)) # <class 'tuple'>

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) # 25
print(b) # 10.8
print(c) # Hyd
print(d) # True
p , q , r =  x # ERROR because less arguments to assign
a , b , c , d  , e = x # ERROR because more arguments to assign

 # Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) # 25
print(b) # 10.8
print(c) #['Hyd',True]
print(type(c)) # <class 'list'>

 # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # 25
print(b) # [10.8, 'Hyd']
print(c) # True

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)
print(b)
print(c)
print(d)
print(e) # ---> ERROR because tpl has less no.of values to unpack

 # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) # 25
print(b) # 10.8
print(_) # 3+4j
print(d) # True
print(_) # 3+4j

 # tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b) # (100, 110, 120, 130, 140)
print(type(b)) # <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) # (10, 20, 15, 18)
e = tuple('Vamsi')
print(e) # ('V', 'a', 'm', 's', 'i')
print(tuple(25)) # ERROR because aruguments in tuple should be a sequence
print(tuple()) # ()

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

Answer:               
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15 is found 3 times
'''
 #  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35 # ERROR
print(a) # (10, 20, 30, 40, 50)
print(id(a)) # address of tuple a
b = list(a)
b[2] = 35
a = tuple(b)
#How  to  modify  30  in  tuple  to  35
print(a) # (10, 20, 35, 40, 50)
print(id(a)) # address of new tuple a

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) # ERROR because no method called remove()  in tuple class
del  a[2] # ERROR because del operator can't be used with tuple
a . pop(2) # ERROR because no method called pop()  in tuple class
print(a) # (10, 20,30, 40, 50)
print(id(a)) # address of tuple a
b = list(a)
b.remove(30)
a = tuple(b)
#How  to  remove  30  from  tuple  'a'
print(a) # (10, 20, 40, 50)
print(id(a)) # address of new tuple a

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(a[0]) # How  to  print  1st  inner  tuple)
print(a[1]) # How  to  print  2nd  inner  tuple)
print(a[2]) # How  to  print  3rd  inner  tuple)
print(a[0][1]) # How  to  print  20)
print(a[1][2]) # How  to  print  50)
print(a[2][3]) # How  to  print  90)

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0]) # How  to   print  inner  tuple)
print(*a) # How  to   print  inner  tuple  in  another  way)
print(a[0][0]) # How   to  print   10)
print(a[0][1])) # How   to  print   20)
print(a[0][2]) # How   to  print   30)
b = ((),)
print(b[0]) # How  to   print  inner  tuple  of  tuple  'b')
print(*b) # How  to   print  inner  tuple  of  tuple  'b'  in  another  way)

 #  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # ((10, 20, 30))
print(*a) # 10 20 30
b = (())
print(b) # (())
print(*b) # ()

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # {10, 12, 15, 18, 20}
print(type(b)) # <class 'set'>

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10, 20, 30)}
print({[10 , 20 , 30]}) # ERROR because set can have only immutable objects
print({{10 , 20 , 30}}) # ERROR because set can have only immutable objects
print({{}}) # ERROR because set can have only immutable objects

 # How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
#print('set  with  print  function')
print(a)# {25, True, 'Hyd', 10.8}
#print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop
for x in a:
    print(x)

 # Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {25, 'Hyd', True}
print(len(s)) # 3
print(type(s)) # <class 'set'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, True, 10.8, 'Hyd'}
a , b , c , d = s
print(a) # 25
print(b) # True
print(c) # 10.8
print(d) # Hyd

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  # {25, True, 10.8, 'Hyd'}
a , *b = s
print(a) # 25
print(b) # [True, 10.8, 'Hyd']
print(type(b)) # <class 'list'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, True, 10.8, 'Hyd'}
a , *b , c = s
print(a) # 25
print(b) # [True, 10.8]
print(c) # Hyd

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {10, 20}
x , y = s
print(x) # 10
print(y) # 20

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) # {130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10, 12, 15, 18, 20, 50}
e = set('Rama  rAo')
print(e) # {'R', 'a', ' ', 'o', 'm'}
print(set(25)) # ERROR because set can have only immutable sequences
print(set()) # set()

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
print(a) # {True, 25, 10.8, 'Hyd', None}
a . add(10 , 20 , 30) # ERROR because add method takes only 1 argument
a . add([10,20,30]) # ERROR because add method takes only 1 argument

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25, 10.8, 'Hyd', True}
print(id(a)) # address of tuple a
a . add(tpl)
a . add('Sec')
print(a) # {True, 10.8, 25, 'Hyd', (10, 20, 30), 'Sec'}
print(id(a)) # same address as tuple a
print(len(a)) # 6
a . add([100 , 200 , 300]) # ERROR because set can have only immutable objects
a . add(set()) #  ERROR because set can have only immutable objects
a . add({ }) # ERROR because set can have only immutable objects

 # Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10, 20, 15, 18)}
print(len(s)) # 1

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s) # {10, 18, 20, 15}
s . update(25) # ERROR because set can have only immutable objects

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) # {10, 20, 30, 40, 50, 60, 70}
print(len(s)) # 7
s . add(a , b , c) # ERROR because add() takes only 1 argument

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) # {'R', 'a', 'm', ' ', 'o'}
print(len(a)) # 5
a . update(3 + 4j , 10.8 , True) # ERROR because we can't use complex object

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10, 20, 18, 15}
b = a . copy()
print(b) # {10, 20, 18, 15}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is  c) # True

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
print(a . pop())  # 25
print(a . pop())  # 10.8
print(a . pop())  # Hyd
print(a . pop())  # True
print(a . pop()) # ERROR because pop() can't be used on empty set
print(a) #{ }
b = {10 , 20 , 30 , 40}
print(b . pop(2))  # ERROR because pop() takes no arguments

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25, 10.8, 'Hyd', True}
a . remove('Hyd')
print(a)  # {25, 10.8, True}
a . remove('Sec')   # ERROR because Sec is not in set

 # discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
a . discard('Hyd')
print(a) # {25, 10.8, True}
a . discard('Sec')
print(a) # {25, 10.8, True}
a . remove('Sec') # ERROR because Sec is not in set

 # clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10, 20, 18, 15}
a . clear()
print(a) # set()
print(len(a)) # 0

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {10, 20, 30, 40, 50, 60}
print(a | b) # ERROR pipe operator works between set and set only
print(b . union(a)) # ERROR because list class don't have union() method
print(a + b) # ERROR plus operator works between set and set only

#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) # {40, 30}
print(type(c)) # <class 'set'>
d = a & b
print(d) # {40, 30}
print(type(d)) # <class 'set'>
print(c  is  d) # False
print(c  ==  d) # True

 # difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) # {10, 20}
print(type(c)) # <class 'set'>
d = a - b
print(d) # {10, 20}
print(type(d)) # <class 'set'>
print(c  is  d) # False
print(c  ==  d) # True


# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) # {10, 20, 50, 60}
print(type(c)) # <class 'set'>
d = a ^ b
print(d) # {10, 20, 50, 60}
print(type(d)) # <class 'set'>
print(c   is   d) # False
print(c  ==   d) # True


 # Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a)) #<class 'set'>

'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o
2) Both  input  and  output  are  strings
3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)
4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'

Sample output:
Enter input string : MISSISIPI
String without duplicates : MSIP
Press any key to continue . . .

a = input('Enter input string : ')
b = set(a)          
c = ''.join(b)      
print('String without duplicates :', c)


Write  a  program  to  remove  duplicate  elements  of   list  using  set
1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
2) Both  input  and  output  are  lists

Sample output:
Enter list with duplicates : [False , 25 , 10.8 , 1 , 25 , 0 , 'Hyd' , 10.8 , 1.0 , None , 'Sec' , 'Hyd' , True ]
List without duplicates : [False, 1, None, 'Sec', 10.8, 'Hyd', 25]
Press any key to continue . . .

a = eval(input('Enter list with duplicates : '))
b = list(set(a))    
print('List without duplicates :', b)

Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]
2) Both  input  and  output  are  lists

Sample output:
Enter 1st list : [10,20,30,40,50,60]
Enter 2nd list : [30,40,70,80,20]
Common elements between the 2 lists : [40, 20, 30]
Press any key to continue . . .

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = list(set(a) & set(b))
print('Common elements between the 2 lists :', c)
'''