# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) #[10 , 20 , 15 , 18]
print(a  is  b) #False
print(a  ==  b) #True
c = a[:]
print(c) #[10 , 20 , 15 , 18]
print(a  is  c) #False
print(a  ==  c) #True
d = a
print(d) #[10 , 20 , 15 , 18]
print(a  is  d) #True
print(a  ==  d) #True


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

#output
2
5
8
15 is found 3 times


a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]

try:
    i = a.index(15)
    print(i)
    while (i := a.index(15, i+1)):
        print(i)
except ValueError:
    print(f'15 is found {a.count(15)} times')



try:
    a = eval(input("Enter first list:  "))
    b = eval(input("Enter second list:  "))
    i = b.index(a[0])
    for x in a[1:]:
        if i:= b.index(x,i+1):
            continue
    print("True")
except:
    print("False")
	



