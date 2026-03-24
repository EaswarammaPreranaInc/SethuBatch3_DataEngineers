Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
a=input('Enter string: ')
a=sorted(a.upper())
b={}
for x in a[1:]:
    if x in 'AEIOU':
        b[x]=b.get(x,0)+1
print(b)

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

'''
(10,20,30)
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
return   100  #error

'''
10
End
'''

#  Find  outputs
f1()  #error
def   f1():
        print('Hello')
print(f1())  #Hello
             #None
print(f1)  #address

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
Hello
Hi
f1 function
None
address
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
Begin
<class 'function'>
address
End
'''
