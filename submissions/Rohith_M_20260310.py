#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) # True
print(a  ==  b) # True
b[2] = 12
print(a) # [10, 20, 15, 18]
#--------------------
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # [10 , 20 , 15 , 18, 100 , 200 , 150]
print(a + 5) #  Error 
print(a + '5') # Error
print([10 , 20] + (30 , 40)) # Error
#---------------------------------------------
# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) # [1 , 2 , 3] , address of the class "a"
a += b
print(a , id(a)) # [1 , 2 , 3, 4 , 5 , 6] , address of the class "

#-------------------------------------------

list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) # a : 25 
print('b : ' , b) # b : 10.8, Hyd
print('c : ' , c) # c : True
print(type(b)) # <class list>
x , *y = list
print('x : ' , x) # x: 25
print('y : ' , y) # y : 10.8 , 'Hyd' ,  True
*p , q = list
print('p : ' , p) # 25, 10.8 , 'Hyd' 
print('q : ' , q) # True

#---------------------------------------
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list # Error
a , b , *c , d , e = list # error
print('a : ' , a)  # Error 
print('b : ' , b) # Error
print('c : ' , c) # Error
print('d : ' , d) # Error
print('e : ' , e) # Error
#----------------------------------------
a , b , *c , d , e , f = list
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) # a: 25 
print('b : ' , b) # b : 10.8 
print('_ :  ' , _) # : "Hyd"
print('d : ' , d) # d = True

#---------------------------------
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) # Error
print('b : ' , b) # b : 10.8
print('d : ' , d) # d : True

#-------------------------------
#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) # a : 25
print('b : ' , b) #  b : 10.8
print('_ : ' , _)  # _ : 3 + 4j
print('d : ' , d) # True 
print('_: ' , _) # _ : 3 + 4j

#-----------------------------------------
# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list

#---------------------------------
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) # a : [25 , 10.8]
print('b :  ' , b) # b: Hyd
print('c :  ' , c) # c : True

#----------------------------------
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # a : [25 , 10.8]
print('b : ' , b) # b : Hyd
print('c : ' , c) # c : True
print('d : ' , d) # Error
a , b , c , d = list

#-----------------------
# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # True
print(a  is   b) # False
print(a < c) # True
print(a > d)  # True
print(a >= c) # False
print(a <= d)  # False
print(a != c) # True
print(a != b) # False
print(a == c) # False
#------------------------------------------------
# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # False
print(a  is   b) # False

# -------------------------------------
#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # 4
b = []
print(len(b)) # 0
c = [[10 , 20] , 30 , 40] 
print(len(c))# 3

'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''
#---------------------------------------------

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # 8 + 10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # Error 
d = [10 , 20 , 15 , 18]
print(sum(d)) # 63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # Error


'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''

#---------------------------------------------------------------
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a)) #Error 
print(How  to  determine  sum  of  inner  list  elements)  # print(sum(*a))

print(How  to  determine  sum  of  inner  list  elements  in  another  way) # print(sum(a[0]))

#--------------------------------------------------------- 
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5 
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) # Error
d = [25 , '35']
print(max(d)) # Error
print(max([]))  # Error
print(min([])) # Error


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''

#------------------------------------------------
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) #  [10 , 20 , 15, 18]
print(type(b)) # < class list > 
print(a  is  b)# False
print(a == b) # False 

#----------------------------------
#  Find  outputs (Home  work)
a = range(4 , 10 , 2) # 4,6,8
b = list(a) 
print(b)  # [ 4,6,8]
print(type(b)) # < class list > 
a = list('Vamsi')
print(a) # ['V', 'a', 'm', 's', 'i']
a = list()
print(a) # []
print(list(25)) # Error
print(list(10.8)) # Error
print(list(True)) # Error 
print(list(None)) # Error



'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  --->  Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''

#---------------------------------------------------------
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))  #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) #[[10 , 20] , (30 , 40) , {50 , 60}]

#-----------------------------------------------------------

# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b) # [5, 10, 12, 15, 20]
print(type(b)) # < class list > 
c = sorted(a , reverse = True)
print(c)     #[ 12, 5, 15, 20, 10]
print(a)      #[10 , 20 , 15 , 5 , 12]



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

#---------------------------------------------------------------------
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)   #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c)   #['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
#----------------------------------------------
# all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))  # true
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))  # False
d = [10 , 0 , 20] 
print(all(d)) # False
e = []
print(all(e)) # true


'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''

#-----------------------------------------------------------------------
# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) # true
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

#-------------------------------------------------------
# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del    a[2]
print(a) # [10 , 20 , 18]
del  a[3]
del  a
print(a) # Error

#-----------------------------------------------
#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)# [10 , 20 , 15 , 18]
list . append(19) 
print(list) # [10 , 20 , 15 , 18 ,19 ]

#-------------------------------------
#  Find  outputs (Home  work)
list = []
print(list) # []
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) # [25, 10.8, 'Hyd', True]

#---------------------------------
# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)  # [ 0 , 10 , 20 , 30, 40] 

#------------------------------------------
#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd') 
print(a) # [10, 20, 30, 'Hyd']
print(len(a)) # 4
print(How  to  print  4th  element  of  list  'a') # a[3]
print(How  to  print  'H') # a[3][0]
print(How  to  print  'y')# a[3][1]
print(How  to  print  'd') # a[3][2]

#--------------------------------------------------
#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a) # [10, 20, [50, 60, 70], 30, 40]
print(len(a)) # 5
print(How  to  print  inner  list) # a[2]
print(How  to  print  50) # a[2][0]
print(How  to  print  60) # a[2][1]
print(How  to  print  70) # a[2][2]


#------------------------------------------------------
# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)  
	list . remove(25) 
except:
	print('25  is   not  in  the  list')



'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  ---> Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Raises  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->  Call  remove()  method  in  a  loop
'''

#--------------------------------------------------------------
'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''


#------------------------
a = [10, 20, 15, 18, 19, 15, 17, 20, 15, 14]
x = 15

while x in a:
    a.remove(x)

print(a)  # [10, 20, 18, 19,17, 20, 14]


#------------------------------------------------
#  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2))  #  15
print(a) # [10 , 20 , 18 , 12]
print(a . pop(len(a))) # Error
print(a . pop(-3)) # 20
print(a) #[10 , 18 , 12] 
print(a . pop(-4)) # Error
print(a . pop()) ] # 12 
+t(a)
b = [] # [10,18]
b . pop()



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

#---------------------------------------------------------------------------------
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)  # [10 , 20 , 15 , 18]
list . clear()
print(list) # []


'''
clear()  method
------------------
1) What  does  clear()  method  do ?  ---> Removes  all  the  elements  of  the  list  and  list  becomes  empty

2) What  about  remove()  and  pop()  methods  ?  --->  They  remove  single  element  of  the  list
'''

#--------------------------------------------------------------------------------
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
a . reverse()
print(a) # [ 18, 15, 20, 10]

'''
reverse()  method
---------------------
1) What  does  reverse()  method  do ?  --->  Reverses  all  the  elements  of  list

2) Where  are  the  results  stored ?  ---> In  the  same  list  replacing  existing  elements (List  is  mutable)
'''

#---------------------------------------------------------------------------------------------------------
#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10 , 20 , 15 , 18 , 5]
list . sort() 
print(list) # [5, 10, 15, 18, 20]
list . sort(reverse = True)
print(list) # [ 20, 18, 15, 10, 5 ]


#---------------------------------------
# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a . sort()
print(a) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True) 
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']


#----------------------------------------------------------------
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() # error is "Hyd"


#------------------------------
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3 
print(a . count(25))  # 0 
print(len(a))  # 9


'''
What  does  list . count(x)  do ?  --->  Returns  number  of  times  'x'  is  in  the  list
'''
'''

#-----------------------------------------------------------
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
#------------------------------------

a = [10, 20, 15, 10, 14, 10, 18, 20, 19]

result = []

for i in a:
    if a.count(i) == 1:
        result.append(i)

print(result)



#----------------------------------------------------------------------------
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