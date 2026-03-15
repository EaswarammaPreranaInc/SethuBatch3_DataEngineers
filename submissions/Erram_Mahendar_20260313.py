#Write  a  program  to  determine  mode
'''
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
#Program:

a = list(map(int, input("Enter list : ").split()))

mode = None
ctr = 0

for i in set(a):        # unique elements
    count = a.count(i)  # count occurrences
    
    if count > ctr:
        ctr = count
        mode = i

print("mode =", mode)

#Output:
# Enter list : [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
# mode =   15

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) # [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
print(len(a)) # 3
print(a[0]) # How  to  print  1st  inner  list [10, 20, 30, 40]
print(a[1]) # How  to  print  2nd  inner  list [50, 60, 70, 80]
print(a[2]) # How  to  print  3rd  inner  list [90, 100, 110, 120]
print(a[0][2]) # How  to  print  30
print(a[1][3]) # How  to  print  80
print(a[2][1]) # How  to  print  100

#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0]) # How  to  print  1st   inner  list [10, 20]
print(a[1]) # How  to  print  2nd   inner  list [30, 40, 50]
print(a[2]) # How  to  print  3rd   inner  list [60, 70, 80, 90]
print(len(a[0])) # How  to  print  number  of  elements  in  1st  inner  list 2
print(len(a[1])) # How  to  print  number  of  elements  in  2nd  inner  list 3
print(len(a[2])) # How  to  print  number  of  elements  in  3rd  inner  list 4

#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function') # [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print(a) # [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Each  inner  list   of   outer  list  without  indexes')
for x in a:
    print(x) # 10 20
print('Elements  in  the  form   of  matrix   without  using  indexes')
for x in a:
    for y in x:
        print(y, end=' ') # 30 40 50
    print()
print('Elements  in  the  form   of  matrix  using  indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')# 60 70 80 90
    print()
'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x) # [10, 20]
             # [30, 40]
             # [50, 60]
             # [70, 80]
print()
for  x , y  in  a:
	print(x , y , sep = '...') # 10...20
                                    #  30...40
                                    #  50...60
                                    #  70...80
#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x) # [10, 20, 30]
             # [40, 50, 60]
             # [70, 80, 90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...') # 10...20...30
                                       # 40...50...60
                                       # 70...80...90

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x) # [10, 20]
                 # [30, 40, 50]
                 # [60, 70, 80, 90]
for  x , y  in  a:
	print(x , y ,	sep = '...') # 10...20
                                     # Error Because [30,40,50] has 3 elements but only 2 variables

#  Find  outputs  (Home  work)
a = [[]]
print(a[0]) # How  to  print  inner  list []
print(*a) # How  to  print  inner  list  in  another  way []

#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) #[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True)) # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a) # [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]


# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
# Program:

a = [x**3 for x in range(2, 11, 2)]

print(a) # [8, 64, 216, 512, 1000]


'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
#Program:

a = ['hyd', 'pune', 'chennai', 'vijayawada']
b = []
for x in a:
    b.append(x[0].upper())
print(b)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
#Program:
a = ['hyd', 'pune', 'chennai', 'vijayawada']
b = [x[0].upper() for x in a]
print(b)

'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
#Program:
s = input("Enter a sentence: ")
words = s.split()
result = []
for w in words:
    result.append([w.upper(), len(w)])
print(result)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
#Program:
s = input("Enter a sentence: ")
a = [[w.upper(), len(w)] for w in s.split()]
print(a)

'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
#Program:

a = list(map(int, input("Enter first list elements: ").split()))
b = list(map(int, input("Enter second list elements: ").split()))
c = []
n = min(len(a), len(b))   # minimum length
for i in range(n):
    c.append(a[i] + b[i])
print("Result =", c)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
#Program:
a = list(map(int, input("Enter first list elements: ").split()))
b = list(map(int, input("Enter second list elements: ").split()))
c = [a[i] + b[i] for i in range(min(len(a), len(b)))]
print("Result =", c)

'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
#Program:
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
a = []
for i in range(rows):
    a.append([0] * cols)
print(a)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
# Program:
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
a = [[0] * cols for i in range(rows)]
print(a)

'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
# Program:
a = list(map(int, input("Enter 1st list elements: ").split()))
b = list(map(int, input("Enter 2nd list elements: ").split()))
c = []
for x in a:
    if x not in b:
        c.append(x)
print("Output =", c)



'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
#Program:

a = list(map(int, input("Enter 1st list elements: ").split()))
b = list(map(int, input("Enter 2nd list elements: ").split()))
c = [x for x in a if x not in b]
print("Output =", c)


#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

#Program:
a = [x for x in range(1, 21) if x % 2 == 0]
print(a)

'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
# Program:
a = [x for x in range(2, 21, 2)]
print(a)


'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
#Program:
a = [x**2 for x in range(1, 21) if (x**2) % 2 == 0]
print(a)

#  Repeat  previous  program  with  comprehension  and  without  using  if
# Program:
a = [x**2 for x in range(2, 21, 2)]
print(a)

'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
#Program:
a = list(map(int, input("Enter 1st list elements: ").split()))
b = list(map(int, input("Enter 2nd list elements: ").split()))
c = []
for x in a:
    for y in b:
        c.append(x + y)

print("Result =", c)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
#Program:
a = list(map(int, input("Enter 1st list elements: ").split()))
b = list(map(int, input("Enter 2nd list elements: ").split()))

c = [x + y for x in a for y in b]

print("Result =", c)

'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
#Program:
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
result = [x + y for x in s1 for y in s2]
print("Result =", result)

'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
#Program:
a = eval(input("Enter a nested list: "))
b = []
for x in a:
    for y in x:
        b.append(y)
print("Output =", b)

'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
#Program:
a = eval(input("Enter a nested list: "))
b = [y for x in a for y in x]
print("Output =", b)

# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10, 20], [10, 20],[30, 40, 50], [30, 40, 50], [30, 40, 50],[60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
                              
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50],[60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]