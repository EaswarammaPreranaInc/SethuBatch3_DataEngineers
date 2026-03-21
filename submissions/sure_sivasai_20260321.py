##1.(Home  work)
##Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)
##
##Let  input  be  RamA    raO
##What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
##
##Hint:  Same  as  prog23a  with  minor  changes

s = input('Enter mixed case string : ')
d = sorted(s.upper())
new = {}
for ch in d:
    if ch.isalpha() and ch in 'AEIOU':
        new[ch] = new.get(ch,0)+1
print(new)

#------------------------------------------

#2.Find outputs  (Home  work)
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

# Output
'''
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End
'''

#----------------------------------------------

#3.Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x)          # (10,20,30)
print(type(x))    # <class 'tuple'>
a , b , c =  f1()   
print(a)          # 10
print(b)          # 20
print(c)          # 30
print('for  loop')# for loop
for  k   in   f1():
	print(k) # 10
	         # 20
	         # 30

#----------------------------

#4.Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin') # Begin
x = f1()       
print(x)       # 10 return 10 and remaining are skipped
print('End')   # End
return   100   # Error

#----------------------------

#5.Find  outputs
f1()        # Error
def   f1():
        print('Hello') # Hello
print(f1()) # None
print(f1)   # <function f1 at 0x000000000>

#----------------------------

#6.Find  outputs  (Home  work)
print('Hello')  
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

# output
'''
Hello
Hi
f1 function
None
<function f1 at ox0000>
Bye
'''

#-------------------------------

#7.Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')

# output
'''
Begin
<class 'function'>
1000
End
'''

#-------------------------------






















