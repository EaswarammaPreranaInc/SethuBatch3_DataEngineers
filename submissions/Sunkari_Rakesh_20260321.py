 '''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
# program

a = input('Enter  mixed  case  string : ')  #   Reads  a  string
b = a . upper()  #  Converts string  to  uppercase
c = sorted(b)  #  Sorts  characters  of  the  uppercase  string  to  form  a  list
d = { }  # Empty  dictionary
e='A','E','I','O','U'
for  ch  in   c:  # ch  is   each  char  of  the  list
	if  ch . isalpha():  #  Is  ch  an  alphabet
		d[ch] = d . get(ch , 0) + 1

for ch in e:
	if ch in d:

# End  of  for  loop
		print(ch,d[ch])
	#else:
		#print(ch,"not found") # to get the missing vowels also we use this else
 




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

# output
Begin
Hyd
Sec
Cyb
None
address and type of function
<class "function">
End




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

# output
10,20,30
<class "function">
10
20
30
for loop




 # Find  outputs
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

#output
Begin
10
20
30
10 20 30 
End 
100



#  Find  outputs
f1()  
def   f1():
        print('Hello')
print(f1())  
print(f1)

#output
error bec function cant be called before the function is defined


# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1()) # address and type of function
print(f1) # error
print('Bye') # Bye






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


#Output
Begin
<class 'function'>
address of f1
End