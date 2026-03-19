'''
Tricky  program
Write  a  program  to  determine  mode

1) What  is  mode ?  --->  The  element  which  is  repeated  maximum  number  of  times  in  the  list

2) Let  input  be  [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  is  set(list) ?  --->  {12 , 20 , 18 , 15 , 10}
    How  many  times  is  first  element  12  repeated  in  the  list  ?  --->  1
    How  many  times  is  2nd  element  20  repeated  in  the  list  ?  --->  3
    How  many  times  is  3rd  element  18  repeated  in  the  list  ?  ---> 2
    How  many  times  is  4th  element  15  repeated  in  the  list  ?  --->  5
    How  many  times  is  last  element  10  repeated  in  the  list  ?  --->  4
    What  is  the  mode  ?  --->  15  becoz  it  is  repeated  max  number  of  times  i.e.  5

3) mode =   15
    ctr =  5
'''
'''lst = [12,20,18,15,10,15,10,15,20,18,15,10,20,15,10]

mode = None
ctr = 0

for i in set(lst):
    c = lst.count(i)
    
    if c > ctr:
        ctr = c
        mode = i

print(lst)
print("Mode =", mode)
#===============================================================================================================
#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print(a[0])#print(How  to  print  1st  inner  list)
print(a[1])#print(How  to  print  2nd  inner  list)
print(a[2])#print(How  to  print  3rd  inner  list)
print(a[0][2])#print(How  to  print  30)
print(a[1][3])#print(How  to  print  80)
print(a[2][1])#print(How  to  print  100)
#===============================================================================================================
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])#(How  to  print  1st   inner  list)
print(a[1])#(How  to  print  2nd   inner  list)
print(a[2])#(How  to  print  3rd   inner  list)
print(len(a[0]))#(How  to  print  number  of  elements  in  1st  inner  list)
print(len(a[1]))#(How  to  print  number  of  elements  in  2nd  inner  list)
print(len(a[2]))#(How  to  print  number  of  elements  in  3rd  inner  list)
#===============================================================================================================#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
#('Nested list  with  print function')
print(a)
print('Each  inner  list   of   outer  list  without  indexes')
for i in a:
    print(i)
#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (with  for  loop)
for i in a:
    print(i)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for i in a:
    for j in i:
        print(j,end=" ")
    print()
#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (with  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)
#===============================================================================================================#
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x) #[[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
print()
for  x , y  in  a:
	print(x , y , sep = '...') #10...20
                                #30...40
                                #50...60
                                #70...80
#===============================================================================================================#
#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)  #[[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...') #10...20...30
                                    #40...50...60
                                    #70...80...90
#===============================================================================================================#
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x) #[[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
#for  x , y  in  a: #error because of out of range
	#print(x , y ,	sep = '...')
#===============================================================================================================#	
#  Find  outputs  (Home  work)
a = [[]]
print(a[0])#(How  to  print  inner  list)
#print(How  to  print  inner  list  in  another  way)
for i in a:
    print(i)	
#===============================================================================================================#    
#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) #[[5, 'Amar', 5000.0],
                # [10, 'Rama', 1000.0],
                #[15, 'Rajesh', 3500.0],
                #[18, 'Kiran', 2800.0],
                #[20, 'Sita', 2000.0]]
print(sorted(a , reverse = True))#[[20, 'Sita', 2000.0],
                                #[18, 'Kiran', 2800.0],
                                #[15, 'Rajesh', 3500.0],
                                #[10, 'Rama', 1000.0],
                                #[5, 'Amar', 5000.0]]
print(a)#[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
#===============================================================================================================#
# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a = [x**3 for x in [2,4,6,8,10]]
print(a)
#===============================================================================================================#
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']

a = ['hyd', 'pune', 'chennai', 'vijayawada']

b = []

for i in a:
    b.append(i[0].upper())

print(b)
#===============================================================================================================#
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']'''

'''a = ['hyd', 'pune', 'chennai', 'vijayawada']

b = [i[0].upper() for i in a]

print(b)
#===============================================================================================================#

Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

s = input("Enter any sentence : ")

words = s.split()

result = []

for i in words:
    result.append([i.upper(), len(i)])
print(result)  
#===============================================================================================================# 

(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]

s = input("Enter any sentence : ")

result = [[i.upper(), len(i)] for i in s.split()]

print(result)
#===============================================================================================================#

Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]

a = [10, 20, 30, 40, 50, 60, 70]
b = [100, 200, 300, 400]

c = []

n = min(len(a), len(b))

for i in range(n):
    c.append(a[i] + b[i])

print(c)
#===============================================================================================================#

(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]

a = [10, 20, 30, 40, 50, 60, 70]
b = [100, 200, 300, 400]

c = [a[i] + b[i] for i in range(min(len(a), len(b)))]

print(c)
#===============================================================================================================#
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
r = int(input("How many lists ? : "))
c = int(input("How many elements in each list ? : "))

a = []

for i in range(r):
    a.append([0] * c)

print(a)'''
#===============================================================================================================#
'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

r = int(input("How many lists ? : "))
c = int(input("How many elements in each list ? : "))

a = [[0] * c for i in range(r)]

print(a)'''
#===============================================================================================================#
'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]

a = [10, 20, 15, 18, 25, 32]
b = [30, 40, 10, 25, 15]

c = []

for i in a:
    if i not in b:
        c.append(i)

print(c)'''
#===============================================================================================================#
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]

a = [10, 20, 15, 18, 25, 32]
b = [30, 40, 10, 25, 15]

c = [i for i in a if i not in b]

print(c)
#===============================================================================================================#
#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
a = [i for i in range(1,21) if i % 2 == 0]

print("Even numbers between 1 and 20 :", a)'''
#===============================================================================================================#
'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]

a = [i for i in range(2, 21, 2)]

print("Even numbers between 1 and 20 :", a)
#===============================================================================================================#

Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]

a = [i*i for i in range(1,21) if (i*i) % 2 == 0]

print("Squares of 1 to 20 which are divisible by 2 :", a)'''
#===============================================================================================================#
#  Repeat  previous  program  with  comprehension  and  without  using  if
a = [i*i for i in range(2, 21, 2)]

print("Squares of 1 to 20 which are divisible by 2 :", a)
#===============================================================================================================#
'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops

a = [10, 20, 15]
b = [30, 40, 35, 32]

c = []

for i in a:
    for j in b:
        c.append(i + j)

print(c)
#===============================================================================================================#

(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
a = [10, 20, 15]
b = [30, 40, 35, 32]

c = [i + j for i in a for j in b]

print(c)
#===============================================================================================================#
'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''

a = input("enter a 1st string : ")
b = input("enter a 2nd string : ")
c = [i+j for i in a for j in b]
print(c)
#===============================================================================================================#
'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

a = eval(input("enter a list : "))
b = []
for i in a:
    b.extend(i)
print(b)
#===============================================================================================================#
'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
c = [j for i in a for j in i ]
print(c)
#===============================================================================================================#
# Find  outputs (Home  work)

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10 , 20],[10 , 20],[30 , 40 , 50],[30 , 40 , 50],[30 , 40 , 50],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90]]
#===============================================================================================================#
#  Nested  comprehension  demo  program (Home  work)

a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # [[],[0],[0,1],[0,1,2],[0,1,2,3]]