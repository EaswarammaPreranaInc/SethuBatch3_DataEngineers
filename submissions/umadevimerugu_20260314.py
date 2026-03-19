# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a)) #<class 'tuple'>
a[3] = 'Sec' #error
a[3 : 6] = 60 , 70 , 80 #error
##########################################################################################
#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1, 2, 3) address of a
a += b
print(a , id(a)) #(1, 2, 3) another address of a ##########################################################################################
#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1, 2, 3) address of a
a = a + b
print(a , id(a)) #(1, 2, 3, 4, 5, 6) address of a
##########################################################################################
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) #(1,2,3,4,5,6)
print(type(a)) #<class 'str'>
b = eval(a)
print(b) #(1, 2, 3, 4, 5, 6)
print(type(b))#<class 'tuple'>
print(len(b)) #6
##########################################################################################
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)
a[1] = [80 , 90 , 100]
print(a)
##########################################################################################
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a) #(10, [70, 30, 40], 50, 60)
a[1] = [80 , 90]
print(a) #error bcz tuple is immutable
##########################################################################################
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25, 10.8, 'Hyd', True)
print(type(x)) #<class 'tuple'>
##########################################################################################
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25
print(b) #10.8
print(c) #Hyd
print(d) #True
p , q , r =  x  #error
a , b , c , d  , e = x#error
##########################################################################################
# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) #25
print(b) #10.8
print(c) #['Hyd', True]
print(type(c)) #<class 'list'>
##########################################################################################
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) #25
print(b) #[10.8,'Hyd']
print(c)#True
##########################################################################################
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)#Hyd
print(e)#True
##########################################################################################
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#(3+4j)
print(d)#True
print(_)#(3+4j)
##########################################################################################
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b) #(100,110,120,130,140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c) 
print(d) #(10 , 20 , 15, 18)
e = tuple('Vamsi')
print(e) #('V', 'a', 'm', 's', 'i')
print(tuple(25))
print(tuple()) #error


'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  --->  Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''
##########################################################################################
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
output:
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times
##########################################################################################
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

output:
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times
##########################################################################################
#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a) #(10 ,  20 ,  25 ,   40 ,  50)
print(id(a)) #<class 'tuple'>
How  to  modify  30  in  tuple  to  35
a[2]=35
print(a)  #(10 ,  20 ,  35 ,   40 ,  50)
print(id(a))# address of a
##########################################################################################
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a.remove(30) #error
del  a[2] #error
a . pop(2) #error
print(a) #(10 , 20 , 30 , 40 , 50)
print(id(a))#address of a
How  to  remove  30  from  tuple  'a'
b = list(a)
b.remove(30)
a = tuple(b)

print(a) #(10 , 20  , 40 , 50)
print(id(a)) #new address of a
##########################################################################################
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) #( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) #<class 'tuple'>
print(len(a)) #3
print("How  to  print  1st  inner  tuple",a[0])
print("How  to  print  2nd  inner  tuple",a[1])
print("How  to  print  3rd  inner  tuple",a[2])
print("How  to  print  20",a[0][1])
print("How  to  print  50",a[1][2])
print('How  to  print  90',a[2][3])
##########################################################################################
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
##########################################################################################
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) #((10 , 20 , 30))
print(*a) #10 , 20 , 30
b = (())
print(b) #(())
print(*b) #
##########################################################################################
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # <class 'str'>
b = eval(a) #
print(b) #{18, 20, 10, 12, 15}
print(type(b)) # <class 'set'>
##########################################################################################
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) #{(10,20,30)}
print({[10 , 20 , 30]})##error
print({{10 , 20 , 30}})#error
print({{}}) # #error
##########################################################################################
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) #{25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop
for i in a:
    print(i)
##########################################################################################
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) #{'Hyd', True ,25}
print(len(s))#3
print(type(s)) #<lass 'set'>
##########################################################################################
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd') #{25 , 10.8  , True}
print(a)  #{25 , 10.8  , True}
a . remove('Sec')  #error  


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''
##########################################################################################
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd') 
print(a) #{25 , 10.8  , True}
a . discard('Sec') #returns nothing doesn't raises error
print(a) #{25 , 10.8  , True}
a . remove('Sec') #error


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''
##########################################################################################
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
a . clear() 
print(a) #set()
print(len(a)) #0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''
##########################################################################################
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) #{10,20,30,40,50,60}
print(a | b) #error
print(b . union(a)) #error
print(a + b) #error
##########################################################################################
 #  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b) #
print(c) #{30,40}
print(type(c)) #<class 'set'>
d = a & b 
print(d)#{30,40}
print(type(d)) #<class 'set'>
print(c  is  d) #Flse
print(c  ==  d) #True


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
##########################################################################################
 # difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) #{10,20}
print(type(c)) #<class 'set'>
d = a - b 
print(d) #{10,20}
print(type(d)) #<class 'set'>
print(c  is  d) #False
print(c  ==  d) #True


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->  
										Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''
##########################################################################################
# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) #{13,20,50,60}
print(type(c)) #<class 'set'>
d = a ^ b 
print(d) #{13,20,50,60}
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

3) What  is  the  alternative  to  a . symmetric_…
##########################################################################################
 # Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) #{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a)) #<class 'set'>
##########################################################################################
'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o
s = input()
a = set(s)          # convert string → set
b = ''.join(a)      # convert set → string
print(b)

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
a=input()
b=set(a)
print(b)

    How  to  convert  set  to  string ?  --->  '' . join(set)
a=input()
b="".join(a)
print(b)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''
##########################################################################################
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a=eval(input())
print(list(set(a)))
##########################################################################################
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
a=eval(input())
b=eval(input())
c=set(a).intersection(set(b))
print(list(c))
