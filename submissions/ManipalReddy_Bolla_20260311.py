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

'''
output
2
5
8
15  is  found  3  times 
'''


'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
i=-1
try:
	while (i:=a.index(15,i+1))>=0:
		print(i)
except:
	print(F'15  is  found  {a . count(15)}  times ')
	

lt1=eval(input("Enter the first list : "))
lt2=eval(input("Enter the second list : "))
indx=0
try:
    for i in lt1:
        indx=lt2.index(i,indx)+1
    print("True")
except:
    print("False")


'''
output
Enter the first list : [2 , 4 , 3]
Enter the second list : [2 , 2 , 3 , 4 , 5]
False
Enter the first list :  [10 , 20 , 30]
Enter the second list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
True
'''


# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)#[10,20,15,18]
print(a  is  b)#False
print(a  ==  b)#True
c = a[:]
print(c)#[10,20,15,18]
print(a  is  c)#False
print(a  ==  c)#True
d = a
print(d)#[10,20,15,18]
print(a  is  d)#True
print(a  ==  d)#True



