Name-Dhruva Gupta			Subject-Python			Date-27/2/26

1)
x=int(input("Enter the number terms you need: "))
a=0
b=1
print(a)
print(b)
c=0
while c<x:
    c=a+b
    print(c)
    a=b 
    b=c

2)
a=eval(input("Enter the input: "))
for i in a:
    print(i)

3)
# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
    print(x) #[10,30,50]
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
    print(x) #[20,40,60]
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
    print(x) #[(10,20),(30,40),(50,60)]
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
    print(x)
    #10
    #30
    #50 

4)
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
    print(x , y , sep = '...') #10,20...30,40...50,60
for  x ,  y  in   a:
    print(x , y) 
    #Error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
    print(x , y , sep = '...')
    #Error
    

5)
# Identify  error  (Home  work)
for  x  in   123:
        print(x)
#Iterartion over sequences only

6)
# Find  outputs  (Home  work)
for  x   in   ():
        print(x) #Empty 
for  x   in  []:
        print(x) #Empty
for  x   in   {}:
        print(x) #Error
for  x   in   set():
        print(x) #Error
for  x   in   '':
        print(x)
for  x  in  range(10 , 10):
        print(x) #Error
for  x  in   range():
        print(x) #Error
for  x  in   (25):
        print(x) #Error

7)
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
    for  j  in  range(1 , 5):
            print(i ,  j)  
    print('Hello')
print('Bye')

'''
1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye
'''

8)
# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
               print(a[i])
print("------------")
print('For each loop')

for i in a:
        print(i)
print(*range(0,len(a)))
        

9)
#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(len(a),0,-1):
    print(a[i]) 
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
for i in a:
    print(i)


10)
'''Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
'''
a = eval(input("Enter the first list: "))
b = eval(input("Enter the second list: "))
c = []
for i in range(len(a)):   
    c.append(a[i] + b[i])
print(c)

a = eval(input("Enter the first list: "))
b = eval(input("Enter the second list: "))
c = []
i = 0
for x in a:
    c.append(x + b[i])
    i += 1
print(c)
             

11)
'''#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
'''
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(len(a)-5,len(a)-2):
    print(a[i])

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
i = 0
for x in a:
    if i >= 2 and i <= 4:
        print(x)
    i += 1


12)

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)): 
    a[i] +=  1
print('a :  ' , a) # a : [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
    x += 1
print('b :  ' ,  b) #b : [10, 20, 15, 18]


13)
l=eval(input("Enter the lines: "))
for i in range(l+1):
    spaces=l-i
    print(" "*spaces+" *"*i)

14)
n=int(input("Enter the number: "))
i=1
while i<=n:
    print(2*i)
    i=i+1
print("Bye")

15)
n=int(input("Enter the number: "))
i=1
while i<=n:
    print(2*i-1)
    i=i+1
print("Bye")

16)
n=int(input("enter the number: "))
i=1
while i<=n:
    print(i)
    i=i+1

17)
n = int(input("Enter the number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + (2*i)
print(sum)

18)
n = int(input("Enter the number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + (2*i-1)
print(sum)

19)
n=int(input("Enter the number of terms: "))
sum=0
for i in range(0,n+1):
    sum=sum+i
print(sum)

20)
n=int(input("Enter the terms: "))
sum=0
for i in range(0,n+1):
    sum=sum+(1.1*i)
print(sum)

21)
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop’)

#Sec
Hello
Sec
Hello
Sec
Hello
Sec
Hello
Sec
Hello
Outside loop

22)
# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print(‘Sec’)
#continue should be in loop and if has no condition

