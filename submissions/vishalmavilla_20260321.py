(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  min

a = input('Enter  mixed  case  string : ')  
b = a . upper() 
c = sorted(b)  
d = { }  
for  ch  in   c:  
	if  ch in 'AEIOU':  
		d[ch] = d . get(ch , 0) + 1  
print(d)


# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')  # Begin
x = f1()
print(x)  # Hyd
            Sec
            Cyb
            None
print(type(x)) #  <class 'NoneType>
print('End') # End



# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x) # 10 , 20 , 30
print(type(x))  # <class 'Tuple'>
a , b , c =  f1()   
print(a)  # 10
print(b)  # 20
print(c)  # 30
print('for  loop')  # for loop
for  k   in   f1():
	print(k) # 10 
                   20 
                   30


# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')   # Begin
x = f1()  
print(x)  # 10
            
print('End')  # End
return   100   # error



#  Find  outputs
f1()  
def   f1():
        print('Hello')
print(f1())   
print(f1)  



# Find  outputs  (Home  work)
print('Hello')  # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')  # Hi
print(f1())  # f1 function
print(f1)  
print('Bye')  # bye



#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')  # Begin
print(type(f1)) # <class 'Function'>
print(id(f1))  # address of the function
print('End')  # End


