'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
'''
a = input('Enter mixed case string : ')
a = a.upper()
b = sorted(a)
c = {}
v = 'AEIOU'

for ch in b :
    if ch in v:
        d = c.get(ch, 0)+1
        c[ch] = d
print(c)
'''

'''
# Find outputs  (Home  work)
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
'''
'''
Begin
Hyd 
Sec 
Cyb 
<class 'NoneType'>
End 
'''

'''
# Find  outputs  (Home  work)
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
'''
'''
(10, 20, 30)
<class 'tuple'>
10
20
30 
for loop
10
20
30
'''

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
return   100
'''
'''
Begin
10
End
Error
'''

'''
#  Find  outputs
#f1()  # Error 
def   f1():
        print('Hello') # Hello 
print(f1())  # None 
print(f1) # Address of the function 
'''

'''
# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
'''
'''
Hello
Hi
f1 function
None 
Address of the function
Bye
'''

'''
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
'''
Begin
<class 'Function'>
Address of the function
End
'''