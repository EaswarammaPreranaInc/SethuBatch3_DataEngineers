# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)#(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))#<class 'tuple'>
a[3] = 'Sec'#error becoz tuple is immutable item assingment  is not possible in set 
a[3 : 6] = 60 , 70 , 80#error becoz tuple is immutable item assingment  is not possible in set
#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))# (1 , 2 , 3)<space>address of a with 3 elements 
a += b
print(a , id(a))# (1,2,3,4,5,6)<space>address of a with 6 elements different address
 #  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))# (1 , 2 , 3)<space>address of a with 3 elements 
a = a + b
print(a , id(a))# (1,2,3,4,5,6)<space>address of a with 6 elements different address 
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)#'(10,20,30)'
print(type(a))#<class 'str'>
b = eval(a)
print(b)#(10,20,30)
print(type(b))#<class 'tuple'>
print(len(b))#3
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)#(10 , [70, 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]
print(a)##(10 , [80 , 90 , 100] , 50 , 60)
 # Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70#error item assignment is not possible in tuple as it is immutable
print(a)#error item assignment is not possible in tuple as it is immutable
a[1] = [80 , 90]
print(a)#[10 , [80 , 90], 50 , 60]
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25,10.8,'Hyd',True)
print(type(x))#<class 'tuple'>
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25 
print(b)#10.8
print(c)#'Hyd'
print(d)#True
p , q , r =  x#error  tuple with excess elments
a , b , c , d  , e = x#error tuple with few  elments
# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)#25
print(b)#10.8
print(c)#['Hyd' , True]
print(type(c))#<class 'tuple'>
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#[ 10.8 , 'Hyd']
print(c)#True
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)#'Hyd'
print(e)#True
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#3+4j
print(d)#'Hyd'
print(_)#3+4j
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)#(100,110,120,130,140)
print(b)##(100,110,120,130,140)
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)#(10 , 20 , 15, 180)
print(d)#(10 , 20 , 15, 180)
e = tuple('Vamsi')
print(e)#('v','a','m','s','i')
print(tuple(25))#error , is missing
print(tuple())#()


#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1   2     3    4   5     6    7   8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)#2,5,8
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')#15  is  found 3  times

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0     1     2       3     4
a[2] = 35#error 
print(a)#(10 ,  20 ,  30 ,   40 ,  50)
print(id(a))#address of a 
a=list(a)#[10 ,  20 ,  30 ,   40 ,  50]
a=tuple(a.list(2,35))#How  to  modify  30  in  tuple  to  35
print(a) #[10 ,  20 ,  35 ,   40 ,  50]
print(id(a))#address of a changed
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1   2     3    4
a . remove(30)#error no method in tuple 
del  a[2]#error tuple does not support it
a . pop(2)#error no method in tuple
print(a)#(10 , 20 , 30 , 40 , 50)
print(id(a))#address of a with 5 elements
#How  to  remove  30  from  tuple  'a'
print(a)
print(id(a))
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))#<class 'set'>
print(len(a))#3
print(a[0])#How  to  print  1st  inner  tuple
print(a[1])#How  to  print  2nd  inner  tuple
print(a[2])#How  to  print  3rd  inner  tuple
print(a[0][1])#How  to  print  20
print(a[1][2])#How  to  print  50
print(a[2][3])#How  to  print  90
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])#How  to   print  inner  tuple
print(a[:])#How  to   print  inner  tuple  in  another  way
print(a[0][0])#How   to  print   10
print(a[0][1])#How   to  print   20
print(a[0][2])#How   to  print   30
b = ((),)
print(a[0])#How  to   print  inner  tuple  of  tuple  'b'
print(a[:0])#How  to   print  inner  tuple  of  tuple  'b'  in  another  way#a[0][:0]
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)#((10 , 20 , 30))
print(*a)#10,20,30
b = (())
print(b)#(())
print(*b)#nothing is printed becoz empty
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}#10 , 20 , 15 , 18 ,12 in any order
a = input('Enter  Set  :  ')#{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a)#'{10 , 20 , 15 , 18 , 20 , 12 , 18}'
print(type(a))#<class 'str'>
b = eval(a)
print(b)#{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(b))#<class 'set'>
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})#{(10 , 20 , 30)}
print({[10 , 20 , 30]})#error set cannot contain mutable elements
print({{10 , 20 , 30}})#error set cannot contain mutable elements
print({{}})#error set cannot contain mutable elements
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(a)#'set  with  print  function'
print(a)
for x in a:
	print(x)#'Iterate  elements  of  set  with  for  loop'
for x in a :
	print(x)#How  to  iterate  set  with  for  loop
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{'Hyd',True,25,1}in any order because it is a set 
print(len(s))#4
print(type(s))#<class 'set'>
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 } in any order 
a , b , c , d = s
print(a)#first element of set  in  which is displayed in output ex:Hyd
print(b)# second element of set  in which is displayed in output ex:25
print(c)# 3rd  element of set  in which is displayed in output ex:True
print(d)#4rth element of set  inwhich is displayed in  output ex:10.8
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) 
a , *b = s
print(a)#first element of set  in which is displayed in output ex:Hyd
print(b)#except first  element of set  in which is displayed in output list is printed ex:[25,  True,  10.8]
print(type(b))#<class 'list'>
 # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 } in anyorder
a , *b , c = s
print(a)#first element of set  in output ex:Hyd 
print(b)#except first and last element off set displayed in list here ex:[25,  True]
print(c)#last  element of set  in output ex:10.8
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)#{20 , 10 }in any order
x , y = s
print(x)#10 or 20 ex:10
print(y)#other than x value ex:20
 # set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)#{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10,20,15,18,50,12,18} in anyorder
e = set('Rama  rAo')
print(e)#{'R','a' ,'m', ' ' , 'r' ,'A','o'}
print(set(25))#error arguments should be sequence only
print(set())#set()


# add()  method  demo  program  (Home  work)
a = set()
a . add(True)#{True} in any order
a . add(25)#{True,25} in any order 
a . add(10.8)#{True,25,10.8} in any order
a . add(1)#ignore
a . add('Hyd')#{True,25,10.8,'Hyd'}in any order
a . add(25)#ignore
a . add(None)#{True,25,10.8,'Hyd',None}in any order
a . add('Hyd')#ignore
a . add(1.0)#ignore
print(a)#{True,25,10.8,'Hyd',None}
a . add(10 , 20 , 30)# error set supports only one arguments only
a . add([10,20,30])#error,set does not support sequences to add 


# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{25 , 10.8 , 'Hyd' , True} in any order
print(id(a))#address of a
a . add('Sec')#{25 , 10.8 , 'Hyd' , True,'Sec'}
print(a)#{25 , 10.8 , 'Hyd' , True,'Sec'}
print(id(a))#address of a
print(len(a))#5
a . add([100 , 200 , 300])#error ,set does not support sequences to add
a . add(set())#error ,set does not support sequences to add
a . add({ })#error ,set does not support sequences to add
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)#{(10 , 20 , 15 , 18)}
print(len(s))#1
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)#{10 , 20 , 15, 18 } in any order
print(len(s))#4
print(s)#{10 , 20 , 15, 18}
s . update(25)#error arguments shloud be set sequence only 

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)#{a,b,c}in any order
print(len(s))#3
s . add(a , b , c)#error can add one argument\value at a time
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)#{'R','a','m',' ','o'}
print(len(a))#5
a . update(3 + 4j , 10.8 , True)##{'R','a','m',' ','o',3 + 4j , 10.8 , True}
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
b = a . copy()
print(b)#{10 , 20 , 15 , 18}
print(a  is  b)#False
print(a  ==  b)#True
c = a
print(a  is  c)#True

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True} in any order 
print(a . pop())#  first element of the set 
print(a . pop())#  second element of the set
print(a . pop())#  3rd element of the set  
print(a . pop())#  4th element of the set  
print(a . pop())# error empty set 
print(a) #set()
b = {10 , 20 , 30 , 40}
print(b . pop(2)) #error cann't delete becouse set is not indexed  


# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)  #{25 , 10.8 , True}
a . remove('Sec')  #error becoz no  'Sec' in set a 


# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . discard('Hyd')
print(a)#{25 , 10.8 , True}
a . discard('Sec')
print(a)#{25 , 10.8 , True}
a . remove('Sec')#error becoz no  'Sec' in set a 

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()
print(a)#set()
print(len(a))#0


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))#{10 , 20 , 30 , 40 , 50 , 60}
print(a | b)#error pipe operator supports set and set only here b is list 
print(b . union(a))#{10 , 20 , 30 , 40 , 50 , 60}
print(a + b)#error concatination is not possible for set with + operator
#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)#{30,40}
print(c)#{30,40}
print(type(c))#<class 'set'>
d = a & b
print(d)#{30,40}
print(type(d))#<class 'set'>
print(c  is  d)#False
print(c  ==  d)#True



# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)#{10,20}
print(type(c))#<class 'set'>
d = a - b
print(d)##{10,20}
print(type(d))#<class 'set>'
print(c  is  d)#False
print(c  ==  d)#True

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10,20,50,60}
print(type(c))#<class 'set'>
d = a ^ b
print(d)#{10,20,50,60}
print(type(d))#<class 'set'>
print(c   is   d) #False
print(c  ==   d)#True
# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)#{0,1,4,,9,16,25,36,49,64,81}
print(type(a))#<class 'sest'>
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
# a=input("Enter a string:")
# a=a.upper()
# c=set()
# d=''
# for x in set(a):
# 		c.add(x)
# d="".join(c)
		
# print("string without duplicates :",d)


'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set
1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
2) Both  input  and  output  are  lists
'''
a=eval(input("enter a list:"))
b=set()
result=[]
for x in set(a):
        if x not in b:
        	b.add(x)
result=list(b)
print("list without duplicates:",result)


	


'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]
2) Both  input  and  output  are  lists
'''
a=eval(input("enter a list:"))
b=eval(input("enter a list:"))
c=set(a).intersection(set(b))
d=list(c)
print("list without duplicates:",d)
'''

