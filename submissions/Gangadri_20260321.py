#1. Find outputs  (Home  work)
def   f1():
	print('Hyd')  #2. output : 'hyd'
	print('Sec') #3. output : 'Sec'
	print('Cyb') #4. output : 'Cyb'
# End  of  the  function
print('Begin') # 1.output : function start here 'Begin'
x = f1() # it becomes None
print(x) # 4.output : None
print(type(x)) #5. output : <class 'NoneType'>
print('End') # 6.output : 'End'

# ----------------------------------------------------------------------------------

# 2. # Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x) # output : (10 , 20 , 30)
print(type(x)) # output : <class 'tuple'>
a , b , c =  f1()   
print(a) # output : 10
print(b) # output : 20
print(c) # output : 30
print('for  loop') # output : for loop
for  k   in   f1():
	print(k) # 10 next 20 next 30

#------------------------------------------------------------------------------------

# 3 . # Find  outputs
def    f1():
	return  10 # output : 10
	return  20
	return  30
# End  of  the  function
print('Begin') # output : 'Begin'
x = f1()  
print(x)

print('End') # output : 100
#return   100 # error
 
# -----------------------------------------------------------------------

# 4 . #  Find  outputs
#f1()  # output : NameError : f1 is not defineds
def   f1():
        print('Hello') # output : 'Hello'
print(f1())  # output : None
print(f1) # output : <both Address and type


#--------------------------------------------------------------

# 5 . # Find  outputs  (Home  work)
print('Hello') # output : Hello
def  f1():
        print('f1  function') # output : f1 function
#End  of   function
print('Hi') # output : Hi
print(f1()) # output : None
print(f1) # output : To print both address and type
print('Bye') # output : Bye


# ---------------------------------------------------------

# 6 . #  Find  outputs
def    f1():
        print('Hyd') 
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # output : 'Begin'
print(type(f1)) # output : <class 'function'>
print(id(f1)) # output : id of the f1
print('End') # output : 'End'



#--------------------------------------------------------------------------------------

# 7. (Home  work)
# Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

# Let  input  be  RamA    raO
# What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

#Hint:  Same  as  prog23a  with  minor  changes

a = input('Enter a mixed string: ')

b = a.upper()
c=sorted(b)
d={}

for i in c:
	if i in "AEIOU":
		a[i] =d.get(i,0)+1
print(d)		
