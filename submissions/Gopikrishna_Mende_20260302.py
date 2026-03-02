'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''

for i in range(65,123):
    if i<=90:
        print(chr(i),end=" ")
        if i==90:
            print()
    elif i>=97:
        print(chr(i),end=" ")


'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
x= int(input("Enter a value x :"))
if x<0:
    print("invalid")
elif x>=0:
    a=0
    b=1
    sum=a+b #2
    print(f"first {x} terms:")
    while sum < x:
        print(a, end= " ")
        sum=a+b
        a=b
        b=sum
        sum+=1
     

'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
x= int(input("Enter a number:"))
a=0
b=1
if x<0:
    print('invalid')
elif x==0 or x==1:
    print("Found")
else:
     n=0
     while n<x:
        n=a+b
        a=b
        b=n
     if n==x:
            print("Found")
     else:
             print("Not found")     


    x= int(input("Enter a number:"))

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')

'''
1
sec
Hello
2
sec
Hello
3
4
sec  
Hello
5
sec
Hello
6
7
sec
Hello
else suite
outside Loop 
'''    
Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')

'''
1
sec
Hello
2
Sec
Hello
3
Sec
Hello
4
sec   
Hello
5
sec
Hello
6
sec
Hello
7
sep
Hello
else suite
outside loop
'''


'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  ---> Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
																												Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  when  'x'  matches   with  list  element ?  ---> Print  found   message  along  with  index  and
																														do  not  search  for  'x'  in  rest  of  the  list

5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->  Print  not  found   message

6) Hint: Use  for  loop

'''
a= eval(input("Enter a list:"))
b=int(input("Enter the element to search:"))
count=0
for i in a:
	if i==b:
		print(f" {b} is found at : {count}")
		break
	count=count+1
else:
	print("Not found")

'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
												   15 is  found  at  index  5
												   15 is  found  at  index  8
												   15 is  found   3  times
												   
'''	   
a= eval(input("Enter a list:"))
b=int(input("Enter the element to search:"))
count=0
total=0
for i in a:  [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
if i ==b:
		print(f" {b} is found at : {count}")
		total=total+1
		count=count+1
if total>0:
	print(f'{b} is found {total}')
else:
	print("not found")

#  Walrus   operator (:=)  demo  program
print(a := 25) #25
print(a = 25) # Error
print(a) # 25
print(a := 6 + 7) #13
print(a)#13 
print((a := 6) + 7) #13
print(a)#6
print((a = 6) + 7) # Error

# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b) #sec :0
if  c = 0:
	print('Hyd') # Error
else:
	print('Sec')

'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''
try:
	sum=0
	count=0
	k=0
	while True:
		k=eval(input("enter any input:"))
		sum=sum+k
		count=count+1
except:
	average=sum/count
	print(average)
  
 
 
 #  del  operator  demo program  (Home  work) 
a = 25 
print(a) # 25  
del   a  
print(a) # ERROR-Nothing 
  

  # Find  outputs  (Home  work) 
 a = b = c = 25 
 print(a , b , c)# 25 25 25 
 del   a 
 print(b , c) # 25 25 
 print(a)  # ERROR-Nothing 
 del   b 
 print(c) # 25 
 print(b)# ERROR-Nothing 
 del   c 
 print(c) #ERROR-Nothing 
  
  #  Can  multiple  objects  be  deleted  with  same  del  operator ? 
 a , b , c = 25 , 10.8 , 'Hyd' 
 print(a , b , c) #25  10.8  'Hyd' 
 del   a , b , c 
 print(a) #ERROR-Nothing 
 print(b) #ERROR-Nothing 
 print(c) #ERROR-Nothing 
  
  # Find outputs  (Home  work) 
 a = [10 , 20 , 15 , 18] 
 print(a) # [10 , 20 , 15 , 18] 
 del  a[2]  # [10 , 20 , 18] 
 print(a) # [10 , 20 , 18] 
 del  a  
 print(a) # ERROR 
 print(a[0]) # ERROR  
  
 # Find outputs  (Home work) 
 a = (10 , 20 , 15 , 18) 
 print(a)   
 print(a[0])  
 del  a[2]  
 del  a  
 print(a)   
 print(a[0])