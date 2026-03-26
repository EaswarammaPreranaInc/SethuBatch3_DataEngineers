'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)
Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
'''

st=input("Enter String : ").upper()
a={}
vowels='AEIOU'
nw_st=sorted(st)
for i in nw_st:
    if i.isalpha() and i in vowels:
        a[i]=a.get(i,0)+1
print(a)


'''
output
Enter String : RamA RaO
{'A': 3, 'O': 1}
'''


# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')#Begin
x = f1()
print(x)#Hyd <nextline> Sec <nextline> Cyb
print(type(x))#class 'typle'
print('End')#End


# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#(10,20,30)
print(type(x))#class 'typle'
a , b , c =  f1()   
print(a)#10
print(b)#20
print(c)#30
print('for  loop')#for loop
for  k   in   f1():
	print(k)#10 <nextline> 20 <nextline> 30
	

# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')#Begin
x = f1()  
print(x)#10 first return will be taken
print('End')#End
return   100#error return outside fuction


#  Find  outputs
f1()  #error f1 not defined
def   f1():
        print('Hello')
print(f1())#Hello <nextline> None 
print(f1)# function f1 at f1-object address 


# Find  outputs  (Home  work)
print('Hello')#Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')#Hi
print(f1())#f1 function <nextline> None
print(f1)#function f1 at f1-object address
print('Bye')#Bye


#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')#Begin
print(type(f1))#class 'function'
print(id(f1))#address of function f1
print('End')#End


