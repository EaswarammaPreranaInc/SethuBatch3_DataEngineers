'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

a = input("enter a string : ").upper()
b = sorted(a)
d = {}
c = "AEIOU"
for i in b:
    if i.isalpha() and i in c:
        d[i] = d.get(i ,0)+1
print("output : " , d)

# Find outputs  (Home  work)

def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') # Begin
x = f1() # 'Hyd' <nextline> 'Sec' <nextline> 'Cyb' <nextline>
print(x) # None
print(type(x)) # class None
print('End') # End

# Find  outputs  (Home  work)

def  f1():
	return   10 , 20 , 30

# End  of  the  function
x = f1()
print(x) # (10,20,30)
print(type(x)) # class tuple
a , b , c =  f1()   
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop') # for loop
for  k   in   f1(): 
	print(k) # 10 <nextline> 20 <nextline> 30 <nextline>

# Find  outputs

def    f1():
	return  10 
	return  20 # error 
	return  30 # error

# End  of  the  function
print('Begin') # Begin
x = f1()  
print(x) # 10
print('End') # End
return   100 # error

#  Find  outputs
f1() # Hello 
def   f1():
        print('Hello')
print(f1()) # None 
print(f1) # address of function f1

# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1()) # f1 function
print(f1) # None
print('Bye') # bye

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # begin
print(type(f1)) # class function
print(id(f1)) # address of f1
print('End') # end