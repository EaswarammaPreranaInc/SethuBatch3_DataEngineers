# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) # 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(type(a)) # tuple
a[3] = 'Sec'
a[3 : 6] = 60 , 70 , 80


#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1,2,3)
a += b
print(a , id(a))#(1,2,3,4,5,6)


#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1,2,3)
a = a + b
print(a , id(a)) #(1,2,3,4,5,6)


#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  : 10 ')
print(a)
print(type(a)) #tuple
b = eval(a)
print(b)
print(type(b))
print(len(b))


# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) # (10, [70, 30, 40], 50, 60)
a[1] = [80 , 90 , 100]
print(a)


# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)# error
a[1] = [80 , 90]
print(a) # error



# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) # 25,10.8,'Hyd',True
print(type(x)) # tuple


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) # 25
print(b) # 10.8
print(c) # Hyd
print(d) # True
p , q , r =  x
a , b , c , d  , e = x


# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) # 25
print(b) # 10.8
print(c) #['Hyd',True]
print(type(c)) # list


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # 25
print(b) #[10.8,'Hyd']
print(c) # True


# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) # 10.8
print(c) # []
print(d) # Hyd
print(e) # True


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) # 25
print(b) # 10.8
print(_) # (3+4j)
print(d) # True
print(_) #(3+4j)


# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a) 
print(b) # 100,110,120,130,140
print(type(b)) # tuple
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) # (10, 20, 15, 18)
e = tuple('Vamsi')
print(e) #('V','a','m','s','i')
print(tuple(25)) # error
print(tuple()) # error


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
		i = a . index(15 , i + 1) # 2,5,8
except:
		print(F'15  is  found  {a . count(15)}  times') # 15 is found 3 times 



#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a) #(10 ,  20 ,  30 ,   40 ,  50)
print(id(a))
How  to  modify  30  in  tuple  to  35
print(a) # (10, 20, 35, 40, 50)
print(id(a))


# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)
del  a[2]
a . pop(2)
print(a) # (10 , 20 , 30 , 40 , 50)
print(id(a))
How  to  remove  30  from  tuple  'a'
print(a) #(10, 20, 40, 50)
print(id(a))


#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))# tuple
print(len(a)) # 3
print(How  to  print  1st  inner  tuple) # print(a[0])
print(How  to  print  2nd  inner  tuple) #print(a[1])
print(How  to  print  3rd  inner  tuple) #print(a[2])
print(How  to  print  20) #(10,20)
print(How  to  print  50) # (30,40,50)
print(How  to  print  90) #(60,70,80,90)


# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple) # print(a[0])
print(How  to   print  inner  tuple  in  another  way) 
print(How   to  print   10) # print(a[0][1])
print(How   to  print   20) # print(a[0][1])
print(How   to  print   30) # print(a[0][2])
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b') #b[0]
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)


#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # (10,20,30)
print(*a) #10,20,30
b = (())
print(b) #()
print(*b)


# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ') # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a) #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # string
b = eval(a)
print(b) # {10, 12, 15, 18, 20}
print(type(b)) # set


#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10,20,30)}
print({[10 , 20 , 30]}) # error
print({{10 , 20 , 30}}) # error
print({{}}) # error


# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # {10.8, True, 25, 'Hyd'} # 10.8, True, 25, 
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop


# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) #{True,'Hyd',25}
print(len(s)) # 3
print(type(s)) # set


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)#25
print(b) # 10.8
print(c) # Hyd
print(d) # True

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a) # 25
print(b) #['Hyd',  25,  True,  10.8]
print(type(b)) # list


# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) #{10,20}
x , y = s
print(x) # 10
print(y)# 20



a = range(100 , 151 , 10)
b = set(a)
print(b) # {130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e)# {'A', 'm', 'R', 'r', ' ', 'o', 'a'}
print(set(25)) #error
print(set()) 


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
print(a) # {None, True, 10.8, 'Hyd', 25}
a . add(10 , 20 , 30)
a . add([10,20,30])


# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25 , 10.8 , 'Hyd' , True}
print(id(a))
a . add(tpl)
a . add('Sec')
print(a) # {True, 'Hyd', 10.8, (10, 20, 30), 'Sec', 25}
print(id(a))
print(len(a)) # 6
a . add([100 , 200 , 300])
a . add(set())
a . add({ })



# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10 , 20 , 15 , 18)}
print(len(s)) # 1


# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
a . discard('Hyd')
print(a) # {25, 10.8,True}
a . discard('Sec')
print(a) # {25, 10.8, True}
a . remove('Sec')


program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear()
print(a) #set()
print(len(a))# 0


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))
print(a | b) # {40, 10, 50, 20, 60, 30}
print(b . union(a))
print(a + b)

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) # {40,30}
print(type(c))# set
d = a & b
print(d) # {40,30}
print(type(d)) # set
print(c  is  d) # false
print(c  ==  d) # True


# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) #{10,20}
print(type(c)) # set
d = a - b
print(d) # {10,20}
print(type(d)) # set
print(c  is  d) # false
print(c  ==  d)# True


# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) #{10,50,20,60}
print(type(c)) #set
d = a ^ b
print(d) # {10,50,20,60}
print(type(d)) #set
print(c   is   d)# False
print(c  ==   d)#True


# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a)) # set



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

s = "MISSISIPI"
result = ''
for ch in s:
    if ch not in result:
        result += ch
print(result)  


'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''

lst = [False, 25, 10.8, 1, 25, 0, 'Hyd', 10.8, 1.0, None, 'Sec', 'Hyd', True]

unique_list = []
seen = set()
for item in lst:
        if item not in seen:
        unique_list.append(item)
        seen.add(item)

print(unique_list)


'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 70, 80, 20]

set2 = set(list2)

common_list = [x for x in list1 if x in set2]

print(common_list)
