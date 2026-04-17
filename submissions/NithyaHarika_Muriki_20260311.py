
 # index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#    0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')#3



'''
index()  method
-------------------
1) What  does  index(x)  do ?  --->  Returns  index  of  first  'x'  in  the  list

2) What  does  index(invalid-element)  do  ?  --->  Raises  an  error

3) list . index(x , i)
    list . index(x)
    What  is  the  difference  between  the  two  statements ?  --->
														list . index(x , i)  searches  for  'x'  from   index  'i'  of  the  list  but

list . index(x)   searches  for  for  'x'  from…
'''
'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = a . index(15)
	while  i := a . index(15 , i + 1):
		print(i)
		#2,5,8
except:
	print(F'15  is  found  {a . count(15)}  times ')#15  is  found  3 times 
      

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)#[10 , 20 , 15 , 18]
print(a  is  b)#false
print(a  ==  b)#True
c = a[:]
print(c)#[10 , 20 , 15 , 18]
print(a  is  c)#false
print(a  ==  c)#True
d = a #object is copied
print(d)#[10 , 20 , 15 , 18]
print(a  is  d)# True            
print(a  ==  d)#True
