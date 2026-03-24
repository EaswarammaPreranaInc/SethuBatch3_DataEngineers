
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
'''
Begin
None
<class 'function'>
End
'''



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
'''
(10 , 20 , 30)
<class 'function'>
10
20
30
for loop
10
20
30
'''


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
# return   100    #error

'''
Begin
10
End

'''



#  Find  outputs
f1()                                  #error
def   f1():
        print('Hello')
print(f1())                          #Hello and None
print(f1)                            #Type and address     (dunder str, __str__()) 




# Find  outputs  (Home  work)
print('Hello')                                #Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')                                  #Hi
print(f1())                                  #f1 function and returning None
print(f1)                                    #type and address
print('Bye')                                 #Bye



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
'''
Begin
<class 'function'>
address of the function
End

'''



'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''


#program
a = input('Enter mixed case string: ')
b = a.upper()
c = sorted (b)
x = 'AEIOU'
d={}
for ch in c :
	    if ch in x:
		    d[ch]=d.get(ch, 0) + 1
print(d)
