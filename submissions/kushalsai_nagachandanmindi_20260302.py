# Write  a  program  to  print  upper  and  lower  case  alphabets
for a in range(65,91):
    print(chr(a), end=' ')
print()
for b in range(97,123):
    print(chr(b), end=' ')

# Write  a  program  to  print  first  'n'  terms  of  fibonacci  series
n = int(input("Enter number of elements : "))
a, b = 0, 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

# Write  a  program  to  search  for  'x'  in  fibonacci  series
x = int(input("Enter a number : "))
a, b = 0, 1
if x == 0 or x == 1:
    print("Found")
else:
    while b < x:
        c = a + b
        a = b
        b = c
    if b == x:
        print("Found")
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
print('Outside  loop') # 1 <nextline> Sec <nextline> Hello <nextline> 2 <nextline> Sec <nextline> Hello <nextline> 3 <nextline> 4 <nextline> Sec <nextline> Hello <nextline> 
                       # 5 <nextline> Sec <nextline> Hello <nextline> 6 <nextline> 7 <nextline> Sec <nextline> Hello <nextline> else  suite <nextline> Outside  loop

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
print('Outside loop') # 1 <nextline> Sec <nextline> Hello <nextline> 2 <nextline> Sec <nextline> Hello <nextline> 3 <nextline> Sec <nextline> Hello <nextline> 4 <nextline> Sec <nextline> Hello <nextline> 
                      # 5 <nextline> Sec <nextline> Hello <nextline> 6 <nextline> Sec <nextline> Hello <nextline> 7 <nextline> Sec <nextline> Hello <nextline> else  suite <nextline> Outside loop

#Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and print  Found  or  Not  Found  message
lst = [10, 20, 15, 12, 18]
x = int(input("Enter the element to be searched: "))
for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index :", i)
        break
else:
    print("Not found")

#Write a program to search for an element in the list and print index of each occurrence and total count
lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
x = int(input("Enter element to search: "))
count = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(x, "is found at index", i)
        count += 1
print(x, "is found", count, "times")

#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) # Error
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 25
print((a = 6) + 7) # Error

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
	print('Sec') # Hyd <NextLine> Sec :  0 <NextLine> SyntaxError: invalid syntax (at "if  c = 0:")

# Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
total = 0
count = 0
try:
    while True:
        x = input("Enter value: ")
        value = eval(x)     # converts 25, 10.8, True properly
        total = total + value
        count = count + 1
except EOFError:
    pass
if count > 0:
    print("Average =", total / count)
else:
    print("No inputs given")

#  del  operator  demo program  (Home  work)
a = 25
print(a)  # 25
del   a 
print(a) # Error

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) # 25 25
print(a)  # Error
del   b
print(c) # 25
print(b) # Error
del   c
print(c) # Error

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
print(a) # Error
print(b) # Error
print(c) # Error

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [10, 20, 15, 18]
del  a[2]  
print(a)  # [10, 20, 18]
del  a
print(a)  # Error
print(a[0])

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  # (10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2] 
del  a 
print(a)  # Error
print(a[0]) # Error