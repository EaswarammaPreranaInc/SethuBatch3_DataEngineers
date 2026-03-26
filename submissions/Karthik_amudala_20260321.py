Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

CODE:

a = input("Enter a string: ")
b = a.upper()
c = {}
for i in b:
    if i in 'AEIOU':
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
print(c)


Output:

Enter a string: RamA raO
{'A': 3, 'O': 1}

# Find outputs  (Home  work)

def   f1():
     print('Hyd')
     print('Sec')
     print('Cyb')

print('Begin')
x = f1()
print(x)
print(type(x))
print('End')

Output:

Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End

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
      
Output:

(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30

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

Output:

Begin
10
End
SyntaxError: 'return' outside function

#  Find  outputs
f1()  
def   f1():
        print('Hello')
print(f1())  
print(f1)

Output:

Hello
None
function f1 


# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

Output:

Hello
Hi
f1  function
None
function f1 
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

Output:

Begin
<class 'function'>
Address of f1
End