a = [10, 20, 15, 13, 25, 15, 19, 15];
try:
    i = a.index(15);
    while True:
        print(i, end="");
        i = a.index(15, i+1)
    
except:
    print(F'15  is  found  {a . count(15)}  times ')

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = -1
	while  (i := a.index(15, i + 1)) >= 0:
		print(i)
except:
	print(F'15  is  found  {a . count(15)}  times ')


# using count method finding the substring in the string
a=list(eval(input("Enter elements: ")))
b = list(eval(input("Enter elements: ")))
for i in a:
    if b.count(i)<=0:
        print("Fasle");
        break;
else: 
    print("True")

# using index method finding the substring in the string
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
print(b) # [10 , 20 , 15 , 18]
print(a  is  b) # False
print(a  ==  b) # True
c = a[:] 
print(c) #[10 , 20 , 15 , 18]
print(a  is  c) # False
print(a  ==  c) # True
d = a
print(d) # [10 , 20 , 15 , 18]
print(a  is  d) # True
print(a  ==  d) # True