
# Write  a  program  to  determine  mode



a= [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
b=list(set(a))
mode=None
max_count=0
for i in range(len(b)):
    ctr=0
    for j in range(len(a)):
        if b[i]==a[j]:
            
            ctr+=1
    if  ctr>max_count:
        max_count=ctr
        mode=b[i] 

print("mode:",mode)  

#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]

print(a)  #  print('Nested list  with  print function')

for i in a:
    print(i) #  print('Each  inner  list   of   outer  list  without  indexes')
for i in a:
    for j in i:
        print(j,end=" ")  
    print()         #  How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (with  for  loop)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end="   ")
    print()  # How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)


# Create list with cubes of 2, 4, 6, 8, 10 using list comprehension

a = [x**3 for x in range(2, 11, 2)]

print(a)
# Repeat   previous  program  with  comprehension
a= eval(input("Enter a list of strings: "))

b = [i[0].upper() for i in a ]
print(b)


# Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

a= eval(input("Enter a list of strings: "))

b=[]

for i in a:
    
    b.append(i[0].upper())

print(b)


# Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list

a= input("Enter a string with spaces: ")
b=a.split()
c=[]
for i in b:
    d=[]
    d.append(i.upper())
    d.append(len(i))
    c.append(d)
print(c)


# Repeat   previous  program  with  comprehension
a= input("Enter a string with spaces: ")
b=a.split()
c=[[x.upper(),len(x)] for x in b ]
print(c)


# Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c=[]
for i in range(min(len(a), len(b))):
            c.append(a[i]+b[i])

print(c)



# Repeat   previous  program  with  comprehension
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c=[(a[i]+b[i]) for i in range(min(len(a),len(b)))]
print(c)



# Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

a=int(input("Enter 1st integer: "))
b=int(input("Enter 1st integer: "))
c=[]
d=[]
for i in range(b):
    c.append((0))

for j in range(a):
    d.append(c)

print(d)



# Repeat   previous  program  with  comprehension
a=int(input("Enter 1st integer: "))
b=int(input("Enter 1st integer: "))
c=[0 for i in range(b)]
d=[c for i in range(a)]

print(d)



# Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c=[]
for i in a:
    if i not in b:
        c.append(i)
print("Elements are not in b: " ,c)



# Repeat   previous  program  with  comprehension

a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c=[i for i in a if i not in b]
print(c)



#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

a=[x for x in range(1,21) if x%2==0]

print(a)

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

a=[x*2 for x in range(1,11)]

a=[x for x in range(2,21,2)]


print(a)

# Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

a=[x**2 for x in range(2,21,2)]

print(a)



# Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

a=[x**2 for x in range(1,21) if x%2==0]

print(a)



a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))

c=[]
for i in a:
    for j in b:
        c.append(i+j)

print(c)


# Repeat   previous  program  with  comprehension
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c=[i+j for i in a for j in b]
print(c)



# Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

a="HYD"
b="PUNE"
c=[i+j for i in a for j in b]

print(c)



# Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

a=eval(input("Enter the list with lists: "))
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)




# Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
a=eval(input("Enter the list with lists: "))

b=[j for i in a for j in i]

print(b)


#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) # [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) # 3
print([j  for j in a[0]])# print(How  to  print  1st  inner  list)
print([j for j in a[1]])# print(How  to  print  2nd  inner  list)
print([j  for j in a[2]])# print(How  to  print  3rd  inner  list)
print([a[0][2] ])     #  print(How  to  print  30)

# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]