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

# Modify  the  following  program  with  walrus  operator
# Hint:  Call  index()  method  only  once

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
    i = -1
    while (i := a.index(15, i + 1)) >= 0:
        print(i)
except:
    print(f'15 is found {a.count(15)} times')
    
# Most   tricky  program
# Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
# Print  True  if  it  is  a  sublist  and  False  otherwise

a = eval(input("Enter the first input : "))
b = eval(input("Enter the second input : "))
try:
    i = -1
    for x in a:
        i = b.index(x, i + 1)
    print(True)
except:
    print(False)

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) # [10 , 20 , 15 , 18]
print(a  is  b) # False
print(a  ==  b) # True
c = a[:]
print(c) # [10 , 20 , 15 , 18]
print(a  is  c) # False
print(a  ==  c) # True
d = a
print(d) # [10 , 20 , 15 , 18]
print(a  is  d) # True
print(a  ==  d) # True
