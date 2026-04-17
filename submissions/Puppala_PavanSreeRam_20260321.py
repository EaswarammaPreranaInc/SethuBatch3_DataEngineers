'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

s = input("Enter a string: ")

s = s.upper()

vowels = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0}

for ch in s:
    if ch in vowels:
        vowels[ch] += 1

result = {}
for k in vowels:
    if vowels[k] > 0:
        result[k] = vowels[k]

print(result)

#..............................................................................................>

# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function

print('Begin')  = Begin 

x = f1()

print(x)        = Hyd
                  Sec
                  Cyb

print(type(x))  = <class 'None Type'>
print('End')    = End

#..............................................................................................>

# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()

print(x)       = (10, 20, 30)

print(type(x)) = <class 'tuple'>

a , b , c =  f1() 
  
print(a)            = 10

print(b)            = 20

print(c)            = 30

print('for  loop')  = for loop

for  k   in   f1():
	print(k)    = 10
                      20
                      30

#..............................................................................................>

# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function

print('Begin') = Begin

x = f1()  
print(x)       = 10

print('End')   = End
return   100

#..............................................................................................>

#  Find  outputs
f1()  
def   f1():
        print('Hello')   = Error = f1 is not defined
print(f1())  
print(f1)

#..............................................................................................>

# Find  outputs  (Home  work)

print('Hello') = Hello

def  f1():
        print('f1  function')
#End  of   function

print('Hi')  = Hi

print(f1())  = None
print(f1)
print('Bye') = Bye

#..............................................................................................>

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function

print('Begin')  = Begin

print(type(f1)) = <class 'function'>

print(id(f1))   = Address Of f1

print('End')    = End

#..............................................................................................>