a = eval(input('Enter a list of elements: '))
s = set(a)
b = list(s)
res = 0
max = 0
count = 0
for i in range(len(b)):
    count = a.count(b[i])
    if count > max:
        max = count
        res = b[i]
print('mode = ',res)
print('counts = ',max)



#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
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



a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print('Nested list with print function')
print(a)
print('Each inner list of outer list without indexes')
for i in a:
    print(i)
print('Elements in the form of matrix without using indexes')
for i in a:
    for j in i:
        print(j, end="\t")
    print()
print('Elements in the form of matrix using indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end="\t")
    print()


a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for x in a:
    print(x)    # [10, 20] \n [30, 40] \n [50, 60] \n [70, 80]
print()     
for x, y in a:
    print(x , y , sep = '...')   # 10...20 \n 30...40 \n 50...60 \n 70...80



a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for x in a:
    print(x)    # [10, 20, 30] \n [40, 50, 60] \n  [70, 80, 90]
print()            
for x, y, z in a:
    print(x , y , z , sep = '...')   # 10...20...30 \n  40...50...60 \n  70...80...90


a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for x in a:
    print(x)          # [10, 20] \n  [30, 40, 50] \n  [60, 70, 80, 90]
for x, y in a:
    print(x , y , sep = '...')   # 10...20


a = [[]]
print(a[0])     # []
print(*a)       # []


a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))    # [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse=True))  # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)    # [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]



# Write a program to create a list with cubes of 2, 4, 6, 8, 10 using list comprehension
a = [x**3 for x in [2, 4, 6, 8, 10]]
print(a)   # [8, 64, 216, 512, 1000]



# Write a program to extract 1st character of each string in capital letters
# without using list comprehension
a = ['hyd', 'pune', 'chennai', 'vijayawada']
b = []
for x in a:
    b.append(x[0].upper())
print(b)   # ['H', 'P', 'C', 'V']



# Repeat previous program using list comprehension
a = ['hyd', 'pune', 'chennai', 'vijayawada']
b = [x[0].upper() for x in a]
print(b)   # ['H', 'P', 'C', 'V']


# Program to append each word of a sentence and its length to a list (without comprehension)
sentence = "hyd is green city"
words = sentence.split()
result = []
for word in words:
    result.append([word.upper(), len(word)])
print(result)   # [['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 3]]


# Repeat previous program using list comprehension
sentence = "hyd is green city"
result = [[word.upper(), len(word)] for word in sentence.split()]
print(result)   # [['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]


# Program to add two lists of unequal length without comprehension
list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]
result = []
min_len = min(len(list1), len(list2))
for i in range(min_len):
    result.append(list1[i] + list2[i])
print(result)   # [110, 220, 330, 440]



# Repeat previous program using list comprehension
list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]
result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]
print(result)  # [110, 220, 330, 440]


# Program to initialize a nested list with zeroes without comprehension
rows = 3
cols = 4
nested_list = []
for i in range(rows):
    nested_list.append([0] * cols)
print(nested_list)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, # Repeat previous program using list comprehension



rows = 3
cols = 4
nested_list = [[0] * cols for _ in range(rows)]
print(nested_list)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]0]]


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