1.
#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) # True
print(a  ==  b) # True
b[2] = 12
print(a) # [10, 20, 12, 18]



2.
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # [10, 20, 15, 18, 100, 200, 150]
print(a + 5) # TypeError: can only concatenate list (not 'int') to list
print(a + '5') # TypeError: can only concatenate list (not "str") to list
print([10 , 20] + (30 , 40)) # TypeError: can only concatenate list (not "tuple") to list



3.
# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) # [1, 2, 3] <some memory address>
a  = a + b
print(a , id(a)) # [1,2,3,4,5,6] <some diffrent memoty address>


4.
# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) # [1,2,3] <some memory address>
a += b
print(a , id(a)) # [1,2,3,4,5,6] <same memory address>



5.
# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) # a : 25
print('b : ' , b) # b : [10.8, 'Hyd']
print('c : ' , c) # c : True
print(type(b)) # <class 'list'>
x , *y = list
print('x : ' , x) # x : 25
print('y : ' , y) # y : [10.8, 'Hyd', True]
*p , q = list
print('p : ' , p) # p : [25, 10.8, 'Hyd]
print('q : ' , q) # q : True


6.
# # Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list # valueError: 5 variables <-- 4 values
a , b , *c , d , e = list
print('a : ' , a)  # a : 25
print('b : ' , b)  # b : 10.8
print('c : ' , c)  # c : []
print('d : ' , d)  # d : 'Hyd'
print('e : ' , e)  # e : True
a , b , *c , d , e , f = list # ValueError: not enough values to unpack (expected 6, got 4)



7.
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) # a : 25
print('b : ' , b)  # b : 10.8
print('_ :  ' , _) # _ : Hyd
print('d : ' , d) # d : True


8.
# Find  outputs (Home  work)
      # 0    1       2       3         4
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) # 3 + 4j
print('b : ' , b) # 10.8
print('d : ' , d) # True



9.
#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) # a : 25
print('b : ' , b) # b : 10.8
print('_ : ' , _) # _ : 3 + 4j
print('d : ' , d) # d : True
print('_: ' , _) # _ : (3 + 4j)


10.
# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list # syntaxError : two starred expressions in assignment
                            # in python only one * unpacking is allowed in assignment



11.
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) # a: [25, 10.8]
print('b :  ' , b) # b : Hyd
print('c :  ' , c) # c : True



12.
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # a : 25
print('b : ' , b) # b : 10.8
print('c : ' , c) # c : 'Hyd'
print('d : ' , d) # d : True
a , b , c , d = list  # ValueError: not enough values to unpack (expected 4, got 3)



13.
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



14.
# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # False
print(a  is   b) # False



15.
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


16.
#sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # (8 + 11j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) # 63 
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # TypeError: unsupported operand type(s) for +: 'float' and 'str'
'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''


17.
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a)) # sum([[10 , 20 , 15 , 18]])
              # 0 + [10,20, 15, 18]
              # typeError: unsupported operand type(s) for +: 'int' and 'list'
print(How  to  determine  sum  of  inner  list  elements)    # print(sum(a[0])) # 63
print(How  to  determine  sum  of  inner  list  elements  in  another  way) #
# print(sum(a[0][0]) + sum(a[0][1]) + sum(a[0][2]) + sum(a[0][3])) # 63



18.
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # 'Vamsi'
print(min(b)) # 'Amar'
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) # TypeError: '>' not supported between instances of 'complex' and 'int'
d = [25 , '35']
print(max(d)) # TypeError: '>' not supported between instances of 'str' and 'int'
print(max([])) # ValueError: max() iterable argument is empty
print(min([])) # ValueError: min() iterable argument is empty
'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''


19.
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) # [10,20,15,18]
print(type(b)) # <class 'list'>
print(a  is  b) # False 
print(a == b) # False 


20.
#  Find  outputs (Home  work)
a = range(4 , 10 , 2) 
b = list(a) 
print(b) # [4 , 6, 8]
print(type(b)) # <class 'list'>
a = list('Vamsi')
print(a) # ['V' , 'a' , 'm' , 's' , 'i']
a = list()
print(a) # []
print(list(25)) # TypeError: 'int' object is not iterable
print(list(10.8)) # TypeError: 'float' object is not iterable
print(list(True)) # TypeError: 'bool' object is not iterable
print(list(None)) # TypeError: 'NoneType' object is not iterable
'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  --->  Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''


21.
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))

print(list(a)) # [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]

b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}

print(list(b)) # [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]

c = ([10 , 20] , (30 , 40) , {50 , 60})

print(list(c)) # [[10 , 20] , (30 , 40) , {50 , 60}]


22.
# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a) # [5, 10, 12, 15, 20]
print(b)
print(type(b)) # <class 'list'>
c = sorted(a , reverse = True)
print(c) # [20, 15, 12, 10, 5]
print(a) # [10 , 20 , 15 , 5 , 12]
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



22.
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)  # ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']



23.
# all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) # True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) # False
d = [10 , 0 , 20]
print(all(d)) # False
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


24.
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


25.
# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20, 15, 18]
del    a[2] 
print(a) # [10, 20, 18]
del  a[3] # IndexError: list assignment index out of range
del  a
print(a) # NameError: name 'a' is not defined



26.
#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10, 20, 15, 18]
list . append(19)
print(list) # [10 , 20 , 15 , 18, 19]



27.
#  Find  outputs (Home  work)
list = []
print(list) # []
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) # [25, 10.8, 'Hyd', True]


28.
# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) # [0, 10, 20, 30, 40]


29.
#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) # [10, 20, 30, 'Hyd']
print(len(a)) # 4
print(How  to  print  4th  element  of  list  'a') # print(a[3])
print(How  to  print  'H') # print(a[3][0])
print(How  to  print  'y') # print(a[3][1])
print(How  to  print  'd') # print(a[3][2])



30.
#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a) # [10, 20,[50, 60, 70], 30, 40]
print(len(a)) # 
print(How  to  print  inner  list) # print(a[2])
print(How  to  print  50) # print(a[2][0])
print(How  to  print  60) # print(a[2][1])
print(How  to  print  70) # print(a[2][2])



31.
# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)
	list . remove(25)
except:
	print('25  is   not  in  the  list')
	
	#o/p: [10, 20, 18, 15, 12, 15, 19]
    #     25 is not in the list
'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  ---> Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Raises  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->  Call  remove()  method  in  a  loop
'''



32.
'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''
list = [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
x = 15
while x in list:
    list.remove(x)
    print(list)



33.
#  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2))
print(a) # [10, 20, 18, 12]
print(a . pop(len(a))) # IndexError: pop index out of range
print(a . pop(-3)) # IndexError: pop index out of range
print(a) # [10, 20, 18, 12]
print(a . pop(-4)) # IndexError: pop index out of range
print(a . pop()) # 12
print(a) # [10, 20, 18]
b = []
b . pop() # IndexError: pop from empty list

'''
pop()   method
------------------
1) What  does  pop(index)  do ?  --->  Removes  element  at  the  specified  index  and  returns  the  deleted   element

2) What  does  pop(invalid-index)  do  ?  --->  Raises  IndexError

3) What  does  pop(No-args)  do ?  --->  Removes  last  element  of  the  list  and  returns  the  deleted  element

4) How  many  arguments  can  pop()  method  take ?  --->  1  (or)  0

5) What  does  pop(No-args)  do  when  list  is  empty ?  --->  Raises  error

6) del  list[index]
    list . pop(index)
    What  is  the  difference  between  the  two  statements ?  --->
											del  operator  removes  element  but  does  not  return  the  deleted  element
											whereas  pop()  method  not  only  deletes  element  but  also  returns  the  deleted  element
'''



34.
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10, 20, 15, 18]
list . clear()
print(list) # []
'''
clear()  method
------------------
1) What  does  clear()  method  do ?  ---> Removes  all  the  elements  of  the  list  and  list  becomes  empty

2) What  about  remove()  and  pop()  methods  ?  --->  They  remove  single  element  of  the  list
'''



35.
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10, 20, 15, 18]
a . reverse()
print(a) # [18, 15, 20, 10]
'''
reverse()  method
---------------------
1) What  does  reverse()  method  do ?  --->  Reverses  all  the  elements  of  list

2) Where  are  the  results  stored ?  ---> In  the  same  list  replacing  existing  elements (List  is  mutable)
'''


36.
#  sort()  method  demo  program (Home  work)
# list = [10 , 20 , 15 , 18 , 5]
# print(list) # [10, 20, 15, 18, 5]
# list . sort()
# print(list) # [5, 10, 15, 18, 20]
# list . sort(reverse = True)
# print(list) # [20, 18, 15, 10, 5]



37.
# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']


38.
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() # TypeError: '<' not supported between instances of 'str' and 'int'


39.
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) # 0
print(len(a)) # 9
'''
What  does  list . count(x)  do ?  --->  Returns  number  of  times  'x'  is  in  the  list
'''


40.
'''
Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  --->  [15 , 14 , 18 , 19]

Element         count               Action
---------------------------------------------
  10                  3                       Ignore
  
  20                  2                       Ignore
  
  15                  1                       [15]
  
  14                  1                       [15 , 14]
  
  18                  1                       [15 , 14 , 18]
  
  19                  1                       [15 , 14 , 18 , 19]
'''
list = [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
result = []
for x  in list:
    if list.count(x) == 1:
        result.append(x)
        print(result)



41.
'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  --->  All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->  All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3
'''
list = [10, 10, 20, 10]
if list.count(list[0]) == len(list):
    print('All  the  elements  are  identical')
else:
    print('All  the  elements  are  not  identical')
