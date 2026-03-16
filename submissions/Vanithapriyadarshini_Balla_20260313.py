# Write  a  program  to  determine  mode
ls=eval(input("Enter list : "))
max_count=0
mode=ls[0]
for x in set(ls):
    ctr=ls.count(x)
    if ctr > max_count:
       max_count=ctr
       mode=x
print(f' mode = {mode}')
print(f' ctr = {max_count}')

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) # [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) # 3
print(a[0])
print(a[1])
print(a[2])
print(a[0][2])
print(a[1][3])
print(a[2][1])

#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])
print(a[1])
print(a[2])
print(len(a[0]))
print(len(a[1]))
print(len(a[2]))

#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)
print('Each  inner  list   of   outer  list  without  indexes')
for x in a:
   print(x)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for x in a:
 print(*x)
print('Elements  in  the  form   of  matrix  using  indexes')
for i in range(len(a)):
   for j in range(len(a[i])):
      print(a[i][j],end=' ')
   print()

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x) # [10,20]<nl>[30,40]<nl>[50,60]<nl>[70,80]
    print()
for  x , y  in  a:
	print(x , y , sep = '...')
'''10...20
30...40
50...60
70...80'''

#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x) # [10,20,30]<nl>[40,50,60]<nl>[70,80,90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
'''
10...20...30
40...50...60
70...80...90
'''

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x) # [10 , 20]<nl> [30 , 40 , 50] <nl>[60 , 70 , 80 , 90]
for  x , y  in  a:
	print(x , y ,	sep = '...')
'''
10...20
Error
'''

#  Find  outputs  (Home  work)
a = [[]]
print(a[0])
print(*a)

#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) # [[5 , 'Amar'  ,5000.0],[10 , 'Rama' , 1000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] ,[20 , 'Sita' , 2000.0]]
print(sorted(a , reverse = True)) # [[20 , 'Sita' , 2000.0],[18 , 'Kiran' , 2800.0],[15 , 'Rajesh' , 3500.0],[10 , 'Rama' , 1000.0] ,[5 , 'Amar'  ,5000.0]]
print(a) # [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]

# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
num=eval(input("Enter num : "))
print([i for i in range(2,num+1) if i%2==0])

#Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
ls=eval(input("Enter list : "))
l=[]
for x in ls:
     l.append(x[0].upper())
print(l)

# (Home  work)
#Repeat   previous  program  with  comprehension
ls=eval(input("Enter list : "))
print([x[0].upper() for x in ls ])

# Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
#(word  should  be  in  capital  letters)  without  comprehension
ls=eval(input("Enter list : "))
l=[]
for x in ls:
     x=x.upper()
     l.append(x)
print(ls,len(x))

# Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

l1=eval(input("Enter 1st list : "))
l2=eval(input("Enter 2nd list : "))
l=[]
if len(l1)<len(l2):
    for i in range(len(l1)):
     l.append(l1[i]+l2[i])
else:
    for i in range(len(l2)):
     l.append(l2[i]+l1[i])
print(l)

# (Home  work)
#Repeat   previous  program  with  comprehension
l1=eval(input("Enter 1st list : "))
l2=eval(input("Enter 2nd list : "))
ls=[l1[i]+l2[i] for i in range(l1) if len(l1)<len(l2) l2[i]+l1[i] for i in range(len(l2)) else]


# Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
n=eval(input("Enter inner list : "))
e=eval(input("Enter elements to be : "))
ls=[]
for i in range(3):
    l=[]
    for j in range(e):
        l.append(0)
    ls.append(l)
print(ls)

#Repeat   previous  program  with  comprehension

n=eval(input("Enter inner list : "))
e=eval(input("Enter elements to be : "))
ls=[[0 for j in range(e)] for i in range(n)]
print(ls)

#Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
l1=eval(input("Enter 1st list : "))
l2=eval(input("Enter 2nd list : "))
l=[]
for x in l1:
    if x not in l2:
        l.append()
print(l)

# Repeat   previous  program  with  comprehension
l1=eval(input("Enter 1st list : "))
l2=eval(input("Enter 2nd list : "))
print([x for x in l1 if x not in l2])

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

print([x for x in range(1,21) if x%2==0])

# Repeat  previous  program  with  comprehension  and  without  using  if
print([x for x in range(2,21,2)])

# Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

print([x*x for x in range(1,21) if x%2==0])

#  Repeat  previous  program  with  comprehension  and  without  using  if

print([x*x for x in range(2,21,2)])

#Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
l1=eval(input("Enter 1st list : "))
l2=eval(input("Enter 2nd list : "))
l=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        l.append(l1[i]+l2[i])
print(l)

#Repeat   previous  program  with  comprehension
l1=eval(input("Enter 1st list : "))
l2=eval(input("Enter 2nd list : "))
print([l1[i]+l2[j] for i in range(len(l1)) for j in range(len(l2))])       
    
# Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
s1=input("Enter str1: ")
s2=input("Enter str2: ")
s=[]
for x in s1.split():
    for y in s2.split():
        s.append(x+y)
print(s)

#Write  a  program  to  convert  a  nested  list  to  list  without  comprehension




