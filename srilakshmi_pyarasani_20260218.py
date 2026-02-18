1) outputs
a = 25
print(id(a))#Address of 25
a = 35
print(id(a))#Address of 35

2) outputs
a = 25.7
print(id(a))#Address of 27.5
print(a)#25.7
a = 35.6
print(id(a))#Address of 35.6
print(a)#35.6
b = True
print(id(b))#Address of True
b = False
print(id(b))#Address of False
c = None
print(id(c))#Address of None
c = None
print(id(c))#Address of None

3) outputs  
a = 'Hyd'
print(id(a))#Address of 'Hyd'
a[1] = 'e' #Error because it is not valid   
a = 'Sec'
print(id(a))#Address of 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))#Address of tuple
b[2] = 19#Error because it is not valid
b = (30 , 40 , 35 , 32)
print(id(b))#Address of tuple
c = range(5)
print(id(c))#Address of range
c[3] = 10#Error because it is not valid
c = range(5)
print(id(c))#Address of range

4) outputs
a = 25
b = 25
print(a  is  b)#True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)#True
e = False
f = False
print(e  is  f)#True
g = range(10)
h = range(10)
print(g  is  h)#False

5) outputs
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)#False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)#False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)#True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)#False

6) outputs 
print(10 + 20)#30
print(10.8 + 20.6)#31.400
print(3 + 4j + 5 + 6j)#8+10j
print(True + False)#1
print('Hyder' + 'abad')#'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')#'SankarDayalSarma'
print('10' + '20')#1020
print([10 , 20 , 30] + [1 , 2 , 3])#[10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))#(25, 10.8, 'Hyd', 3+4j, True, None)
print({10 , 20} + {30 , 40})#Error because it is not valid
print({10 : 'Hyd'} + {20 : 'Sec'})#Error because it is not permitted
print(range(4) + range(5))#Error because it is not permitted
print(10 + '20')#Error because it is not permitted
print([10 , 20 , 30] + 5)#Error because it is not permitted
print([10 , 20 , 30] + (40 , 50 , 60))#Error because it is not permitted

7) outputs 
print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#
print(3 + 4j * 5 + 6j)
print('25' * 3)#252525
print(3 * '25')#252525
print('Hyd' * 4)#'HydHydHyd
print([10 , 20 , 15] * 2)#[10, 20, 15, 10, 20,15]
print((25, 10.8, 'Hyd', True) * 3)#(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True, 25,10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)#Error because float value is not permitted
print({10 , 20 , 15} * 2)#Error because it is not permitted
print({10 : 20 , 30 : 40} * 2)#Error because it is not permitted
print([10] * [20])#Error because it is not permitted




