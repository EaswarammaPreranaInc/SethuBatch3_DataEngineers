'''
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

a = input('Enter a string : ')
b = a.upper()
c = sorted(b)
d = {}

for i in c:
    if i in 'AEIOU':
        d[i] = d.get(i , 0) + 1
print(d)

# Find outputs  (Home  work)
def   f1():
	print('Hyd')	# 2nd excecuted
	print('Sec')	# 3rd excecuted
	print('Cyb')	# 4th excecuted
# End  of  the  function
print('Begin')		# first excecuted
x = f1()
print(x)	    	# 5th excecuted
print(type(x))		# 6th excecuted
print('End')		# last excecuted

# Begin
# 'Hyd'
# 'Sec'
# 'Cyb'
# none
# <class 'function'>
# End


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

# (10 , 20 , 30)
# <class 'tuple'>
# 10
# 20
# 30
# for loop
# 10
# 20
# 30



# Find  outputs
def    f1():
	return  10         # 2nd excecuted
	return  20         # return argument should be write in only one line
	return  30
# End  of  the  function
print('Begin')      # 1st excecuted
x = f1()  
print(x)
print('End')        # last excecuted
# return   100

# Begin
# 10
# End


#  Find  outputs
# f1()  		# error
def   f1():
        print('Hello')
print(f1())  	# Hello
print(f1)       # returns type (function) and address in hexadecimal 
                # <function f1 at 0x000002660BF01440>
				

# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

# Hello
# Hi
# f1 function
# None
# <function address of function>
# Bye


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

# Begin
# <class 'function'>
# address of function
# End
