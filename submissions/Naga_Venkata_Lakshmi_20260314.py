# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)  #(25 , 10.8 , 3+4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a)) #<class 'tuple'>
a[3] = 'Sec' #tuple object does not support item assignment.
a[3 : 6] = 60 , 70 , 80  #tuple object does not support item assignment.


#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1 , 2 , 3)  Address of tuple a
a += b
print(a , id(a)) #(1 , 2 , 3 , 4 , 5 , 6)  Address of tuple with six elements.


#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #(1 , 2 , 3)  Address of tuple a.
a = a + b
print(a , id(a)) #(1 , 2 , 3 , 4 , 5 , 6)  address of tuple with six elements.


#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) #"(10 , 20 , 30 , 40)"
print(type(a)) #<class 'str'>
b = eval(a) #(10 , 20 , 30 , 40)
print(b) #(10 , 20 , 30 , 40)
print(type(b)) #<class 'tuple'>
print(len(b)) #4



# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) #(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]
print(a) #(10 , [80 , 90 , 100] , 50 , 60)



# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a) #Type error
a[1] = [80 , 90]
print(a) #[10 , [80 , 90] , 50 , 60]


# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25 , 10.8 , 'Hyd; , True)
print(type(x)) #<class 'tuple'>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25
print(b) #10.8
print(c) #'Hyd'
print(d) #True
p , q , r =  x #Error
a , b , c , d  , e = x #Error


# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a) #25
print(b) #10.8
print(c) #('Hyd' , True)
print(type(c)) #<class 'tuple'>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) #25
print(b) #(10.8 , 'Hyd')
print(c) #True

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) #25
print(b) #10.8
print(c) #('Hyd')
print(d) #True
print(e) #Error

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) #25
print(b) #10.8
print(_) #'Hyd'
print(d) #True
print(_) #3+4j


# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b) #(100 , 110 , 120 , 130 , 140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) #(10 , 20 , 15 , 18)
e = tuple('Vamsi')
print(e) #('V' , 'a' , 'm' , 's' , 'i')
print(tuple(25)) #Error it should be sequence here 25 is non-sequence.
print(tuple()) #()


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


#outputs
2
4
7
15 is found at 3 times.




#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a_list = list(a)
a_list[2]  = 35
a = tuple(a_list)
print(a)
print(id(a))




# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a = list(a)
a.remove(30)
a = tuple(a)
print(a, id(a))



#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)  #( (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90) )
print(type(a)) #<class 'tuple'>
print(len(a)) #3
print(a[0])
print(a[1])
print(a[2])
print(a[0][1])
print(a[1][2])
print(a[2][3])


# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])
print(a[1])
print(a[2])
print(a[0][1])
print(a[2][3])
b = ((),)
print(b[0])
for inner in b:
    print(inner)



#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)#((10 , 20 , 30))
print(*a) #(10 , 20 , 30)
b = (())
print(b) #()
print(*b) 


# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) #'{10 , 20 , 15 , 18 , 20 , 12 , 18}'
print(type(a)) #<class 'str'>
b = eval(a) 
print(b) #{10 , 20 , 15 , 18 , 20}
print(type(b)) #<class 'set'>


#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) #{(10 , 20 , 30)}
print({[10 , 20 , 30]}) # set cannot have mutable elements.
print({{10 , 20 , 30}}) #{10 , 20 , 30}
print({{}}) #{set()}



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
print(s) #{'Hyd' , True , 25}
print(len(s)) #3
print(type(s)) #<class 'set'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd' , 25 , True , 10.8}
a , b , c , d = s
print(a) #'Hyd'
print(b) #25
print(c) #True
print(d) #10.8


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd' , 25 , True , 10.8} 
a , *b = s
print(a) #'Hyd'
print(b) #{25 , True , 10.8}
print(type(b)) #<class 'set'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd' 25 , True , 10.8}
a , *b , c = s
print(a) #'Hyd'
print(b) #{25 , True}
print(c) #10.8

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)  #{20 , 10}
x , y = s
print(x) #20
print(y) #10






# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a) #{100 , 110 , 120 , 130 , 140 , 150}
print(b) #{100 , 110 , 120 , 130 , 140 , 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) #{10 , 20 , 15 , 18 , 50 , 12}
e = set('Rama  rAo')
print(e) #{' ' , 'r' , 'R' , 'a' , 'm' , 'A' , 'o'}
print(set(25)) #Error it should be sequence only.
print(set()) #set()


# add()  method  demo  program  (Home  work)
a = set()
a . add(True) #{True}
a . add(25) #{True , 25}
a . add(10.8) #{True , 25 , 10.8}
a . add(1) #{True , 25 , 10.8 , 1}
a . add('Hyd') #{True , 25 , 10.8 , 1 , 'Hyd'}
a . add(25) #duplicates are ignored.
a . add(None) #{True , 25 , 10.8 , 1 , 'Hyd' , None}
a . add('Hyd') #duplicates are ignored.
a . add(1.0) #duplicates are ignored.
print(a) #{True , 25 , 10.8 , 1 , 'Hyd' , None}

a . add(10 , 20 , 30) #{True , 25 , 10.8 , 1 , 'Hyd' , None , (10 , 20 , 30)}
a . add([10,20,30]) #set cannot take mutable elements.



# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) #{25 , 10.8 , 'Hyd' , True}
print(id(a)) #Address of set a.
a . add(tpl) #{25 , 10.8 , 'Hyd' , True , (10 , 20 , 30)}
a . add('Sec') #{25 , 10.8 , 'Hyd' , True , (10 , 20 , 30) , 'Sec'}
print(a) #{25 , 10.8 , 'Hyd' , True , (10 , 20 , 30) , 'Sec'}

print(id(a)) #Address of set with 6 elements.
print(len(a)) #6
a . add([100 , 200 , 300]) #set cannot have mutable elements.
a . add(set()) #set cannot have mutable elements.
a . add({ }) #set cannot have mutable elements.



# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) #{ (10 , 20 , 15 , 18) }
print(s) #{ (10 , 20 , 15 , 18) }

print(len(s)) #1

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) #{10 , 20 , 15 , 18}
print(len(s)) #4
print(s) #{10 , 20 , 15 , 18 }

s . update(25) #Error


# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) #{10 , 20 , 30 , 40 , 50 , 60 , 70}
print(len(s)) #7
s . add(a , b , c) #Error


# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao') #{'R' , 'a' , 'm' , ' ' , 'Rao'}
print(a) #{' ' , 'R' , 'a' , 'm' , 'o'}
print(len(a)) # 5
a . update(3 + 4j , 10.8 , True) #{' ' , 'R' , 'a' , 'm' , 'o' , (3+4j) , 10.8 , True}


# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
b = a . copy()
print(b) # {10 , 20 , 15 , 18} 
print(a  is  b) # False
print(a  ==  b) #True
c = a
print(a  is  c) #True


# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True} 
print(a . pop())  
print(a . pop())  
print(a . pop())  
print(a . pop())  
print(a . pop()) 
print(a) # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2)) #{10 , 20 , 40} 


# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}  
a . remove('Hyd') #{25 , 10.8 , True}
print(a)  #{25 , 10.8 , True}
a . remove('Sec')  #Error  


# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a) #{25 , 10.8 , True}
a . discard('Sec') #{25 , 10.8 , True}
print(a) #{25 , 10.8 , True}
a . remove('Sec') #Error


# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
a . clear()
print(a) #set()
print(len(a)) #0


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) #{10 , 20 , 30 , 40 , 50 , 60}
print(a | b) #{10 , 20 , 30 , 40 , 50 , 60}
print(b . union(a)) #{10 , 20 , 30 , 40 , 50 , 60}
print(a + b) #Type error


#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b) #{30 , 40}
print(c) #{30 , 40}
print(type(c)) #<class 'set'>
d = a & b #{30 , 40}
print(d) #{30 , 40}
print(type(d)) #<class 'set'>
print(c  is  d) #False
print(c  ==  d) #True


# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) #{10 , 20}
print(c) #{10 , 20}
print(type(c)) #<class 'set'>
d = a - b #{10 , 20}
print(d) #{10 , 20}
print(type(d)) #<class 'set'>
print(c  is  d) #False
print(c  ==  d) #True


# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) #{10 , 20 , 50 , 60}
print(type(c)) #<class 'set'>
d = a ^ b
print(d) #{10 , 20 , 50 , 60}
print(type(d)) #<class 'set'>
print(c   is   d) #False
print(c  ==   d) #True


# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) #{0 , 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81}
print(type(a)) #<class 'set'>


s = input("Enter a string:  ")
result = set(s)
output = "".join(result)
print("String after removing duplicate characters:" , ouput)


lst = list(map(int, input("Enter list elements separated by space:  ").split()))

unique_list = list(set(lst))

print("List after removing duplicate elements:" , unique_list)


list1 = eval(input("Enter elements of first list:  "))
list2 = eval(input("Enter elements of second list:  "))

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

print("Common elements are:", list(common))

























