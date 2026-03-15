'''
Tricky  program
Write  a  program  to  determine  mode
What  is  mode ?  --->  The  element  which  is  repeated  maximum  number  of  times  in  the  list
'''


data=eval(input("Enter List : "))
unique_elements = set(data)
mode = None
max_count = 0
for item in unique_elements:
    current_count = data.count(item)
    if current_count > max_count:
        max_count = current_count
        mode = item
print(f"Mode : {mode}")

'''
output
Enter List : [12, 20, 18, 15, 10, 15, 10, 15, 20, 18, 15, 10, 20, 15, 10]
Mode : 15
'''


#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)#[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))#3
print(How  to  print  1st  inner  list)#print(a[0])
print(How  to  print  2nd  inner  list)#print(a[1])
print(How  to  print  3rd  inner  list)#print(a[2])
print(How  to  print  30)#print(a[0][2]
print(How  to  print  80)#print(a[1][3])
print(How  to  print  100)#print(a[2][1])


#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)#print(a[0])
print(How  to  print  2nd   inner  list)#print(a[1])
print(How  to  print  3rd   inner  list)#print(a[2])
print(How  to  print  number  of  elements  in  1st  inner  list)#print(len(a[0]))
print(How  to  print  number  of  elements  in  2nd  inner  list)#print(len(a[1))
print(How  to  print  number  of  elements  in  3rd  inner  list)#print(len(a[2]))


#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')#
print(???)#print(a)
print('Each  inner  list   of   outer  list  without  indexes')
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (with  for  loop)
'''
print('Each inner list of outer list without indexes')
for sublist in a:
    print(sublist)
'''
print('Elements  in  the  form   of  matrix   without  using  indexes')
How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (with  nested  loop)
'''
for sublist in a:
    for item in sublist:
        print(item, end=' ') # print item followed by a space
    print()
'''
print('Elements  in  the  form   of  matrix  using  indexes')
How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)
'''
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
'''


#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()#[10,20] <nextline> [30,40] <nextline> [50,60] <nextline> [70,80]
for  x , y  in  a:
	print(x , y , sep = '...')#10...20 <nextline> 30...40 <nextline> 50...60 <nextline> 70...80
	
	
#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()#[10,20,30] <nextline> [40,50,60] <nextline> [70,80,90]
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')#10...20...30 <nextline> 40...50...60 <nextline> 70...80...90
	
	
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)#[10,20] <nextline> [30,40,50] <nextline> [60,70,80,90]
for  x , y  in  a:
	print(x , y ,	sep = '...')#10...20 <nextline> error to many values to unpack

#  Find  outputs  (Home  work)
a = [[]]
print(How  to  print  inner  list)#print(a[0]
print(How  to  print  inner  list  in  another  way)#for inner in a: <nextline> <tab> print(inner)


# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
lt=[ 2 , 4 , 6 , 8 , 10]
cube_list=[item*item*item for item in lt]
print(cube_list)


'''
output
[8, 64, 216, 512, 1000]
'''



'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''


lt=eval(input("Enter list of lower case strings : "))
fl=[]
for i in range(len(lt)):
    fl+=lt[i][0].upper()
print(fl)


'''
output
Enter list of lower case strings : ['hyd','pune','chennai','vijayawada']
['H', 'P', 'C', 'V']
'''







'''
(Home  work)
Repeat   previous  program  with  comprehension
Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
Output :  ['H' , 'P' , 'C' , 'V']
'''
lt=eval(input("Input: "))
fl=[lt[i][0].upper() for i in range(len(lt))]
print(fl)

'''
output
Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
Output :  ['H' , 'P' , 'C' , 'V']
'''


'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension
Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]


'''
sentence=input("Enter any sentence : ")
words = sentence.split()
result = []
for word in words:
    upper_word = word.upper()
    word_len = len(word)
    result.append([upper_word, word_len])
print(result)


'''
output
Enter any sentence : hyd  is  green  city     
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
'''



'''
(Home  work)
Repeat   previous  program  with  comprehension
Input :  hyd  is  green  city
Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''


sentence = input("Enter any sentence : ")
result = [[word.upper(), len(word)] for word in sentence.split()]
print(result)


'''
output
Enter any sentence : hyd  is  green  city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
'''


'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

lt1=eval(input("Enter 1st list : "))
lt2=eval(input("Enter 2nd list : "))
result=[]
for i in range(min(len(lt1),len(lt2))):
    result.append(lt1[i]+lt2[i])
print(result)


'''
output
Enter 1st list : [10,20,30,40]
Enter 2nd list : [1,2,3,4,5,6,7,8]
[11, 22, 33, 44]
'''

'''
(Home  work)
Repeat   previous  program  with  comprehension
Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''

lt1=eval(input("Enter 1st list : "))
lt2=eval(input("Enter 2nd list : "))
result=[lt1[i]+lt2[i] for i in range(min(len(lt1),len(lt2)))]
print(result)

'''
output
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

lists = int(input("How many lists : "))
elements=int(input("How many elements in each lists : "))
result=[]
for i in range(lists):
    n_list = [0] * elements
    result.append(n_list)
print(result)

'''
output
How many lists ? : 4
How many elements in each lists ? : 5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''


'''
(Home  work)
Repeat   previous  program  with  comprehension
Inputs :  3  and  4
Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

lists = int(input("How many lists : "))
elements=int(input("How many elements in each lists : "))
result=[[0] * elements for i in range(lists)]
print(result)


'''
output
How many lists : 4
How many elements in each lists : 5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''

'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

l1 = eval(input("Enter 1st list : "))
l2 = eval(input("Enter 2st list : "))
res = []
for x in l1:
    if x not in l2:
        res.append(x)
print("Elements of 1st list which are not in second list : ",res) 


'''
output
Enter 1st list :  [10 , 20 , 15 , 18 , 25 , 32]
Enter 1st list :  [30 , 40 , 10 , 25 , 15]
Elements of 1st list which are not in second list : [20, 18, 32]
'''


'''
(Home  work)
Repeat   previous  program  with  comprehension
Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''

l1 = eval(input("Enter 1st list : "))
l2 = eval(input("Enter 2st list : "))
res = [x for x in l1 if x not in l2]
print("Elements of 1st list which are not in second list : ",res) 

'''
output
Enter 1st list :  [10 , 20 , 15 , 18 , 25 , 32]
Enter 1st list :  [30 , 40 , 10 , 25 , 15]
Elements of 1st list which are not in second list : [20, 18, 32]
'''

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

lt=[ x for x in range(1,21) if x%2==0]
print("Even numbers between 1 to 20 : ",lt)#Even numbers between 1 to 20 : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
Repeat  previous  program  with  comprehension  and  without  using  if
Output: [Even  numbers  between  1  and  20]
'''

print([i for i in range(2,20,2)]

'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
print([i*i if i*i%2==0 for i in range(1,21)]

#Repeat  previous  program  with  comprehension  and  without  using  if
print([i*i  for i in range(1,21,2)]

 '''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
l1=list(input())
l2=list(input())
l=[]
for i in l1:
	l.append(i+sum(l2)]
print(l)
	

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
l1=list(input())
l2=list(input())
print([i+sum(l2) for i in l1]


 '''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
s1=input()
s2=input()
l=[]
for i in range(s1):
	l.append(s1[i}+s2[i]]
print(l)

 '''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
l=[]
for i in list:
	for j in i:
		l.append(j)
print(l)

'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
print(j for i in list for j in i])

 # Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
#[10 , 20, 30 , 40 , 50, 60 , 70 , 80 , 90]

 #  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
#[[0],[0,1],[0,1,2],[0,1,2,3],[0,1,2,3,4]]
