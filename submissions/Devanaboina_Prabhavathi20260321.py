(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
a = "RamA  raO"
a = a.upper()
vowels = ['A','E','I','O','U']
result = {}
 
for v in vowels:
    count = a.count(v)
    if count > 0:
       result[v]=count
print(result)



# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') # Begin
x = f1() # Hyd Sec Cyb
print(x) # None
print(type(x)) # <class none type>
print('End') # End



# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x) # 10, 20, 30
print(type(x)) # <class 'tuple'>
a , b , c =  f1()   
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop')
for  k   in   f1():
	print(k) # 10,20,30


# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin') # Begin
x = f1()  
print(x) # 10
print('End') # End
return   100 


#  Find  outputs
f1()  
def   f1():
        print('Hello') # Hello
print(f1())  
print(f1) #NameError: name 'f1' is not defined



# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1()) 
print(f1) # f1  function'
print('Bye') # Bye


#  Find  outputs
def    f1():
        print('Hyd') # Hyd
        print('Sec') # Sec
        print('Cyb') #Cyb
#End  of  the  function
print('Begin') # Begin
print(type(f1)) # String
print(id(f1)) # Hyd Sec Cyb
print('End') # End