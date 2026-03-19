# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a) #Hyd
print(b) #25
print(c) #True
print(d) #10.8

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  #{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a) #Hyd
print(b)#{  25,  True,  10.8 }
print(type(b))#<class 'set'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a)#Hyd
print(b)#{  25,  True }
print(c) #10.8

 # Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) #{20 , 10 }
x , y = s
print(x) #20
print(y)#10

 # set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) #{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10,20,15,18,50,12}
e = set('Rama  rAo')
print(e) # {'R','a', 'm', ' ', 'r' ,'o'}
print(set(25)) # Error
print(set()) #{}


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
a . add(True)
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a) #{ True, 25, 10.8, 'Hyd', None}
a . add(10 , 20 , 30) ##{ True, 25, 10.8, 'Hyd', None, (10 , 20 , 30)}
a . add([10,20,30]) #Error


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
print(a) # {25 , 10.8 , 'Hyd' , True}
print(id(a)) #1000
a . add(tpl)
a . add('Sec')
print(a)## {25 , 10.8 , 'Hyd' , True,(10 , 20 , 30),'Sec'}
print(id(a)) #2000
print(len(a)) #6
a . add([100 , 200 , 300]) #error
a . add(set()) #error
a . add({ }) #error

 # Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) #{(10 , 20 , 15 , 18)}
print(len(s)) #1


 # update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set() 
s . update(tpl)
print(len(s)) #4
print(s) #{10, 20, 15, 18}
s . update(25) ##{10, 20, 15, 18, 25}

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) #{10, 20, 30, 40, 50, 60, 70 }
print(len(s)) #7
s . add(a , b , c) #error

 # Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) #{'R', 'a', 'm', 'r', ' ', 'o'}
print(len(a)) #7
a . update(3 + 4j , 10.8 , True) # #{'R', 'a', 'm', 'r', ' ', 'o', 3 + 4j , 10.8 , True}

 # copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
b = a . copy()
print(b) #{10 , 20 , 15 , 18}
print(a  is  b) #False
print(a  ==  b) #True
c = a
print(a  is  c) #True

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}
print(a . pop()) #25 
print(a . pop())  #10.8
print(a . pop()) #Hyd 
print(a . pop())  #True
print(a . pop()) #Error
print(a) #{}
b = {10 , 20 , 30 , 40}
print(b . pop(2))  #Error


# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)  ##{25 , 10.8 , True}
a . remove('Sec') #Error  


# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a) #{25 , 10.8 , True}
a . discard('Sec')
print(a) #{25 , 10.8 , True}
a . remove('Sec') #Error


# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
a . clear()
print(a) #{}
print(len(a)) #0


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) #{10, 20, 30, 40, 50, 60}
print(a | b) #{10, 20, 30, 40, 50, 60}
print(b . union(a)) #{10, 20, 30, 40, 50, 60}
print(a + b) #Error

#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b) 
print(c) #{30, 40}
print(type(c)) #<class 'set'>
d = a & b
print(d) #{30, 40}
print(type(d))#<class 'set'>
print(c  is  d) #False
print(c  ==  d) #True


# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) #{10, 20, 50, 60}
print(type(c))#<class 'set'>
d = a - b
print(d)  #{10, 20, 50, 60}
print(type(d))#<class 'set'>
print(c  is  d)#False
print(c  ==  d)#True


# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) #{10, 20}
print(type(c))#<class 'set'>
d = a ^ b
print(d) #{10, 20}
print(type(d))#<class 'set'>
print(c   is   d) #False
print(c  ==   d)#True


# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) #{0, 1,4,9,16, 25,36,49,64,81}
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
s= input('Enter string')
p=set(s)
print(''.join(p))

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
l= eval(input('Enter list'))
p=set(l)
print(f'list without duplicates : {list(p)}'))

 '''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
l1= eval(input('Enter list'))
l2= eval(input('Enter list'))
s1= set(l1)
s2=set(l2)
r= s1.intersection(s2)
print(f'Common elements between the lists: {list(r)}')