# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)# 2 5 8
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ') #15 is found 3 times



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
a = eval(input("Enter the first list : "))
b = eval(input("Enter the second list : "))

pos = -1
n = True

for x in a:
    try:
        pos = b.index(x, pos + 1)
    except:
        n = False
        break

print(n)

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)#[10 , 20 , 15 , 18]
print(a  is  b) #false
print(a  ==  b) #true
c = a[:]
print(c)  # [10 , 20 , 15 , 18]
print(a  is  c)#false
print(a  ==  c)#true
d = a
print(d)   #[10 , 20 , 15 , 18]
print(a  is  d)  #true
print(a  ==  d)  #true


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Copies  elements of  list  to  a  new  list  and  returns  the  new  list

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  	b = a[:]
'''
