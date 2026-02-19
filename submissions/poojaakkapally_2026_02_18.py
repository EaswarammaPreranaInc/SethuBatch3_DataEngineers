1.# Find  outputs
a = 25
print(id(a))----address of the object a
a = 35
print(id(a))-----different address of the object a

2.# Find  outputs (Home  work)
a = 25.7
print(id(a))-----address of the object a
print(a)-----25.7
a = 35.6
print(id(a))----different address of the object a
print(a)----35.6
b = True
print(id(b))------address of the object b
b = False
print(id(b))------different address of the object B
c = None
print(id(c))------address of the object c
c = None
print(id(c))------address of the object c

3.#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))-----address of the object a
a[1] = 'e' ---error  
a = 'Sec'
print(id(a))----different address of the object a
b = (10 , 20 , 15 , 18)
print(id(b))-----address of the object b
b[2] = 19----error
b = (30 , 40 , 35 , 32)
print(id(b))-----different address of the object b
c = range(5)
print(id(c))---address of the object c
c[3] = 10----error
c = range(5)
print(id(c))----different address of the object c

4.# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)----true
c = 'Hyd'
d = 'Hyd'
print(c  is  d)----true
e = False
f = Falses
print(e  is  f)----true
g = range(10)
h = range(10)
print(g  is  h)----false

5.#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)---------------False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)---------------False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)---------------True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)---------------False

6.# Find outputs (Home work)
print(10 + 20)---------------30
print(10.8 + 20.6)---------------30.14
print(3 + 4j + 5 + 6j)---------------8+10j
print(True + False)---------------1
print('Hyder' + 'abad')---------------Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')---------------SankarDayalSarma
print('10' + '20')---------------1020
print([10 , 20 , 30] + [1 , 2 , 3])---------------[10 , 20 , 30,1 ,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))---------------(25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40})---------------error
print({10 : 'Hyd'} + {20 : 'Sec'})---------------error
print(range(4) + range(5))---------------error
print(10 + '20')---------------error
print([10 , 20 , 30] + 5)---------------error
print([10 , 20 , 30] + (40 , 50 , 60))---------------error

7.# Find outputs (Home work)
print(25 * 3)--------------75
print(10.8 * 25.6)-----------276.48
print(True * False)--------------0
print((3 + 4j) * (5 + 6j))--------------(-9+38j)
print(3 + 4j * 5 + 6j)--------------(3+26j)
print('25' * 3)--------------252525
print(3 * '25')--------------252525
print('Hyd' * 4)--------------HydHydHydHyd
print([10 , 20 , 15] * 2)--------------[10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)--------(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)---------------error
print({10 , 20 , 15} * 2)---------------error
print({10 : 20 , 30 : 40} * 2)---------------error
print([10] * [20])---------------error




