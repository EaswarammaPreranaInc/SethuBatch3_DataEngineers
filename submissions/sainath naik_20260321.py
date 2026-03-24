
'''
(Home  work)
1.Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

s = input('Enter any string:')
s = s.upper()
res = {}
for ch in s:
    if ch in 'AEIOU':
        if ch in res:
            res[ch]+=1
        else:
            res[ch] = 1
print(res)




2.# Find outputs  (Home  work)
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
Hyd
Sec
Cyb
None
<class 'NoneType'>
End
'''




3.# Find  outputs  (Home  work)
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
(10 ,20, 30)
<class 'tuple'>
10
20
30
for loop
10
20
30
'''




4.# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()  
print(x)
print('End')
#return   100 return statement only in inside the function
'''
Begin
10
End
'''


5.#  Find  outputs
#f1()  can not be call the function before the  function define
def   f1():
        print('Hello')
print(f1())  
print(f1)
'''
Hello
None
'''




6.# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

'''
Hello
Hi
f1 function 
None
<function f1 at addresss>
Bye
'''




7.#  Find  outputs
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
address of f1 function
End
'''