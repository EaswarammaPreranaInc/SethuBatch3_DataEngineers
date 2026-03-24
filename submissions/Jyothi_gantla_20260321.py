'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
a = input('Enter  mixed  case  string : ')  #   Reads  a  string
b = a . upper()  #  Converts string  to  uppercase
c = sorted(b)  #  Sorts  characters  of  the  uppercase  string  to  form  a  list
d = { }  # Empty  dictionary
e = ['A','E','I','O','U']
for  ch  in   c:  # ch  is   each  char  of  the  list
	if  ch in e:  #  Is  ch  an  alphabet
		d[ch] = d . get(ch , 0) + 1  
# End  of  for  loop
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
#output:;
#Begin
#Hyd
#Sec
#Cyb
#None
#<class 'NoneType'>
#End


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

#outputs
#(10, 20, 30)
#<class 'tuple'>
#10
#20
#30
#for loop
#10
#20
#30

	
#Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')
x = f1()  
print(x)
print('End')
return   100  #Error

#output
#Begin
#10
#End

 #  Find  outputs
f1()  
def   f1():
        print('Hello')
print(f1())  
print(f1)
#error f1 not defined
# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
#output
Hello
Hi
f1  function
None
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

#output
#Begin
#<class 'function'>
#address of the function
#End
