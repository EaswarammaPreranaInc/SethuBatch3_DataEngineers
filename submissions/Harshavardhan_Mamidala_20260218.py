#  Find  outputs
a = 25
print(id(a))  #address will be printed
a = 35
print(id(a))  #different address will be printed-since int object is immutable


# Find  outputs (Home  work)
a = 25.7
print(id(a))  #address will be printed
print(a)  #25.7
a = 35.6
print(id(a))  #different address will be printed since float object is immutable
print(a)  #35.6
b = True
print(id(b))  #address will be printed
b = False
print(id(b))  #different address will be printed since bool object is immutable
c = None
print(id(c))  #address will be printed
c = None
print(id(c))  #same address will be printed


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))  #address will be printed
a[1] = 'e'   #error-str in immutable
a = 'Sec'
print(id(a))  #different address will be printed
b = (10 , 20 , 15 , 18)
print(id(b))  #address will be printed
b[2] = 19  #error-since tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b))  #different address will be printed
c = range(5)
print(id(c))  #address will be printed
c[3] = 10  #error
c = range(5)  
print(id(c))  #different address will be printed since  range is immutable but not reusable

# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)  #True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)  #True
e = False
f = False
print(e  is  f)  #True
g = range(10)
h = range(10)
print(g  is  h)  #False-since range is immutable but not reusable

#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)  #False since list is mutable and not reusable
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)  #False since dict is mutable and not reusable
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)  #True since tuple is immutable and reusable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  #False since set is mutable not reusable


# Find outputs (Home work)
print(10 + 20)  #30
print(10.8 + 20.6)  #31.4
print(3 + 4j + 5 + 6j)  #8+10j
print(True + False)  #1
print('Hyder' + 'abad')  #Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') #SankarDayalSarma
print('10' + '20')  #1020
print([10 , 20 , 30] + [1 , 2 , 3])  #[10 , 20 ,30 , 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  #(25 , 10.8 , 'Hyd' , 3 + 4j , True , None )
print({10 , 20} + {30 , 40})  #error-since unordered
print({10 : 'Hyd'} + {20 : 'Sec'})  #error
print(range(4) + range(5))  #error
print(10 + '20')  #error-since non sequence cannot be added to a sequence
print([10 , 20 , 30] + 5)  #error-since non sequence cannot be added to a sequence
print([10 , 20 , 30] + (40 , 50 , 60))  #error-both are of different type


# Find outputs (Home work)
print(25 * 3)  #75
print(10.8 * 25.6)  #276.48
print(True * False)  #0
print((3 + 4j) * (5 + 6j))  #-9+38j
print(3 + 4j * 5 + 6j)  #3+26j
print('25' * 3)  #'252525'
print(3 * '25')  #'252525'
print('Hyd' * 4)  #'HydHydHydHyd'
print([10 , 20 , 15] * 2)  #[10 , 20 , 15 , 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)  #(25, 10.8, 'Hyd', True , 25, 10.8, 'Hyd', True , 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)  #error-when operand 1 is a sequence ,operand 2 must be int but not float
print({10 , 20 , 15} * 2)  #error-set cannot be repeated
print({10 : 20 , 30 : 40} * 2)  #error-dict cant be repeated
print([10] * [20])  # when operand 1 is a sequence ,operand 2 must be int but not another sequence






