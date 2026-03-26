#Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)
inp=input("Enter string : ")
inp=inp.upper()
sor_inp=sorted(inp)
dic={}
for x in sor_inp:
    if x.isalpha():
        if x in "AEIOU":
          dic[x]=dic.get(x,0)+1
print(dic)

# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') # Begin
x = f1() 
print(x) # Hyd<nl>'Sec'<nl>'Cyb'<nl>None
print(type(x)) # <class 'NoneType'>
print('End') #End

# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x) # (10 ,20 ,30)
print(type(x)) # <class 'tuple'>
a , b , c =  f1()   
print(a) #10
print(b) #20
print(c) #30
print('for  loop') # for loop
for  k   in   f1():
	print(k) # 10<nl>20<nl>30
      
# Find  outputs
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin') # Begin
x = f1()  # 10
print(x) # 10
print('End') # End
# return   100  Error, bcz return should be in func only

#  Find  outputs
f1()  # Error, bcs f1 is not defined
def   f1():
        print('Hello')
print(f1())  # Hello<nl>None
print(f1) #<function func_name  Address of func>

# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1()) # f1 function<nl>None
print(f1) # <function f1 addr of f1>
print('Bye') # Bye

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # Begin
print(type(f1)) # <class 'function'>
print(id(f1)) # Addr of f1
print('End') #End
