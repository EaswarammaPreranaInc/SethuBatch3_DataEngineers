


'''
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

a = input('Enter  mixed  case  string : ') .upper()
vowel="A,E,I,O,U"
d = { }  # Empty  dictionary
for  ch  in   a:  
	if  ch in vowel: 
			d[ch] = d . get(ch , 0) + 1
# End  of  for  loop
print(dict(sorted(d.items())))


# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')   # Begin
x = f1() # Hyd<next line> Sec<next line>Cyb
print(x)  # Returns none
print(type(x))  # <class 'nonetype'>
print('End')  # End



# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()   # (10,20,30)
print(x)  # None
print(type(x))   # <class 'Nonetype'>
a , b , c =  f1()   
print(a)  # 10
print(b)  # 20
print(c)  # 30
print('for  loop')
for  k   in   f1():
	print(k)
# 10<next line>20<next line>30


# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')  # begin
x = f1() 
print(x)  # 10
print('End')  # End
return   100  # Error




#  Find  outputs
f1()  
def   f1():
        print('Hello')
print(f1())  
print(f1)  # Error

# Find  outputs  (Home  work)
print('Hello')  # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1())  # f1 function
print(f1)  # None
print('Bye')   # Bye






#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')  # Begin
print(type(f1))  # <class 'function'>
print(id(f1)) #  Address of function
print('End')  # End

