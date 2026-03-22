# Topic - 1

'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

"""
x = sorted(input("Enter String : ").upper())
y = {}
z = "AEIOU"
for a in x:
    if a.isalpha:
        if a in z:
            y[a] = y.get(a,0)+1
print(y)

"""

#Topic - 2
"""
#Topic- 2.1

# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') #Begin
x = f1() #Hyd<NewLine>Sec<NewLine>Cyb and return None
print(x) #None
print(type(x))#<class 'NoneType'>
print('End') #End


#Topic- 2.2

# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1() #(10, 20, 30)
print(x) #(10, 20, 30)
print(type(x)) #<class 'Tuple'>
a , b , c =  f1()   
print(a) #10
print(b) #20
print(c) #30
print('for  loop') #for  loop
for  k   in   f1():
	print(k)#10<newline>20<newline>30<newline>

#Topic- 2.3

# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')#Begin
x = f1()  
print(x) #10
print('End')#End
#return   100 #Error

#Topic- 2.4
#  Find  outputs
f1()  
def   f1():
        print('Hello')
print(f1()) # None
print(f1) #addres in Dunder

#Topic- 2.5

# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi') #Hi
print(f1()) #f1  function
print(f1) #addres in Dunder
print('Bye') #Bye
print()

#Topic- 2.6

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #Begin
print(type(f1)) #<class "function">
print(id(f1)) #1000
print('End') #End
"""