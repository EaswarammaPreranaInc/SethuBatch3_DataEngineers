#python Homwork

# 1 . #  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)  # output is True .because reference is same.
print(a  ==  b)  # output is True. because list as same a values assigned to b .
b[2] = 12 # output : 15 replace the 12.
print(a) # output : [10 ,20 ,12 , 18]


# 2 . #  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # output : [10, 20, 15, 18, 100, 200, 150]
# print(a + 5) # output : TypeError : beacuse can only concatinate list (not "Int")
#print(a + '5')  # output : TypeError : can only concatinate list (not 'str')
#print([10 , 20] + (30 , 40)) # output : TypeError : can only concatinate list (not "tuple")


# 3 # Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) # output : [1,2,3]<space>Address of the object a.
a += b # output : [1,2,3,4,5,6]
print(a , id(a)) # output :[1,2,3,4,5,6]<space>Address of the object a.


# 4 . # Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) # output : [1,2,3]<space> Address of the object a .
a  = a + b # [1, 2, 3, 4, 5, 6] here list is concatinated
print(a , id(a)) # output : [1, 2, 3, 4, 5, 6]<space> Address of the another object a.

# 5 . # Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) # output : 25
print('b : ' , b) # output : [10.8, 'Hyd']
print('c : ' , c) # output : True
print(type(b)) # output : <class list>
x , *y = list  
print('x : ' , x) # output : 25
print('y : ' , y) # [10.8, 'Hyd', True]
*p , q = list 
print('p : ' , p) # output : [25, 10.8, 'Hyd']
print('q : ' , q) # output :True


 #6 . # Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list # output : ValueError (expect is 5 , but here got 4)
#a , b , *c , d , e = list # output : ValueError (excpected is 5 , but got 4)
#print('a : ' , a) # output : a is not defined.
#print('b : ' , b)
#print('c : ' , c)
#print('d : ' , d)
#print('e : ' , e)
a , b , *c , d , e , f = list # output is ValueError.


#7 . # Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True] 
a , b , _  , d = list # a = 25, b=10.8, _='Hyd', d=True
print('a : ' , a) # output : 25
print('b : ' , b) # output : 10.8
print('_ :  ' , _) # output : 'Hyd'
print('d : ' , d) # output : True

#8 . # Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list # a=25, b=10.8, a='Hyd', d=True, a=3+4j
print('a : ' , a) # output : 3+4j
print('b : ' , b) # output : 10.8
print('d : ' , d) # output : True


#9.#  Tricky  program
#Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list # a=25, b=10.8, _='Hyd', d=True, _=3+4j
print('a : ' , a) # output : 25
print('b : ' , b) # output : 10.8
print('_ : ' , _) # output : 'Hyd'
print('d : ' , d) # output : True
print('_: ' , _)  #output : 3+4j


#10 . # Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
#a , *b , c , *d , e  = list # syntaxerror : because multiple starred expressions in assignment


#11 . # Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list # a=[25,10.8], b= 'Hyd', c=True
print('a :  ' , a) # output : [25,10.8]
print('b :  ' , b) #  output : 'Hyd'
print('c :  ' , c) # output : True


#12 . Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) #output : 25
print('b : ' , b) # output : 10.8
print('c : ' , c) # output : 'Hyd'
print('d : ' , d) # output : True
a , b , c , d = list # output : valueError


#13 . # Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # output : True
print(a  is   b) # output : False
print(a < c) # output : True
print(a > d) # output : True
print(a >= c) # output : False
print(a <= d) # output : False
print(a != c) # output : True
print(a != b) #  output : False
print(a == c) # output : False


#14 . # Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # output : False
print(a  is   b)  # output : False

#15 . #  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # output : 4
b = [] # empty list 0
print(len(b)) # empty list 0
c = [[10 , 20] , 30 , 40]
print(len(c)) # 3
#What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list 


#16 . # sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # output : 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # output :8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # output : (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) # output : 63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # output : Tyeperror 
#What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements


#17 . #  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a)) # output : TypeError : because 'int' and 'list' sequence and non-sequence
#print(How  to  determine  sum  of  inner  list  elements)
a = [[10,20,15,18]]
total = 0
for i in a[0]:
    total = total+i
    print(total)
#print(How  to  determine  sum  of  inner  list  elements  in  another  way)
a = [[10,20,15,18]]
total = 0
for i in a:
    for j in i:
        total += j
        print(total)


#18 . # max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # output : 30
print(min(a)) # output : 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # output : vamsi
print(min(b))# output : Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) # output : TyepeError : not supported between the 'complex' and 'int'.
d = [25 , '35']
print(max(d)) # output : TyepeError : not supported between 'str' and 'int'.
print(max([])) # output : Valueerror : there is no argument
print(min([])) # output : Valueerror : there is no argument
#1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

#2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list


 #19 . # list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a) # [10, 20, 15, 18]
print(b) # output :[10,20,15,18]
print(type(b)) # output : <class 'list'>
print(a  is  b) # output : False
print(a == b) # output : False


#20 . #  Find  outputs (Home  work)
a = range(4 , 10 , 2) # 4 , 5 , 6 , 7 , 8 , 9 , 10 => 4 , 6 , 8
b = list(a) # [4,6,8]
print(b) # output : [4,6,8]
print(type(b)) # output : <class 'list'>
a = list('Vamsi') 
print(a) # ['v','a','m','s','i']
a = list() # empty tuple convert to empty list
print(a) # output : []
print(list(25)) # output : TypeError
print(list(10.8)) # output : TypeError
print(list(True)) # output : TyepeError
print(list(None)) # output : TyepeError 


#21 .  Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) # output : [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) # output : [(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) # output : [[10, 20], (30, 40), {50, 60}]


#22 .
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b) # output : [5, 10, 12, 15, 20]
print(type(b)) # output : <class 'list'>
c = sorted(a , reverse = True)
print(c) # output : [20, 15, 12, 10,5]
print(a) # output : [10,20, 15, 5, 12]


#23 . # Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) # output : ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) # output : ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # output : ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']


#24 . # all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) # output : True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # output : False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) # output : False
d = [10 , 0 , 20]
print(all(d)) # output : False
e = []
print(all(e)) # output : True


#24 . # del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # output : [10, 20, 15, 18]
del    a[2]
print(a) # output : [10, 20, 18]
#del  a[3]
#del  a # output : IndexError
print(a) # output : [10,20,18]


#25 #  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # output : [10 , 20 , 15 , 18]
list . append(19) # 19 add to in the above list
print(list) # output : [10,20,15,18,19]


# 26 . #  Find  outputs (Home  work)
list = []
print(list) # output : []
list . append(25) # output : [25]
list . append(10.8) # output : [25,10.8]
list . append('Hyd') # output : [25,10.8,'Hyd']
list . append(True) # output : [25,10.8,'Hyd','True]
print(list) # output : [25,10.8,'Hyd','True]


#27 . # Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) # output : [0,10,20,30,40]


#28 . #  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) # output : [10, 20, 30,'Hyd']
print(len(a)) # output : 4
# print(How  to  print  4th  element  of  list  'a') # output : print(a[3])
# print(How  to  print  'H') # print(a[3][0])
# print(How  to  print  'y') # print(a[3][1])
# print(How  to  print  'd') # print(a[3][2]])


#29 . #  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a) # output : [10, 20, [50, 60, 70], 30, 40]
print(len(a)) # output : 5
#print(How  to  print  inner  list)
# print(How  to  print  50)
# print(How  to  print  60)
# print(How  to  print  70)


# 30 . # remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list) # output : [10, 20, 18, 15, 12, 15, 19]
	list . remove(25) # output : 25  is   not  in  the  list
except:
	print('25  is   not  in  the  list')

#31  . #  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2)) # output : 15
print(a)  # output : [10, 20, 18, 12]
#print(a . pop(len(a))) # indexError
print(a . pop(-3)) # output : 20
print(a) # [10, 18, 12]
#print(a . pop(-4)) # output : IndexError
print(a . pop()) # output : 12
print(a) # output : [10,18]
b = []
# b . pop() # output : IndexError


#33 . # clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # output : [10, 20, 15, 18]
list . clear()
print(list) # output : []

#34 . # reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # output : [10 , 20 , 15 , 18]
a . reverse()
print(a) # output : [18 , 15 , 20 , 10]


#35 . #  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) # output : [10, 20, 15, 18, 5]
list . sort()
print(list) # output : [5, 10, 15, 18, 20]
list . sort(reverse = True)
print(list) # output : [20, 18, 15, 10, 5]


#36 . # Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # output : ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a . sort()
print(a) # output : ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a) # output : ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

#37 . # Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() # output : TypeError


# 38 . #  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # output : 3
print(a . count(25)) # output : 0
print(len(a))  # output : 9


# 39 . # Input list

#Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

# 1#) Let  input  be  [25 , 25 , 25 , 25]
#     What  is  the  output ?  --->  All  the  elements  are  identical
#     How  many  elements  are  in  the  list ?  ---> 4
#     How  many  times  is  first  element  repeated ?  ---> 4

# #2) Let  input  be  [10 , 10 , 20 ,  10]
#     What  is  the  output ?  --->  All  the  elements  are  not  identical
#     How  many  elements  are  in  the  list ?  ---> 4
#     How  many  times  is  first  element  repeated ? ---> 3

a = [25, 25, 25, 25]
length = len(a)
count = a.count(a[0])
if length == count:
    print("All the elements are identical")
else:
    print("All the elements are not identical")

print("How many elements are in the list? --->", length)
print("How many times is first element repeated? --->", count)



# 40 . Tricky  program
# Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
# Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
# What  is  the  output ?  --->  [15 , 14 , 18 , 19]

# Element         count               Action
# ---------------------------------------------
#   10                  3                       Ignore
  
#   20                  2                       Ignore
  
#   15                  1                       [15]
  
#   14                  1                       [15 , 14]
  
#   18                  1                       [15 , 14 , 18]
  
#   19                  1                       [15 , 14 , 18 , 19]


# output : a = [10, 20, 15, 10, 14, 10, 18, 20, 19]

result = []

for x in a:
    if a.count(x) == 1:
        result.append(x)

print("Output:", result)


#42 . ''
# Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

# Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
# 2nd  input  be  15
# What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

a = [10, 20, 15, 18, 19, 15, 17, 20, 15, 14]
x = 15

result = []

for i in a:
    if i != x:
        result.append(i)

print("Output:", result)