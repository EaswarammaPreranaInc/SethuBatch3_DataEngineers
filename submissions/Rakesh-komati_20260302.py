#Write  a  program  to  print  upper  and  lower  case  alphabets

for i in range(65,91):
    print(chr(i),end=' ')
print("\n")
for i in range(97,123):
    print(chr(i),end=' ')



#Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

n=int(input('Number of terms: '))
a=0
b=1
count=0
if(n<=0):
    print('Invalid')
else:
    while(count<n):
        print(a)
        c=a+b
        a=b
        b=c
        count=count+1


#Write  a  program  to  search  for  'x'  in  fibonacci  series

x=int(input('Enter value to be searched: '))
a=0
b=1
while(a<=x):
    if a==x:
        print('Found')
        break
    c=a+b
    a=b
    b=c
else:
    print('Not Found')

output:
Enter value to be searched: 10
Not Found



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

output:
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

output:
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
8
else suite
Outside loop



Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

a=eval(input('Enter any list: '))
x=int(input('Enter the element to be searched: '))
for i in range(len(a)):
    if a[i]==x:
        print('Found')
        break
else:
    print('Not Found')

output:
Enter any list: [10,20,15,12,18]
Enter the element to be searched: 15
Found



Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

a=eval(input('Enter any list: '))
x=int(input('Enter the element to be searched: '))
count=0
for i in range(len(a)):
    if a[i]==x:
        print(f'{x} is found at index {i}')
        count=count+1
else:
    print(f'{x} is found {count} times')


output:
Enter any list: [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
Enter the element to be searched: 15
15 is found at index 2
15 is found at index 5
15 is found at index 8
15 is found 3 times




#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) #Nothing
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a)
print((a = 6) + 7) # Nothing


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
if  c = 0: # error
	print('Hyd')
else:
	print('Sec')

output:
Hyd
Sec: 0



Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

sum=0
count=0
try:
    while True:
        x=eval(input('Enter input (crtl+z to stop): '))
        sum=sum+x
        count=count+1
except EOFError:
    if count==0:
        print('No inputs')
    else:
        print(sum/count)


#  del  operator  demo program  (Home  work)
a = 25
print(a)  # 25
del   a 
print(a) # both object and reference are deleted


# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)  # 25 25 25
del   a  # reference a is deleted
print(b , c) # 25 25
print(a)  # error
del   b  #reference b is deleted
print(c) # 25
print(b) # error
del   c   # reference c is deleted
print(c) # error 



#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
print(a) # error reference a is deleted 
print(b) # error reference b is deleted 
print(c) # error reference c is deleted 



# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #  [10 , 20 , 15 , 18]
del  a[2]  
print(a) # [10 , 20 , 18]
del  a
print(a) # error
print(a[0]) # error



# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  # (10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2] 
del  a 
print(a) # error 
print(a[0]) # error