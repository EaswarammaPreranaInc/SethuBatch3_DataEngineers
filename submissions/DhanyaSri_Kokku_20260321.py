'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
# Code :
n = input('Enter String : ')
a = sorted(n.upper())
s = 'AEIOU'
d = {}
for x in a:
    if x.isalpha() and x in s:
        d[x] = d.get(x,0)+1
print(d)

'''
Output:
Enter String : RamA raO
{'A': 3, 'O': 1}

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

'''Output:
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End
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

''' Output:
(10 , 20 , 30)
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
return   100 # Error because return statement can only be written in function

''' Output:
Begin
10
End
'''

#  Find  outputs
f1()   # Error because function cannot be called before function declaration
def   f1():
        print('Hello')
print(f1()) # Hello <nextline> None
print(f1) # <class 'function'> and address of the function f1 in hexa decimal


# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

'''Output:
Hello
Hi
f1 function
None
<class 'function'> and address of the function f1 in hexa decimal
Bye
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
Output:
Begin
<class 'function'>
Address of function f1 in decimal
End

'''
