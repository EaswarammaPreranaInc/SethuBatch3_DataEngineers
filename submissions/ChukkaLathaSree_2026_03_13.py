image

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

x = input('Enter the list: ')
mode = max(x, key=x.count)
ctr = 0
for y in set(x):
 count = x.count(y)
if count> ctr:
  ctr = count
  mode = y
print("mode = " , mode)

image

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)--->[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))--->len(3)
print(How  to  print  1st  inner  list)--->[:1]
print(How  to  print  2nd  inner  list)--->[:2]
print(How  to  print  3rd  inner  list)--->[:-1]
print(How  to  print  30)
print(How  to  print  80)
print(How  to  print  100)


#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)--->[:1]
print(How  to  print  2nd   inner  list)--->[:2]
print(How  to  print  3rd   inner  list)--->[:-1]
print(How  to  print  number  of  elements  in  1st  inner  list)
print(How  to  print  number  of  elements  in  2nd  inner  list)
print(How  to  print  number  of  elements  in  3rd  inner  list)

#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(???)
print('Each  inner  list   of   outer  list  without  indexes')
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (with  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (with  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)



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
    print(x)--->[[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
print()
for  x , y  in  a:
	print(x , y , sep = '...')


#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)--->[[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')


#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)--->[[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x , y  in  a:
	print(x , y ,	sep = '...')--->[10,20]...[30,40,50]...[60,70,80,90]


#  Find  outputs  (Home  work)
a = [[]]
print(How  to  print  inner  list)--->[:1]
print(How  to  print  inner  list  in  another  way)


#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 ,  , 'Amar'  ,5000.05 , 'Amar'  ,5000.05 , 'Amar'  ,5000.0 , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))--->[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0]  , [5 , 'Amar'  ,5000.0] ]
print(sorted(a , reverse = True))--->[[5 , 'Amar'  ,5000.0], ]
print(a)

image

# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)


image
'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
lst = ['hyd', 'pune', 'chennai', 'vijayawada']

result = []

for x in lst:
    ch = x[0].upper()
    result.append(ch)

print(result)

image
'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
# Input sentence
s = "hyd is green city"

result = []

words = s.split()

for w in words:
    word = w.upper()
    length = len(w)
    result.append([word, length])

print(result)
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
s = "hyd is green city"

result = [[word.upper(), len(word)] for word in s.split()]

print(result)

image
'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
# First list
list1 = [10, 20, 30, 40, 50, 60, 70]

# Second list
list2 = [100, 200, 300, 400]

result = []

n = min(len(list1), len(list2))

for i in range(n):
    result.append(list1[i] + list2[i])

print(result)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
list1 = [10, 20, 30, 40, 50, 60, 70]

list2 = [100, 200, 300, 400]

result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]

print(result)
'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *


rows = 3
cols = 4

result = []

for i in range(rows):
    row = [0] * cols
    result.append(row)

print(result)

'''
'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

rows = 3
cols = 4

result = [[0] * cols for i in range(rows)]

print(result)
'''

image
'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
list1 = [10, 20, 15, 18, 25, 32]

list2 = [30, 40, 10, 25, 15]

result = []

for x in list1:
    if x not in list2:
        result.append(x)

print(result)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
list1 = [10, 20, 15, 18, 25, 32]

list2 = [30, 40, 10, 25, 15]

result = [x for x in list1 if x not in list2]

print(result)

image
#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

nums = [i for i in range(1, 21) if i % 2 == 0]

print(nums)

'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
nums = []

for i in range(1, 21):
    if i % 2 == 0:
        nums.append(i)

print(nums)
'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
#  Repeat  previous  program  with  comprehension  and  without  using  if

squares = [i*i for i in range(1,21) if (i*i) % 2 == 0]

print(squares)
'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
list1 = [10, 20, 15]

list2 = [30, 40, 35, 32]

result = []

for x in list1:
    for y in list2:
        result.append(x + y)

print(result)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

result = [x + y for x in list1 for y in list2]

print(result)
'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
s1 = "HYD"
s2 = "PUNE"

result = [x + y for x in s1 for y in s2]

print(result)
'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]


lst = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

result = []

for sublist in lst:
    for x in sublist:
        result.append(x)

print(result)

'''

# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)--->  [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

b = [x for x in a for y in x]

print(b)

#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)--->1 , 2 , 3 , 4 , ss5

a = [[j for j in range(i)] for i in range(5)]
print(a)












