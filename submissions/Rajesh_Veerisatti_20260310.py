
#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) # True
print(a  ==  b) # True
b[2] = 12
print(a)  # [10, 20, 12, 18]
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[10, 20, 15, 18, 100, 200, 150]
# print(a + 5) # error int is not allowed to concate nate to list
# print(a + '5') # error str is not allowed to concate nate to list
# print([10 , 20] + (30 , 40))  # error tuples is not allowed to concate nate to list
# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) # [1, 2, 3] address of object a
a += b
print(a , id(a)) # [1, 2, 3, 4, 5, 6] new adrees of object a
# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) # [1, 2, 3] address of object a
a  = a + b
print(a , id(a)) # [1, 2, 3, 4, 5, 6] new adrees of object a

# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) # a :  25
print('b : ' , b) # b :  [10.8, 'Hyd']
print('c : ' , c) # c: True
print(type(b)) # <class list>
x , *y = list
print('x : ' , x) # x :  25
print('y : ' , y) # y :  [10.8, 'Hyd', True]
*p , q = list
print('p : ' , p) # p :  [25, 10.8, 'Hyd']
print('q : ' , q) # q :  True 
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
 # a , b , c , d , e = list # error there is no exists elements in list
 #v a , b , *c , d , e = list # error there is no exists elements in list
print('a : ' , a) # a : 25 
print('b : ' , b) # b : [10.8 , "hyd"]
print('c : ' , c) # c; true
# print('d : ' , d) # error there is no exists elements in list
 # print('e : ' , e) # error there is no exists elements in list
 # a , b , *c , d , e , f = list # error there is no exists elements in list
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) # a :  25
print('b : ' , b) #  b :  10.8
print('_ :  ' , _) #  _ :   Hyd
print('d : ' , d) # d :  True
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) # a :  (3+4j)
print('b : ' , b) # b :  10.8
print('d : ' , d) #  d :  True
#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) # a :  25
print('b : ' , b) # b :  10.8
print('_ : ' , _) # _ :  (3+4j)
print('d : ' , d) # d : True
print('_: ' , _)  #_ :  (3+4j)
# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
# a , *b , c , *d , e  = list # Two stars are not allowed
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) # a :   [25, 10.8]
print('b :  ' , b) #  b :   Hyd
print('c :  ' , c) # c :   True
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # a :  25
print('b : ' , b) #  b :  10.8
print('c : ' , c) # c :  Hyd
print('d : ' , d) # d :  True
 # a , b , c , d = list # thre are no 4 existing elements
# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # True
print(a  is   b) # False
print(a < c) # True
print(a > d) # True
print(a >= c) # False 
print(a <= d) # False
print(a != c) # True
print(a != b) # False
print(a == c) # False
# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # False
print(a  is   b) # False
#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # 4
b = []
print(len(b)) # 0
c = [[10 , 20] , 30 , 40]
print(len(c)) # 3


'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # 25+10.8+1-->36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # 8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # 39.8+4j
d = [10 , 20 , 15 , 18]
print(sum(d)) # 63
e = [25 , 10.8 , 'Hyd' , True]
# print(sum(e)) # error sum funtion not allows str


'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
[[b,c,d,e]]=a
#print(sum(a))# print(sum(a))  
 # print(How  to  determine  sum  of  inner  list  elements)
 # print(How  to  determine  sum  of  inner  list  elements  in  another  way)
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
 # print(max(c)) # error complex +int  is not supported
d = [25 , '35']
 # print(max(d)) #  error str and int not allowed to compare
 # print(max([])) # error elements should be more than 2
# print(min([]))


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''

# list()  function  demo  program
a = (10 , 20 , 15, 18)
# b = list(a)
 # print(b)
 #print(type(b))
 #print(a  is  b) # Error 
 #print(a == b) # error
#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
# b = list(a)
 # print(b) # error
 # error print(type(b))
 # a = list('Vamsi')
print(a) # range(4, 10, 2)
 #a = list() # error
print(a)  # range(4, 10, 2)
# print(list(25)) # error
# print(list(10.8)) # Error
 # print(list(True)) # error
 #print(list(None)) 



'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  --->  Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
# print(list(a)) # Error
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
 # print(list(b)) # Error
c = ([10 , 20] , (30 , 40) , {50 , 60})
 # print(list(c)) # Error 
# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a) # [5, 10, 12, 15, 20]
print(b) #[5, 10, 12, 15, 20]
print(type(b)) # <class list>
c = sorted(a , reverse = True)
print(c) # [20, 15, 12, 10, 5]
print(a) #  [10 , 20 , 15 , 5 , 12]



'''
sorted()  function
---------------------
1) What  does  sorted(list)  do  ?  --->  Sorts  elements  of  the  list  in  ascending  order

2) Where  are  the  results  stored  ?  --->  In  another  list

3) Is  argument  list  modified ?  --->  No  and  it  remains  unchanged

4) How  to  sort  list  in  descending  order ?  --->  sorted(list , reverse = True)

5) What  are  the  two  arguments  of  sorted()  function ?  ---> List  to  be  sorted
																												and
																					                 reverse = True  which  is  an  optional  argument
'''
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) #['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
# all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))  # True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) # False
d = [10 , 0 , 20]
print(all(d)) # false
e = []
print(all(e)) # True


'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''
# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) # True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) # False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) # True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # False
e = []
print(any(e)) # False


'''
any()   function
-------------------
1) What  does  any(list)  do ?  --->  Returns  True  when  at  least  one  element  of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  every  element  of  the  list  is  false

3) if  cond1  or  cond2  or  cond3  or  cond4:
     How  to  reduce  the  four  conditions  to  a  single  condition ?  ---> if  any([cond1 , cond2 , cond3 , cond4]):

4) all()  and  any()  functions  are  used  as  an  alternative  when  there  are  too  many  conditions  in  if  and  while
'''
# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del    a[2]
print(a) # [10 , 20 ,  18]
# del  a[3] # error index out of range
del  a
 #print(a) # a is already del
#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . append(19) 
print(list) # [10 , 20 , 15 , 18, 19]
#  Find  outputs (Home  work)
list = []
print(list) # []
list . append(25) 
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) # [25, 10.8, 'Hyd', True]
# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) # [0, 10, 20, 30, 40]
#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) # [10, 20, 30, 'Hyd']
print(len(a)) # 4
 # print(How  to  print  4th  element  of  list  'a')
 # print(How  to  print  'H')
# print(How  to  print  'y')
 # print(How  to  print  'd')
#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a) # [10, 20, [50, 60, 70], 30, 40]
print(len(a)) # 5
# print(How  to  print  inner  list)
# print(How  to  print  50)
# print(How  to  print  60)
# print(How  to  print  70)
# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list) # [10, 20, 18, 15, 12, 15, 19]
	list . remove(25) # error and except suite is excuted
except:
	print('25  is   not  in  the  list')



'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  ---> Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Raises  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->  Call  remove()  method  in  a  loop
'''
'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''

a = eval(input(" enter list of elements: "))
b=int(input("Enter del num: "))

while b in a:
	a.remove(b)
print (f"list witout {b}'s:{a}") # [10, 20, 18, 19, 17, 20, 14]