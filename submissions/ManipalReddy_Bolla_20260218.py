#  Find  outputs
a = 25
print(id(a))-->result=address of a 
a = 35
print(id(a))-->result=address of a which is new address


# Find  outputs (Home  work)
a = 25.7
print(id(a))-->result=address of a
print(a)-->result=25.7
a = 35.6
print(id(a))-->result=address of a which is different from the initial address
print(a)-->result=35.6
b = True
print(id(b))-->result=address of b
b = False
print(id(b))-->result=address of b which is different from initial b's address
c = None
print(id(c))-->result=address of c 
c = None
print(id(c))-->address of c which is same from initial c's address


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))-->result=address of a
a[1] = 'e'-->result=error(strings are immutable)
a = 'Sec'
print(id(a))-->result=address of a which is different from initial address
b = (10 , 20 , 15 , 18)
print(id(b))-->result=address of b
b[2] = 19-->result= error(typles are immutable)
b = (30 , 40 , 35 , 32)
print(id(b))-->result=address of b which is different from initial b address
c = range(5)
print(id(c))-->result=address of c 
c[3] = 10-->result=error (range object is immutable)
c = range(5)
print(id(c))-->result=(address of c which same from different address)


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)-->result=True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)-->result=True
e = False
f = False
print(e  is  f)-->result=True
g = range(10)
h = range(10)
print(g  is  h)-->result=False


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)-->result=False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)-->result=False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)-->result=False
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)-->result=False


# Find outputs (Home work)
print(10 + 20)-->result=30
print(10.8 + 20.6)-->result=31.4
print(3 + 4j + 5 + 6j)-->result=8+10j
print(True + False)-->result=1
print('Hyder' + 'abad')-->result=Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')-->result=SankarDayalSarma
print('10' + '20')-->result='1020'
print([10 , 20 , 30] + [1 , 2 , 3])-->result=[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))-->result=(25,10.8,'Hyd',3+4j,True,None)
print({10 , 20} + {30 , 40})-->result=error
print({10 : 'Hyd'} + {20 : 'Sec'})-->result=error
print(range(4) + range(5))-->result=error
print(10 + '20')-->result=error
print([10 , 20 , 30] + 5)-->result=error
print([10 , 20 , 30] + (40 , 50 , 60))-->result=error


# Find outputs (Home work)
print(25 * 3)-->result=75
print(10.8 * 25.6)-->result=276.48
print(True * False)-->result=0
print((3 + 4j) * (5 + 6j))-->result=-9+38j
print(3 + 4j * 5 + 6j)-->result=3+26j
print('25' * 3)-->result='252525'
print(3 * '25')-->result='252525'
print('Hyd' * 4)-->result='HydHydHydHyd'
print([10 , 20 , 15] * 2)-->result=[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)-->result=(25,10.8,'Hyd',True,25,10.8,'Hyd',True)
print([10 , 20 , 15] * 3.0)-->result=error
print({10 , 20 , 15} * 2)-->result=error
print({10 : 20 , 30 : 40} * 2)-->result=error
print([10] * [20])-->result=error
