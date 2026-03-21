'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)
Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Sample output:
Enter String:RamA raO
{'A': 3, 'O': 1}
Press any key to continue . . .
'''
a = input('Enter  mixed  case  string : ')  
b = a . upper()  
vowels ='AEIOU'  
d = { } 
for  ch  in   b:
	if  ch in vowels:  
		d[ch] = d . get(ch , 0) + 1  
print(d)


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
Output:
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
'''

# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin') # Begin
x = f1()  # x=10
print(x)  # 10
print('End') # End
return   100 # ERROR only single return statement should be in any program

#  Find  outputs
f1()  # ERROR because function is not defined before calling a function
def   f1():
        print('Hello')
print(f1())  
print(f1)

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
Output:
Hi
f1  function
None
<function f1 at address>
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
address in decimal
End
'''