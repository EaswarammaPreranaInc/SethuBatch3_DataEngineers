Name-Dhruva Gupta
Roll Number-D238

1)
s = "RamA    raO"
s = s.upper()
vowels = "AEIOU"
d = {}
for ch in s:
    if ch in vowels:
        d[ch] = d.get(ch, 0) + 1
d = dict(sorted(d.items()))
print(d)

2)
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
print(‘End')

#Output-
Begin
Hyd
Sec
Cyb
None 
Class None
End

3)
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

#Output-
(10,20,30)
Class tuple
10
20
30
For loop 
10 
20
30

3)
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
return   100 #Error as return is inside Function only

#Output-
Begin
30
End

4)
#  Find  outputs
f1()   #Error
def   f1():
        print('Hello')
print(f1())  
print(f1)

#Outputs-
Hello
None
Function f1 at address

5)
# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print(‘Bye')

#Output-
Hello
Hi
f1 Function
None
Function f1 at address
Bye

6)
#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print(‘End')

#Output-
Begin
Class function
Address of function
End