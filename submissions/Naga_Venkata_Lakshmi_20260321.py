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

#'Begin'
'Hyd'
'Sec'
'Cyb'
'None'
<class 'None Type'>
End




# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#(10 , 20 , 30)
print(type(x)) #<class 'tuple'>
a , b , c =  f1()   
print(a) #10
print(b) #20
print(c) #30
print('for  loop')
for  k   in   f1():
	print(k) #10
                  20
                  30



# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin') #'Begin'
x = f1()  
print(x) #10
print('End') #'End'
return   100 #Error



#  Find  outputs
f1() #Error function call shpuld be inside the definition function.  
def   f1():
        print('Hello') #Error 

print(f1())  #Error 
print(f1) #Error




# Find  outputs  (Home  work)
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
f1 function
<function f1 at Address>
'Bye'



#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #'Begin'

print(type(f1)) #<class 'functionf1'>
print(id(f1)) #Address of function f1
print('End') #'End'



N = input("Enter mixed case string :  ")
upper_N = N.upper()
print(upper_N)
Sorted_N = sorted(upper_N)
print(Sorted_N) 
Vowels = ('A' , 'E' , 'I' , 'O' , 'U')

a ={}    
for ch in Sorted_N:
     if ch in Vowels:
          a[ch] = a.get(ch , 0) + 1
print(a)       
        