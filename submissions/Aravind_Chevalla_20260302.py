'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
i=65
while i<=90:
  print(chr(i),end="  ")
  i+=1
print()
j=97
while j<=122:
    print(chr(j),end="  ")
    j+=1

'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''

x=int(input("Enter values to be searched:"))
a=0
print(a)
if x==1:
	exit()
b=1
print(b)
for i in range(x-2):
    c=a+b
    a=b
    b=c
    print(c)




'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
x=int(input("Enter values to be searched:"))
a=0
b=1
for i in range(x):
    c=a+b
    a=b
    b=c
    if c==x:
        print("Found")
        break
else:
    print("Not found")



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
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
else suite
Outside loop

'''
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
1
Sec
Hello
2
Sec
Hello
3
Sec
Hello
4
Sec
Hello
5
Sec
Hello
6
Sec
Hello
7
Sec
Hello
else suite
Outside loop



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

5) What  …
'''

a=eval(input("Enter any list:"))
b=int(input("Enter element to be searched:"))
for i in range(len(a)):
    if a[i]==b:
        print("Found at index",i)
        exit()
else:
    print("Not found")


'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
'''

a=eval(input("Enter any list:"))
b=int(input("Enter element to be searched:"))
count=0
for i in range(len(a)):
    if a[i]==b:
        print("Found at index",i)
        count+=1
else:
    print("not")
print(b,"is found",count,"times")							



'''

#  Walrus   operator (:=)  demo  program
print(a := 25) #25
print(a = 25) #error
print(a) #25
print(a := 6 + 7)# 13
print(a) #13
print((a := 6) + 7) #13
print(a)#6
print((a = 6) + 7) #error


 # Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') #Hyd
else:
	print('Sec') 
if  b := 0:
	print('Hyd')   
else:
	print('Sec : ' , b) #Sec  0
if  c = 0:
	print('Hyd') #Error
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


sum=0
count=0
try:
 while True:
    a=eval(input("Enter elements: "))
    sum+=a
    count+=1
except:
    print()
b=sum/count
print("Average=",b)



 #  del  operator  demo program  (Home  work)
a = 25
print(a)  #25 
del   a 
print(a) #error


 # Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) # 25
print(a)  
del   b
print(c) #25
print(b) #error
del   c
print(c)# error


#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) #25 10.8 Hyd
del   a , b , c
print(a) #error
print(b) #error
print(c) #error


 # Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)    #[10 , 20 , 15 , 18]
del  a[2] 
print(a) #[10,20,18]
del  a
print(a)  #error
print(a[0]) #error

 # Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #(10 , 20, 15 , 18)
print(a[0])  #10
del  a[2] 
del  a 
print(a)  #error

print(a[0])#error
