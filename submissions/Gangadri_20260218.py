#   Python-Homework          Date:18/02/2026


 #1 . #  Find  outputs
a = 25
print(id(a))  #=> output : Address of the integer object 25 .
a = 35
print(id(a))  #=> Output : Address of the integer object 35 .


#2 .  # Find  outputs (Home  work)
a = 25.7
print(id(a)) #=> output is : Address  of the float object 25.7
print(a)
a = 35.6  
print(id(a)) #=>  => output is : Address of the  float object 35.6
print(a)    # => output is : 35.6
b = True    
print(id(b)) #=> output : Address of the bool True
b = False
print(id(b))   #=> output : Address of the bool False
c = None
print(id(c))  #=> output : Address of the None
c = None
print(id(c))  #=> output : Same object Address


#3 .  #  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) #=> Output : Address of the object 'Hyd'
a[1] = 'e'    #=> Output : 'str' object does not support item assignment
a = 'Sec'
print(id(a))  #=> Output : Address of the string 'sec'
b = (10 , 20 , 15 , 18)
print(id(b))  #=> output : Address of the object 'tuple'
b[2] = 19     #=> output : 'tuple' object does not support item assignment
b = (30 , 40 , 35 , 32)
print(id(b))  #=> output : Address of the new object 'tuple'
c = range(5) 
print(id(c))  #=> Output : Address of the range object
c[3] = 10      #=> Output : range is immutable
c = range(5)  #=> output : 0,1,2,3,4
print(id(c))   #=> output : It create New Address of the range


#4 . # Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #=> Output : True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)  #=> Output : True
e = False
f = False
print(e  is  f)  #=> Output : True
g = range(10)
h = range(10)
print(g  is  h)  #=> output : range(10) creates new object every time


#5 . #Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)       #=> Output : False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)      #=> Output : False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)       #=> Output : False
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)       #=> Output : False


#6 . # Find outputs (Home work)
print(10 + 20)    #=> Output : 30
print(10.8 + 20.6) #=> Output : Output : 31.4
print(3 + 4j + 5 + 6j) #=> Output : Output : (8+ 10j)
print(True + False)  #=> Output : 1
print('Hyder' + 'abad')  #=> Output : 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')  #=> Output : 'Sankar Dayal Sarma'
print('10' + '20')  #=> Ouput : '1020'
print([10 , 20 , 30] + [1 , 2 , 3])  #=> Output : [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #=> Output : (25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40})  #=> Output : TypeError
print({10 : 'Hyd'} + {20 : 'Sec'}) #=> Output : TypeError
print(range(4) + range(5)) #=> Output : TypeError
print(10 + '20') #=> Output : TypeError
print([10 , 20 , 30] + 5) #=> Output : TypeError
print([10 , 20 , 30] + (40 , 50 , 60)) #=> Output : TypeError



#7 . # Find outputs (Home work)
print(25 * 3)  #=> Output : 75
print(10.8 * 25.6)  #=> Ouput : 276.48
print(True * False) #=> Ouput : (True = 1, False = 0 → 1 * 0 = 0)
print((3 + 4j) * (5 + 6j))  #=> Output : (-9+38j)
print(3 + 4j * 5 + 6j) #=> Output : 4j * 5 = 20j , 3 + 20j + 6j = (3+26j)
print('25' * 3)  #=> Output : '252525'
print(3 * '25')  #=> Output : '252525'
print('Hyd' * 4)  #=> Output : 'HydHydHydHyd'
print([10 , 20 , 15] * 2) #=> Output : [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) #=> Output : (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)  #=> Output : List can multiply only with int, not float 
print({10 , 20 , 15} * 2) #=> Output : set does not support *
print({10 : 20 , 30 : 40} * 2) #=> Output : Dictionary does not support *
print([10] * [20])  #=> Output : TypeError