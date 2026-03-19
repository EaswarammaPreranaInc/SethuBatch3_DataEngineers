
1Q)

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

   
output:

2
5
8
15 is found 3 times



'''
index()  method
-------------------
1) What  does  index(x)  do ?  --->  Returns  index  of  first  'x'  in  the  list

2) What  does  index(invalid-element)  do  ?  --->  Raises  an  error

3) list . index(x , i)
    list . index(x)
    What  is  the  difference  between  the  two  statements ?  --->
list . index(x , i)  searches  for  'x'  from   index  'i'  of  the  list  but	list . index(x)   searches  for  for  'x'  from   index  0  of  the  list

Note:
1) What  are  the  four  search  methods  in  str  class  --->  find() , rfind() , index() , rindex()

2) What  is  the  only  search  method  in  list  class  --->  index()
'''






2Q)

'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')


#CODE:

#By using walrus operator:


a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
    i = -1
    while  True:
        print(i := a . index(15 , i + 1))
		
except:
	print(F'15  is  found  {a . count(15)}  times '

#Output:

2
5
8
15 is found 3 times





3Q)
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


1.)

list1 =  [10 , 20 , 30]
list2 =  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]

i = 0

try:
    while i < len(list1):
        pos = list2.index(list1[i])
        list2.pop(pos)
        i += 1
    print(True)
except:
    print(False)

Output:

True

2.)

a = [10, 20, 20]
b = [15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]

c = b.copy()

try:
    for x in a:
        i = c.index(x)   
        c.pop(i)         
    print(True)
except ValueError:
    print(False)

Output:
False
 
3.)

a = [2, 2, 5]
b = [2, 2, 3, 4, 5]

c = b.copy()

try:
    for x in a:
        i = c.index(x)  
        c.pop(i)         
    print(True)
except ValueError:
    print(False)

Output:

True

4.)
a = [2, 4, 3]
b = [2, 2, 3, 4, 5]

c = b.copy()

try:
    for x in a:
        i = c.index(x)   
        c.pop(i)        
    print(True)
except ValueError:
    print(False)


Output:
  False





4Q)

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)            #[10, 20, 15, 18]
print(a  is  b)     #False
print(a  ==  b)     #True
c = a[:]
print(c)            #[10, 20, 15, 18]
print(a  is  c)     #False
print(a  ==  c)     #True
d = a
print(d)            #[10, 20, 15, 18]
print(a  is  d)     #True
print(a  ==  d)     #True


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Copies  elements of  list  to  a  new  list  and  returns  the  new  list

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  	b = a[:]
'''