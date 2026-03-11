# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)			#2,5,8
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')	#15 is found '3' times



a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
i=-1
try:
	while(i:=a.index(15))>=0:
		print(i)
except:
	print(F'15  is  found  {a . count(15)}  times ')


# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)	#[10,20,15,18]
print(a  is  b)	#False
print(a  ==  b)	#True
c = a[:]
print(c)	#[10,20,15,18]
print(a  is  c)	#False
print(a  ==  c)	#True
d = a
print(d)	#[10,20,15,18]
print(a  is  d)	#True
print(a  ==  d)	#True


list_1=eval(input("Enter first list: "))
list_2=eval(input("Enter second list: "))
current_position=0
sublist=True
try:
    for  i in list_1:
       found_index=list_2.index(i,current_position)
       current_position=found_index+1
except:
    sublist=False
print(sublist)
