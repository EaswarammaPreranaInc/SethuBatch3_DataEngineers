 #  Find  outputs
a = 25
print(id(a))#Address of object(25)
a = 35
print(id(a))#address of object(25)

 # Find  outputs (Home  work)
a = 25.7
print(id(a))#adress of object(25.7)
print(a)# 25.7
a = 35.6
print(id(a))#address of object(35.6)
print(a)#35.6
b = True
print(id(b))#address of object (True)
b = False
print(id(b))#Address of object(False)
c = None
print(id(c))#address of object None
c = None
print(id(c)same address

 #  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))#address of object'Hyd'
a[1] = 'e'   #error
a = 'Sec'
print(id(a))#adress of object'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))#address of tuple(10 , 20 , 15 , 18)
b[2] = 19#error
b = (30 , 40 , 35 , 32)
print(id(b))#address of tuple (30 , 40 , 35 , 32)
c = range(5)
print(id(c))#address of range object (01234)
c[3] = 10# error
c = range(5)
print(id(c))#address of2nd range object(01234)

: # Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)#True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)# True
e = False
f = False
print(e  is  f)#True
g = range(10)
h = range(10)
print(g  is  h)#false

 #Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)#false
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)#false
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)#true
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)#false

 # Find outputs (Home work)
print(10 + 20)#30
print(10.8 + 20.6)#31.4
print(3 + 4j + 5 + 6j)#8+10j
print(True + False)#1
printt('Hyder' + 'abad')#Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')#sankardayalsarma
print('10' + '20')#1020
print([10 , 20 , 30] + [1 , 2 , 3])#[10 , 20 , 30,1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))#(25 , 10.8 , 'Hyd',3 + 4j , True , None)
print({10 , 20} + {30 , 40})#error
print({10 : 'Hyd'} + {20 : 'Sec'})#error
print(range(4) + range(5))#error
print(10 + '20')#error
print([10 , 20 , 30] + 5)#error
print([10 , 20 , 30] + (40 , 50 , 60))#error

 # Find outputs (Home work)
print(25 * 3)#75
print(10.8 * 25.6)#something
print(True * False)#0
print((3 + 4j) * (5 + 6j))#15+18j+20j-24=9+38j
print(3 + 4j * 5 + 6j)#3+26j
print('25' * 3)#'252525'
print(3 * '25')#252525
print('Hyd' * 4)#hydhydhydhyd
print([10 , 20 , 15] * 2)#10 , 20 , 15,10 , 20 , 15
print((25, 10.8, 'Hyd', True) * 3)#25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True
print([10 , 20 , 15] * 3.0)#error
print({10 , 20 , 15} * 2)#error
print({10 : 20 , 30 : 40} * 2)#error
print([10] * [20])#error




