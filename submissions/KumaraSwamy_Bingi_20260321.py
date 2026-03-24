'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

n = input()
res = {}
n = n.upper()

for i in n:
    if i in 'AEIOU':
        res[i] = res.get(i, 0) + 1

res = dict(sorted(res.items()))
print(res)










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
output:

Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End

'''







# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x)             #(10,20,30)
print(type(x))       #<class 'tuple'>

a , b , c =  f1()   
print(a)             #10
print(b)              #20
print(c)              #30
print('for  loop')
for  k   in   f1():
	print(k)               # 10 <nextline> 20 <nextline> 30<nextline>
	









  # Find  outputs
def    f1():
	return  10               #only this is execute and remain are ignored
	return  20
	return  30
# End  of  the  function
print('Begin')              #begin
x = f1()                    
print(x)                    #10
print('End')                #end
return   100                #error 
















#  Find  outputs
f1()              #ignored
def   f1():        
        print('Hello')
print(f1())                 #Hello and None
print(f1)                    #prints type of object that is fountion and address of it










# Find  outputs  (Home  work)
print('Hello')                    #Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')                         #Hi
print(f1())                         #f1 function  and None
print(f1)                           #prints type of object that is fountion and address of it

print('Bye')                        #Bye








#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')             #Begin
print(type(f1))             #<class 'function'>

print(id(f1))               #prints address of f1()
print('End')                  #End