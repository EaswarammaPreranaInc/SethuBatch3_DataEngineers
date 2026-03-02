# upper lower and lower case
a='a'
for i in range(26):
    print(a,end=" ")
    a=chr(ord(a)+1)
print()

a='A'
for i in range(26):
    print(a,end=" ")
    a=chr(ord(a)+1)
print()

#fibonacci series
n=int(input("how many number you want in fibonacci series"))
a=0
s=0
b=1
if(n==0 or n>1):
    print(a,end= " ")
if(n==1 or n>1):
    print(b,end= " ")
n=n-2
while(n!=0):
    s=a+b
    print(s,end=" ")
    n-=1
    a,b=b,s

#fibonnaci series
n=int(input("Is this element present in fibonnaci series"))
a=0
s=0
c=0
k=n
b=1
if(n==0 or n==1 ):
    print("Found")
    exit()

while(n!=0):
    s=a+b
    if(s==k):
        print("Found")
        break
    n-=1
    a,b=b,s
else:
    print("Not found")

    
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)#1 2 3 4 5 6 7 8
	if   i % 3 == 0:
		continue
	else:
		print('Sec')#sec sec  sec  sec sec sec 
	print('Hello')#'Hello hello Hello hello Hello hello Hello hello
else:
	print('else  suite') #else suite
# End  of  the  loop
print('Outside  loop')#outside loop


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i) #1 2 3 4 5 6 7 
	if  i == 8:
		break
	else:
		print('Sec') # sec sec sec sec sec sec sec sec
	print('Hello')  #hello Hello hello Hello hello Hello hello
else:
	print('else  suite') #else  suite
# End  of  the  loop
print('Outside loop')#outside loop

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


array=eval(input("please enter array"))
a=int(input("please give input"))
for i in range(len(array)):
    if(a==array[i]):
        print("element found at index ",i)
        break
else:
    print("element not found")
    
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


array=eval(input("please enter array"))
a=int(input("please give input"))
c=0
for i in range(len(array)):
    if(a==array[i]):
        print("element found at index ",i)
        c+=1
if(c==0):
    print("element not found")

    
#  Walrus   operator (:=)  demo  program
print(a := 25) #25
print(a = 25)#error
print(a)#25
print(a := 6 + 7)#13
print(a)#13
print((a := 6) + 7)#6
print(a)#6
print((a = 6) + 7)#error


# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')#"Hyd"
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)# sec 0
if  c = 0:#error
	print('Hyd')
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
    total=0
    while(True):
        a=eval(input())
        total+=a
except:
    print(total)
    

#  del  operator  demo program  (Home  work)
a = 25
print(a)  #25
del   a 
print(a)#error

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) #25 25 25
del   a 
print(b , c) #25 25
print(a)  #error
del   b
print(c)#25
print(b)#error
del   c
print(c)#error

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) #25 10.8 Hyd
del   a , b , c
print(a) #erro
print(b) #error
print(c)#error

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #[10,20,15,18]
del  a[2]  
print(a) #[10,20,18]
del  a
print(a) #erro
print(a[0])#error
        
        
 
 
    


    

    
    


