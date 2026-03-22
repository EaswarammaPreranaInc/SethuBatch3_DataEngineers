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
begin
hyd
sec
cyb
None
<class 'NoneType'>
end
'''

def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x)   #(10,20,30)
print(type(x)) # <class 'tuple'>
a , b , c =  f1()   
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop')
for  k   in   f1():
	print(k)      #10
	              #20
                     #30				  
def    f1():
	return  10
	return  20
	return  30
# End  of  the  function
print('Begin')  # begin
x = f1()  
print(x)       # 10
print('End')   # end
#return   100	   #eorror

#f2()   # error
def   f2():
        print('Hello')
print(f2())   # None
print(f2)     # type anda ddress


print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

'''
hello
hi
f1 function
None
function address
Bye
'''


def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')  # begin
print(type(f1)) # <class 'function'>
print(id(f1))   # address of function
print('End')# end