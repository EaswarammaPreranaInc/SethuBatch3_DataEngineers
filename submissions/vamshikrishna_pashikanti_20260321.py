'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
try:
	s=input()
	d={}
	for i in sorted(s.upper()):
		d[i]=d.get(i,0) +1
	print(d)
except:
	print('Error')

		
# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') #Begin
x = f1() 
#Hyd
#Sec
#Cyb
print(x) #None
print(type(x)) #<class 'None'>
print('End') #End

 # Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x) #(10, 20, 30)
print(type(x)) #<class 'tuple'>
a , b , c =  f1()   
print(a) #10
print(b) #20
print(c) #30
print('for  loop') #for loop
for  k   in   f1():
	print(k)
#10
#20
#30

 # Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin') #Begin
x = f1()  
print(x)  #10
print('End') #End
return   100 #Error must be return inside a function

 #  Find  outputs
f1()  #Error cannot be called before declaration
def   f1():
        print('Hello')
print(f1()) #None  
print(f1) # <class 'function'> and f1 address


# Find  outputs  (Home  work)
print('Hello') #Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') #Hi
print(f1()) #None
print(f1) #<class 'function'> and f1 address
print('Bye') #Bye

 #  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #Begin
print(type(f1)) #<class 'function'>
print(id(f1)) #<Address of f1>
print('End') #End
