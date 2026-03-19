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
# Code :
n = eval(input("Enter list : "))
mode = 0
cou = 0
for x in set(n):
    if n.count(x) > cou:
        mode = x
        cou = n.count(x)
print("Mode : ",mode)    

''' Output:
Enter list : [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode :  15
'''

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) # [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) # 3
print(a[0]) # How  to  print  1st  inner  list
print(a[1] ) # How  to  print  2nd  inner  list
print(a[2]) # How  to  print  3rd  inner  list
print(a[0][2]) # How  to  print  30
print(a[1][3]) # How  to  print  80
print(a[2][1]) # How  to  print  100

#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0]) # How  to  print  1st  inner  list
print(a[1] ) # How  to  print  2nd  inner  list
print(a[2]) # How  to  print  3rd  inner  list
print(*a[0]) # How  to  print  number  of  elements  in  1st  inner  list
print(*a[1]) # How  to  print  number  of  elements  in  2nd  inner  list
print(*a[2]) # How  to  print  number  of  elements  in  3rd  inner  list

#  How  to  print  nested  list  in  differnent  ways
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
   for i in x:
      print(i,end=' ')
   print()
print('Elements  in  the  form   of  matrix  using  indexes')
# How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)
for i in range(len(a)):
   for j in range(len(i)):
       print(a[i][j],end=' ')
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
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')
''' Output:
[10 , 20]

[30 , 40]

[50 , 60]

[70 , 80]

10...20
30...40
50...60
70...80
'''

#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
	print(x , y , sep = '...')
''' Output:
[10 , 20 , 30]

[40 , 50 , 60]

[70 , 80 , 90]

10...20...30
10...20
40...50...60
40...50
70...80...90
70...80
'''

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')
''' Output:
[10 , 20]

[30 , 40 , 50]

[60 , 70 , 80 , 90]

10...20
Error because less number of variables while unpacking

'''

#  Find  outputs  (Home  work)
a = [[]]
print(a[0]) # How  to  print  inner  list
print(*a) # How  to  print  inner  list  in  another  way

#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))# [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True)) # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a) # [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]

# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
# Code :
a = [2,4,6,8,10]
n = [pow(x,3) for x in a]
print(n)

# Output : [8, 64, 216, 512, 1000]
'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
# Code :
n = eval(input("Enter list of lower case strings : "))
res = []
for x in n:
    char = x[0].upper()
    res.append(char)
print(res)

''' Output:
Enter list of lower case strings : ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
'''
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
# Code :
n = eval(input("Enter list of lower case strings : "))
res = [x[0].upper() for x in n]
print(res)

''' Output:
Enter list of lower case strings : ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
'''
'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
# Code :
n = input("Enter any scentence : ").split()
res = []
for x in n:
    a = []
    a.append(x.upper())
    a.append(len(x))
    res.append(a)
print((res))

''' Output:
Enter any scentence : hyd  is  green  city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
'''
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
# Code :
n = input("Enter any scentence : ").split()
res = [[x.upper(),len(x)] for x in n]
print(res)

''' Output:
Enter any scentence : hyd  is  green  city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
'''
'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
# Code :
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
m = min(len(a),len(b))
res = []
for i in range(m):
    res.append(a[i]+b[i])
print(res)

''' Output:
Enter 1st list : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Enter 2nd list : [100 , 200 , 300 , 400]
[110, 220, 330, 440]
'''
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
# Code :
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
m = min(len(a),len(b))
res = [a[i]+ b[i] for i in range(m)]
print(res)

''' Output:
Enter 1st list : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Enter 2nd list : [100 , 200 , 300 , 400]
[110, 220, 330, 440]
'''
'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
# Code :
a = int(input("How many lists ?  : "))
b = int(input("How many elements in each list ? : "))
res = []
for i in range(a):
    n = [0] * b
    res.append(n)
        
print(res)

''' Output:
How many lists ?  : 3
How many elements in each list ? : 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''
'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
# Code:
a = int(input("How many lists ?  : "))
b = int(input("How many elements in each list ? : "))
res = [[0] * b for i in range(a)]
print(res)

''' Output:
How many lists ?  : 3
How many elements in each list ? : 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''
'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
# Code :
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
res = []
for x in a:
    if x not in b:
        res.append(x)
print(res)

''' Output:
Enter 1st list : [10 , 20 , 15 , 18 , 25 , 32]
Enter 2nd list : [30 , 40 , 10 , 25 , 15]
[20, 18, 32]
'''
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
# Code :
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
res = [x for x in a if x not in b]
print(res)

''' Output:
Enter 1st list : [10 , 20 , 15 , 18 , 25 , 32]
Enter 2nd list : [30 , 40 , 10 , 25 , 15]
[20, 18, 32]
'''
#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
res = [x for x in range(1,21) if x%2 ==0 ]
print("Even numbers between 1 and 20 : ",res)

'''
Even numbers between 1 and 20 :  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
# Code :
res = [x for x in range(0,21,2)]
print("Even numbers between 1 and 20 : ",res)

'''
Even numbers between 1 and 20 :  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
# Code :
res = [pow(x,2) for x in range(0,21) if x%2 ==0]
print("Squares of 1 to 20 which are divisible by 2 : ",res)

''' Output:
Squares of 1 to 20 which are divisible by 2 :  [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''
#  Repeat  previous  program  with  comprehension  and  without  using  if
# Code :
res = [pow(x,2) for x in range(0,21,2)]
print("Squares of 1 to 20 which are divisible by 2 : ",res)

''' Output:
Squares of 1 to 20 which are divisible by 2 :  [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''
'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
# Code :
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
res = []
for x in a:
    for y in b:
        res.append(x+y)
print(res)

''' Output:
Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,32]
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]
'''
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
# Code :
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
res = [x+y for x in a for y in b]
print(res)

''' Output:
Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,32]
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]
'''

'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
# Code :
a = input("Enter 1st string : ")
b = input("Enter 2nd string : ")
res = [x+y for x in a for y in b]
print(res)

''' Output:
Enter 1st string : HYD
Enter 2nd string : PUNE
['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']
'''
'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
# Code :
a = eval(input("Enter nested list : "))
res = []
for x in a:
    res.extend(x)
print(res)

''' Output:
Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''
'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
# Code :
a = eval(input("Enter nested list : "))
res = [e for x in a for e in x]
print(res)

''' Output:
Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
''' Output:
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)

''' Output:
[[] , [0] , [0,1] , [0,1,2] , s[0,1,2,3]]




