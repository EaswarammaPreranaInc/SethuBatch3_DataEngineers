'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
print('upper case:')
for i in range(65,91):
    print(chr(i),end=' ')
print()

print('lower case')
for i in range(97,123):
    print(chr(i), end=' ')
print()
#========================================================================================================================================================
'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
n=int(input('enter a number:'))
a=0
b=1
for i in range(n):
      print(a,end=' ')
      c=a+b
      a=b
      b=c
print()
#========================================================================================================================================================
'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
x=int(input('enter the number:'))
a=0
b=1
while a<x:
    c=a+b
    a=b
    b=c
if a==x:
    print('found')
else:
    print('not found')
print()
#========================================================================================================================================================
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)            #1      #2     #3     #4       #5       #6     #7
	if   i % 3 == 0:
		continue
	else:
		print('Sec')#Sec    #Sec          #Sec     #Sec           #Sec
	print('Hello')      #Hello  #Hello       #Hello    #Hello         #Hello
else:
	print('else  suite')                                                #else suite
# End  of  the  loop
print('Outside  loop')                                                       #Outside loop
#print()
#========================================================================================================================================================
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)             #1     #2     #3        #4       #5       6       7
	if  i == 8:
		break
	else:
		print('Sec') #Sec    #Sec  #Sec     #Sec     Sec       Sec      Sec
	print('Hello')       #Hello  #Hello #Hello  #Hello    Hello    Hello    Hello
else:
	print('else  suite')                                                   #else suite
# End  of  the  loop
print('Outside loop')                                                          #Outside loop
print()
#========================================================================================================================================================
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
list=[10 , 20 , 15 , 12 , 18]
x=int(input('enter the number:'))
for i in range(len(list)):
    if list[i]==x:
        print('found at',i)
        break
    
else:
    print('not found')
print()
#========================================================================================================================================================
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
list=[10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
x=int(input('enter the search number:'))
count=0
for i in range(len(list)):
    if list[i]==x:
       print('found at',i)
       count+=1
if count==0:
   print('not found')
else:
   print( x,'is found',count,'times')
print()
#========================================================================================================================================================
#  Walrus   operator (:=)  demo  program
print(a := 25) #25
#print(a = 25)#error
print(a) #25
print(a := 6 + 7)#13
print(a)#13
print((a := 6) + 7) #13
print(a)#6
#print((a = 6) + 7)#error
#========================================================================================================================================================
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') #Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b) #Sec:0
#if  c = 0:
	print('Hyd') #Hyd
#else:
	print('Sec')#Sec
#========================================================================================================================================================
#  del  operator  demo program  (Home  work)
a = 25
print(a)  #25
del   a # a is deleted
#print(a)  #error-because del a is deleted  
#========================================================================================================================================================
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)#25 25 25
del   a
print(b , c) #25 25
#print(a) #error -deleted 
del   b
print(c)#25
#print(b)#error
del   c
#print(c)  #error
#========================================================================================================================================================
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) #25 10.8 Hyd
del   a , b , c
#print(a) #error
#print(b) #error
#print(c)#error
#========================================================================================================================================================
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #[10, 20, 15, 18]
del  a[2]  
print(a) #[10, 20, 18]
del  a
print(a) #error
print(a[0])#error
#========================================================================================================================================================
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #(10, 20, 15, 18)
print(a[0]) #10
#del  a[2] 
del  a 
#print(a)  #error
#print(a[0])



     
