'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
'''
a = input('Enter  mixed  case  string : ') 
b = a . upper() 
c = sorted(b) 
d = {}  
for  ch  in  c:  
	if  ch in 'AEIOU':  
		d[ch] = d.get(ch , 0) + 1  
print(d)'''

'''
# Find outputs  (Home  work)
def   f1():
	print('Hyd') #O/p 2 : Hyd
	print('Sec') #O/p 3: Sec
	print('Cyb') #O/p 4: Cyb
# End  of  the  function
print('Begin') # output 1: Begin
x = f1() 
print(x) #None
print(type(x)) #<class 'NoneType'>
print('End') # End '''


''
# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x) #(10, 20, 30)
print(type(x)) # <class 'tuple'>
a , b , c =  f1()   
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop') # for loop
for  k   in   f1():
	print(k) #10 <nextline> 20 <next line> 30''
	


# Find  outputs
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


#  Find  outputs
#f1()  # f1 is not defined
def   f1():
        print('Hello') # output : 'Hello'
print(f1())  # None
print(f1) # both Address and type

# Find  outputs  (Home  work)
print('Hello') # 'Hello'
def  f1():
        print('f1  function') #o/p2: f1 function
#End  of   function
print('Hi') # o/p 1:Hi
print(f1()) #o/p 3: None
print(f1) # both Address and type
print('Bye') #Bye



#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #'Begin'
print(type(f1)) #<class 'function>
print(id(f1))# address of function
print('End') #End