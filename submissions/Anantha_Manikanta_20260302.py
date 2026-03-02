'''
1) Write  a  program  to  print  upper  and  lower  case  alphabets
'''
i = 65
while i <= 90:
    print(chr(i), end=' ')
    i += 1
print()   # move to next line
i = 97
while i <= 122:
    print(chr(i), end=' ')
    i += 1
'''
2) Write  a  program  to  print  first  'n'  terms  of  fibonacci  series
'''
n = int(input('Enter number of terms : '))
a = 0
b = 1
count = 1
while count <= n:
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    count += 1
'''
3) Write  a  program  to  search  for  'x'  in  fibonacci  series
1) Let  input  be   10
    What  is  the  output ? --->	Not  found
'''
x = int(input('Enter value to be searched : '))
a = 0
b = 1
if x == 0:
    print('Found')
else:
    while b <= x:
        if b == x:
            print('Found')
            break
        c = a + b
        a = b
        b = c
    else:
        print('Not Found')
'''
4) Find  outputs  (Home  work)
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
print('Outside  loop') 1 <nextline> Sec <nextline> Hello <nextline> 2 <nextline> Sec <nextline> Hello <nextline >3 <nextline> 4 <nextline> Sec <nextline> Hello <nextline> 5 <nextline> Sec <nextline> Hello <nextline >6 <nextline> 7 <nextline> Sec <nextline> Hello <nextline> else suite <nextline> Outside loop
'''
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
print('Outside loop')  1 <nextline> Sec <nextline> Hello <nextline> 2 <nextline> Sec <nextline> Hello <nextline >3 <nextline> Sec <nextline Hello> <nextline> 4 <nextline> Sec <nextline> Hello <nextline> 5 <nextline> Sec <nextline> Hello <nextline >6 <nextline> Sec <nextline> Hello <nextline> 7 <nextline> Sec <nextline> Hello <nextline> else suite <nextline> Outside loop
'''
'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  ---> Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found
'''
lst = eval(input('Enter any list: '))
x = eval(input('Enter the element to be searched : '))
for i in range(len(lst)):
    if lst[i] == x:
        print('Found at index :', i)
        break
else:
    print('Not Found')
'''
  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) # Error
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # Error
print(a)  # 13
print((a = 6) + 7) # Error
'''
'''
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)  # Sec : 0
if  c = 0:
	print('Hyd')  # Error because = cannot be used in if condition
else:
	print('Sec')
'''
'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)
Let  inputs  be  25 , 10.8 , True ,  ctrl + z
sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1
'''
total = 0
count = 0
try:
    while True:
        x = eval(input('Enter value : '))
        total += x
        count += 1
except EOFError:
    pass
if count != 0:
    print('Average : ', total / count)
else:
    print('No inputs given')
'''
 del  operator  demo program  (Home  work)
a = 25
print(a) # 25  
del   a 
print(a) # Error because a is not defined and the previously created  a was deleted
'''
 Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 , 10.8 , 'Hyd'
del   a , b , c
print(a) # Error because a is not defined and the previously created  a was deleted
print(b) # Error because b is not defined and the previously created  b was deleted
print(c) # Error because c is not defined and the previously created  c was deleted
'''
'''
 Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [10 , 20 , 15 , 18]
del  a[2]  
print(a) # [10 , 20 , 18]
del  a
print(a) # Error because a is not defined and the previously created  a was deleted
print(a[0]) # Error because a is not defined
'''
'''
Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #  (10 , 20 , 15 , 18)
print(a[0])  # 10
del  a[2] # Error because tuples are immutable
del  a 
print(a)  # Error because a is not defined and the previously created  a was deleted
print(a[0])  # Error because a is not defined
'''