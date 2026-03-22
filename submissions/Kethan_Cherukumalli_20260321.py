# Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

# Let  input  be  RamA    raO
# What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}


a=input('Input :')
a=a.upper()
a=list(a)
b='AEIOU'
c=[]
for x in a:
    if x in b:
        c.append(x)
d=list(sorted(set(c)))

e=[]
for x in d:
   y= a.count(x)
   e.append(x)
   e.append(y)

result = {e[i]: e[i + 1] for i in range(0, len(e), 2)}
print(result)


---------------------------------------------------------------

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

#Begin
Hyd
Sec
Cyb
None
<class'function'>
End
---------------------------------------------------------------
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
10,20,30
<class'tuple'>
10
20
30
for loop
10
20
30
'''

---------------------------------------------------------------

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
return   100 # error

'''

Begin
10
End

'''

---------------------------------------------------------------

#  Find  outputs
f1()  # Error
def   f1():
        print('Hello')
print(f1())  
print(f1)

---------------------------------------------------------------

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
f1  function
None
class function, address
Bye

'''
---------------------------------------------------------------

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
Address
End

'''
