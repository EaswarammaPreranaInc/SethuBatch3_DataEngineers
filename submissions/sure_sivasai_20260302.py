#1. Write  a  program  to  print  upper  and  lower  case  alphabets

'''
Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''


for i in range(65,91):
    print(chr(i),end=' ')
print()
for i in range(97,123):
    print(chr(i),end=' ')
print()
print()

#---------------------------------------------------------------------------
    
#2. Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

'''
Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''


n = int(input('Enter number : '))
a = 0
b = 1
i = 1
while i<=n:
    print(a)
    a,b = b,a+b
    i += 1    
print()
#---------------------------------------------------------------------------

#3. Write  a  program  to  search  for  'x'  in  fibonacci  series

'''
1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''

n = int(input('Enter number : '))
a = 0
b = 1
while a<=n:
    if a==n:
        print('Found')
        break
    a,b = b,a+b
else:
    print('Not Found')
print()
print()
    
#--------------------------------------------------------------------------

#4. Find  outputs  (Home  work)
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
print()

'''
Output

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
'''


#-----------------------------------------------------------------------

#5. Find  outputs  (Home  work)
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
print()
print()
print()


'''
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
else suite
Outside loop

'''

#-------------------------------------------------------------------------

#6. Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
#print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)
'''
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

a = [int(i) for i in input('Enter list : ').split()]
search = int(input('Enter a number to search : '))
l = len(a)
i=0
while i<l:
    if a[i]==search:
        print(f'Found at index {i}')
        break
    i += 1
else:
    print('Not Found')
print()

#--------------------------------------------------------------------------

#7. Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
#and  also  number  of  times  it  is  found

'''
List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
												   15 is  found  at  index  												   15 is  found  at  index  8												   15 is  found   3  times
'''

a = [int(i) for i in input('Enter list : ').split()]
search = int(input('Enter a number to search : '))
l = len(a)
i=0
count = 0
while i<l:
    if a[i]==search:
        print(f'Found at index {i}')
        count += 1
    i += 1
else:
    if count>0:
        print(f'{search} is found {count} times')
    else:
        print('Not Found')
print()

#-------------------------------------------------------------------------

#8. Walrus   operator (:=)  demo  program
print(a := 25)      # 25
print(a = 25)       # Error
print(a)            # 25
print(a := 6 + 7)   # 13
print(a)            # 13
print((a := 6) + 7) # 13
print(a)            # 6
print((a = 6) + 7)  # Error

#--------------------------------------------------------------------------

#9. Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')    # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')    
else:
	print('Sec : ' , b)  # Sec : 0
if  c = 0:
	print('Hyd')    # Error
else:
	print('Sec')    # Error

#-----------------------------------------------------------------------

#10. Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
# (without  walrus  operator)
'''
(Home  work)
Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''


try:
    count = 0
    summ = 0
    while True:
        n = int(input('Enter input : '))
        summ += n
        count += 1
except:
    print(summ/count)

#----------------------------------------------------------------------------------------------------------

#11. del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a 
print(a) # Error

#---------------------------------------------------------------------------------------------------------

#12. Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c)     # 25 25
print(a)         # Error
del   b   
print(c)         # 25
print(b)         # Error
del   c
print(c)         # Error

#------------------------------------------------------------------------------------------------------------

#13. Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)  # 25 10.8 Hyd
del   a , b , c
print(a)          # Error
print(b)          # Error
print(c)          # Error

#-------------------------------------------------------------------------------------------------------------

#14. Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)   # [10 , 20 , 15 , 18]
del  a[2]  
print(a)   # [10,20,18]
del  a
print(a)   # Error
print(a[0])# Error

#--------------------------------------------------------------------------------------------------------------

#15. Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)   # (10 , 20 , 15 , 18)
print(a[0])# 10
del  a[2]  # Error
del  a 
print(a)   # Error
print(a[0])# Error

#---------------------------------------------








