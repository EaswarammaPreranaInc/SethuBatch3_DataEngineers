'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
# print("Captial Letters")
# for x in range(65,90):
#   print(chr(x),end='  ')
  
#   print("small letters :") 
# for y in range(97,122):
#      print(chr(y),end='  ') 

'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''

 
# n=int(input("Enter the elements :"))
# a=0
# b=1
# x=[0,1]

# while a<=n :
#     x.append(a)
#     c=a+b
#     a=b
#     b=c
# print(f"Found {n}") if n in x else print(f"{n} Not found")
    
#Find  outputs  (Home  work)
# for  i  in  range(1 , 8):
# 	print(i)
# 	if   i % 3 == 0:
# 		continue
# 	else:            
# 		print('Sec')
# 	print('Hello')
# else:
# 	print('else  suite')
# # End  of  the  loop
# print('Outside  loop')    
# #1
# #sec
#hello
#2
#sec
#hello
#3
#4
#sec
#hello
#5
#sec
#hello
#6
#7
#sec
#hello

# Find  outputs  (Home  work)
# for  i  in  range(1 , 8):
# 	print(i)
# 	if  i == 8:
# 		break
# 	else:
# 		print('Sec')
# 	print('Hello')
# else:
# 	print('else  suite')
# # End  of  the  loop
# print('Outside loop') 
# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# 4
# Sec
# Hello
# 5
# Sec
# Hello
# 6
# 7
# Sec
# Hello
# else  suite
# Outside  loop
# PS C:\Users\user\Desktop\SSSSDPstudents> & C:/Users/user/AppData/Local/Programs/Python/Python314/python.exe c:/Users/user/Desktop/SSSSDPstudents/Mukesh_20260301.py
# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# 4
# Sec
# Hello
# 5
# Sec
# Hello
# 6
# 7
# Sec
# Hello
# else  suite
# Outside  loop
# a=25
# print(a)

#print(a:=25)    
#  Walrus   operator (:=)  demo  program
#print(a = 25)#error
# print(a = 25) #error
# print(a)
# print(a := 6 + 7)#13
# print(a)
# print((a := 6) + 7)#32
# print(a)
# print((a = 6) + 7)#error : missing

# Find  outputs  (Home  work)
# a = 0
# if  a == 0:
# 	print('Hyd')
# else:
# 	print('Sec')
# if  b := 0:
# 	print('Hyd')
# else:
# 	print('Sec : ' , b)
# if  c = 0:   # error 
# 	print('Hyd')
# else:
# 	print('Sec')
        
#  #  del  operator  demo program  (Home  work)
# a = 25
# print(a)  # 25
# del   a   # delete
# print(a) a #not defined error 
#  # Find  outputs  (Home  work)
# a = b = c = 25
# print(a , b , c) # 25 25 25
# del   a
# print(b , c)#25 25
# print(a)  #error
# del   b #delete
# print(c)#25
# print(b)#not defined
# del   c #deleted
# print(c)#not defined
#  #  Can  multiple  objects  be  deleted  with  same  del  operator ?
# a , b , c = 25 , 10.8 , 'Hyd'
# print(a , b , c) #25 , 10.8 , 'Hyd'
# del   a , b , c 
# print(a) #error
# print(b) #error
# print(c)#error
#  # Find outputs  (Home  work)
# a = [10 , 20 , 15 , 18]
# print(a)  #10 , 20 , 15 , 18
# del  a[2]  #15 delete
# print(a)  #10 20 18
# del  a 
# print(a)  #error
# print(a[0])#error
#  # Find outputs  (Home work)
# a = (10 , 20 , 15 , 18)
# print(a)  #10 , 20 , 15 , 18
# print(a[0])  #10
# del  a[2]  #15
# del  a  
# print(a)  #error
# print(a[0])  #error     


'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''

while True:
 
 n=eval(input("Enter the elemnts :"))
 

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