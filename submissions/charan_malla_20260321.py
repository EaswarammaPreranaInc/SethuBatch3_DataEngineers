'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
''

a = input("enter a string :")
b = a.upper()
c = sorted(b)
d = {}
for x in c:
    if x in "AEIOU":
        count = c.count(x)
        d[x] = count
        
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
'Begin'
'Hyd'
'Sec'
'Cyb'
None
<class'None'>
'End'
'''



# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1() # function is called
print(x) # (10 , 20 , 30)
print(type(x)) # <class'tuple'>
a , b , c =  f1() # function is called  
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop')
for  k   in   f1():
	print(k) # 10 <next line> 20 <next line> 30 <next line>


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
return   100 # Error, return cannot be outside the function 


'''
'Begin'
10
'End'
'''


#  Find  outputs
f1()  # Error , function is not defined
def   f1():
        print('Hello') # 'Hello'
print(f1())  # None
print(f1) # returns type and address of function



# Find  outputs  (Home  work)
print('Hello') # 'Hello'
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # 'Hi'
print(f1()) # 'f1 function'
print(f1) # type and address of f1 function
print('Bye') # 'Bye'

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # 'Begin'
print(type(f1)) # <class'function'>
print(id(f1)) # address of f1 function
print('End') # 'End'
       