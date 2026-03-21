# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')		#Begin
x = f1()
print(x)		#Hyd\nSec\nCyb
print(type(x))		#<class 'function'>
print('End')		#End



# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x)	#10,20,30
print(type(x))	#<class 'function'>
a , b , c =  f1()   
print(a)	#10
print(b)	#20
print(c)	#30
print('for  loop')	#for loop
for  k   in   f1():
	print(k)	#10\n20\n30



# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')		#Begin
x = f1()  
print(x)		#10
print('End')		#End
return   100		#error



#  Find  outputs
f1()			#error f1() is not defiined  
def   f1():
        print('Hello')	#Hello
print(f1())		#None  
print(f1)		#<class 'function' at address of function in hexadecimal>



# Find  outputs  (Home  work)
print('Hello')		#Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')		#Hi
print(f1())		#None
print(f1)		#<f1 function at address of function in hexadecimal>
print('Bye')		#Bye



#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')		#Begin
print(type(f1))		#<class 'function'>
print(id(f1))		#address of function
print('End')		#End



user_input=input("Enter mixed case string: ").upper()
vowels="A E I O U"
sorted_list=sorted(user_input)
vowel_count={}
for char in vowels.split():
    count=user_input.count(char)
    if count>0:
        vowel_count[char]=count
print(vowel_count)        
    