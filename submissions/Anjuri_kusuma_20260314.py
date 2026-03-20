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
a=eval(input("Enter any list : "))
b=set(a)
mode=None
ctr=0
for x in b:
    y=a.count(x)
    if y>ctr:
        ctr=y
        mode=x
print("mode=",mode," ",ctr)
----------------------------------------------------------------------------------------
#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)#[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))#3
print(How  to  print  1st  inner  list)#a[0]
print(How  to  print  2nd  inner  list)#a[1]
print(How  to  print  3rd  inner  list)#a[2]
print(How  to  print  30)#a[0][2]
print(How  to  print  80)#a[1][3]
print(How  to  print  100)#a[2][1]
-------------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)#a[0]
print(How  to  print  2nd   inner  list)#a[1]
print(How  to  print  3rd   inner  list)#a[2]
print(How  to  print  number  of  elements  in  1st  inner  list)#len(a[0])
print(How  to  print  number  of  elements  in  2nd  inner  list)#len(a[1])
print(How  to  print  number  of  elements  in  3rd  inner  list)#len(a[2])
------------------------------------------------------------------------------------------
#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a[0])
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
-------------------------------------------------------------------------------------------
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)#[10,20]/n[30,40]/n[50,60]/n[70,80]
print()
for  x , y  in  a:
	print(x , y , sep = '...')#10...20/n30...40/n50...60/n70...80
-------------------------------------------------------------------------------------------
#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)#[10,20,30]/n[40,50,60]/n[70,80,90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')#10...20...30/n40...50...60/n70...80...90
-------------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
a = [[]]
print(How  to  print  inner  list)#a[0]
print(How  to  print  inner  list  in  another  way)for x in a: -->print(x)
------------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))#[[5 , 'Amar'  ,5000.0],[10 , 'Rama' , 1000.0], [15 , 'Rajesh' , 3500.0],[18 , 'Kiran' , 2800.0] ,[20 , 'Sita' , 2000.0]]
print(sorted(a , reverse = True))#[[20 , 'Sita' , 2000.0],[18 , 'Kiran' , 2800.0],[15 , 'Rajesh' , 3500.0],[10 , 'Rama' , 1000.0],[5 , 'Amar'  ,5000.0]]
print(a)#[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
------------------------------------------------------------------------------------------
# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
--------------------------------------------------------------------------------
'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
a=eval(input("Enter any list :"))
b=[]
for x in a:
    b.append(x[0].upper())
print(b)
--------------------------------------------------------------------------------------
'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension
Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
a=input("ENter any sentence : ")
a.split()
b=[]
for x in a:
    b.append([x.upper,len(x)])
print(b)
---------------------------------------------------------------------------------------
'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
----------------------------------------------------------------------------------------
'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
Let inputs  be  3  and  4
What  is  the  output ?  ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
Hint:  Use  repetition  operator  *
'''


