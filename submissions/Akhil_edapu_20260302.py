'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''



number = int(input("Enter a number :"))
num = number
fib1=0
fib2=1
fib3=fib1+fib2

if number == 0:
    print(fib1)
elif number == 1:
    print(fib1)
elif number == 2:
    print(fib1)
    print(fib2)
elif number <0:
    print('invalid')
else:
    #print(fib1)
    #print(fib2)
    while(number > 0):
        #print(fib3)
        
        
        fib1=fib2
        fib2=fib3
        fib3=fib1+fib2
        number=number-1
        if num == fib3:
            print('found')
            exit()
        
    print('not found')
            
            
'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''

for i in range(65,91):
    print(chr(i), end=' ')
print()
for j in range(97,123):
    print(chr(j),end=' ')
    
    
'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''

number = int(input("Enter a number: "))

fib1=0
fib2=1

count=2
num=number


if number == 0:
    print(fib1)
elif number == 1:
    print(fib2)
elif number == 2:
    print(fib1)
    print(fib2)
elif number <0:
    print('Invalid')
else:
    print(fib1)
    print(fib2)
    while(number > 0):
        fib3=fib1+fib2
        print(fib3)
        fib1=fib2
        fib2=fib3
        count=count+1
        number=number-1
        if(count == num):
            break
       
      
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
#1
#sec
#hello
#2
#sec
#hello
#3
#hello
#4
#sec
#hello
#5
#sec
#hello
#6
#hello
#7
#sec
#hello
#outside loop





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

#1
#sec
#hello
#2
#sec
#hello
#3
#sec
#hello
#4
#sec
#hello
#5
#sec
#hello
#6
#sec
#hello
#7
#sec
#hello
#8
#else suite
#outside loop


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

element = eval(input("Enter any list :"))
key = int(input("Enter the element to be searched :"))


list1 = element

for x in range(len(list1)):
    if key == list1[x]:
        print('Found')
        print(f'index:{x} element:{list1[x]}')
        break
else:
    print('Not found')
    
#second approach to find element in list by using the flag varable 
n = eval(input("Enter any list : "))
key = int(input("Enter number to search:"))
flag=0

for x in range(len(n)):
    if key == n[x]:
        flag=1
        break

if flag == 1:
    print('found')
    print(f'index: {x} element:{n[x]}')
else:
    print('not found')

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

num = eval(input("Enter any list :"))
key = int(input("Enter number to search :"))
count=0

for i in range(len(num)):
    if key == num[i]:
        count+=1
        print(f'{num[i]} is found at {i}')
print(f'{key} found {count} times')
    
if count ==0:
    print(f'not found the key in list{key}')



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

num = eval(input("Enter anything :"))

sum=0
for x in range(len(num)):
    sum=sum+num[x]
    
avg = sum/len(num)
print(avg)


#  Walrus   operator (:=)  demo  program
print(a := 25) #a = 25
print(a = 25) # nothing
print(a) #25
print(a := 6 + 7) #13
print(a) nothing
print((a := 6) + 7) #6
print(a) #nothing 
print((a = 6) + 7) #6


# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
if  c = 0:
	print('Hyd')
else:
	print('Sec')
	
	



#  del  operator  demo program  (Home  work)
a = 25
print(a)  #25
del   a  #reference got deleted
print(a) #None


# Find  outputs  (Home  work)
a = b = c = 25 
print(a , b , c) #25 25 25
del   a # reference of a is deleted
print(b , c) #25 25
print(a)   #None
del   b #reference of b is deleted
print(c) # 25
print(b) #none
del   c #reference and now object 25 deleted
print(c) #none


#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd' 
print(a , b , c) #25 10.8 hyd
del   a , b , c #yes
print(a)  #none
print(b) #none
print(c)#none


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18] 
print(a)   [10,20,15,18]
del  a[2]  # 15 is deleted from list
print(a) #[10,20,18]
del  a #whole list reference and object is also deleted
print(a)  #nothing
print(a[0]) #error


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)   #(10,20,15,18)
print(a[0])  10 
del  a[2] #Error
del  a  #error
print(a)  #not executed
print(a[0]) #not executed
