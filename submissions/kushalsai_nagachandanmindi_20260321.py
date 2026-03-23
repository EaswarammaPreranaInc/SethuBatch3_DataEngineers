'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
str = input("enter the string: ")
str = str.upper()
a = sorted(str)
vowl = ['A', 'E', 'I', 'O', 'U']
dic = {}
for x in a:
    if x.isalpha():
        if x in vowl:
            dic[x]=dic.get(x, 0)+1
print(dic)


# Find outputs  
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')
# Outputs:
'''Begin
Hyd
Sec 
Cyb
None
<class 'NoneType'>
End 
'''

# Find  outputs  
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
# outputs: 
	
'''
(10, 20 ,30)
<class 'tuple'>
10
20
30
for loop
10
20
30
'''

# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')
x = f1()  
print(x)
print('End')
# return   100
# Outputs:
# Begin
# 10
# End 
# error ''return' outside function'

#  Find  outputs
# f1()  
def   f1():
        print('Hello')
print(f1())  
print(f1)
# outputs:
# error 'as f1() has not defined'
# Hello
# None
# <function f1 at 0x00000182DBCDAAC0>

# Find  outputs 
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
'''
outputs:
Hello
Hi
f1 function
None
<function f1 at 0x00000182DBCDAAC0>
Bye '''

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')
'''
Begin
<class function>
232093295095
End
'''