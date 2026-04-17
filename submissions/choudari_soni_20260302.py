'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''

for ch in range(ord('A'),ord('Z')+1):
 print(chr(ch),end=' ')
print()
for ch in range(ord('a'),ord('z')+1):
    print(chr(ch),end=' ')

#__________________________________________

'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''


n=int(input('Enter value to be searched ='))
a=0
b=1
c=a+b
for i in range(0,n+1):
    print(a)
    a=b
    b=c
    c=a+b


#_______________________________________________
'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''

n=int(input('Enter value to be searched ='))
a=0
b=1

for i in range(n+1):
    if(a==n):
        print("Found")
        break
    
    c=a+b
    a=b
    b=c  
else:
    print('Not found')

#__________________________________________________________
'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
'''

n=eval(input('Enter any list :'))
a=eval(input('Enter the element to be searched :'))
for i in range(len(n)):
    if(n[i]==a):
        print('Found')
        break
else:
    print('Not found')

#____________________________________________________________________________
'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)
'''

x=eval(input('Enter any list :'))
y=eval(input('Enter the element to be searched :'))
for i in range(len(x)):
    if(x[i]==y):
        print('Found at index =',i)

#________________________________________________________________

#  Walrus   operator (:=)  demo  program
print(a := 25)#25
print(a = 25)#nothing
print(a)	#error
print(a := 6 + 7)#13
print(a)	#13
print((a := 6) + 7)#13
print(a)	   #13
print((a = 6) + 7)#error

#________________________________________________

# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')	#nothing
else:
	print('Sec')#Sec
if  b := 0:
	print('Hyd')#Hyd
else:
	print('Sec : ' , b)
if  c = 0:	
	print('Hyd')	#nothing
else:
	print('Sec')#Sec

#________________________________________

#  del  operator  demo program  (Home  work)
a = 25
print(a)	 #25 
del   a		# del(25) 
print(a)	#error

#____________________________________

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)#(25,25,25)
del   a		#del(25)
print(b , c)#(25,25)
print(a)  
del   b		#del(25)
print(c)	#25
print(b)	#error
del   c		#del(25)
print(c)	#error

#____________________________________
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)#(25 , 10.8 , 'Hyd')
del   a , b , c #del(25,10.8.Hyd)
print(a) #error 
print(b) #error
print(c) #error

#______________________________________________

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del  a[2] # del(15)
print(a) # [10 , 20 ,18]
del  a	#del(10,20,18)
print(a) #nothing
print(a[0])#nothing

#_____________________________________________



# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)# (10 , 20 , 15 , 18) 
print(a[0])# (10)
del  a[2] #del(15)
del  a #del(10,20,15,18)
print(a) # nothing 
print(a[0])#nothing

#_________________________________________________

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)		#1 <\n>Sec<\n>Hello
	if   i % 3 == 0:	#2 <\n>Sec<\n>Hello
		continue	#3
	else:			#4<\n>Sec<\n>Hello
		print('Sec')	#5<\n>Sec<\n>Hello
	print('Hello')		#6
else:				#7<\n>Sec<\n>Hello
	print('else  suite')	#else  suite
# End  of  the  loop		#Outside  loop
print('Outside  loop')

#_________________________________________________

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)	    #1 <\n>Sec<\n>Hello
	if  i == 8:	   #2 <\n>Sec<\n>Hello
		break	   #3
	else:		  #Outside loop
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')




												 
