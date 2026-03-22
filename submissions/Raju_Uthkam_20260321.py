'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

a = input('Enter any word : ').upper()
b = sorted(a)
d = ['A','E','I','O','U']
c = {}
for x in a:
    if x in d:
        c[x] = c.get(x,0) + 1
print(c)
        


# Find outputs  (Home  work)
def   f1():
	print('Hyd') #2nd Hyd
	print('Sec') #3rd Sec
	print('Cyb') #4th Cyb
# End  of  the  function
print('Begin') # Begin is printed first
x = f1() #5th None
print(x)
print(type(x)) #<class 'None'>
print('End') #End is printed at last


# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1() 
print(x) #(10,20,30)
print(type(x)) #<class 'tuple'>
a , b , c =  f1()   
print(a) #10
print(b) #20
print(c) #30
print('for  loop') #for loop 
for  k   in   f1():
	print(k) #10 <nextline> 20 <nextline> 30



# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin') #begin is printed 1st
x = f1()  
print(x) #10 after once return is excuted all the remaining statements are ignored or discarded 
print('End') #End
#return   100 Error is writtened outside the function 



#  Find  outputs
#f1()  Without funtion defination we can't call the function 
def   f1():
        print('Hello')
print(f1())  #Hello NoNe
print(f1) #Address and funtion name printed 



# Find  outputs  (Home  work)
print('Hello') #Hello is printed 1st
def  f1():
        print('f1  function')
#End  of   function
print('Hi') #Hi is printed 2nd
print(f1()) #f1 funtion <nextline> None is printed 3rd 
print(f1) #function name and hexa decimal address is printed 
print('Bye') #Bye is printed at last


#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # Begin is printed first 
print(type(f1)) #<class 'function'>
print(id(f1)) #Address of Function
print('End') #End is printed at last