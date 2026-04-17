'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
s = input("Enter a string: ")

s = s.upper()

lst = sorted(s)

a = {}
vowels = ['A','E','I','O','U']


for ch in lst:
    if ch.isalpha() and ch in vowels : 
          
           a[ch] = a.get(ch, 0) + 1


print(a)

# Find outputs  (Home  work)
# def   f1():
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# # End  of  the  function
# print('Begin') 
# x = f1()
# print(x)
# print(type(x))
# print('End')
'''
Answers of above program
1) line number 34 "Begin" will be printed
2) line number 30 "Hyd"   will be printed
3) line  number 31 "Sec" will be printed
4) line  number 32 "Cyb" will be printed
5) line number 35 will be printed i.e "None"
6) line  number 37  will be printed , i.e <class NoneType>
7) line  number 38 "End" will be printed
'''

# Find  outputs  (Home  work)
# def  f1():
# 	return   10 , 20 , 30
# # End  of  the  function
# x = f1() 
# print(x)#(10,20,30)
# print(type(x))#<class 'tupple'>
# a , b , c =  f1()   
# print(a)#10
# print(b)#20
# print(c)#30
# print('for  loop')#for loop
# for  k   in   f1():
# 	print(k) #10 <next line> 20 <next line> 30

# Find  outputs
# def    f1():
# 	return  10
# 	return  20#ignored
# 	return  30#ignored because only one return statement will be returned
# End  of  the  function
# print('Begin')# Begin
# x = f1()  
# print(x)#10
# print('End')#End
# return   100#Error

#  Find  outputs
# f1() #Error because def key word is missing  
# def   f1():
#         print('Hello')#Hello

# print(f1()) #Hello <next line> None

# print(f1)# type of class and Address  will be printed

# Find  outputs  (Home  work)
# print('Hello')#Hello
# def  f1():
#         print('f1  function')
# # End  of   function
# print('Hi')#Hi
# print(f1())#f1 function <next line> None
# print(f1)#type of class and Address  will be printed
# print('Bye')#Bye

#  Find  outputs
# def    f1():
#         print('Hyd')
#         print('Sec')
#         print('Cyb')
# #End  of  the  function
# print('Begin')#Begin
# print(type(f1))#<class function>
# print(id(f1))# address of f1 will be printed
# print('End')#End