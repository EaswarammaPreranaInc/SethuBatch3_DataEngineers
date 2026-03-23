'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

inp = input("Enter the string : ")

n = inp.upper()

v = "AEIOU"
a = {}

for char in sorted(n):
    if char.isalpha() and char in v:
        a[char] = a.get(char, 0) + 1

print(a)

'''
Output :
Enter the string : Auspicious
{'A': 1, 'I': 2, 'O': 1, 'U': 2}
'''
# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') # Begin
x = f1()
print(x) # Hyd
         # Sec
         # Cyb
print(type(x)) # <class 'None'>
print('End') # End

# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x) # (10 , 20 , 30)
print(type(x)) # <class 'tuple'>
a , b , c =  f1()   
print(a)
print(b)
print(c)
print('for  loop')
for  k   in   f1():
	print(k)
 

def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin') # Begin
x = f1()  
print(x) # 10 
print('End') # End 

#  Find  outputs
f1()  # Error
def   f1():
        print('Hello')
print(f1())  
print(f1)

# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1()) # f1 function
print(f1) # None , <funciton at 0x000016
print('Bye') # Bye


#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # Begin
print(type(f1)) # <class 'function'>
print(id(f1)) # 100023
print('End') # End

