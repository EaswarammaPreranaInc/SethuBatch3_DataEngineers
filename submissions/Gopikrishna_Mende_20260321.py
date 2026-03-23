'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

a=input("Enter a dictionary:")
b={}
for i in a:
    if i .lower() in "aeiou":
        ch=i.upper()
        if ch in b:
            b[ch]+=1
        else:
            b[ch]=1
result=dict(sorted(b.items()))
print(result)

# ===============================================================
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
# Begin
# Hyd
# sec
# cyb
# <class nonetype>
# End

# ======================================================================

# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30 #30
# End  of  the  function
x = f1()
print(x) # 10<new line>20<new line>30
print(type(x)) # <class tuple>
a , b , c =  f1()   
print(a) #10
print(b) # 20
print(c) #30
print('for  loop') # For loop
for  k   in   f1():
	print(k) #10 <new line> 20 <new line> 30<new line>
	

# ======================================================================

# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin') # Begin
x = f1()  
print(x) #30
print('End') # End
# return   100 #error

# =====================================================================

#  Find  outputs
f1()  # Error

def   f1():
        print('Hello') # Hello
print(f1())   #Hello
print(f1) # none

# ====================================================================

# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function') #f1  function
#End  of   function
print('Hi') #Hi
print(f1()) #f1  function
print(f1) # It returns function and its address
print('Bye') # Bye

# ===================================================================

#  Find  outputs
def    f1():
        print('Hyd')  
        print('Sec') 
        print('Cyb') 
#End  of  the  function
print('Begin') # Begin
print(type(f1)) # <class function>
print(id(f1)) # Address of f1
print('End') # End