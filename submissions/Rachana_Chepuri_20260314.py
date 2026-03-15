'''Find  outputs   (Home  work)'''
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)#(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))#class 'tuple'
a[3] = 'Sec'#Error --because tuple is immutable
a[3 : 6] = 60 , 70 , 80#Error--because tuple elements cannot modified
''' Find  outputs '''
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))#(1,2,3),adress of an tuple with 3 elements
a += b
print(a , id(a))#(1,2,3,4,5,6)same address
''' Find  outputs'''
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))#(1 , 2 , 3) address of an tuple with 3 element
a = a + b
print(a , id(a))#(1,2,3,4,5,6)address different
'''What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)'''
a = input('Enter  Tuple  :  ')#(10 , 20 , 30 , 40)
print(a)#(10 , 20 , 30 , 40)
print(type(a))#<class 'str'>
b = eval(a)
print(b)#(10 , 20 , 30 , 40)
print(type(b))#<class 'Tuple'>
print(len(b))#4
'''Find  outputs  (Home  work)'''
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70#--list is mutable so updated
print(a)#(10 , [0, 20 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]#Error--tuple is immutable
print(a)#(10 , [0, 20 , 30 , 40] , 50 , 60)
'''Find  outputs  (Home  work)'''
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70#--not modified it is tuple
print(a)#[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)#[10 , (20 , 30 , 40) , 50 , 60]
'''Find  outputs   (Home  work)'''
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25,10.8,'Hyd',True)
print(type(x))#<class 'tuple'>
'''Find  outputs   (Home  work)'''
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#'Hyd'
print(d)#True
p , q , r =  x#error--left side !=right side
a , b , c , d  , e = x#error--left side !=right side
'''Find outputs'''
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)#25
print(b)#10.8
print(c)#[]'Hyd' , True]
print(type(c))#<class 'list'>
'''Find  outputs   (Home  work)'''
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#[10.8 , 'Hyd']
print(c)#True
'''Find  outputs   (Home  work)'''
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)#'Hyd'
print(e)#True
'''Find  outputs   (Home  work)'''
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#3+4j
print(d)#True
print(_)#3+4j
''' tuple()  function  demo  program   (Home  work)'''
a = range(100 , 150 , 10)#100,110,120,130,140
b = tuple(a)#(100,110,120,130,140)
print(b)#(100,110,120,130,140)
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)#(10 , 20 , 15, 18)
print(d)#(10 , 20 , 15, 18)
e = tuple('Vamsi')
print(e)#('V','a','m','s','i')
print(tuple(25))#error---bcoz arg is non seq
print(tuple())#empty
'''index()  and  count()  methods  demo  program   (Home  work)'''
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1   2     3    4    5     6    7   8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)#2,5,8
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')#3times
''' How  to  modify  an  element  of  tuple ?    (Home  work)'''
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1    2       3      4
a[2] = 35
print(a)#(10 ,  20 ,  30 ,   40 ,  50)
print(id(a))#adress of tuple with 6 elements
How  to  modify  30  in  tuple  to  35#tuple(list(a[2]=35))
print(a)#(10 ,  20 ,  35 ,   40 ,  50)
print(id(a))#same address
'''How  to  delete  an  element  of  tuple ?   (Home  work)'''
a  = 10 , 20 , 30 , 40 , 50
#    0     1    2    3    4
a . remove(30)#error
del  a[2]#a[:2]+a[3:]
a . pop(2)#error--pop method not applicable
print(a)# (10 , 20 , 40 , 50)
print(id(a))#address of tuple obj
How  to  remove  30  from  tuple  'a'#a[:2]+a[3:]
print(a)#(10 , 20 , 40 , 50)
print(id(a))#same address
'''Nested   tuple  (Home  work)'''
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))#<class 'list'>
print(len(a))#3
print(How  to  print  1st  inner  tuple)#a[0]
print(How  to  print  2nd  inner  tuple)#a[1]
print(How  to  print  3rd  inner  tuple)#a[2]
print(How  to  print  20)#a[0][1]
print(How  to  print  50)#a[1][2]
print(How  to  print  90)#a[2][3]
''' Find  outputs  (Home  work)'''
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)#a[0]
print(How  to   print  inner  tuple  in  another  way)#a[:]
print(How   to  print   10)#a[0][0]
print(How   to  print   20)#a[0][1]
print(How   to  print   30)#a[0][2]
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')#a[0]
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)#a[:]
'''Find  outputs (Home  work)'''
a = ((10 , 20 , 30))
print(a)#(10 , 20 , 30)
print(*a)#10 , 20 , 30
b = (())
print(b)#(,)
print(*b)#()
'''What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}'''
a = input('Enter  Set  :  ')
print(a)#"{10 , 20 , 15 , 18 , 20 , 12 , 18}"
print(type(a))#<class 'str'>
b = eval(a)
print(b)#{10 , 20 , 15 , 12 , 18}
print(type(b))#<class 'set'>
'''Find  outputs  (Home  work)'''
print({(10 , 20 , 30)})#{(10 , 20 , 30)}
print({[10 , 20 , 30]})#Error
print({{10 , 20 , 30}})#Error--a set cannot be in another set
print({{}})#Empty dictionary
'''How  to  print  set  in  differnet ways  (Home  work)'''
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')#set  with  print  function
print(a)#{25 , True , 'Hyd' , 10.8} in any order
print('Iterate  elements  of  set  with  for  loop')#Iterate  elements  of  set  with  for  loop
How  to  iterate  set  with  for  loop
    #25
    #True
    #'Hyd'
    #10.8
'''Find  outputs  (Home  work)'''
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{'Hyd',True,25}
print(len(s))#3
print(type(s))#<class 'set'>
'''Find  outputs  (Home  work)'''
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s#True
print(a)#'Hyd'
print(b)#25
print(c)#True
print(d)#10.8
'''Find  outputs  (Home  work)'''
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 } in any order
a , *b = s#
print(a)#'Hyd'
print(b)#[25,  True,  10.8]
print(type(b))#class 'list'>
'''Find  outputs  (Home  work)'''
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }any order
a , *b , c = s#True
print(a)#'Hyd'
print(b)#[25,  True]
print(c)#10.8
'''Find  outputs  (Home  work)'''
s = {20 , 10 , 20 , 10}
print(s)#{20 , 10 }any order
x , y = s#True
print(x)#20
print(y)#10
'''set()  function  demo  program  (Home  work)'''
a = range(100 , 151 , 10)#100,110,120,130,140,150
b = set(a)#100,110,120,130,140,150
print(b)#100,110,120,130,140,150
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10,20,15,18,50,12}aany order
e = set('Rama  rAo')
print(e)#{Ram o}
print(set(25))#Error--argument should be sequence
print(set())#empty set
'''add()  method  demo  program  (Home  work)'''
a = set()#{}
a . add(True)#{True}
a . add(25)#{True,25}
a . add(10.8)#{True,25,10.8}
a . add(1)#duplicate not allowed
a . add('Hyd')#{True,25,10.8,'Hyd'}
a . add(25)#duplicate not allowed
a . add(None)#{True,25,10.8,'Hyd'}
a . add('Hyd')#duplicate not allowed
a . add(1.0)#duplicate not allowed
print(a)#{True,25,10.8,'Hyd'} any order
a . add(10 , 20 , 30)#error--argument should only one
a . add([10,20,30])#error
'''Find  outputs  (Home  work)'''
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{25 , 10.8 , 'Hyd' , True}
print(id(a))#address of set element
a . add(tpl)#{25 , 10.8 , 'Hyd' , True, (10 , 20 , 30)}
a . add('Sec')#{25 , 10.8 , 'Hyd' , True, (10 , 20 , 30),'hyd'}
print(a)#{25 , 10.8 , 'Hyd' , True, (10 , 20 , 30),'hyd'}in any order
print(id(a))#same address
print(len(a))#6
a . add([100 , 200 , 300])#error--list is mutable
a . add(set())#Error
a . add({ })#Error
'''Find  outputs (Home  work)'''
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)#{(10 , 20 , 15 , 18)}
print(s)#{(10 , 20 , 15 , 18)}
print(len(s))#1
'''update()  method  demo program  (Home  work)'''
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)#{10 , 20 , 15, 18}
print(len(s))#4
print(s)#{10 , 20 , 15, 18}any order
s . update(25)#Error--arg should be seq
'''Find  outputs  (Home  work)'''
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)#{10 , 20 , 30 , 40 , 50 ,60 , 70}
print(len(s))#7
s . add(a , b , c)#Error--add accept only 1 
'''Find  outputs  (Home  work)'''
a = set()
a . update('Rama Rao')
print(a)#{'R','a','m','<space>','o' }any order
print(len(a))#5
a . update(3 + 4j , 10.8 , True)#Error--
'''copy()  method  demo  program  (Home  work)'''
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
b = a . copy()
print(b)##{10 , 20 , 15 , 18}any order
print(a  is  b)#False
print(a  ==  b)#True
c = a
print(a  is  c)#True
'''pop()  method  demo  program  (Home  work)'''
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #{25 , 10.8 , 'Hyd' , True}
print(a . pop())   #{ 10.8 , 'Hyd' , True}
print(a . pop())   #{ 'Hyd' , True}
print(a . pop())   #{True}
print(a . pop())   #{True}
print(a . pop()) #Error
print(a) #error
b = {10 , 20 , 30 , 40}
print(b . pop(2)) #error--index is not valid
'''remove()  method  demo  program  (Home  work)'''
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')#remove "Hyd"
print(a) # {25 , 10.8 , True}
a . remove('Sec') #Error
''' discard()  method  demo  program (Home  work)'''
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}any order
a . discard('Hyd')
print(a)#{25 , 10.8  , True}
a . discard('Sec')
print(a)#nothing
a . remove('Sec')#{25 , 10.8  , True,'Sec'}
'''clear()  method  demo  program (Home  work)'''
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()
print(a)#{}
print(len(a))#0
'''Find  outputs  (Home work)'''
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))# {10 , 20 , 30 , 40,50,60}any order
print(a | b)#error
print(b . union(a))# {10 , 20 , 30 , 40,50,60}any order
print(a + b)#Error
'''intersection()   method  demo  program (Home  work)'''
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)#{30,40}
print(type(c))#<class 'set'>
d = a & b
print(d)#{30,40}
print(type(d))#<class 'set'>
print(c  is  d)#False
print(c  ==  d)#True
'''difference()   method  demo  program  (Home  work)'''
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)#{10,20}
print(type(c))#<class 'set'>
d = a - b
print(d)#{10,20}
print(type(d))#<class 'set'>
print(c  is  d)#True
print(c  ==  d)#True
''' symmetric_difference()   method  demo  program  (Home  work)'''
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10,20,50,60}
print(type(c))##<class 'set'>
d = a ^ b
print(d)#{10,20,50,60}
print(type(d))#<class 'set'>
print(c   is   d)#True
print(c  ==   d)#True
'''Find  outputs  (Home  work)'''
a = {x * x  for   x   in   range(10)}
print(a)#{0,1,4,9,16,25,36,49,64,81}
print(type(a))#<class 'set'>
'''(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o
2) Both  input  and  output  are  strings
3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)
4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''
s = "Rama Rao"
seen = set()
result = ""
for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch
print(result)
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set
1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
2) Both  input  and  output  are  lists
'''
a = [False , 25 , 10.8 , 1 , 25 , 0 , 'Hyd' , 10.8 , 1.0 , None , 'Sec' , 'Hyd' , True]
seen = set()
result = []
for x in a:
    if x not in seen:
        seen.add(x)
        result.append(x)
print('List without duplicate:'result)
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]
2) Both  input  and  output  are  lists
'''
a=eval(input('Enter 1st list:'))
b=eval(input('Enter 2nd list:'))
s1 = set(a)
s2 = set(b)
common = list(s1 & s2)
print('common elements between the 2 lists:',common)
