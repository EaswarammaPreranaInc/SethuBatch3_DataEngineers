##1.Tricky  program
##Write  a  program  to  determine  mode
##
##1) What  is  mode ?  --->  The  element  which  is  repeated  maximum  number  of  times  in  the  list
##
##2) Let  input  be  [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
##    What  is  set(list) ?  --->  {12 , 20 , 18 , 15 , 10}
##    How  many  times  is  first  element  12  repeated  in  the  list  ?  --->  1
##    How  many  times  is  2nd  element  20  repeated  in  the  list  ?  --->  3
##    How  many  times  is  3rd  element  18  repeated  in  the  list  ?  ---> 2
##    How  many  times  is  4th  element  15  repeated  in  the  list  ?  --->  5
##    How  many  times  is  last  element  10  repeated  in  the  list  ?  --->  4
##    What  is  the  mode  ?  --->  15  becoz  it  is  repeated  max  number  of  times  i.e.  5
##
##3) mode =   15
##    ctr =  5

n = eval(input('Enter any list : '))
mode = 0
count = 0
new = set(n)
for i in new:
    if n.count(i) > count:
        mode = i
        count= n.count(i)
print(mode)
print(count)

#-----------------------------------------------------------------------------------------------------------

#2.Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)     # [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))# 3
print(a[0])    # How  to  print  1st  inner  list
print(a[1])    # How  to  print  2nd  inner  list
print(a[2])    # How  to  print  3rd  inner  list
print(a[0][2]) # How  to  print  30
print(a[1][3]) # How  to  print  80
print(a[2][1]) # How  to  print  100

#----------------------------------------------------------------------------------------------------------

#3.Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])      # How  to  print  1st   inner  list
print(a[1])      # How  to  print  2nd   inner  list
print(a[2])      # How  to  print  3rd   inner  list
print(len(a[0])) # How  to  print  number  of  elements  in  1st  inner  list)
print(len(a[1])) # How  to  print  number  of  elements  in  2nd  inner  list)
print(len(a[2])) # How  to  print  number  of  elements  in  3rd  inner  list)


#--------------------------------------------------------------------------------------------------------

#4.How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)


print('Each  inner  list   of   outer  list  without  indexes')
# How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (with  for  loop)
for x in a:
    print(x)



print('Elements  in  the  form   of  matrix   without  using  indexes')
# How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (with  nested  loop)
for x in a:
    print(*x,sep=' ')

print('Elements  in  the  form   of  matrix  using  indexes')
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)
for x in range(len(a)):
    print(*a[x],sep=' ')


#----------------------------------------------------------------------------------------------------------

#5.Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)     # [10,20] <nl> [30,40] <nl> [50,60] <nl> [70,80]
print()
for  x , y  in  a:
	print(x , y , sep = '...') # 10...20 <nl> 30...40 <nl> 50...60 <nl> 70...80
	
#-----------------------------------------------------------------------------------------------------------

#6.Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)  # [10 , 20 , 30] <nl> [40 , 50 , 60] <nl> [70 , 80 , 90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...') # 10...20...30 <nl> 40...50...60 <nl> 70...80...90

#-----------------------------------------------------------------------------------------------------------

#7.Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x) # [10 , 20] <nl> [30 , 40 , 50] <nl> [60 , 70 , 80 , 90]
for  x , y  in  a:
	print(x , y ,	sep = '...') # 10...20 # Error

#------------------------------------------------------------------------------------------------------------

#8.Find  outputs  (Home  work)
a = [[]]
print(a[0])  # How  to  print  inner  list)
print(a[-1]) # How  to  print  inner  list  in  another  way)


#-----------------------------------------------------------------------------------------------------------

#9.Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] ,
     [5 , 'Amar'  ,5000.0] ]
print(sorted(a))   # [[5,'Amar',5000.0],[10,'Rama',1000.0],[15,'Rajesh',3500.0],[18,'Kiran',2800.0],
                   #  [20,'Sita',2000.0]]
print(sorted(a , reverse = True)) # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)     # [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]


#------------------------------------------------------------------------------------------------------------

#10.Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10
# with  list  comprehension (Home  work)

print([x**3 for x in range(1,11) if x%2==0])

#-------------------------------------------------------------------------------------------------------------

##11.(Home  work)
##Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters
##in  a  list  of  srings  without  comprehension
##Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
##What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']

s = eval(input('Enter any list : '))
new = []
for x in a:
    new.append(x[0].upper())
print(new)

#---------------------------------------------------------------------------------------------------------------

##12.(Home  work)
##Repeat   previous  program  with  comprehension
##
##Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
##
##Output :  ['H' , 'P' , 'C' , 'V']

s = eval(input('Enter any list : '))
print([x[0].upper() for x in s])

#---------------------------------------------------------------------------------------------------------------

##13.Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
##(word  should  be  in  capital  letters)  without  comprehension
##
##Let  input  be   hyd  is  green  city
##What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]


n = input('Enter any string : ')
new = []
s = n.split()
for i in s:
    new .append([i.upper(),len(i)])
print(new)

#--------------------------------------------------------------------------------------------------------------

##14.(Home  work)
##Repeat   previous  program  with  comprehension
##
##Input :  hyd  is  green  city
##
##Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]


n = input('Enter any string : ')
print([[i.upper(),len(i)] for i in n.split()])

#----------------------------------------------------------------------------------------------------------

##15.Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
##
##Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
##What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]

n1 = eval(input('Enter 1st list : '))
n2 = eval(input('Enter 2nd list : '))
n3 = []
for i in range(min(len(n1),len(n2))):
    n3.append(n1[i]+n2[i])
print(n3)

#----------------------------------------------------------------------------------------------------------

##16.(Home  work)
##Repeat   previous  program  with  comprehension
##
##Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
##Input2 :  [100 , 200 , 300 , 400]
##Output :  [110 , 220 , 330 , 440]

n1 = eval(input('Enter 1st list : '))
n2 = eval(input('Enter 2nd list : '))
print([n1[i]+n2[i] for i in range(min(len(n1),len(n2)))])

#-------------------------------------------------------------------------------------------------------------

##17.Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
##
##Let inputs  be  3  and  4
##What  is  the  output ?  ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
##
##Hint:  Use  repetition  operator  *


n1 = int(input('How many Lists ? : '))
n2 = int(input('How many elements in each lists ?  : '))
new = []
for i in range(n1):
    new.append([0]*n2)
print(new)

#--------------------------------------------------------------------------------------------------------

##18.(Home  work)
##Repeat   previous  program  with  comprehension
##
##Inputs :  3  and  4
##
##Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]


n1 = int(input('How many Lists ? : '))
n2 = int(input('How many elements in each lists ?  : '))
print([[0]*n2 for i in range(n1)])

#---------------------------------------------------------------------------------------------------------


##19.Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list
##without  comprehension
##Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
##What  is  the  output ?  --->  [20 , 18 ,  32]

n1 = eval(input('Enter 1st list : '))
n2 = eval(input('Enter 2nd list : '))
new = []
for i in range(len(n1)):
    if n1[i] not in n2:
        new.append(n1[i])
print(new)

#-------------------------------------------------------------------------------------------------------

##20.(Home  work)
##Repeat   previous  program  with  comprehension
##
##Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
##Input2 :  [30 , 40 , 10 , 25 , 15]
##Output :  [20 , 18 , 32]


n1 = eval(input('Enter 1st list : '))
n2 = eval(input('Enter 2nd list : '))
print([n1[i] for i in range(len(n1)) if n1[i] not in n2])

#---------------------------------------------------------------------------------------------------------

#21.Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

print('Even Numbers between 1 and 20 : ',[x for x in range(1,21) if x%2==0])

#--------------------------------------------------------------------------------------------------------

##22.Repeat  previous  program  with  comprehension  and  without  using  if
##Output: [Even  numbers  between  1  and  20]

print('Even Numbers between 1 and 20 : ',[x for x in range(2,21,2)])

#--------------------------------------------------------------------------------------------------------

##23.Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20
##which  are  divisible   by  2  with  comprehension
##What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]

print('Squares of 1 to 20 which are divisible by 2 : ',[x**2 for x in range(1,21) if (x**2)%2==0])

#---------------------------------------------------------------------------------------------------------

#24.Repeat  previous  program  with  comprehension  and  without  using  if

print('Squares of 1 to 20 which are divisible by 2 : ',[x**2 for x in range(2,21,2)])

#---------------------------------------------------------------------------------------------------------

##25.Write  a  program  to  add  each  element  of  1st  list  with
##all  the  elements  of  2nd  list  without  comprehension
##
##Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
##What  is  the  result ?  --->
##[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 ,
## 15 + 40 , 15 + 35 , 15 + 32]
##
##Hint : Nested  for  loops

n1 = eval(input('Enter 1st list : '))
n2 = eval(input('Enter 2nd list ; '))
new = []
for i in range(len(n1)):
    for j in range(len(n2)):
        new.append(n1[i]+n2[j])
print(new)

#---------------------------------------------------------------------------------------------------------

##26.(Home  work)
##Repeat   previous  program  with  comprehension
##
##Input1 :  [10 , 20 , 15]
##Input2 :  [30 , 40 , 35 , 32]
##Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32,
##           15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

n1 = eval(input('Enter 1st list : '))
n2 = eval(input('Enter 2nd list ; '))
print([n1[i]+n2[j] for i in range(len(n1)) for j in range(len(n2))])

#----------------------------------------------------------------------------------------------------------

##27.Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
##
##Let  1st string  be  HYD  and   2nd string  be   PUNE
##What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']
##
##Hint: Same  as  previous  program


n1 = input('Enter 1st list : ')
n2 = input('Enter 2nd list ; ')
print([n1[i]+n2[j] for i in range(len(n1)) for j in range(len(n2))])

#------------------------------------------------------------------------------------------------------------

##28.Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
##Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
##What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]

n1 = eval(input('Enter any list : '))
new = []
for i in range(len(n1)):
    new.extend(n1[i])
print(new)

#--------------------------------------------------------------------------------------------------

##29.Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
##
##Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
##
##What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]

n1 = eval(input('Enter any list : '))
print([n1[i][j] for i in range(len(n1)) for j in range(len(n1[i])) ])

#----------------------------------------------------------------------------------------------------

#30.Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10, 20], [10, 20],
         # [30, 40, 50], [30, 40, 50], [30, 40, 50],
         # [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
 

#--------------------------------------------------------------------------------------------------

#31Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]

print(a)  # [[],[0],[0,1],[0,1,2],[0,1,2,3]]

#-----------------------------------------------------------------------------------------------------























































































    
