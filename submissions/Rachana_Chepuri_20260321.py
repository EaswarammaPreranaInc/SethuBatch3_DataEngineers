'''Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
n=input('Enter mixed case String:')
n=n.upper()
b=sorted(n)
vowel='AEIOU'
a={}
for ch in b:
  if ch in vowel and ch not in a: 
    a[ch]=  a . get(ch , 0) + 1 
print(a)

'''Find outputs  (Home  work)'''
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
#End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')
'''output'''
# Begin
# Hyd
# Sec
# Cyb
# None
# <class 'NoneType'>
# End
'''Find  outputs  (Home  work)'''
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x)
print(type(x))
a , b , c =  f1()   
print(a)
print(b)
print(c)
print('for  loop')
for  k   in   f1():
	print(k)
	
'''output'''    
# (10,20,30)
# None
# <class 'NoneType'>
# 10
# 20
# 30
# for loop
# 10
# 20
# 30
'''Find  outputs'''
# def    f1():
# 	return  10
# 	return  20
# 	return  30
# # End  of  the  function
# print('Begin')# Begin
# x = f1()  
# print(x)# 10
# print('End')# End
# return   100#Error

''' Find  outputs'''
f1()  #Error--function should call after function is define
def   f1():
        print('Hello')#Hello
print(f1())  #None
print(f1)# type and address
'''Find  outputs  (Home  work)'''
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
'''output'''
# Hello
# Hi
# f1 function
# address anf Type
# Bye
'''Find  outputs'''
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')#Begin
print(type(f1))#<class 'function'>
print(id(f1))#address of f1
print('End')#End
