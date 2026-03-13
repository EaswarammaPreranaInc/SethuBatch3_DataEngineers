# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)#[10 , 20 , 15 , 18]
print(a  is  b)#False
print(a  ==  b)#True
c = a[:]
print(c)#[10 , 20 , 15 , 18]
print(a  is  c)#True
print(a  ==  c)#True
d = a
print(d)#True
print(a  is  d)#True
print(a  ==  d)#True
#------------------------------------------------------------------------------------------------------------------

# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')

out put 
2
5
15 is found

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
-------------------------------------------------------------------------------------------------
'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]

try:
    i = -1
    while True:
        print(i := a.index(15, i + 1))
except:
    print(f'15 is found {a.count(15)} times')
