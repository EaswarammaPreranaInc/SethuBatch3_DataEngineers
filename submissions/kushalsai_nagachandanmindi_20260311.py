# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0    1    2    3    4    5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print(i)    #2 5 8
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')    # 15 is found 3 times



a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = -1
	while  True:
		print(i = a . index(15 , i + 1))
except:
	print(F'15  is  found  {a . count(15)}  times ')



list1 = eval(input("Enter the first list: "))
list2 = eval(input("Enter the second list: "))

x=0
try:
    for i in list1:
        x = list2.index(i, x+1)
    print(True)
except:
    print(False)



# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)    #[10, 20, 15, 18]
print(a  is  b)    #False becoz a and b has different location
print(a  ==  b)    #True
c = a[:]
print(c)    #[10, 20, 15, 18]
print(a  is  c)    #False becoz a and b has different location
print(a  ==  c)    #True
d = a
print(d)        #[10, 20, 15, 18]
print(a  is  d) #True becoz here a and b points to same reference
print(a  ==  d) #true