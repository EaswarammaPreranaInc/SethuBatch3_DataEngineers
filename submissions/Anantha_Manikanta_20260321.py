'''
1) Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)
Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
Hint:  Same  as  prog23a  with  minor  changes
'''
s = input("Enter String : ")
s = s.upper()
a = {}
for ch in sorted(s):
    if ch in "AEIOU":
        a[ch] = a.get(ch, 0) + 1
print(a)

'''
2) # Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x)
print('End')  # Begin <nextline> Hyd <nextline> Sec <nextline> Cyb <nextline> None <nextline> <class 'NoneType'> <nextline> End
'''

'''
3)  # Find  outputs  (Home  work)
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
	print(k)  # (10, 20, 30) <nextline> <class 'tuple'> <nextline> 10 <nextline> 20 <nextline> 30 <nextline> for loop <nextline> 10 <nextline> 20 <nextline> 30

'''

'''
4) # Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')
x = f1()  
print(x)
print('End')
return   100  # Begin <nextline> 10 <nextline> End <nextline> Error because return is outside function
'''

'''
5) #  Find  outputs
f1()  
def   f1():
        print('Hello')
print(f1())  
print(f1)  # Error because f1 is not defined the order is 1st we should create f1 and then we should call it
'''

'''
6) # Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')  # Hello <nextline> Hi <nextline>  <nextline> f1 function <nextline> None <nextline> <function f1 at 0xA1D3> <nextline> Bye
'''

'''
7) #  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')  # Begin  <nextline> <class 'function'> <nextline> 1000 <nextline> End  
'''