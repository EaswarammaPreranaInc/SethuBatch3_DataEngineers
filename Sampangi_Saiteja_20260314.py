""'
Tricky  program
Write  a  program  to  determine  mode

1) What  is  mode ?  --->  The  element  which  is  repeated  maximum  number  of  times  in  the  list

2) Let  input  be  [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  is  set(list) ?  --->  {12 , 20 , 18 , 15 , 10}
    How  many  times  is  first  element  12  repeated  in  the  list  ?  --->  1
    How  many  times  is  2nd  element  20  repeated  in  the  list  ?  --->  3
    How  many  times  is  3rd  element  18  repeated  in  the  list  ?  ---> 2
    How  many  times  is  4th  element  15  repeated  in  the  list  ?  --->  5
    How  many  times  is  last  element  10  repeated  in  the  list  ?  --->  4
    What  is  the  mode  ?  --->  15  becoz  it  is  repeated  max  number  of  times  i.e.  5

3) mode =   15
    ctr =  5
"""
lst = [12,20,18,15,10,15,10,15,20,18,15,10,20,15,10]

mode = None
ctr = 0

for i in set(lst):
    count = lst.count(i)
    if count > ctr:
        ctr = count
        mode = i

print("mode =", mode)
print("ctr =", ctr)
#------------------------------------------------------------------------------------------------
"""
#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print(How  to  print  1st  inner  list)
print(How  to  print  2nd  inner  list)
print(How  to  print  3rd  inner  list)
print(How  to  print  30)
print(How  to  print  80)
print(How  to  print  100)
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)
print(How  to  print  2nd   inner  list)
print(How  to  print  3rd   inner  list)
print(How  to  print  number  of  elements  in  1st  inner  list)
print(How  to  print  number  of  elements  in  2nd  inner  list)
print(How  to  print  number  of  elements  in  3rd  inner  list)

 #  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(???)
print('Each  inner  list   of   outer  list  without  indexes')
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (with  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (with  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)



 #  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print(How  to  print  1st  inner  list)
print(How  to  print  2nd  inner  list)
print(How  to  print  3rd  inner  list)
print(How  to  print  30)
print(How  to  print  80)
print(How  to  print  100)
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)
print(How  to  print  2nd   inner  list)
print(How  to  print  3rd   inner  list)
print(How  to  print  number  of  elements  in  1st  inner  list)
print(How  to  print  number  of  elements  in  2nd  inner  list)
print(How  to  print  number  of  elements  in  3rd  inner  list)

 #  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(???)
print('Each  inner  list   of   outer  list  without  indexes')
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (with  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (with  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)

"""

a = [[10 , 20 , 30 , 40] , [50 , 60 , 70 , 80] , [90 , 100 , 110 , 120]]

print(a)        # [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]

print(len(a))   # 3

print(a[0])     # [10, 20, 30, 40]

print(a[1])     # [50, 60, 70, 80]

print(a[2])     # [90, 100, 110, 120]

print(a[0][2])  # 30

print(a[1][3])  # 80

print(a[2][1])  # 100
#--------------------------------------------------------------------------------------------

a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

print(a[0])        # [10, 20]

print(a[1])        # [30, 40, 50]

print(a[2])        # [60, 70, 80, 90]

print(len(a[0]))   # 2

print(len(a[1]))   # 3

print(len(a[2]))   # 4

#-----------------------------------------------------------------------
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

print('Nested list with print function')
print(a) 
# [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

print('Each inner list of outer list without indexes')

for x in a:
    print(x)
# [10, 20]
# [30, 40, 50]
# [60, 70, 80, 90]

print('Elements in the form of matrix without indexes')

for x in a:
    for y in x:
        print(y, end=' ')
    print()
# 10 20
# 30 40 50
# 60 70 80 90
#----------------------------------------------------------------------------
print('Elements in the form of matrix using indexes')

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
# 10 20
# 30 40 50
# 60 70 80 90


#------------------------------------------------------------------------------------------------

a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]

for x in a:
    print(x)
# [10, 20]
# [30, 40]
# [50, 60]
# [70, 80]

print()

for x , y in a:
    print(x , y , sep='...')
# 10...20
# 30...40
# 50...60
# 70...80

#-----------------------------------------------------------------------------------

a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]

for x in a:
    print(x)
# [10, 20, 30]
# [40, 50, 60]
# [70, 80, 90]



for x , y , z in a:
    print(x , y , z , sep='...')
# 10...20...30
# 40...50...60
# 70...80...90

#-----------------------------------------------------

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

for x in a:
    print(x)
# [10, 20]
# [30, 40, 50]
# [60, 70, 80, 90]

for x , y in a:
    print(x , y , sep='...')

#----------------------------------------------------------
a = [[]]

print(a[0])        # []

print(*a)          # []

#----------------------------------------------------------------------
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar' ,5000.0]]

print(sorted(a))
# [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]

print(sorted(a , reverse = True))
# [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]

print(a)
# [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]

#------------------------------------------------------------------------------------
# Write a program to create a list with cubes of 2 , 4 , 6 , 8 , 10 with list comprehension (Home work)

a = [i**3 for i in range(2, 11, 2)]
print(a)  # [8, 64, 216, 512, 1000]

#--------------------------------------------------------------

"""
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
"""
a = ['hyd', 'pune', 'chennai', 'vijayawada']

b = []

for i in a:
    b.append(i[0].upper())

print(b)   # ['H', 'P', 'C', 'V']


#------------------------------------------------------------------------------------

 '''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
a = ['hyd' , 'pune' , 'chennai' , 'vijayawada']

b = [i[0].upper() for i in a]

print(b)   # ['H', 'P', 'C', 'V']




 '''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

s = "hyd is green city"

a = []
words = s.split()

for i in words:
    a.append([i.upper(), len(i)])

print(a)   # [['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]



(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]

s = "hyd is green city"

a = [[i.upper(), len(i)] for i in s.split()]

print(a)  # [['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]

#
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]

a = [10 , 20 , 30 , 40 , 50 , 60 , 70]
b = [100 , 200 , 300 , 400]

c = []

n = min(len(a), len(b))

for i in range(n):
    c.append(a[i] + b[i])

print(c)  # [110, 220, 330, 440]


(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]

a = [10 , 20 , 30 , 40 , 50 , 60 , 70]
b = [100 , 200 , 300 , 400]

c = [a[i] + b[i] for i in range(min(len(a), len(b)))]

print(c)  # [110, 220, 330, 440]


'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *


r = 3
c = 4

a = []

for i in range(r):
    a.append([0] * c)

print(a)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]


a = [10 , 20 , 15 , 18 , 25 , 32]
b = [30 , 40 , 10 , 25 , 15]

c = []

for i in a:
    if i not in b:
        c.append(i)

print(c)  # [20, 18, 32]


(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]


a = [10 , 20 , 15 , 18 , 25 , 32]
b = [30 , 40 , 10 , 25 , 15]

c = [i for i in a]


print(c)  # [20, 18, 32]

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension 
a = int(input("enter number b/w 1 to 20--"))

b = [i for i in range(1, a+1) if i % 2 == 0]

print(b)

'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''


a = [10 , 20 , 15]
b = [30 , 40 , 35 , 32]

c = []

for i in a:
    for j in b:
        c.append(i + j)

print(c)  # [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]


(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

a = [10 , 20 , 15]
b = [30 , 40 , 35 , 32]

c = [i + j
     for i in a
     for j in b]

print(c)  # [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]

Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program

a = "HYD"
b = "PUNE"

c = [i + j
     for i in a
     for j in b]

print(c)  # ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']


# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]


 #  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)## [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]



###14-3-26 home work


 # Find  outputs (Home  work)

a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)                 # (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))           # <class 'tuple'>
a[3] = 'Sec'             # error
a[3 : 6] = 60 , 70 , 80  # error


# Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))         # (1, 2, 3) <id1>
a += b
print(a , id(a))         # (1, 2, 3, 4, 5, 6) <id2>


# Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))         # (1, 2, 3) <id1>
a = a + b
print(a , id(a))         # (1, 2, 3, 4, 5, 6) <id2>


# What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)                 # (10 , 20 , 30 , 40)
print(type(a))           # <class 'str'>
b = eval(a)
print(b)                 # (10, 20, 30, 40)
print(type(b))           # <class 'tuple'>
print(len(b))            # 4


# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)                 # (10, [70, 30, 40], 50, 60)
a[1] = [80 , 90 , 100]   # error
print(a)


# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70             # error
print(a)
a[1] = [80 , 90]
print(a)                 # [10, [80, 90], 50, 60]


# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)                 # (25, 10.8, 'Hyd', True)
print(type(x))           # <class 'tuple'>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)                 # 25
print(b)                 # 10.8
print(c)                 # Hyd
print(d)                 # True
p , q , r =  x           # error
a , b , c , d  , e = x   # error


# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)                 # 25
print(b)                 # 10.8
print(c)                 # ['Hyd', True]
print(type(c))           # <class 'list'>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)                 # 25
print(b)                 # [10.8, 'Hyd']
print(c)                 # True


# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl # error
print(a)
print(b)
print(c)
print(d)
print(e)


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _ = x
print(a)                 # 25
print(b)                 # 10.8
print(_)                 # (3+4j)
print(d)                 # True
print(_)                 # (3+4j)



# update()  method  demo program  (Home  work)

tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s.update(tpl)
print(len(s))        # 4
print(s)             # {10, 20, 15, 18}
s.update(25)         # error


'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  --->  Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                         (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  ---> One  (or)  more
'''


# Find  outputs  (Home  work)

a = [10 , 20 , 30]
b = {30 , 40 , 50}
c = (50 , 60 , 70)

s = set()
s.update(a , b , c)
print(s)             # {10, 20, 30, 40, 50, 60, 70}
print(len(s))        # 7
s.add(a , b , c)     # error


# Find  outputs  (Home  work)

a = set()
a.update('Rama Rao')
print(a)             # {'R', 'a', 'm', ' ', 'o'}
print(len(a))        # 5
a.update(3 + 4j , 10.8 , True)   # error


# copy()  method  demo  program  (Home  work)

a = {10 , 20 , 15 , 18}
print(a)             # {10, 20, 15, 18}
b = a.copy()
print(b)             # {10, 20, 15, 18}
print(a is b)        # False
print(a == b)        # True
c = a
print(a is c)        # True


'''
copy()  method
------------------
1) What  does  copy()  method  do ?  ---> Returns  a  new  set  with  same  elements

2) a = b
    What  does  the  statement  do ?  --->  Reference  copy
																   i.e.  id  is  copied

3) What  is  shallow  clone ?  ---> Reference  copy
     What  is  deep  clone ?  --->  Object  copy
'''


# pop()  method  demo  program  (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
print(a)             # {25, 10.8, 'Hyd', True}
print(a.pop())       # element
print(a.pop())       # element
print(a.pop())       # element
print(a.pop())       # element
print(a.pop())       # error
print(a)             # set()
b = {10 , 20 , 30 , 40}
print(b.pop(2))      # error


'''
pop()  method
----------------
1) What  does  pop(No-args)  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  ---> Zero
'''


# remove()  method  demo  program  (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
print(a)             # {25, 10.8, 'Hyd', True}
a.remove('Hyd')
print(a)             # {25, 10.8, True}
a.remove('Sec')      # error


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''


# discard()  method  demo  program (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
print(a)             # {25, 10.8, 'Hyd', True}
a.discard('Hyd')
print(a)             # {25, 10.8, True}
a.discard('Sec')
print(a)             # {25, 10.8, True}
a.remove('Sec')      # error


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''


# clear()  method  demo  program (Home  work)

a = {10 , 20 , 15 , 18}
print(a)             # {10, 20, 15, 18}
a.clear()
print(a)             # set()
print(len(a))        # 0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''


# Find  outputs  (Home work)

a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a.union(b))    # {10, 20, 30, 40, 50, 60}
print(a | b)         # error
print(b.union(a))    # error
print(a + b)         # error


# intersection()   method  demo  program (Home  work)

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}

c = a.intersection(b)
print(c)             # {30, 40}
print(type(c))       # <class 'set'>

d = a & b
print(d)             # {30, 40}
print(type(d))       # <class 'set'>

print(c is d)        # False
print(c == d)        # True


'''
intersection()  method
---------------------------
1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

2) Is  set . intersection(list)  valid  ?  --->
							Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  another  way  to  obtain  common  elements ?  ---> a & b

4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

5) Is  list . intersection(set)  valid ?  --->  No  becoz  there  is  no  intersection()  method  in  list  class
'''


# difference()   method  demo  program  (Home  work)

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}

c = a.difference(b)
print(c)             # {10, 20}
print(type(c))       # <class 'set'>

d = a - b
print(d)             # {10, 20}
print(type(d))       # <class 'set'>

print(c is d)        # False
print(c == d)        # True


# symmetric_difference()   method  demo  program  (Home  work)

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}

c = a.symmetric_difference(b)
print(c)             # {10, 20, 50, 60}
print(type(c))       # <class 'set'>

d = a ^ b
print(d)             # {10, 20, 50, 60}
print(type(d))       # <class 'set'>

print(c is d)        # False
print(c == d)        # True


'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
						                                                              without  common  elements
																					  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b

4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only
'''


# Find  outputs  (Home  work)

a = {x * x for x in range(10)}
print(a)             # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
print(type(a))       # <class 'set'>


(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'


s = input("Enter string: ")

a = set(s)

b = ''.join(a)

print(b)


''' Write a program to obtain common elements between two lists using sets 
1) Let 1st list be [10 , 20 , 30 , 40 , 50 , 60] and 2nd list be [30 , 40 , 70 , 80 , 20] What is the output ? ---> [20 , 30 , 40] 
2) Both input and output are lists '''
a = [10 , 20 , 30 , 40 , 50 , 60]
b = [30 , 40 , 70 , 80 , 20]

s1 = set(a)
s2 = set(b)

c = list(s1 & s2)

print(c)  # [20, 30, 40]
