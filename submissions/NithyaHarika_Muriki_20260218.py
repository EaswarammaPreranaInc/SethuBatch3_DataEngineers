#  Find  outputs
a = 25
print(id(a))#OUTPUT:Address of the int object
a = 35
print(id(a))#OUTPUT:Address of the int object

# Find  outputs (Home  work)
a = 25.7
print(id(a))#OUTPUT:Address of the float object
print(a)#OUTPUT:25.7
a = 35.6
print(id(a))#OUTPUT:Address of the float object
print(a)#OUTPUT:35.6
b = True
print(id(b))#OUTPUT:Address of the bool object
b = False
print(id(b))#OUTPUT:Address of the bool object
c = None
print(id(c))#OUTPUT:Address of the none object
c = None
print(id(c))#OUTPUT:Address of the none object

#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))#OUTPUT:Address of the str object
a[1] = 'e'   
a = 'Sec'
print(id(a))#OUTPUT:Address of the str object
b = (10 , 20 , 15 , 18)
print(id(b))#OUTPUT:Address of the tuple object
b[2] = 19#OUTPUT:error, tuple cannot be modified
b = (30 , 40 , 35 , 32)
print(id(b))#OUTPUT:Address of the tuple object
c = range(5)
print(id(c))#OUTPUT:Address of the range object
c[3] = 10#OUTPUT:error
c = range(5)
print(id(c)#OUTPUT:Address of the range object


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)#OUTPUT:True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)#OUTPUT:True
e = False
f = False
print(e  is  f)#OUTPUT:True
g = range(10)
h = range(10)
print(g  is  h)#OUTPUT:False


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)#OUTPUT:False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)#OUTPUT:False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)#OUTPUT:True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)#OUTPUT:False


# Find outputs (Home work)
print(10 + 20)#OUTPUT:30
print(10.8 + 20.6)#OUTPUT:31.4
print(3 + 4j + 5 + 6j)#OUTPUT:8+10j
print(True + False)#OUTPUT:1
print('Hyder' + 'abad')#OUTPUT:Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')#OUTPUT:SankarDayalSarma
print('10' + '20')#OUTPUT:1020
print([10 , 20 , 30] + [1 , 2 , 3])#OUTPUT:[10 , 20 , 30,1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))#OUTPUT:(25 , 10.8 , 'Hyd',(3 + 4j) , True , None)
print({10 , 20} + {30 , 40})#OUTPUT:error, set cannot be concatenated
print({10 : 'Hyd'} + {20 : 'Sec'})#OUTPUT:error, dictionary cannot be concatenated
print(range(4) + range(5))#OUTPUT:error , range does not support + operator
print(10 + '20')#OUTPUT:error
print([10 , 20 , 30] + 5)#OUTPUT:error
print([10 , 20 , 30] + (40 , 50 , 60))#OUTPUT:error , list and tuple cannot be concatenated 


# Find outputs (Home work)
print(25 * 3)#OUTPUT:75
print(10.8 * 25.6)#OUTPUT:276.48
print(True * False)#OUTPUT:0
print((3 + 4j) * (5 + 6j))#OUTPUT:-9+38j
print(3 + 4j * 5 + 6j)#OUTPUT:3+6j
print('25' * 3)#OUTPUT:252525
print(3 * '25')#OUTPUT:252525
print('Hyd' * 4)#OUTPUT:HydHydHydHyd
print([10 , 20 , 15] * 2)#OUTPUT:[10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)#OUTPUT:(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)#OUTPUT:error, repetition always should be integer
print({10 , 20 , 15} * 2)#OUTPUT:error set does not contain duplicate values
print({10 : 20 , 30 : 40} * 2)#OUTPUT:error,keys in dictionaries cannot be duplicate
print([10] * [20])#OUTPUT:error, operand 2 always must be a non-sequence i.e. integer