# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) # (25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a)) # <class Tuple>
#a[3] = 'Sec' # Error
#a[3 : 6] = 60 , 70 , 80 # Error

#  Find  outputs
a = (1 , 2 , 3) 
b = (4 , 5 , 6)
print(a , id(a)) # (1 , 2 , 3), Address of a
a += b 
print(a , id(a)) # (1 ,2 , 3 , 4 , 5 , 6) Address of a with diff address

#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # (1 , 2 , 3), Address of a
a = a + b
print(a , id(a)) # (1 ,2 , 3 , 4 , 5 , 6) Address of a with diff add

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) #"(10 , 20 , 30 , 40)"
print(type(a)) # <class string>
b = eval(a) # 
print(b) # (10 , 20 , 30 , 40)
print(type(b)) # <class tuple>
print(len(b)) # 4

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
#a[1][0] = 70 # Error
print(a) # (10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]
print(a) # (10 , [70 , 30 , 40] , 50 , 60)

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70 # Error
print(a) #[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a) # [10 , [80, 90] , 50 , 60]

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) # (25, 10.8, 'Hyd', True)
print(type(x)) # <class tuple>

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) # 25
print(b) # 10.8
print(c) # 'Hyd'
print(d) # True
p , q , r =  x # Error
a , b , c , d  , e = x # Error

# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) # 25
print(b) # 10.8
print(c) # ('Hyd', True)
print(type(c)) # <class tuple>

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # 25
print(b) # (10.8, 'Hyd')
print(c) # True

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) # 10.8
print(c) # ()
print(d) # 'Hyd'
print(e) # True

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
print(type(b))# <class tuple>
c = [10 , 20 , 15, 18]
d = tuple(c) 
print(d) # (10,20,15,18)
e = tuple('Vamsi')
print(e) # ('V', 'a', 'm', 's', 'i')
print(tuple(25)) # Error
print(tuple()) # ()

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
print(a) # (10 ,  20 ,  30 ,   40 ,  50)
print(id(a)) # Address of a
# How  to  modify  30  in  tuple  to  35
a=a[:2] | (35,) |a[2:]
print(a) # (10 ,  20 ,  35, 30 ,   40 ,  50)
print(id(a)) # Diff adress

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) # error
del  a[2] # Error
a . pop(2) # Error
print(a) #(10 , 20 , 30 , 40 , 50)
print(id(a)) # Address of a
#How  to  remove  30  from  tuple  'a'
a=list(a)
a.remove(30)
a=tuple(a)
print(a)
print(id(a))

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # <class tuple>
print(len(a)) # 3
print(a[0])
print(a[1])
print(a[2])
print(a[0][1])
print(a[1][2])
print(a[2][3])

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])
print(*a)
print(a[0][0])
print(a[0][1])
print(a[0][2])
b = ((),)
print(a[0])
print(*a)

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # (10,20,30)
print(*a) # 10 20 30
b = (())
print(b) # ()
print(*b) # nothing

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # '{10 , 20 , 15 , 18 , 20 , 12 , 18}'
print(type(a)) # class str>
b = eval(a) 
print(b) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(b)) # <class set>

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10 , 20 , 30)}
print({[10 , 20 , 30]}) # Error
print({{10 , 20 , 30}}) # Error
print({{}}) # Error

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(str(a))
print(a) # {25 , True , 'Hyd' , 10.8}
print(x for x in a)

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) {'Hyd', True, 25}
print(len(s)) # 3
print(type(s)) # <class set>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } 
a , b , c , d = s
print(a) # 'Hyd'
print(b) # 25
print(c) # True
print(d) # 10.8

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  # {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a) #  'Hyd'
print(b) # {25,  True,  10.8}
print(type(b)) # <class set>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a) # 'Hyd'
print(b) # {25, True}
print(c) # 10.8

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {20 , 10 , 20 , 10}
x , y = s # Error
print(x) # Error
print(y) # Error

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a) 
print(b) # {100, 110, 120, 130, 140, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10, 20, 15, 18, 50, 12}
e = set('Rama  rAo')
print(e) # { 'R' , 'a', 'm', ' ', 'o'}
print(set(25)) # Error
print(set()) # {}

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
a . add(10 , 20 , 30) # error
a . add([10,20,30]) # error , set doesnt accept mutable obj

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25 , 10.8 , 'Hyd' , True}
print(id(a)) # <class set>
a . add(tpl) 
a . add('Sec')
print(a) # {25 , 10.8 , 'Hyd' , True , (10,20,30), 'sec'}
print(id(a)) # Address same
print(len(a)) # 6
a . add([100 , 200 , 300]) # Error
a . add(set()) # Error
a . add({ }) # Error

# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10,20,15,18)}
print(len(s)) # 1

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s) # {10, 20, 15, 18}
s . update(25) # error, bcz arg should be seq only

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) # {10, 20, 30, 40, 50, 60, 70}
print(len(s)) # 7
s . add(a , b , c) # Error

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) # {'R', 'a', 'm', ' ', 'o'}
print(len(a)) # 5
a . update(3 + 4j , 10.8 , True) # Error, bcz arg should be seq

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
b = a . copy()
print(b) # {10 , 20 , 15 , 18}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is  c) # True

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25 , 10.8 , 'Hyd' , True}
print(a . pop())  
print(a . pop())  
print(a . pop())  
print(a . pop())  
print(a . pop()) # Error
print(a) # {}
b = {10 , 20 , 30 , 40}
print(b . pop(2))  # Error

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)  # {25 , 10.8 , True}
a . remove('Sec')   # Error

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd') 
print(a) # {25 , 10.8 , True}
a . discard('Sec') # no error
print(a) # {25 , 10.8 , True}
a . remove('Sec') # no Error

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear()
print(a) # {}
print(len(a)) # 0

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {10,20,30,40,50,60}
print(a | b) # Error, bcz oprs should be both sets
print(b . union(a)) # Error, list class doesnt have union method
print(a + b) # set doesnt support '+'

#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) # {30,40}
print(type(c)) # <class set>
d = a & b 
print(d) # {30,40}
print(type(d)) #  <class set>
print(c  is  d) # False
print(c  ==  d) # True

# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) # {10,20}
print(type(c)) #<class set>
d = a - b
print(d) # {10,20}
print(type(d)) #<class set>
print(c  is  d) # False
print(c  ==  d) # True

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) # {10,20,50,60}
print(type(c)) #<class set>
d = a ^ b
print(d) # {10,20,50,60}
print(type(d)) # <class set>
print(c   is   d) # False
print(c  ==   d) # True

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)} # {1,4,9,16,25,36,49,64,81}
print(a) # {1,4,9,16,25,36,49,64,81}
print(type(a)) # <class set>

# Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
s=input("Enter string input : ")
ns=''
for x in list(set(s)):
    ns+=''.join(x)
print(ns)

# Write  a  program  to  remove  duplicate  elements  of   list  using  set
ls=eval(input("Enter the list : "))
ls=set(ls)
print(list(ls))

# Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
l1=eval(input("Enter 1st list : "))
l2=eval(input("Enter 2nd list : "))
l1=set(l1)
l2=set(l2)
print(f'Common elements between two lists are : {list(l1.intersection(l2))}')