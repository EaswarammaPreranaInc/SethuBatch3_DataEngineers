'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
a=input("Enter the string : ")
a=a.lower()
b="aeiou"
d={}
for x in a:
    if x in b:
        d[x]=d.get(x,0)+1
print(d)
-----------------------------------------------------
# Find outputs  (Home  work)  #Begin
def   f1():                   #Hyd
	print('Hyd')          #Sec
	print('Sec')          #Cyb
	print('Cyb')          #None
# End  of  the  function      #class<NoneType>
print('Begin')                #End
x = f1()
print(x)
print(type(x))
print('End')
------------------------------------------------------
# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30 
# End  of  the  function
x = f1()
print(x) #(10,20,30)
print(type(x)) #class<tuple>
a , b , c =  f1()   
print(a) #10
print(b) #20
print(c) #30
print('for  loop') #for loop
for  k   in   f1():
	print(k)  #10/n20/n30/n
--------------------------------------------------------
# Find  outputs               #Begin
def    f1():                  #10
	return  10            #10
	return  20            #End
	return  30
# End  of  the  function
print('Begin')
x = f1()  
print(x)
print('End')
return   100   #error because return should be inside the function
---------------------------------------------------------
#  Find  outputs
f1()  #error first function should be defined
def   f1():
        print('Hello')
print(f1())  
print(f1)
--------------------------------------------------------
# Find  outputs  (Home  work)       #Hello
print('Hello')                      #Hi
def  f1():                          #f1 function
        print('f1  function')       #None
#End  of   function                 #Bye
print('Hi')
print(f1())
print(f1)
print('Bye')
----------------------------------------------------------
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