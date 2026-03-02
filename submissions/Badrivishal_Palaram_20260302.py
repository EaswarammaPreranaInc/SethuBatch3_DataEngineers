'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
	
for i in range(65,91):
    print(chr(i),end =" ")
    
print("\n")

for j in range(97,123):
    print(chr(j),end=" ")


'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''

x=int(input("enter any number:"))

i=1
a=0
b=1

while i<=x;
	print(a)
	c=a+b
	a=b
	b=c
	i=i+1


'''
Write  a  program  to  search  for  'x'  in  fibonacci  series
1) Let  input  be   10
    What  is  the  output ? --->	Not  found
2) Let  input  be   21
    What  is  the  output ? --->  Found
3) Do  not  generate  fibonacci  series
'''
x=int(input("Eenter number to be searched:"))

a=0
b=1

while a<x:
	c=a+b
	a=b
	b=c
if a==x:
	print("found")
else:
	print("not found")



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







# Find  outputs  (Home  work)
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
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  ---> Found  at  index  2
2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found
3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
												Compare  'x'  with  next  element  of  list
4) What  action  to  be  made  when  'x'  matches   with  list  element ?  ---> Print  found   message  along  with  index  and do  not  search  for  'x'  in  rest  of  the  list
5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->  Print  not  found   message
6) Hint: Use  for  loop'''
 

y=eval(input("enter any list:"))
x=int(input("enter element to be found:"))

for i in range(len(y)):
	if y(i)==x:
		print("element found at the index:",i)
		break
	else:
		print("element not found")




'''Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
							 15 is  found  at  index  5
							 15 is  found  at  index  8										                                                 15 is  found   3  times



x=eval(input("Enter elements of the list"))
y=int(input("enter element you want to search"))

count=0

for i in range(len(x)):
	if x[i]==y;
		print(y,"is found at the index",i)
		count=count+1
if count>0:
	print(y,"is found ",count ,"times")
else:
	print(y , "is not found")


'''
#  Walrus   operator (:=)  demo  program
print(a := 25)#O/P:25
print(a = 25)#O/P:error
print(a)
print(a := 6 + 7)#O/P:13
print(a)#O/P:13
print((a := 6) + 7)#O/P:13
print(a)#O/P:13
print((a = 6) + 7)#O/P:error



# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
#O/P:Hyd

if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
#O/P:Sec:0

if  c = 0:
	print('Hyd')
else:
	print('Sec')
#O/P:error



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

sum=0
count=0

try:
    while True:
        x=eval(input("enter values:"))
        sum = sum+1
        count = count+1
except EOFError:
    pass

if count>0:
    print("Average =", sum / count)
else:
    print("No inputs given")						



 #  del  operator  demo program  (Home  work)
a = 25
print(a) #O/P:25
del   a 
print(a) #O/P:error



 # Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) #O/P: 25,25,25
del   a 
print(b , c)#O/P: 25,25
print(a)  #O/P:error
del   b
print(c)#O/P: 25
print(b)#O/P: error
del   c
print(c)#O/P: error



 #  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)#O/P:25 , 10.8 , 'Hyd'
del   a , b , c
print(a) #O/P: error
print(b) #O/P: error
print(c)#O/P: error


 # Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #O/P:[10 , 20 , 15 , 18]
del  a[2]  
print(a) #O/P:[10 , 20 , 18]
del  a
print(a) #O/P:error
print(a[0])#O/P:error



 # Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) #O/P:(10 , 20 , 15 , 18)
print(a[0]) #O/P:(10)
del  a[2] #O/P:error
del  a 
print(a)  #O/P:error
print(a[0])#O/P:error