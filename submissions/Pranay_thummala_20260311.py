'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')
'''	

a = [10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]

try:
    i = -1
    while (i := a.index(15, i + 1)) >= 0:
        print(i)
except:
    print(f'15 is found {a.count(15)} times')


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
a = [10, 20, 30]   # first list
b = [15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]   # second list

pos = -1

try:
    for x in a:
        pos = b.index(x, pos + 1)
    print(True)
except ValueError:
    print(False)




# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) # [10 , 20 , 15 , 18]
print(a  is  b) # false
print(a  ==  b) # true
c = a[:]
print(c) # [10 , 20 , 15 , 18]
print(a  is  c) # false
print(a  ==  c) # true
d = a
print(d) # [10 , 20 , 15 , 18]
print(a  is  d) # true
print(a  ==  d) # true
