#1.Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)                # (25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))          # <class 'tuple'>
a[3] = 'Sec'            # Error
a[3 : 6] = 60 , 70 , 80 # Error


#2.Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))  # (1 , 2 , 3) 1000
a += b
print(a , id(a))  # (1,2,3,4,5,6) 2000


#3.Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # (1 , 2 , 3) 1000
a = a + b
print(a , id(a)) # (1,2,3,4,5,6) 2000


#4.What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)       # '(10,20,30)'
print(type(a)) # <class 'str'>
b = eval(a)
print(b)       # (10,20,30)
print(type(b)) # <class 'str'>
print(len(b))  # 3



#5.Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70           
print(a)               # (10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100] # Error
print(a)               # (10 , [70 , 30 , 40] , 50 , 60)



#6.Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70     # Error
print(a)         # [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90] 
print(a)         # [10 , [80 , 90] , 50 , 60]



#7.Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)      # (25,10.8,'Hyd',True)
print(type(x))# <class 'tuple'>



#8.Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)  # 25
print(b)  # 10.8
print(c)  # 'Hyd'
print(d)  # True
p , q , r =  x  # Error
a , b , c , d  , e = x  # Error



#9.Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)       # 25
print(b)       # 10.8
print(c)       # ['Hyd',True]
print(type(c)) # <class 'list'>



#10.Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # 25
print(b) # [10.8,'Hyd']
print(c) # True



#11.Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) # 10.8
print(c) # []
print(d) # 'Hyd'
print(e) # True



#12.Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) # 25
print(b) # 10.8
print(_) # (3+4j)
print(d) # True
print(_) # (3+4j)


#13.tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)           # (100,110,120,130,140)
print(type(b))     # <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)           # (10,20,15,18)
e = tuple('Vamsi')
print(e)           # ('V','a','m','s','i')
print(tuple(25))   # Error
print(tuple())     # ()



#14.index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0   1    2    3    4     5   6    7    8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')

'''
15 is found at index : 2
15 is found at index : 5
15 is found at index : 8
15  is  found  3  times
'''


#15.How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0     1      2     3      4
#a[2] = 35           # Error
print(a)            # (10 ,  20 ,  30 ,   40 ,  50)
print(id(a))        # 1000
a = a[:2]+(35,)+a[3:] # How  to  modify  30  in  tuple  to  35
print(a)            # (10 ,  20 ,  35 ,   40 ,  50)
print(id(a))        # 2000



#16.How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0    1    2    3    4
a . remove(30) # Error
del  a[2]      # Error
a . pop(2)     # Error
print(a)       # (10 , 20 , 30 , 40 , 50)
print(id(a))   # 1000
a = a[:2]+a[3:]# How  to  remove  30  from  tuple  'a'
print(a)       # (10 , 20 , 40 , 50)
print(id(a))   # 2000



#17.Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)        # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))  # <class 'tuple'>
print(len(a))   # 3
print(a[0])     # How  to  print  1st  inner  tuple
print(a[1])     # How  to  print  2nd  inner  tuple
print(a[2])     # How  to  print  3rd  inner  tuple
print(a[0][1])  # How  to  print  20
print(a[1][2])  # How  to  print  50
print(a[2][3])  # How  to  print  90



#18.Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])    # How  to   print  inner  tuple
print(*a)      # How  to   print  inner  tuple  in  another  way
print(a[0][0]) # How   to  print   10
print(a[0][1]) # How   to  print   20
print(a[0][2]) # How   to  print   30
b = ((),)
print(b[0])    # How  to   print  inner  tuple  of  tuple  'b'
print(*b)      # How  to   print  inner  tuple  of  tuple  'b'  in  another  way




#19.Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)   # ((10 , 20 , 30))
print(*a)  # 10 20 30
b = (())
print(b)   # ()
print(*b)  # nothing



#20.What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)       # '{10 , 20 , 15 , 18 , 20 , 12 , 18}'
print(type(a)) # <class 'str'>
b = eval(a)
print(b)       # {10 , 20 , 15 , 18 ,12}
print(type(b)) # <class 'set'>



#21.Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10 , 20 , 30)}
print({[10 , 20 , 30]}) # Error
print({{}}) # Error



#22.How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
for i in a:
    print(i) # How  to  iterate  set  with  for  loop



#23.Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)       # {'Hyd',True,25}
print(len(s))  # 3
print(type(s)) # <class 'set'>



#24.Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  # {'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)  # 25
print(b)  # 'Hyd'
print(c)  # True
print(d)  # 10.8



#25.Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)        # {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)        # unordered 'Hyd'
print(b)        # [25,True,10.8]
print(type(b))  # <class 'list'>




#26.Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)   # {'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a)   # 'Hyd'
print(b)   # [25,True]
print(c)   # 10.8



#27.Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)   # {20 , 10}
x , y = s
print(x)   # 10
print(y)   # 20



#28.set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)              # {100,110,120,130,140,150}

c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) 
print(d)              # {10,20,15,18,50,12}
e = set('Rama  rAo')
print(e)              # {'R','a','m',' ','r','A','o'}
print(set(25))        # Error
print(set())          # set()



#29.add()  method  demo  program  (Home  work)
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
print(a)               # {True,25,10.8,'Hyd',None}
a . add(10 , 20 , 30)  # Error
a . add([10,20,30])    # Error




#30.Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)              # {25 , 10.8 , 'Hyd' , True}
print(id(a))          # 1000
a . add(tpl)       
a . add('Sec')
print(a)              # {25 , 10.8 , 'Hyd' , True,'Sec',(10 , 20 , 30)}
print(id(a))          # 1000
print(len(a))         # 6
a . add([100 , 200 , 300]) # Error
a . add(set())        # Error
a . add({ })          # Error



#31.Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) 
print(s)      # {(10 , 20 , 15 , 18)}
print(len(s)) # 1



#32.update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) 
print(len(s))   # 4
print(s)        # {10 , 20 , 15, 18}
s . update(25)  # Error



#33.Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)  
print(s)             # {10,20,30,40,50,60,70}
print(len(s))        # 7
s . add(a , b , c)   # Error



#34.Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)      # {'R','a','m',' ','o'}
print(len(a)) # 5
a . update(3 + 4j , 10.8 , True) # Error



#35.copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)         # {10 , 20 , 15 , 18}
b = a . copy()
print(b)         # {10 , 20 , 15 , 18}
print(a  is  b)  # False
print(a  ==  b)  # True
c = a
print(a  is  c)  # True



#36.pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  
print(a . pop())  # 25 
print(a . pop())  # 10.8 
print(a . pop())  # 'Hyd'
print(a . pop())  # True
print(a . pop())  # Error
print(a)          # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2)) # Error



#37.remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)          # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd') 
print(a)          # {25,10.8,True}
a . remove('Sec') # Error



#38.discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)           # {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a)           # {25 , 10.8 , True}
a . discard('Sec')
print(a)           # {25 , 10.8 , True}
a . remove('Sec')  # Throws Error



#39.clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)      # {10 , 20 , 15 , 18}
a . clear()
print(a)      # set()
print(len(a)) # 0



#40.Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))  # {10,20,30,40,50,60}
print(a | b)         # Error
print(b . union(a))  # Error
print(a + b)         # Error



#41.intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b) 
print(c)         # {30,40}
print(type(c))   # <class 'set'>
d = a & b       
print(d)         # {30,40}
print(type(d))   # <class 'set'>
print(c  is  d)  # False
print(c  ==  d)  # True



#42.difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)         # {10,20}
print(type(c))   # <class 'set'>
d = a - b      
print(d)         # {10,20}
print(type(d))   # <class 'set'>
print(c  is  d)  # False
print(c  ==  d)  # True



#43.symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)          # {10,20,50,60}
print(type(c))    # <class 'set'>
d = a ^ b
print(d)          # {10,20,50,60}
print(type(d))    # <class 'set'>
print(c   is   d) # False
print(c  ==   d)  # True



#44.Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)        # {0,1,4,9,16,25,36,49,64,81}
print(type(a))  # <class 'set'>



##45.(Home  work)
##Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
##
##1) Let  input  be   Rama  Rao
##    What  is  the  output  ? ---> Ram<space>o
##
##2) Both  input  and  output  are  strings
##
##3) How  to  convert  string  to  set  ?  --->  set(string)
##    How  to  convert  set  to  string ?  --->  '' . join(set)
##
##4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'


s = input('Enter any string : ')
new = ''.join(set(s))
print(new)


s = input('Enter any string : ')
new = ''
st = set()
for ch in s:
    if ch not in st:
        new += ch
        st.add(ch)
print(new)



##46.Write  a  program  to  remove  duplicate  elements  of   list  using  set
##
##1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
##    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
##
##2) Both  input  and  output  are  lists

s = eval(input('Enter any List : '))
print(list(set(s)))



##47.Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
##
##1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
##    What  is  the  output ?  ---> [20 , 30 , 40]
##
##2) Both  input  and  output  are  lists


n = eval(input('Enter 1st list : '))
m = eval(input('Enter 2nd List : '))
new = []
new.append(list(set(n).intersection(set(m))))

































































































