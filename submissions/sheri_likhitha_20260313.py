a=eval(input("Enter the input: "))
mode=0
counter=0
for i in a:
    curr_freq=a.count(i)
    if curr_freq>counter:
       counter=curr_freq
       mode=i
print(mode)



#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)	#[[10,20,30,40],[50,60,70,80],[90,100,110,120]]
print(len(a))	#3
print(a[0])	#How  to  print  1st  inner  list
print(a[1])	#How  to  print  2nd  inner  list
print(a[2])	#How  to  print  3rd  inner  list
print(a[0][2])	#How  to  print  30
print(a[1][3])	#How  to  print  80
print(a[2][1])	#How  to  print  100


#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])	#How  to  print  1st   inner  list
print(a[1])	#How  to  print  2nd   inner  list
print(a[2])	#How  to  print  3rd   inner  list
print(len(a[0])	#How  to  print  number  of  elements  in  1st  inner  list)
print(len(a[1])	#How  to  print  number  of  elements  in  2nd  inner  list)
print(len(a[2])	#How  to  print  number  of  elements  in  3rd  inner  list)


#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print(a) 	#'Nested list  with  print function'
print("-"*20)
print('Each  inner  list   of   outer  list  without  indexes')
for inner_list in a:
	print(inner_list)
print("-"*20)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for inner_list in a:
	for element in inner_list:
	     print(element,end="")
        print()

print('Elements  in  the  form   of  matrix  using  indexes')
n=len(a)
for i in range(a):
	m=len(a[i])
	for j in range(m):
	    print(a[i][j],end="")
         print()
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)
for i in range(len(a)):
    for j in range(len(a[i])):
	print(a[i][j],end=" ")



#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)	#[10,20]/n[30,40]/n[50,60]/n[70,80]
print()
for  x , y  in  a:
	print(x , y , sep = '...')	#[10...20]/n[30...40]/n[50...60]/n[70...80]


#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)	#[10,20,30]\n[40,50,60]/n[70,80,90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')	#[10...20...30]/n[40...50...60]/n[70...80...90]


#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)	#[10,20]/n[30,40,50]/n[60,70,80,90]
for  x , y  in  a:
	print(x , y ,	sep = '...')	#error because too many values to unpack


#  Find  outputs  (Home  work)
a = [[]]
print(a[0])	#How  to  print  inner  list
print(How  to  print  inner  list  in  another  way)


#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))		#[[5,'Amar',5000.0],[10,'Rama',1000.0],[15,'Rajesh',35000.0],[18,'Kiran',2800.0],[20,'Sita',2000.0]]
print(sorted(a , reverse = True))
print(a)		#[[20,'sita',2000.0],[18,'Kiran',2800.0],[15,'Rajesh',35000.0],[10,'Rama',1000.0],[5,'Amar',5000.0]]




#list comprehension
cubes=[x**3 for x in range(2,11,2)]
print(cubes)

#without comprehension
input_list=eval(input("Enter the list: "))
result=[]
for item in input_list:
    if item:
        result.append(item[0].upper())
print(result)

#with comprehension
input_list=eval(input("Enter the list: "))
result=[i[0].upper() for i in input_list]
print(result)


#without comprehension
sentence=input("Enter the sentence: ")
words=sentence.split()
result=[]
for word in words:
    word_upper=word.upper()
    word_length=len(word_upper)
    result.append([word_upper,word_length])
print(result)


#with comprehension
sentence=input("Enter the sentence: ")
result=[(word.upper(),len(word))for word in sentence.split()]
print(result)



#without comprehension
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
result=[]
min_length=min(len(a),len(b))
for i in range(min_length):
    sum_val=a[i]+b[i]
    result.append(sum_val)
print(result)



#with comprehension
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
min_length=min(len(a),len(b))
result=[a[i]+b[i] for i in range(min_length)]
print(result)



a=eval(input("How many lists? : "))
b=eval(input("How many elements in each list ? : "))
nested_list=[[0]*b]*a
print(nested_list)



a=eval(input("How many lists? : "))
b=eval(input("How many elements in each list ? : "))
nested_list=[[0 for _ in range(b)]for _ in range(a)]
print(nested_list)



list1=eval(input("Enter 1st list: "))
list2=eval(input("Enter 2nd list: "))
result=[]
for i in list1:
    if i not in list2:
        result+=[i]
print(f"elements of 1st list which are not in 2nd list : {result}")



list1=eval(input("Enter 1st list: "))
list2=eval(input("Enter 2nd list: "))
result=[item for item in list1 if item not in list2]
print(f"elements of 1st list which are not in 2nd list : {result}")



even=[num for num in range(2,21)if num%2==0]
print(even)

#without using if
even=[num for num in range(2,21,2)]
print(even)


squares=[x**2 for x in range(2,21) if x%2==0]
print(f"squares of 1 to 10 which are divisible by 2 : {squares}")



#without using if
squares=[x**2 for x in range(2,21,2)]
print(f"squares of 1 to 10 which are divisible by 2 : {squares}")



list1=eval(input("Enter the list: "))
list2=eval(input("Enter the list: "))
result=[]
for i in list1:
    for j in list2:
        sum_val=(i+j)
        result.append(i+j)
print(result)  


list1=eval(input("Enter the list: "))
list2=eval(input("Enter the list: "))
result=[(i+j) for i in list1 for j in list2]
print(result)



list1=(input("Enter the list: "))
list2=(input("Enter the list: "))
result=[(i+j) for i in list1 for j in list2]
print(result)


#without comprehension
list=eval(input("Enter the list: "))
empty_list=[]
for sublist in list:
    for item in sublist:
        empty_list.append(item)
print(empty_list)


#with comprehension
list=eval(input("Enter the list: "))
nested_list=[item for sublist in list for item in sublist]
print(nested_list)



# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]] 
b = [ x  for  x  in  a  for  y  in  x]
print(b)	#[[10,20],[10,20],[30,40,50][30,40,50],[30,40,50],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90]]




#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)	#[[],[0],[0,1],[0,1,2],[0,1,2,3],[0,1,2,3,4]]












