
lst =list(eval(input("Enter the elements: ")))
set1 = set(lst)
max=0
for i in set1:
    lst.count(i)
    if lst.count(i)>max:
        max = lst.count(i)
        elmnt = i
print(F'Mode of lst is {elmnt}, becoz it is repeated {max} times')

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print("How  to  print  1st  inner  list: ", a[0] )
print("How  to  print  2nd  inner  list : ", a[1])
print("How  to  print  3rd  inner  list : ", a[2])
print("How  to  print  30 : ", a[0][2] )
print("How  to  print  80 :", a[1][3])
print("How  to  print  100 :", a[0][1])

#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print("How  to  print  1st   inner  list: ", a[0])
print( "How  to  print  2nd   inner  list: ", a[1])
print( "How  to  print  3rd   inner  list: ", a[2])
print( "How  to  print  number  of  elements  in  1st  inner  list: ", len(a[0]))
print("How  to  print  number  of  elements  in  2nd  inner  list: ", len(a[1]))
print("How  to  print  number  of  elements  in  3rd  inner  list: ", len(a[2]))

#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function: ', a[:])
print(*a)
print('Each  inner  list   of   outer  list  without  indexes:', *a)
# How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (with  for  loop)
for i in a:
    print(i, end="")
print('Elements  in  the  form   of  matrix   without  using  indexes:',*a, sep="\n")
# How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (with  nested  loop)
for i  in a:
    for j in i:
        print(j,end=" ")
    print()
print()
print('Elements  in  the  form   of  matrix  using  indexes', a[0] ,a[1] ,a[2], sep="\n")
# How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()

a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x) # [10,20] [30,40] [50,60], [70,80]
print()
for  x , y  in  a:
	print(x , y , sep = '...') # 10...20 30...40 50...60 70...80

 Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x) #[10, 20, 30] [40, 50, 60] [70, 80, 90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')  # 10...20...30 40...50...60 70...80...90

 Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x) # [10 , 20] [30 , 40 , 50] [60 , 70 , 80 , 90]
for  x , y  in  a:
	print(x , y ,	sep = '...') # 10...20 # error 'too many values to unpack (expected 2)'

#  Find  outputs  (Home  work)
a = [[]]
print("How  to  print  inner  list : ", a[0])
print("How  to  print  inner  list  in  another  way: ", *a)

#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) # [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True)) # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a) # [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
# sorted is a function that doesn't modify the original list instead creates new

# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)

a = [x**3 for x in range(2,11,2)]
print(a)

'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''

import ast
lst = ast.literal_eval(input("Enter the list of strings: "))
print(lst)
result = []
for i in lst:
    result.append(i[0].upper())
print(result)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
cities = ['hyd', 'pune', 'chennai', 'vijayawada']
lst = [i[0].upper() for i in cities]
print(lst)

'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''

sentence = input("Enter the sentence: ")
words = sentence.split()
result =  []
for word in words:
    result.append([word.upper(), len(word)])
print(result)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
lst = input("Enter the sentence : ")
words = lst.split()
a = [[word.upper(), len(word)] for word in words]
print(a)

'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

lst1 = eval(input("Enter the elements: "))
lst2 = eval(input("Enter the elements: "))
n = len(lst1)
m = len(lst2)
p = min(n,m)
result = []
for i in range(0,p):
    result.append(lst1[i]+lst2[i])
print(result)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''

lst1 = eval(input("Enter the integers: "))
lst2 = eval(input("Enter the integers: "))

n = len(lst1)
m = len(lst2)
p=min(n,m)

a  = [lst1[i]+lst2[i] for i in range(0,p)]
print(a)

'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
lst=[]
for i in range(0,a):
    lst.append([0]*b)

print(lst)

# Program to extract elements of 1st list not in 2nd list without comprehension
list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]
result = []
for x in list1:
    if x not in list2:
        result.append(x)
print(result)   # [20, 18, 32]


# Repeat previous program using list comprehension
list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]
result = [x for x in list1 if x not in list2]
print(result)   # [20, 18, 32]


# Program to print even numbers between 1 and 20 using list comprehension
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Print even numbers between 1 and 20 using list comprehension without using 'if'
even_numbers = [x for x in range(2, 21, 2)]
print(even_numbers)     # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Program to print squares of numbers 1 to 20 divisible by 2 using list comprehension
squares = [x**2 for x in range(1, 21) if x**2 % 2 == 0]
print(squares)      # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


# Repeat previous program using list comprehension without 'if'
# Only even numbers squared will be divisible by 2
squares = [x**2 for x in range(2, 21, 2)]
print(squares)      # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]



# Program to add each element of 1st list with all elements of 2nd list without comprehension
list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]
result = []
for x in list1:
    for y in list2:
        result.append(x + y)
print(result)   # [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]



# Repeat previous program using list comprehension
list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]
result = [x + y for x in list1 for y in list2]
print(result)   # [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]



# Program to concatenate each character of 1st string with every character of 2nd string using list comprehension
str1 = "HYD"
str2 = "PUNE"
result = [ch1 + ch2 for ch1 in str1 for ch2 in str2]
print(result)   # ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']



# Concatenate each character of 1st string with every character of 2nd string using list comprehension
str1 = "HYD"
str2 = "PUNE"
result = [c1 + c2 for c1 in str1 for c2 in str2]
print(result)   # ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']



# Program to convert a nested list to a flat list without comprehension
nested_list = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)    # [10, 20, 30, 40, 50, 60, 70, 80, 90]


# Program to convert a nested list to a flat list using list comprehension
nested_list = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)    # [10, 20, 30, 40, 50, 60, 70, 80, 90]


a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [x for x in a for y in x]
print(b)    # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]



a = [[j for j in range(i)] for i in range(5)]
print(a)  # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]