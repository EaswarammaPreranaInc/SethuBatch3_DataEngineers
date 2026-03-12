# index()  method  demo  program  (Home  work)

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10

try:
	i = a . index(15)
	while  True:
		print(i)        # 2  then 5  then 8
		i = a . index(15 , i + 1)

except:
	print(F'15  is  found  {a . count(15)}  times ')   # 15 is found 3 times

#------------------------------------------------------------------------------------------------------------

'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]

try:
	i = -1
	while  (i := a.index(15 , i + 1))  >= 0:
		print(i)      # 2  then 5  then 8
except:
	print(F'15  is  found  {a . count(15)}  times ')   # 15 is found 3 times

#------------------------------------------------------------------------------------------------------------

'''
Most   tricky  program

Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [10 , 20 , 30]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  True  becoz  elements  10 , 20 , 30  are  in  2nd  list

2) First  list :  [10 , 20 , 20]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  False  becoz   elements  10 , 20 , 20  are  not  in  2nd  list

3) First  list :  [2 , 2 , 5]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''

a = eval(input('Enter the first list : '))   # Enter the first list : [10,20,30]
b = eval(input('Enter the second list : '))  # Enter the second list : [15 , 18 , 10 , 12 , 19 , 20 , 14 , 12 , 30 , 25 , 16]

try:
	for i in a:
		b . index(i)
	print(True)   # True

except:
	print(False)

#------------------------------------------------------------------------------------------------------------

# copy()  method  demo program  (Home  work)

a = [10 , 20 , 15 , 18]

b = a . copy()
print(b)            # [10, 20, 15, 18]
print(a  is  b)     # False
print(a  ==  b)     # True

c = a[:]
print(c)            # [10, 20, 15, 18]
print(a  is  c)     # False
print(a  ==  c)     # True

d = a
print(d)            # [10, 20, 15, 18]
print(a  is  d)     # True
print(a  ==  d)     # True
