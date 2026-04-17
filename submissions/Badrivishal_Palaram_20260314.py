#14th HW

#1) Find outputs  
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)#(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))#<class 'tuple'>
a[3] = 'Sec'
a[3 : 6] = 60 , 70 , 80
#
2)Find outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))#(1, 2, 3) address of 3 elements
a += b
print(a , id(a))#(1, 2, 3, 4, 5, 6) address of 6 elements

#3) outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))#(1, 2, 3) address of 3 elements
a = a + b
print(a , id(a))#(1, 2, 3, 4, 5, 6) address of 6 elements

#4) What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   
a = input('Enter  Tuple  :  ')#(10 , 20 , 30 , 40)
print(a)#(10 , 20 , 30 , 40)
print(type(a))#<class 'str'>
b = eval(a)
print(b)#(10, 20, 30, 40)
print(type(b))#<class 'tuple'>
print(len(b))#4

#5) outputs  
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)#(10, [70, 30, 40], 50, 60)
a[1] = [80 , 90 , 100]
print(a)#error because it is not valid

#6) outputs 
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)#[10, (20, 30, 40), 50, 60]
a[1] = [80 , 90]
print(a)#[10, [80, 90], 50, 60]

#7) outputs   
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25, 10.8, 'Hyd', True)
print(type(x))#<class 'tuple'>

#8) outputs   
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#Hyd
print(d)#True
p , q , r =  x
a , b , c , d  , e = x

#9) outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)#25
print(b)#10.8
print(c)#['Hyd', 'Tuple']
print(type(c))#<class 'list'>

#10)  outputs  
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#[10.8, 'Hyd']
print(c)#True

#11) outputs  
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)#Hyd
print(e)#True

#12) outputs 
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#3+4j
print(d)#True
print(_)#3+4j

#13) tuple()  function  demo  program   
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100, 110, 120, 130, 140)
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)#
print(d)#(10, 20, 15, 18)
e = tuple('Vamsi')
print(e)#('V', 'a', 'm', 's', 'i')
print(tuple(25))#Error because not valid
print(tuple())#()


'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple
2) What  does  tuple(No-args)  do  ?  --->  Returns  an  empty  tuple
3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only
4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''

#14) index()  and  count()  methods  demo  program   
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')


#15) How  to  modify  an  element  of  tuple ?   
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35#Error
print(a)#(10, 20, 30, 40, 50)
print(id(a))#address of a
How  to  modify  30  in  tuple  to  35 #b = tuple(list(35)))
print(a)#(10, 20, 35, 40, 50)
print(id(a))#address of new tuple

#16) How  to  delete  an  element  of  tuple ? 
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)
del  a[2]#error
a . pop(2)#error
print(a)
print(id(a))
How  to  remove  30  from  tuple  'a'
print(a)
print(id(a))

#17) Nested   tuple 
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))#<class 'tuple'>
print(len(a))#3
print(a[0])(How  to  print  1st  inner  tuple)
print(a[1])(How  to  print  2nd  inner  tuple)
print(a[2])(How  to  print  3rd  inner  tuple)
print(a[0][1])(How  to  print  20)
print(a[1][2])(How  to  print  50)
print(a[2][3])(How  to  print  90)

#18) outputs  
a = ((10 , 20 , 30),)
print(a[0])(How  to   print  inner  tuple)
print(*a)(How  to   print  inner  tuple  in  another  way)
print(a[0][0])(How   to  print   10)
print(a[0][1])(How   to  print   20)
print#(a[0][2])(How   to  print   30)
b = ((),)
print(a[0])(How  to   print  inner  tuple  of  tuple  'b')
print(*a)(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)


#19) outputs
a = ((10 , 20 , 30))
print(a)#(10, 20 30)
print(*a)#10 20 30
b = (())
print(b)#()
print(*b)#Empty

#20) What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)#{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))#<class 'str'>
b = eval(a)
print(b)#{10, 20, 18, 12, 15}
print(type(b))#<class 'set'>

#21) outputs  
print({(10 , 20 , 30)})#{(10, 20 , 30)}
print({[10 , 20 , 30]})#Error because it is not valid
print({{10 , 20 , 30}})#Error because it is not valid
print({{}})#Error because it is not valid

#22) How  to  print  set  in  differnet ways  
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)# {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
for x in a: How  to  iterate  set  with  for  loop
	print(a)

#23)  outputs  
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{'Hyd', True, 25}
print(len(s))#3
print(type(s))#<class 'set'>

#24) outputs  
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)#Hyd
print(b)#25
print(c)#True
print(d)#10.8

#25) outputs 
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)#'Hyd'
print(b)#{25, True, 10.8}
print(type(b))#<class 'set'>

#26) outputs 
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a)#'Hyd'
print(b)#{25, True}
print(c)#10.8

#27) outputs  
s = {20 , 10 , 20 , 10}
print(s)#{10, 20}
x , y = s
print(x)#10
print(y)#20

#28) set()  function  demo  program  
a = range(100 , 151 , 10)
b = set(a)
print(b)#{130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e)#{'A', 'R', 'a', ' ', 'o', 'r', 'm'}
print(set(25))#Error because it is not valid
print(set())#set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set
2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
3) How  many  arguments  can  set()  function  take ?  --->  Zero  (or) One  but  not  more  than  one
4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''

#29) add()  method  demo  program  
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
print(a)#{'Hyd', True, None, 10.8, 25}
a . add(10 , 20 , 30)#Error bcz it is not valid
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
#30) outputs 
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{'Hyd', 25, 10.8, True}
print(id(a))#address of a
a . add(tpl)
a . add('Sec')
print(a)#{True, 'Hyd', 10.8, 'Sec', (10, 20, 30), 25}
print(id(a))#same address
print(len(a))#6
a . add([100 , 200 , 300])
a . add(set())
a . add({ })

#31)  outputs 
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)#{(10, 20, 15, 18)}
print(len(s))#1

#32) update()  method  demo program  
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))#4
print(s)#{10, 18, 20, 15}
s . update(25)


'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  --->  Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence									                         (Like  extend()  method  of  list  class)
2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only
3) How  many  arguments  can  update()  method  take ?  ---> One  (or)  more
'''

#33)  outputs  
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)#{10, 20, 30, 40, 50, 60, 70}
print(len(s))#7
s . add(a , b , c)

#34) outputs  
a = set()
a . update('Rama Rao')
print(a)#{'a', 'o', 'm', 'R', ' '}
print(len(a))#5
a . update(3 + 4j , 10.8 , True)

35) copy()  method  demo  program  
a = {10 , 20 , 15 , 18}
print(a)#{10, 18, 20, 15}
b = a . copy()
print(b)#{10, 18, 20, 15}
print(a  is  b)#false
print(a  ==  b)#True
c = a
print(a  is  c)#True


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
#36) pop()  method  demo  program  
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #{25 , 10.8 , 'Hyd' , True}
print(a . pop())  #25
print(a . pop())  #10.8
print(a . pop())  #Hyd
print(a . pop())  #True
print(a . pop()) #Error 
print(a) #Error bcz not valid
b = {10 , 20 , 30 , 40}
print(b . pop(2))#Error bcz not valid  


'''
pop()  method
----------------
1) What  does  pop(No-args)  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element
2) What  does  emptyset . pop()  do ?  --->  Throws  error
3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed
4) How  many  arguments  can  pop()  method  take  ?  ---> Zero
'''


#37) remove()  method  demo  program  
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)  #{25, 10.8, True}
a . remove('Sec')   


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set
2) What  does  remove(Invalid-element)  do ?  --->  Throws  error
3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''
#38) discard()  method  demo  program 
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25, 10.8, 'Hyd', True}
a . discard('Hyd')
print(a)#{25, 10.8, True}
a . discard('Sec')
print(a)#{25, 10.8, True}
a . remove('Sec')


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set
2) What  does  discard(Invalid-element)  do ?  --->Nothing
3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''
#39) clear()  method  demo  program (Home  work)

a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()
print(a)#set()
print(len(a))#0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''
#40)  outputs  
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))#{, 10, 50, 20, 60, 30}
print(a | b)#Error because it is not valid
print(b . union(a))#Error because it is not valid
print(a + b)#Error because it is not valid

#41) intersection()   method  demo  program 
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)#{30, 40}
print(type(c))#<class 'set'>
d = a & b
print(d)#{40, 30}
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
#42) difference()   method  demo  program 
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)#{10, 20}
print(type(c))#<class 'set'>
d = a - b
print(d)#{10, 20}
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
#43) symmetric_difference()   method  demo  program  
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10, 50, 20, 60}
print(type(c))#<class 'set'>
d = a ^ b
print(d)#{10, 50, 20, 60}
print(type(d))#<class 'set'>
print(c   is   d)#False
print(c  ==   d)#True


'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
						     without  common  elements		  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set
3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b
4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only
'''

#44) outputs 
a = {x * x  for   x   in   range(10)}
print(a)#{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a))#<class 'set'>

#45) Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''

a = input("Enter list with duplicates:")
b = set()
res = []
for i in a:
    if i not in b:
        res.append(i)
        b.add(i)
print(res)	


#46) Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]
2) Both  input  and  output  are  lists
'''

a = input("enter 1st list:")
b = input("enter 2nd list:")
c = list(set(a) & set(b))
c.sort()
print("common elements between 2 lists:",c)

#47) Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o
2) Both  input  and  output  are  strings
3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)
4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''

a = input("Enter input string:")
b = set()
res = ""
for x in a:
	if x not in b:
		res = res + x
		b.add()
print(res)




