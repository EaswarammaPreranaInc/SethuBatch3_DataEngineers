# Write  a  program  to  print  upper  and  lower  case  alphabets

for ch in range(65,91):
    print(chr(ch),end=" ")
print()
for ch in range(97,123):
    print(chr(ch),end=" ")
print()
    
# Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

n = int(input("Enter n :"))
a = 0
b = 1
print("First",n,"trems :",a,b,end=" ")
cnt = 2
while cnt<n:
    c = a+b
    print(c,end=" ")
    a=b
    b=c
    cnt +=1 
print()

# Write  a  program  to  search  for  'x'  in  fibonacci  series

n = int(input("Enter value to be searched :"))
a=0
b=1
while a<=n:
    if a==n:
        print("Found")
        break
    c=a+b
    a=b
    b=c
else:
    print("not found")

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
Seec
Hello
2
Sec
Hello
3
Hello
4 
sec
Hello
5 
Sec
Hello
6
Hello
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
till 7 
outside loop
'''

#Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

list = eval(input("Enter any list :"))
ele = eval(input("Enter the Element to be searched :"))
for i in range(len(list)):
	if list[i]==ele:
		print("Found at index ",i)
		break
else:
	print("Not Found")

#Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element and  also  number  of  times  it  is  found
	
list = eval(input("Enter any list :"))
ele = eval(input("Enter the Element to be searched :"))
for i in range(len(list)):
	if list[i]==ele:
		print("Found at index ",i)
		continue
else:
	print("Not Found")
	