# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)  #[2 , 5 , 8]
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')
		# 15  is  found  3  times 



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
--------------------------------------------------------------------
'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
i=-1
try:
	while  True:
	    (i := a . index(15 , i + 1))
	    print(i)
except:
	print(F'15  is  found  {a . count(15)}  times ')

--------------------------------------------------------------------

a=eval(input('Enter the first list :'))
b=eval(input('Enter the second list :'))
try:
    j=-1
    for x in a:
        while  True:
	        j = b . index(x , j + 1)
	        break
    print('True')	    
except:
     print('False')

--------------------------------------------------------------------

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)  #[10 , 20 , 15 , 18]
print(a  is  b)#false
print(a  ==  b)#true
c = a[:]
print(c) #[10 , 20 , 15 , 18]
print(a  is  c) #false
print(a  ==  c) #true
d = a
print(d) #[10 , 20 , 15 , 18]
print(a  is  d) #true
print(a  ==  d) #true


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Copies  elements of  list  to  a  new  list  and  returns  the  new  list

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  	b = a[:]
'''