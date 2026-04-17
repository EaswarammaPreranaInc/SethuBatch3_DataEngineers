try:
	n1=eval(input())
	n2=eval(input())
	temp=n2
	for x in n1:
		i=temp.index(x)
		temp.pop(i)
	print(True)
except:
	print(False)
-----------------------------------------------------------
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
----------------------------------------------------------------------------
#Modify  the  following  program  with  walrus  operator
#Hint:  Call  index()  method  only  once

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')