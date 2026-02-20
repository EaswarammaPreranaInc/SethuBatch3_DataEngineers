a = 25 #reference to object A.
print(id(a)) #prints id of an object A.
a = 35 # reference to object B.
print(id(b)) # prints id reference of an object.


a = 25.7 #float 25.7 is assigned to a.
print(id(a)) #prints reference or id of an object a.
print(a) #prints element 25.7 on screen.

a = 35.6 #float 35.6 is assigned to a.
print(id(a)) #prints reference or id of an object.
print(a) #print element of an object.

b = True
print(id(b)) #prints id of an object b on screen.

b =False
print(id(b)) #prints id of an object b on screen.

c=None
print(id(c)) #prints id of an object c on screen.


a = 'hyd'
print(id(a)) #prints id of an object.

a[1] = 'e' # error 
a='sec' 
print(id(a)) #prints id or reference of an object

b = (10,20,15,18)
print(id(b)) #prints id of an object

b[2] = 19 # we cannot add item to tuple 
b = (30,40,35,32) 
print(id(b)) #print id of an object

c = range(5) #prints 0 to 4 in steps of 1.
print(id(c)) #prints id of an object

c[3] = 10 #we cannot add item into range object
c = range(5) #prints 0 to 4 in steps of 1.
print(id(c)) #prints id of an object.







 #  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) #id of an object.
a[1] = 'e'   #we cannot replace.
a = 'Sec' 
print(id(a)) id of an object.
b = (10 , 20 , 15 , 18)
print(id(b)) # id of an object.
b[2] = 19 #we cannot modify tuple.
b = (30 , 40 , 35 , 32)
print(id(b)) #id of an object.
c = range(5) #0 to 4 is printed
print(id(c)) # id of an object.
c[3] = 10 we cannot modify tuple
c = range(5) 
print(id(c)) #id of an object.


 # Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)#True
e = False
f = False
print(e  is  f) #True
g = range(10)
h = range(10)
print(g  is  h) #False


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) #False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)#True


# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) #30.4
print(3 + 4j + 5 + 6j) #8+10j
print(True + False)
print('Hyder' + 'abad') #hyderabad
print('Sankar' + 'Dayal' + 'Sarma') #sankar dayal sarma
print('10' + '20') #1020
print([10 , 20 , 30] + [1 , 2 , 3]) #[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25 , 10.8 , 'Hyd',3 + 4j , True , None)
print({10 , 20} + {30 , 40}) #{10,20,30,40}
print({10 : 'Hyd'} + {20 : 'Sec'}) {10:'hyd', 20:'sec'}
print(range(4) + range(5)) # we cannot concatenate range object.
print(10 + '20') #Error
print([10 , 20 , 30] + 5)  #Error
print([10 , 20 , 30] + (40 , 50 , 60)) #by usimg pipe operator.


# Find outputs (Home work)
print(25 * 3) #75
print(10.8 * 25.6)#276.48
print(True * False)
print((3 + 4j) * (5 + 6j)) #(3+26j)
print(3 + 4j * 5 + 6j)  #(3+26j)
print('25' * 3) #252525
print(3 * '25') #252525
print('Hyd' * 4) #hydhydhydhyd
print([10 , 20 , 15] * 2) #[10 , 20 , 15,10 , 20 , 15 ]
print((25, 10.8, 'Hyd', True) * 3)  #(25, 10.8, 'Hyd', True ,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)  #Error 
print({10 , 20 , 15} * 2) #Error
print({10 : 20 , 30 : 40} * 2) #error 
print([10] * [20])#error




















