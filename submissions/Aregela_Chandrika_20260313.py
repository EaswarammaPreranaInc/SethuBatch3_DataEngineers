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

n = eval(input("Enter List : "))  # n = [12,20,18,15,10,15,10,15,20,18,15,10,20,15,10]
a = set(n) # a = {12, 20, 18, 15, 10}
mode = 0 
ctr = 0 
for i in a:
   if n.count(i)>ctr:
        ctr = n.count(i)
        mode=i
print('mode:',mode)





#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) # [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) # 3

print("How  to  print  1st  inner  list")
print(a[0])

print(How  to  print  2nd  inner  list)
print(a[1])

print(How  to  print  3rd  inner  list)
print(a[2])

print(How  to  print  30)
print(a[0][2])

print(How  to  print  80)
print(a[1][-1])

print(How  to  print  100)
print(a[2][1])



#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)
print(a[0])

print(How  to  print  2nd   inner  list)
print(a[1])


print(How  to  print  3rd   inner  list)
print(a[2])


print(How  to  print  number  of  elements  in  1st  inner  list)
print(len(a[0]))


print(How  to  print  number  of  elements  in  2nd  inner  list)
print(len(a[1]))


print(How  to  print  number  of  elements  in  3rd  inner  list)
print(len(a[2]))




#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)

print('Each  inner  list   of   outer  list  without  indexes')
for i in a:
    print(i)

print('How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (with  for  loop)')
for i in a:
    print(i)

print('Elements  in  the  form   of  matrix   without  using  indexes')
for i in a:
    for j in i:
        print(j, end=" ")
    print()

#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (with  nested  loop)
for i in a:
    for j in i:
        print(j, end=" ")
    print()


print('Elements  in  the  form   of  matrix  using  indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()

#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (with  nested  loop)



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
    print(x)   # [10 , 20] <nextline> [30 , 40] <nextline> [50 , 60] <nextline> [70 , 80]
print()
for  x , y  in  a:
	print(x , y , sep = '...')   
    #  10...20
    #  30...40
    #  50...60
    #  70...80
    
    
#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)  # [10 , 20 , 30] <nextline> [40 , 50 , 60] <nextline> [70 , 80 , 90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...') # 10...20...30 <nextline> 40...50...60 <nextline> 70...80...90
    
    
    
    
    
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)    # [[10,20] <nextline> [30,40,50] <nextline> [60,70,80,90]]
for  x , y  in  a:
	print(x , y ,	sep = '...') # Error
    
    
    
    
    
#  Find  outputs  (Home  work)
a = [[]]
print("How  to  print  inner  list")  #  print(a[0])
print("How  to  print  inner  list  in  another  way")
for i in range a:
    print(i)






#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))  #  [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0],[2'Sita', 2000.0]]
print(sorted(a , reverse = True))  # [[20, 'Sita', 2000.0],[18, 'Kiran', 2800.0],[15, 'Rajesh', 3500.0],[10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)    # [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]




# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a = [x**3 for x in range(2,11,2)]
print(a)



'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''

a = input("Enter a list of lowecase letters :").split()
res=[]
for i in a:
    res.append(i[0].upper())
print(res)


 '''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''

a = input("Enter a list of lowecase letters :").split()
res = [i[0].upper() for i in a]
print(res)





'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''


a = input("Enter a list of lowecase letters :").split()
res=[]
for i in a:
    res.append([i.upper(),len(i)])
print(res)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
a = input("Enter a list of lowecase letters :").split()
res=[[i.upper(),len(i)] for i in a]
print(res)




'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

a = eval(input("Enter 1st List : "))
b = eval(input("Enter 2nt List : "))
res=[]
min=min(len(a),min(b))
for i in range(min):
        res.append(a[i]+b[i])
print(res)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''

a = eval(input("Enter 1st List : "))
b = eval(input("Enter 2nt List : "))
min=min(len(a),min(b))
res=[x+y for x,y in range(min+1)]
print(min)




'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

r = int(input("Enter number of rows : "))
c = int(input("Enter number of columns : "))
res = []
for i in range(r):
    res.append([0] * c)
print(res)



'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''






'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''


r = int(input("Enter number of rows : "))
c = int(input("Enter number of columns : "))
res = [[0] * c for i in range(r)]
print(res)




'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''


a = eval(input("Enter 1st List : "))
b = eval(input("Enter 2nd List : "))
res = [i for i in a if i in b]
print(res)



#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension





'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''


res = [i for i in range(1, 21) if i % 2 == 0]

print(res)





'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''




#  Repeat  previous  program  with  comprehension  and  without  using  if




'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''

a = eval(input("Enter 1st List : "))
b = eval(input("Enter 2nd List : "))
res = []
for i in a:
    for j in b:
        res.append(i + j)
print(res)





'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''


a = eval(input("Enter 1st List : "))
b = eval(input("Enter 2nd List : "))
res = [i + j for i in a for j in b]
print(res)





'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
s1 = input("Enter 1st String : ")
s2 = input("Enter 2nd String : ")

res = [i + j for i in s1 for j in s2]

print(res)


'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

a = eval(input("Enter Nested List : "))
res = []
for i in a:        
    for j in i:    
        res.append(j)
print(res)






'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''



a = eval(input("Enter Nested List : "))
res = []
    for j in i:    
        res.append(j)
print("Output :", res)





# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)






#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)  # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]