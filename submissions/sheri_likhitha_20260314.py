# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)	#25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(type(a))	#<class 'tuple'>
a[3] = 'Sec'	#error because tuple does not support item assignment
a[3 : 6] = 60 , 70 , 80	    #error because tuple does not support item assignment



#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))	#(1,2,3) #address of the (1,2,3) object
a += b			
print(a , id(a))	#(1,2,3,4,5,6) #address of the (1,2,3,4,5,6) object


#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))	#(1,2,3) #address of the (1,2,3) object
a = a + b
print(a , id(a))	#(1,2,3,4,5,6) #address of the (1,2,3,4,5,6) object



#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)	#10,20,30,40
print(type(a))	#<class 'string'>
b = eval(a)	
print(b)	#(10,20,30,40)
print(type(b))	#<class 'tuple'>
print(len(b))	#4


# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)	#(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]		#error because tuple does not support item assignment
print(a)


# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)	  #(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90]  #error because tuple does not support item assignment
print(a)


# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)	#25,10.8,'Hyd',True
print(type(x))	#<class tuple>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)	#25
print(b)	#10.8
print(c)	#'Hyd'
print(d)	#True
p , q , r =  x	#error too many values to unpack
a , b , c , d  , e = x	#error no enough values to unpack


# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)	#25
print(b)	#10.8
print(c)	#['Hyd',True]
print(type(c))	#<class 'list'>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)	#25
print(b)	#[10.8,'Hyd']
print(c)	#True


# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)	#25
print(b)	#10.8
print(c)	#[]
print(d)	#'Hyd'
print(e)	#True


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)	#25
print(b)	#10.8
print(_)	#(3+4j)
print(d)	#True
print(_)	#(3+4j)


# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)	#(100,110,120,130,140)
print(type(b))	#<class'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)	#(10,20,15,18)
e = tuple('Vamsi')
print(e)	#('v','a','m','s','i')
print(tuple(25))	#error int object is not sequence
print(tuple())		#empty tuple ()



#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)	#15 is found at index : 2
		i = a . index(15 , i + 1)		#15 is found at index : 5
except:							#15 is found at index : 8  
		print(F'15  is  found  {a . count(15)}  times')	#15 is found 3 times



#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35	#error
print(a)
print(id(a))
How  to  modify  30  in  tuple  to  35
a=a[:2]+(35,)+a[3:]
print(a)
print(id(a))



# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)
del  a[2]
a . pop(2)
print(a)
print(id(a))
How  to  remove  30  from  tuple  'a'
tuple=a[:2]+a[3:]
print(tuple)
print(id(a))
print(id(tuple))



#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print(a[0])	#How  to  print  1st  inner  tuple
print(a[1])	#How  to  print  2nd  inner  tuple
print(a[2])	#How  to  print  3rd  inner  tuple
print(a[0][1])	#How  to  print  20
print(a[1][2])	#How  to  print  50
print(a[2][3])	#How  to  print  90



# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])	#How  to   print  inner  tuple
print(a[-1])	#How  to   print  inner  tuple  in  another  way
print(a[0][0])	#How   to  print   10
print(a[0][1])	#How   to  print   20
print(a[0][2])	#How   to  print   30
b = ((),)
print(b[0])	#How  to   print  inner  tuple  of  tuple  'b'
print(b[-1])	#How  to   print  inner  tuple  of  tuple  'b'  in  another  way



#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)	#(10,20,30)
print(*a)	#10,20,30
b = (())
print(b)	#()
print(*b)	#empty tuple


# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)	#{10,20,15,18,20,12,18}
print(type(a))	#<class 'str'>
b = eval(a)
print(b)	#{18, 20, 10, 12, 15}
print(type(b))	#<class 'set'>



#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})		#{(10,20,30)}
print({[10 , 20 , 30]})		#error
print({{10 , 20 , 30}})		#error
print({{}})			#error



# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
for element in a:
     print(element)



# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)	#{True,'Hyd',25}
print(len(s))	#3
print(type(s))	#<class 'set'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)	#{'Hyd',25,True,10.8}
a , b , c , d = s
print(a)	#25
print(b)	#10.8
print(c)	#Hyd
print(d)	#True


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) 	#{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)	#Hyd
print(b)	#[25,  True,  10.8]
print(type(b))	#<class 'list'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)	#{25, 'Hyd', 10.8, True}
a , *b , c = s
print(a)	#25
print(b)	#['Hyd', 10.8]
print(c)	#True


# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)	#{10,20}
x , y = s
print(x)	#10
print(y)	#20


# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)	#{130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)	#{10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e)	#{'a', 'A', ' ', 'm', 'o', 'R', 'r'}
print(set(25))	#error
print(set())	#set()



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
print(a)	#{None, True, 10.8, 'Hyd', 25}
a . add(10 , 20 , 30)	#error
a . add([10,20,30])	#error



# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)	#{25, 10.8, 'Hyd', True}
print(id(a))	#address of object a
a . add(tpl)
a . add('Sec')
print(a)	#{True, 10.8, (10, 20, 30), 'Sec', 25, 'Hyd'}
print(id(a))	#address of same object a
print(len(a))	#6
a . add([100 , 200 , 300])	#error
a . add(set())			#error
a . add({ })			#error


# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)	#{(10, 20, 15, 18)}
print(len(s))	#1


# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))	#4
print(s)	#{10, 18, 20, 15}
s . update(25)	#error



# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)	#{50, 20, 70, 40, 10, 60, 30}
print(len(s))	#7
s . add(a , b , c)	#error it takes only one argument


# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)	#{'o', 'a', 'm', ' ', 'R'}
print(len(a))	#5
a . update(3 + 4j , 10.8 , True)	#error complex object is not a sequence


# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)	#{10, 18, 20, 15}
b = a . copy()
print(b)	#{10, 18, 20, 15}
print(a  is  b)	#False
print(a  ==  b) #True
c = a
print(a  is  c)	#True



# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) 	#{25, 10.8, 'Hyd', True} 
print(a . pop())  #True  
print(a . pop())  #'Hyd'  
print(a . pop())  #10.8 
print(a . pop())  #25  
print(a . pop())  #error because empty list 
print(a)	  #set() 
b = {10 , 20 , 30 , 40}
print(b . pop(2)) #error it does not take argument 



# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) 	#{25, 10.8, 'Hyd', True} 
a . remove('Hyd')
print(a)	#{25, 10.8, True}  
a . remove('Sec')	#error   



# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)	#{25, 10.8, True, 'Hyd'}
a . discard('Hyd')
print(a)	#{25, 10.8, True}
a . discard('Sec')
print(a)	#error
a . remove('Sec')	#error




# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))	#{40, 10, 50, 20, 60, 30}
print(a | b)		#error
print(b . union(a))	#error
print(a + b)		#error


#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)	#{40, 30}
print(type(c))	#<class 'set'>
d = a & b
print(d)	#{40, 30}
print(type(d))	#<class 'set'>
print(c  is  d)	#False
print(c  ==  d)	#True



# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)	#{10, 20}
print(type(c))	#<class 'set'>
d = a - b
print(d)	#{10, 20}
print(type(d))	#<class 'set'>
print(c  is  d) #False
print(c  ==  d) #True


# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)	#{10, 50, 20, 60}
print(type(c))	#<class 'set'>
d = a ^ b
print(d)	#{10, 50, 20, 60}
print(type(d))	#<class 'set'>
print(c   is   d)  #False
print(c  ==   d)   #True



# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)	#{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a))	#<class 'set'>



a=input("Enter the string: ")
print(set(a))


a=eval(input("Enter the string: "))
print("list without duplicates:",set(a))


a=eval(input("Enter 1st string: "))
b=eval(input("Enter 2nd string: "))
result=list(set(a) & set(b))
print("common between the two lists:",result)