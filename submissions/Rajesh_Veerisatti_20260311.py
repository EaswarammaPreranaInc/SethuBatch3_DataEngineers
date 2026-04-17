

# index()  method  demo  program

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]

try:
	i=-1
	while (i := a . index(15,i+1)) >=0: # 2,5,8,error
		print(i)
	
		
except:
	print(F'15  is  found  {a . count(15)}  times ')
	
a = [10 , 20 , 30]   # first list
b = [15 , 18 , 10 , 12 , 19 , 20 , 14 , 12 , 30 , 25 , 16]   # second list
print(all(a.count(x) <= b.count(x) for x in a))
c = b.copy()

try:
    for x in a:
        i = c.index(x)
        c.pop(i)
    print(True)
except ValueError:
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
print(a  is  d) #  True
print(a  ==  d) # True


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Copies  elements of  list  to  a  new  list  and  returns  the  new  list

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  	b = a[:]
'''