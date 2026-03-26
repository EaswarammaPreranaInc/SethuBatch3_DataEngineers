(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes

s = input("Enter string: ")
s = s.upper()
vowels = ['A', 'E', 'I', 'O', 'U']
a = {}
for x in vowels:
    count = s.count(x)
    if count > 0:
        a[x] = count
print(a)


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

Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End

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

Begin
10
End


#  Find  outputs
f1()  
def   f1():
        print('Hello')
print(f1())  
print(f1)
#error

print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

Hello
Hi
f1  function
None
<function f1 at address
Bye

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

Begin
<class 'function'>
address of function 
End

