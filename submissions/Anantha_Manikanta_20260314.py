'''
1) # Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)  # (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))  # class <tuple>
a[3] = 'Sec'  # Error because tuples are immutable
a[3 : 6] = 60 , 70 , 80  # Error because tuples are immutable
'''
'''
2) #  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))  # (1, 2, 3)  1000
a += b
print(a , id(a))   # (1,2,3,4,5,6)  2000
'''
'''
3) #  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))  # (1, 2, 3)  1000
a = a + b
print(a , id(a))   # (1,2,3,4,5,6)  2000
'''
'''
4) #  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)  # (10 , 20 , 30 , 40)
print(type(a))  # class <string>
b = eval(a)
print(b)  # (10, 20, 30, 40)
print(type(b))  # class <tuple>
print(len(b))  # 4
'''
'''
5) # Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)  # (10, [70, 30, 40], 50, 60)
a[1] = [80 , 90 , 100]
print(a)  # Error because tuple does not support item assignment
'''
'''
6) # Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)  # Error because tuple does not support item assignment
a[1] = [80 , 90]
print(a)  # [10, [80, 90], 50, 60]
'''
'''
7) # Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)  # (25, 10.8, 'Hyd', True)
print(type(x))  # class <tuple>
'''
'''
8) # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)  # 25
print(b)  # Hyd
print(c)  # 10.8
print(d)  # True
p , q , r =  x  # Error because x has 4 elements and objects are only 3
a , b , c , d  , e = x  #  Error because x has 4 elements and objects are 5
'''
'''
9) # Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)  # 25
print(b)  # 10.8
print(c)  # ['Hyd', True]
print(type(c))  # <class 'list'>
'''
'''
10) # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)  # 25
print(b)  # [10.8, 'Hyd']
print(c)  # True
'''
'''
11) # Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)
print(b)
print(c)
print(d)
print(e)  # Error because objects are more
'''
'''
12) # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)  # 25
print(b)  # 10.8
print(_)  # 3+4j
print(d)  # True
print(_)  # 3+4j
'''
'''
13) # tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)  # (100, 110, 120, 130, 140)
print(type(b))  # class <tuple>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)  # (10, 20, 15, 18)
e = tuple('Vamsi')
print(e)  # ('V', 'a', 'm', 's', 'i')
print(tuple(25))  # Error because 25 is integer
print(tuple())  #()
'''
'''
14) #index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')  # 15 is found at index :  2 <next line> 15 is found at index :  5 <next line> 15 is found at index :  8 <next line> 15 is found 3 times
'''
'''
15) #  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a)  # (10, 20, 30, 40, 50)
print(id(a))  # 1000
How  to  modify  30  in  tuple  to  35
print(a)  # a = a[0:2] + (35,) + a[3:]
print(id(a))  # 1000
'''
'''
16) # How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)  # Error because tuple has no remove method
del  a[2]  # Error
a . pop(2)  # Error
print(a)  # (10 , 20 , 30 , 40 , 50)
print(id(a))  # 1000
How  to  remove  30  from  tuple  'a'
print(a)  # a = a[:2] + a[3:]
print(id(a))  # 1000
'''
'''
17) #  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)  # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))  # class <tuple>
print(len(a))  # 3
print(How  to  print  1st  inner  tuple)  # print(a[0])
print(How  to  print  2nd  inner  tuple)  # print(a[1])
print(How  to  print  3rd  inner  tuple)  # print(a[2])
print(How  to  print  20)  # print(a[0][1])
print(How  to  print  50)  # print(a[1][2])
print(How  to  print  90)  # print(a[2][3])
'''
'''
18) # Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)  # print(a[0])
print(How  to   print  inner  tuple  in  another  way)  # print(*a)
print(How   to  print   10)  # print(a[0][0]
print(How   to  print   20)  # print(a[0][1]
print(How   to  print   30)  # print(a[0][2]
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')  # print(b[0])
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)  # print(*a)
'''
'''
19) #  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)  # ((10 , 20 , 30))
print(*a)  # 10 20 30
b = (())
print(b)  # ()
print(*b) # ()
'''
'''
20) # What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)  # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))  # class <str>
b = eval(a)
print(b)  # {10, 12, 15, 18, 20}
print(type(b))  # class <set>
'''
'''
21) #  Find  outputs  (Home  work)
print({(10 , 20 , 30)})  # {(10, 20, 30)}
print({[10 , 20 , 30]})  # Error
print({{10 , 20 , 30}})  # Error
print({{}})  # Error
'''
'''
22) # How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')  # set with print function
print(a)  # {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')  # Iterate elements of set with for loop
How  to  iterate  set  with  for  loop  # for x in a:    print(x)
'''
'''
23) # Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)  # {'Hyd', True, 25}
print(len(s))  # 3
print(type(s))  # class <set>
'''
'''
24) # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  # {True, 25, 10.8, 'Hyd'}
a , b , c , d = s
print(a)  True
print(b)  # 25
print(c)  # 10.8
print(d)  # Hyd
'''
'''
25) # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  # {True, 25, 10.8, 'Hyd'}
a , *b = s
print(a)  # True
print(b)  # [25, 10.8, 'Hyd']
print(type(b))  # class <list>
'''
'''
26) # Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)  # {10, 20}
x , y = s
print(x)  # 10
print(y)  # 20
'''
'''
27) # set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)  # {100, 130, 140, 110, 120, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)  # {10, 12, 15, 18, 20, 50}
e = set('Rama  rAo')
print(e)  # {'R', 'a', 'm', ' ', 'r', 'A', 'o'}
print(set(25))  # Error becauase 25 is integer
print(set())  # set()
'''
'''
28) # add()  method  demo  program  (Home  work)
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
print(a)  # {True, 25, 10.8, 'Hyd', None}
a . add(10 , 20 , 30)  # Error because add takes only 1 argument
a . add([10,20,30])  # Error because set cannot contain list
'''
'''
29) # Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)  # {25, 10.8, 'Hyd', True}
print(id(a))  # 1000
a . add(tpl)
a . add('Sec')
print(a)  # {25, 10.8, 'Hyd', True, (10, 20, 30), 'Sec'}
print(id(a)) # 1000
print(len(a))  # 6
a . add([100 , 200 , 300])  # Error because set cannot have list
a . add(set())  # Error because set cannot have set
a . add({ })  # Error because set cannot have dict
'''
'''
30) # Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)  # {(10, 20, 15, 18)}
print(len(s))  # 1
'''
'''
31) # update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))  # 4
print(s)  # {10, 20, 18, 15}
s . update(25)  # Error because 25 is integer
'''
'''
32) # Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)  # {10, 20, 30, 40, 50, 60, 70}
print(len(s))  # 7
s . add(a , b , c)  # Error because add can take only 1 argument
'''
'''
33) # Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)  # {'R', 'a', 'm', ' ', 'o'}
print(len(a))  # 5 
a . update(3 + 4j , 10.8 , True)  # Error because set cannot have complex number
'''
'''
34) # copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)  {10, 18, 20, 15}
b = a . copy()
print(b)  # {10, 18, 20, 15}
print(a  is  b)  # False
print(a  ==  b)  # True
c = a
print(a  is  c)  # True
'''
'''
35) # pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {True, 25, 10.8, 'Hyd'}
print(a . pop())  # True
print(a . pop())  # 25
print(a . pop())  # 10.8
print(a . pop())  # Hyd
print(a . pop())  # Error because there is nothing left in set to pop
print(a) # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))  # Error because pop dont take any argument
'''
'''
36) # remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)  # {True, 25, 10.8}
a . remove('Sec')  # Error because Sec is not in the list
'''
'''
37) # discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {True, 25, 10.8, 'Hyd'}
a . discard('Hyd')
print(a)  # {True, 25, 10.8}
a . discard('Sec')
print(a)  # {True, 25, 10.8
a . remove('Sec' # Error because if we use remove method and if the element that we want to remove is not in the set it raises error and discard method just ignores it
'''
'''
38) # clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)  # {10, 20, 18, 15}
a . clear()
print(a)  # set()
print(len(a))  # 0
'''
'''
39) # Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))  # {10, 20, 30, 40, 50, 60}
print(a | b)  # Error because pipe operator is for only set and set but here we have set and list
print(b . union(a))  # Error because list dont have union method
print(a + b)  # Error + operator is not for set and list
'''
'''
40) #  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)  # {40, 30}
print(type(c))  # class <set>
d = a & b
print(d)  # {40, 30}
print(type(d))  # class <set>
print(c  is  d)  # Flase
print(c  ==  d)  # True
'''
'''
41) # difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)  # {10, 20} 
print(type(c))  # class <set>
d = a - b
print(d)  # {10, 20} 
print(type(d))  class <set>
print(c  is  d)  # Flase
print(c  ==  d)  # True
'''
'''
42) # symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)  # {10, 20, 50, 60}
print(type(c))  # class <set>
d = a ^ b
print(d)  # {10, 20, 50, 60}
print(type(d))  # class <set>
print(c   is   d)  # False
print(c  ==   d)  # True
'''
'''
43) # Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)  # {0, 1, 4, 36, 9, 16, 49, 64, 81, 25}
print(type(a))  # class <set>
'''
'''
44) (Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o
2) Both  input  and  output  are  strings
3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)
4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''
s = input("Enter input string : ")
a = set(s)          # convert string → set (removes duplicates)
b = ''.join(a)      # convert set → string
print("String without duplicates :", b)

'''
45) Write  a  program  to  remove  duplicate  elements  of   list  using  set
1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
2) Both  input  and  output  are  lists
'''
a = eval(input("Enter list with duplicates : "))
b = list(set(a))      # convert list → set (remove duplicates) → list
print("List without duplicates :", b)

'''
46) Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]
2) Both  input  and  output  are  lists
'''
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c = list(set(a) & set(b))
print("Common elements between the 2 lists :", c)