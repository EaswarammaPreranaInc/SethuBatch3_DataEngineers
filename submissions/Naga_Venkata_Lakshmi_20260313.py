lst = eval(input("Enter any list:   "))
mode = lst[0]
max_count = 0
for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        mode = i
print("Mode is: ", mode)  


#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) # [[10 , 20 , 30 , 40] , [50 , 60 , 70 , 80] , [90 , 100 , 110 , 120]]
print(len(a)) #3
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
print(a[0])
print(a[1])
print('Each  inner  list   of   outer  list  without  indexes')
for inner_list in a:
     print(inner_list)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for inner_list in a:
    for elements in inner_list:
         print(element, end = '  ')
    print()
print('Elements  in  the  form   of  matrix  using  indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()







#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')

#outputs
#[10...20]
#[30...40]
#[50...60]
#[70...80]




#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

#outputs
[10 , 20 , 30]
[40 , 50 , 60]
[70 , 80 , 90]


10...20...30
40...50...60
70...80...90



#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...') #Error

#outputs
[10 , 20]
[30 , 40 , 50]
[60 , 70 , 80 , 90]



#  Find  outputs  (Home  work)
a = [[]]
print(a[0])
print(How  to  print  inner  list  in  another  way)
for inner_list in a:
    print(inner_list)





#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) #[[5 , 'Amar'  ,5000.0] , [10 , 'Rama' , 1000.0] ,  [15 , 'Rajesh' , 3500.0] ,[18 , 'Kiran' , 2800.0] , 
[20 , 'Sita' , 2000.0]] 
print(sorted(a , reverse = True)) #[[20 , 'Sita' , 2000.0] ,[18 , 'Kiran' , 2800.0] ,[15 , 'Rajesh' , 3500.0] ,[10 , 'Rama' , 1000.0]
[5 , 'Amar'  ,5000.0]]  
print(a) #[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]


strings = ['hyd' , 'pune' , 'Chennai' , 'vijayawada']
result = []

for s in strings:
    first_char = s[0].upper()
    result.append(first_char)
print(result)


strings = ['hyd' , 'pune' , 'chennai' , 'vijayawada']
result = [s[0].upper() for s in strings if s]


print(result)


sentence = input("Enter a sentence:  ").strip()
words = sentence.split()
result = []

for word in words:
    upper_word = word.upper()
    length = len(word)
    result.append([upper_word, length])
print(result)


sentence = input("Enter a sentence:  ").strip()
result = [[word.upper(), len(word)] for word in sentence.split()]
print(result)































              
