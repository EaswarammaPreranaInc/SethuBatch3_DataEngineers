# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a)) #<class 'tuple'>
a[3] = 'Sec' #error
a[3 : 6] = 60 , 70 , 80 #error

#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1, 2, 3) 139917931270784
a += b
print(a , id(a)) #(1, 2, 3, 4, 5, 6) 139917932544640

#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1, 2, 3) 135795504484992
a = a + b
print(a , id(a)) #(1, 2, 3, 4, 5, 6) 135795505758848

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) #(10,20,30,40)
print(type(a)) #<class 'str'>
b = eval(a)
print(b) #(10, 20, 30, 40)
print(type(b)) #<class 'tuple'>
print(len(b)) #4

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) #(10, [70, 30, 40], 50, 60)
a[1] = [80 , 90 , 100]
print(a) #error

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70
print(a)#[10, (20, 30, 40), 50, 60]
a[1] = [80 , 90]
print(a) #[10, [80, 90], 50, 60]

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25, 10.8, 'Hyd', True)
print(type(x)) #<class 'tuple'>

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25
print(b) #10.8
print(c) #Hyd
print(d) #True
p , q , r =  x
a , b , c , d  , e = x

# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) #25
print(b) #10.8
print(c) #['Hyd', True]
print(type(c)) #<class 'list'> 

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) #25
print(b) #[10.8, 'Hyd']
print(c) #True 

 Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) #error
print(b) #error
print(c) #error
print(d) #error  
print(e) #error

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) #25
print(b) #10.8
print(_) #(3+4j)
print(d) #True
print(_) #(3+4j)

# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b) #(100, 110, 120, 130, 140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) #(10, 20, 15, 18)
e = tuple('Vamsi')
print(e) # ('V', 'a', 'm', 's', 'i')
print(tuple(25)) #error
print(tuple())#()

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
		
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times  

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a) #error
print(id(a)) #error
How  to  modify  30  in  tuple  to  35
print(a) #(10, 20, 30, 40, 50)
print(id(a))  #20000

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) #error
del  a[2]#error  
a . pop(2) #error
print(a) #(10, 20, 30, 40, 50)
print(id(a))#300000
#How  to  remove  30  from  tuple  'a'
print(a) #(10, 20, 30, 40, 50)
print(id(a)) #30000

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) 
print(a) #((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a)) #<class 'tuple'>
print(len(a)) #3
print(How  to  print  1st  inner  tuple) #a[0]
print(How  to  print  2nd  inner  tuple) #a[1]
print(How  to  print  3rd  inner  tuple) #a[2]
print(How  to  print  20) #a[0][1]
print(How  to  print  50) #a[1][2]
print(How  to  print  90) #a[2][3]

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple) #a[0]
print(How  to   print  inner  tuple  in  another  way) #a[-1]
print(How   to  print   10) #a[0][0]
print(How   to  print   20) #a[0][1]
print(How   to  print   30) #a[0][2]
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b') #b[0]
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way #b[-1]

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) #(10, 20, 30)
print(*a) #0 20 30
b = (())
print(b) #()
print(*b) #()

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) #10000
b = eval(a) 
print(b) #{18, 20, 10, 12, 15}
print(type(b)) #class 'set'>

# How to print set in different ways (Home work)

a = {25, True, 'Hyd', 10.8}

print('set with print function')
print(a) #25, 10.8, 'Hyd', True}

print('Iterate elements of set with for loop')
for x in a:
    print(x) # 25
              10.8 
              Hyd
              True


# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) #True, 'Hyd', 25}
print(len(s)) #3
print(type(s)) #clas set

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{25, 10.8, 'Hyd', True}
a , b , c , d = s
print(a) #25
print(b) #10.8
print(c) #hyd
print(d) #True

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{25, 10.8, 'Hyd', True}
a , *b = s
print(a) #25
print(b) #[10.8, 'Hyd', True]
print(type(b)) #<class 'list'>

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) #{'Hyd', True, 25}
print(len(s)) #3
print(type(s)) #class set 

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) ##{'Hyd', 25, 10.8, 
a , b , c , d = s
print(a) #hyd 
print(b) #25
print(c) #True
print(d) #10.8

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a) #25
print(b) #[10.8, 'Hyd', True]
print(type(b)) #class list

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a) #{130, 100, 140, 110, 150, 120}
print(b) #{10, 12, 15, 18, 50, 20}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) #{10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18}
print(d) ##{10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18}
e = set('Rama  rAo')
print(e) #{'R', ' ', 'o', 'a', 'A', 'm', 'r'}
print(set(25)) #error
print(set()) #eror

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
print(a) #{None, True, 10.8, 'Hyd', 25}
a . add(10 , 20 , 30)
a . add([10,20,30])

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) #{'Hyd', 25, 10.8, True}
print(id(a)) #10000
a . add(tpl)
a . add('Sec')
print(a) #{True, 'Hyd', 10.8, (10, 20, 30), 25, 'Sec'
print(id(a)) #20000
print(len(a)) #6
a . add([100 , 200 , 300])
a . add(set())
a . add({ })

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) #{50, 20, 70, 40, 10, 60, 30}
print(len(s)) #7
s . add(a , b , c)

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) #{' ', 'R', 'm', 'o', 'a'}
print(len(a))#5
a . update(3 + 4j , 10.8 , True)


# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10, 18, 20, 15}
b = a . copy()
print(b) #{10, 18, 20, 15}
print(a  is  b) #false
print(a  ==  b) #True
c = a
print(a  is  c) #True

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #{'Hyd', 25, 10.8, True}
print(a . pop())  #Hyd
print(a . pop())  #25
print(a . pop())  #10.8
print(a . pop())  #True
print(a . pop())  #error
print(a) #()
b = {10 , 20 , 30 , 40}
print(b . pop(2))  #30

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #{25, 10.8, 'Hyd', True}
a . remove('Hyd')
print(a)  #25, 10.8, True
a . remove('Sec')   

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25, 10.8, True, 'Hyd'}
a . discard('Hyd')
print(a)#{25, 10.8, True}
a . discard('Sec')
print(a) #{25, 10.8, True}
a . remove('Sec')

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10, 18, 20, 15}
a . clear()
print(a)#{}
print(len(a))#0

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) #{40, 10, 50, 20, 60, 30}
print(a | b) #error
print(b . union(a))#error
print(a + b)#error

  #intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) #{40, 30}
print(type(c))#class set
d = a & b
print(d)#{40,30}
print(type(d))#class set
print(c  is  d)#False
print(c  ==  d) #True

# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) #{10, 20}
print(type(c))#class set 
d = a - b
print(d) #{10,20}
print(type(d)) #class set
print(c  is  d) #False
print(c  ==  d) #True

 #symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10, 50, 20, 60}
print(type(c))#class set
d = a ^ b
print(d)#{10, 50, 20, 60}
print(type(d)) #class set
print(c   is   d)#False
print(c  ==   d) #True

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) #{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a)) #<class 'set'>

(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hy


s = input("Enter a string: ")
st = set(s)
result = ''.join(st)
print("string without duplicates:",result)

Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists


lst = input("enter the string:")
st = set(lst)
result = list(st)
print(result)

Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists

list1 = eval(input("enter the first list 1:"))
list2 = eval(input("enter the second list 2:"))
set1 = set(list1)
set2 = set(list2)
common = set1 & set2
result = list(common)
print("common elements between the two lists:",result)









