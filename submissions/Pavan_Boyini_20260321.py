'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

output:

a = input()
b=sorted(a.upper())
c = {}
d = 'AEIOU'
for ch in b:
    if  ch in d:
        c[ch] = c.get(ch,0)+1
print(c)


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

output:
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

output:
(10,20,30)
<class 'Tuple'>
10
20
30
for loop
10
20
30

 # Find  outputs
def    f1():
	return  10
	return  20
	return  30
output:
Without calling function it will give nothing.

# End  of  the  function
print('Begin')
x = f1()  
print(x)
print('End')
return   100   # return shouldn't be outside of function

output:

Begin
10
End



 
#  Find  outputs
f1()  
def   f1():
        print('Hello')
print(f1())  
print(f1)

output:Error because without defining function it not possible call a function

       # OR

def   f1():
        print('Hello')
print(f1())  
print(f1)

output:
Hello
None
function at some address


 # Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print("Bye")


output:

Hello
Hi
f1 function
None
function f1 at some address
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

output:

Begin
class function
address of function
End