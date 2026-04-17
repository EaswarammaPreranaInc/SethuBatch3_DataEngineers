
'''Write  a  program  to  print  upper  and  lower  case  alphabets

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
    print(chr(i), end=' ')
          
'''
output:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
a b c d e f g h i j k l m n o p q r s t u v w x y z 

'''




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

#  Walrus   operator (:=)  demo  program
print(a := 25)# 25
print(a = 25)# error
print(a)# 25
print(a := 6 + 7)#13
print(a)# 13
print((a := 6) + 7)# 13
print(a)# 13
print((a = 6) + 7)#error

# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')# Hyd
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)# Sec :  0
if  c = 0:
	print('Hyd')#error 
else:
	print('Sec')

'''Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d ''' 

#  del  operator  demo program  (Home  work)
a = 25
print(a) #25 
del   a 
print(a) # error because object 25 is deleted

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)# 25 25 25
del   a 
print(b , c)# 25 25
print(a)  #error
del   b
print(c)# 25
print(b)# error
del   c
print(c)# error

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)   # 25 10.8 Hyd         
del   a , b , c
print(a) # error
print(b) # error
print(c) # error


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #[10 , 20 , 15 , 18]
del  a[2]  
print(a) #[10, 20, 18]
del  a
print(a) #error because it deleted
print(a[0])# error a is deleted 

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) # (10, 20, 15, 18)
print(a[0]) # 10
del  a[2] # error because it does not allow del
del  a 
print(a)  # error because a is deleted 
print(a[0])# error because a is deleted