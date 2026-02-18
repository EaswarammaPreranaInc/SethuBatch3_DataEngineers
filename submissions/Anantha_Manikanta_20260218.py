1) #  Find  outputs
a = 25
print(id(a))  # 123411
a = 35
print(id(a))  # 121223

2) # Find  outputs (Home  work)
a = 25.7
print(id(a))  # 123143
print(a)  # 25.7
a = 35.6
print(id(a))  # 148343
print(a)  # 35.6
b = True
print(id(b))  # 2342424
b = False
print(id(b))  # 5434234
c = None
print(id(c))  # 100000
c = None
print(id(c))  # 100000

3) #  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))  # 123121
a[1] = 'e'  # Error because string is immutable we cannot change the element
a = 'Sec'
print(id(a))  # 126543
b = (10 , 20 , 15 , 18)
print(id(b))  # 654334
b[2] = 19  # Error because tuple is immutable we cannot change the elements in it
b = (30 , 40 , 35 , 32)
print(id(b))  # 876543
c = range(5)
print(id(c))  # 234567
c[3] = 10  # Error because range is immutable we cannot change its elements
c = range(5)
print(id(c))  # 234567

4) # Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)  # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)  # True
e = False
f = False
print(e  is  f)  # True
g = range(10)
h = range(10)
print(g  is  h)  # False

5) #Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)  # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)  # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)  # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  # True

6) # Find outputs (Home work)
print(10 + 20)  # 30
print(10.8 + 20.6)  # 31.4
print(3 + 4j + 5 + 6j)  # 8+10j
print(True + False)  # 1
print('Hyder' + 'abad')  # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')  # SankarDayalSarma
print('10' + '20')  # 1020
print([10 , 20 , 30] + [1 , 2 , 3])  # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  # (25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40})  # Error because set does not support + operator
print({10 : 'Hyd'} + {20 : 'Sec'})  # Error because set does not support + operator
print(range(4) + range(5))  # Error because range doesnot support + operator
print(10 + '20')  # Error because int and string cannot be concatenated or added
print([10 , 20 , 30] + 5)  # Error because list and int cannot be concatenated
print([10 , 20 , 30] + (40 , 50 , 60))  # Error because list and tuple cannot be concatenated or added

7) # Find outputs (Home work)
print(25 * 3)  # 75
print(10.8 * 25.6)  # 276.48
print(True * False)  # 0
print((3 + 4j) * (5 + 6j))  # 15+24j
print(3 + 4j * 5 + 6j)  # 3+26j
print('25' * 3)  # 252525
print(3 * '25')  # 252525
print('Hyd' * 4)  # HydHydHydHyd
print([10 , 20 , 15] * 2)  # [10 , 20 , 15, 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)  # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)  # Error because list cannot be multiplied with float
print({10 , 20 , 15} * 2)  # Set doesnot support * operator
print({10 : 20 , 30 : 40} * 2)  # Dictionary doesnot support * operator
print([10] * [20])  # Error because List cannot be multiplied with list