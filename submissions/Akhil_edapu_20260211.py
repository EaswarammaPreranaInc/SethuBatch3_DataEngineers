a=10.8
print(a) #class object float value is printed 10.8 on screen
print(type(a))# <class float> is printed because 10.8 is float than the class float
print(id(a))# ID or Reference of an object a is printed on screen

b=25
print(a)#prints value of object b on screen 25
print(type(b)) # prints <class 'int'> on screen because 25 is int object
print(id(b)) # prints Id or reference of an object b on screen.

c = .689 # .689 is assigned to reference object C 
print(c)# prints value by adding 0 to front of the number because no number before decimal point.

d = 3.4e2 # E is exponent.
print(d) # prints value 340.0 on screen 
print(type(d)) #class 'float'
print(id(d)) #id or reference is printed on screen

a = 9.62e-2 # the value is scientific value E in the number
print(a) # prints the value 0.0962 on screen
print(id(a)) # print the id or reference of an object on the screen 
print(type(a)) # class 'float' 


a = 6j
print(a) #prints 6j on screen 
print(type(a)) # class 'complex'
print(a.real) # there is no value as real so 0.0 is printed.
print(a.imag) # 6.0 is printed complex are always float values.
#print(5+j4) #Error J should be after the imah value.
#print(3+4i)  # error because in python we use only J as imag value not I
#print(4+j) #Error j is not defined
print(4+1j) #print values on 4+1j on screen
print(4+0j) #prints value on screen 4+0j 


a = 0xA7B9
print(a) # print octal number to decimal equivalent number.
print(type(a)) #print class 'int' object

b=0xBEEF
print(b) # print octal to decimal equivalent number
print(type(b)) # print class 'int' object.

#print(a7b9)  # A7B9 is not value nor a digit so that gives an Error not defined 
print('a7b9') # prints the same value on the screen because a7b9 is a string.
#print(0xbeer) # prints Error because it not a string nor a number and also not defined.
#print(0xhyd) # it not a number nor string also not defined it gives error
#print(0XA7G9B) # it not a number nor string also not defined it gives error


a = True
print(a) # prints value True on screen its a bool object
print(type(a)) #class 'bool' object 
print(id(a)) #id or reference is printed on screen of an object a.



b = False
print(b) # prints False on screen its a bool class
print(type(b)) # class 'bool' 
print(id(b)) #id or refernce of an b object.

print(True + True) #print value 2 on screen if a bool objects does arithmetic operation.true value is 1

print(True+False) # prints 1 on screen if a bool object is performed arithmetic operation. false value is 1

print(False+False) #prints on screen 0 

print(False+True) #prints 1 on screen 
 

print(True+True+True) #print value 3 on screen.
print(25+10.8+True)# print value 36.8 on screen.
print(True > False) # print True, Because comparison operator gives true or false as an output.
print(True) # True is printed on screen.

a = 0o6247 #prefix o or O represent octal number 
print(a) # prints decimal equivalent 
print(type(a)) # class 'int'
print(id(a)) #prints id or reference of an object A.

b = 0O6247 #refix tell octal it's an octal 
print(b) #prints decimal equivalent number on screen.
print(id(b)) # prints the same address of A object here because in python the object is reusable.

c = 3239
print(c) #prints 3239 on screen.
print(id(c)) #prints id or reference of an object C.
print(type(c)) #prints class 'int'.

#print(0o9248) # not defined in python we cannot or directly print binary or octal or hexadecimal on screen.


