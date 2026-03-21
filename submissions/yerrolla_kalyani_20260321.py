'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)
Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
Hint:  Same  as  prog23a  with  minor  changes
'''
string=input("Enter the string:")
a=string.upper()
b='AEIOU'
c={}
for x in a :
	if x in b:
	    c[x]=c.get(x,0)+1
print(c)
	

 # Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)#None 
print(type(x))
print('End')
#outputs
# Begin
# Hyd
# Sec
# Cyb
#None
# <class 'Nonetype'>
# End 
# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#(10 , 20 , 30)
print(type(x))#<class 'tuple'>
a , b , c =  f1()   
print(a)#10
print(b)#20
print(c)#30
print('for  loop')#for  loop
for  k   in   f1():
	print(k)#10<nextline>20<nextline>30
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
#Begin
#10
#End
#100
#  Find  outputs

f1()  #error we cannot call function without defining the function
def   f1():
        print('Hello')
print(f1())  #Hello <nextline>None
print(f1)#<class type and address><function f1 at hexa-decimal address>


# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
#outputs
#Hello
#Hi
#'f1  function'
#None
#<class type and address><function f1 at hexa-decimal address>
#Bye


#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')#Begin
print(type(f1))#<class function>
print(id(f1))#<address of the function in decimal>
print('End')#End