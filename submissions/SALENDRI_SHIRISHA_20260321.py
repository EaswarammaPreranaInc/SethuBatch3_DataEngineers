'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
a = input('Enter a mixed case string: ')
a = a.upper()
b = sorted(a)
c = {}
y = {'A' , 'E' , 'I' , 'O' , 'U'}
for x in b:
    if x.isalpha:
        if x in y:
            c[x] = c.get(x , 0) + 1
print(c)


# Find outputs  (Home  work)
def   f1():
	print('Hyd')  # Hyd
	print('Sec')  # Sec
	print('Cyb')  # Cyb
# End  of  the  function
print('Begin')  # Begin
x = f1()   # Hyd
	       # Sec
	       # Cyb
print(x)   #  
print(type(x))  # <class 'function'>
print('End')  # End


# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1() 
print(x)  # 10 , 20 , 30
print(type(x))  # <class 'tuple'>
a , b , c =  f1()   
print(a)  # 10
print(b)  # 20
print(c)  # 30
print('for  loop')  # for loop
for  k   in   f1():
	print(k)  # 10
              # 20
              # 30

# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')  # Begin
x = f1()  
print(x)  # 10
print('End')  # End
#return   100


#  Find  outputs
#f1()  # Error
def   f1():
        print('Hello')
print(f1())  # Hello
print(f1)  # <class 'function'>and address of the function f1


# Find  outputs  (Home  work)
print('Hello')  # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')  # Hi
print(f1())  # f1 function
print(f1)  # <class 'function'>and address of the function f1
print('Bye')  # Bye


#  Find  outputs
def    f1():
        print('Hyd')  
        print('Sec')  
        print('Cyb')  
#End  of  the  function
print('Begin')  # Begin
print(type(f1))  # <class 'function'>
print(id(f1))  # Address of object f1.
print('End')  # End