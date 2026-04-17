a = 65
while a <= 90:
    print(chr(a), end=' ')
    a=a+1
print()    
a = 97
while a <= 122:
    print(chr(a), end=' ')
    a=a+1

-------------------------------------
n=int(input('Enter value for no.of terms: '))
a=0
b=1
c=a+b
d=[0,1]
while len(d)<=(n-1):
    c=a+b
    a=b
    b=c
    d.append(c)
print(*d)
-------------------------------------
n=int(input('Enter value to be searched: '))
a=0
b=1
c=a+b
d=[]
while c<=n:
    c=a+b
    a=b
    b=c
    d.append(c)
if n in d:
    print('Found')
else:
    print('Not Found')  

# 1
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
else  suite
Outside  loop
-------------------------------------
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

-------------------------------------
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
else  suite
Outside loop
---------------------------------

a=eval(input('Enter the list: '))
n=int(input('Enter the element to be searched: '))
i=0
while i<len(a):
    if a[i]==n:
        print(f'Found at index {i}')
        break
    i=i+1
else:
    print('Not Found')

--------------------------------------
#  Walrus   operator (:=)  demo  program
print(a := 25)  # 25
print(a = 25) #error
print(a) # error
print(a := 6 + 7) # 13
print(a) #13
print((a := 6) + 7)  #13
print(a)  #6
print((a = 6) + 7) #error
--------------------------------
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')  # Hyd
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)  # Sec : 0
if  c = 0:
	print('Hyd')
else:
	print('Sec')  # Error
---------------------------------

#  del  operator  demo program  (Home  work)
a = 25
print(a)  # 25
del   a 
print(a)  # error

----------------------------------

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)  # 25 25 25
del   a
print(b , c)  # 25 25
print(a)  #error
del   b
print(c) # 25
print(b) #error
del   c
print(c) #error

------------------------------------

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)  #25 10.8 Hyd
del   a , b , c
print(a) #error
print(b) #error
print(c)  #error
------------------------------------
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [10 , 20 , 15 , 18]
del  a[2]  
print(a) #  [10 , 20 , 18]
del  a
print(a) #error
print(a[0])  #error

------------------------------------

a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18) 
print(a[0]) #10
del  a[2] 
del  a 
print(a)  #error
print(a[0])  #error

