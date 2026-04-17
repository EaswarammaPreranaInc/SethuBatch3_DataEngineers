# Write  a  program  to  print  upper  and  lower  case  alphabets

for i in range(65,91):
 print(chr(i), end='  ')
print()
for j in range(97,123):
 print(chr(j), end='  ')

# Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

x=int(input("How many terms ? : "))
f1=0
f2=1
f3=f1+f2
if x==0:
    print()
elif x==1:
    print(f1)
elif x==2:
    print(f1, end=' ')
    print(f2, end=' ')
else:
    print(f1, end=' ')
    print(f2, end=' ')
    for i in range(x-2):
        f3=f1+f3
        print(f3, end=' ')
        f1=f2
        f2=f3
print()

# Write  a  program  to  search  for  'x'  in  fibonacci  series

x=int(input("How many terms ? : "))
f1=0
f2=1
f3=f1+f2
if x==0:
    print("Found")
elif x==1:
    print("Found")
else:
    while f3<x:
        f3=f1+f2
        f1=f2
        f2=f3
    if f3==x:
        print("Found")
    else:
        print("Not found")
print()

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

# 1<nl>Sec<nl>Hello<nl>2<nl>Sec<nl>Hello<nl>3<nl>4<nl>Sec<nl>Hello<nl>5<nl>Sec<nl>Hello<nl>6<nl>7<nl>Sec<nl>Hello<nl>Outside

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

# 1<nl>Sec<nl>Hello<nl>2<nl>Sec<nl>Hello<nl>3<nl>Sec<nl>Hello<nl>4<nl>Sec<nl>Hello<nl>5<nl>Sec<nl>Hello<nl>6<nl>Sec<nl>Hello<nl>7<nl>Sec<nl>Hello<nl>else suite<nl>Outside loop
 
# Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

x=eval(input("Enter list : "))
s=eval(input("Enter search element :"))
for  i  in  range(len(x)):
	if  x[i]==s:
		print(f'Found at index : {i}')
		break;
	
else:
		print('Not found')

# x=eval(input("Enter list : "))
s=eval(input("Enter search element :"))
c=0
for  i  in  range(len(x)):
	if  x[i]==s:
		print(f'Found at index : {i}')
		c+=1
else:
    if c==0:
        print("not found")
    else:
        print(f'Element {s} found {c} times ')


#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) # Error
print(a) # 25
print(a := 6 + 7) # 13
print(a) 13
print((a := 6) + 7) # 13
print(a) 6
print((a = 6) + 7) # Error

# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')            # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')            
else:
	print('Sec : ' , b)     # Sec
if  c = 0:
	print('Hyd')            # Error 
else:
	print('Sec')          

# Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)



#  del  operator  demo program  (Home  work)
a = 25
print(a)  # 25
del   a   
print(a)  # Error

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) # 25 25
print(a)  # Error
del   b   
print(c)  # 25
print(b)  # Error
del   c
print(c)  # Error

#  Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [10 , 20 , 15 , 18]
del  a[2] 
print(a) # [10 , 20 , 18]
del  a
print(a) # Error
print(a[0]) # Error

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  # (10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2] 
del  a 
print(a)  # Error
print(a[0]) # Error

#  Can  multiple  objects  be  deleted  with  same  del  operator ?  # yes
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25  10.8  Hyd
del   a , b , c  
print(a) # Error
print(b) # Error
print(c) # Error