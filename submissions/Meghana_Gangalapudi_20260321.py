1) Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
#Program
a = input("Enter mixed case string: ")

b = a.upper()         
c = sorted(b)         
vowels = "AEIOU"       
d = {}                 

for ch in c:         
    if ch in vowels:  
        d[ch] = d.get(ch, 0) + 1
print(d)

2) outputs  
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
 #Begin
 Hyd
 Sec
 Cyb
 None
 <class 'None'>
 End	  

3) outputs  
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
#(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30

4) outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')
x = f1()  
print(x)
print('End')
return   100
#Begin
10
End

5) outputs
f1()  #Error because it is not valid
def   f1():
        print('Hello')
print(f1())  
print(f1)
#Hello
None

6) outputs 
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
#Hello
Hi
f1  function
None
address
Bye

7) outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')
#Begin
<class 'function'>
address
End