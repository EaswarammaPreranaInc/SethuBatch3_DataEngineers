# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#    0     1    2    3    4    5    6    7    8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')

# 2
# 5
# 8
# 15  is  found 3  times

'''
index()  method
-------------------
1) What  does  index(x)  do ?  --->  Returns  index  of  first  'x'  in  the  list

2) What  does  index(invalid-element)  do  ?  --->  Raises  an  error

3) list . index(x , i)
    list . index(x)
    What  is  the  difference  between  the  two  statements ?  --->
														list . index(x , i)  searches  for  'x'  from   index  'i'  of  the  list  but
														list . index(x)   searches  for  for  'x'  from   index  0  of  the  list

Note:
1) What  are  the  four  search  methods  in  str  class  --->  find() , rfind() , index() , rindex()

2) What  is  the  only  search  method  in  list  class  --->  index()
'''

'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i=-1
	while  i := a . index(15,i+1):
		print(i)
except:
	print(F'15  is  found  {a . count(15)}  times ')
	


'''
Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [10 , 20 , 30]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  True  becoz  elements  10 , 20 , 30  are  in  2nd  list

2) First  list :  [10 , 20 , 20]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  False  becoz   elements  10 , 20 , 30  are  not  in  2nd  list

3) First  list :  [2 , 2 , 5]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''

try:
    a=eval(input('Enter  First list a'))
    b=eval(input('Enter  First list b'))
    i=b.index(a[0])
    for x in a[1:]:
        if i:=b.index(x,i+1):
            continue
    print(True)
except:
    print(False)


# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]  
b = a . copy()
print(b) # [10 , 20 , 15 , 18]
print(a  is  b) # False
print(a  ==  b) #True
c = a[:] 
print(c)#  [10 , 20 , 15 , 18]
print(a  is  c) # False
print(a  ==  c) #True
d = a
print(d) # [10 , 20 , 15 , 18]
print(a  is  d) # True
print(a  ==  d) # False


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Copies  elements of  list  to  a  new  list  and  returns  the  new  list

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  	b = a[:]
'''

#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)  #True
print(a  ==  b) #True
b[2] = 12
print(a)#[10, 20, 12, 18]

#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)  # [10 , 20 , 15 , 18,100 , 200 , 150]
print(a + 5) # error 
print(a + '5') #error
print([10 , 20] + (30 , 40)) # error

# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a))  #  [1 , 2 , 3] address of list [1 , 2 , 3]
a += b 
print(a , id(a)) #[1 , 2 , 3,4 , 5 , 6] same address


# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a))
a  = a + b # [1 , 2 , 3 ,4 , 5 , 6]
print(a , id(a)) #  [1 , 2 , 3 ,4 , 5 , 6] new address

 # Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  
print('a : ' , a) # a: 25
print('b : ' , b) # b: [10.8 , 'Hyd' ]
print('c : ' , c) # c: True
print(type(b))  # class <list>
x , *y = list 
print('x : ' , x) #x: 25
print('y : ' , y) #y:[10.8 , 'Hyd' ,  True]
*p , q = list
print('p : ' , p) #[25 , 10.8 , 'Hyd']
print('q : ' , q) #[True]

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list  # Error
a , b , *c , d , e = list
print('a : ' , a)  #25
print('b : ' , b) # 10.8
print('c : ' , c) #[]
print('d : ' , d) #'Hyd'
print('e : ' , e) #True
a , b , *c , d , e , f = list   # ERrror


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) # a: 25
print('b : ' , b) # b: 10.8
print('_ :  ' , _) # _: Hyd
print('d : ' , d) # d: True

# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)  # a: 3+4j
print('b : ' , b)  # b: 10.8
print('d : ' , d)  # c: True

#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) # 25
print('b : ' , b) # 10.8
print('_ : ' , _) # 3 + 4j
print('d : ' , d) # True
print('_: ' , _) #3 + 4j


# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list  # error 

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list  
print('a :  ' , a) # [25 , 10.8]
print('b :  ' , b) # 'Hyd'
print('c :  ' , c) # True

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list #
print('a : ' , a) # a: 25
print('b : ' , b) # b: 10.8
print('c : ' , c) # c: Hyd
print('d : ' , d) # d: True
a , b , c , d = list

# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # TRue
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
print(a == b)   # False
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
print(sum(a))  # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # 8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) #39.8 +4j
d = [10 , 20 , 15 , 18]
print(sum(d)) # 63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # error


'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''
[12:17 pm, 10/03/2026] +91 99482 50500: #  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a))
print(How  to  determine  sum  of  inner  list  elements)
print(How  to  determine  sum  of  inner  list  elements  in  another  way)

# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) # error 
d = [25 , '35']
print(max(d)) # error 
print(max([]))  # error
print(min([])) # error


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''

# list()  function  demo  program
a = (10 , 20 , 15, 18)  
b = list(a) #
print(b) #[10 , 20 , 15, 18]
print(type(b)) # class 
print(a  is  b) # False
print(a == b) # Fasle