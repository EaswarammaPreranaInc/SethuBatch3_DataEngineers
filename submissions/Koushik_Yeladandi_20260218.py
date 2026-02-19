#  Find  outputs
a = 25
print(id(a))  # Address of the object 25
a = 35
print(id(a))  # Address of the object 35



# Find  outputs (Home  work)
a = 25.7
print(id(a)) # Address of the object 25.7 
print(a) # 25.7
a = 35.6
print(id(a))  # # Address of the object 35.6
print(a)  # 36.6
b = True
print(id(b))  # # Address of the object True
b = False
print(id(b))  # # Address of the object false
c = None
print(id(c))  # Address of the object None
c = None
print(id(c))  # Address of the object None



#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))  # Address of the object 'Hyd'
a[1] = 'e'   # 'Hed'
a = 'Sec'   # 'Sec'
print(id(a))  # # Address of the object 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))  # # Address of the object Tuple
b[2] = 19  # Error
b = (30 , 40 , 35 , 32)
print(id(b)) # Address of the object Tuple
c = range(5)  # (0, 1, 2, 3, 4)
print(id(c))  # # Address of the object range
c[3] = 10  # Error
c = range(5)  # 
print(id(c))  # # Address of the object range




# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # False
e = False
f = False
print(e  is  f) # True
g = range(10)
h = range(10)
print(g  is  h) # True




#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)   # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)  # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)  #  True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  # False





# Find outputs (Home work)
print(10 + 20)  # 30
print(10.8 + 20.6)  # 31.4
print(3 + 4j + 5 + 6j)  # Error
print(True + False) # 1
print('Hyder' + 'abad')  #('Hyderabad')
print('Sankar' + 'Dayal' + 'Sarma')  # ('SankarDayalSarma')
print('10' + '20') # ('1020')
print([10 , 20 , 30] + [1 , 2 , 3]) # [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd', 3+4j, True, None)
print({10 , 20} + {30 , 40})  # {10, 20, 30, 40}
print({10 : 'Hyd'} + {20 : 'Sec'})  {10:'Hyd', 20:'Sec'}
print(range(4) + range(5))  # Error
print(10 + '20')  # Error
print([10 , 20 , 30] + 5)  # Error
print([10 , 20 , 30] + (40 , 50 , 60)) # Error




# Find outputs (Home work)
print(25 * 3)  # 75
print(10.8 * 25.6)  # multiplacation of 10.8*26.6
print(True * False)  #  0
print((3 + 4j) * (5 + 6j)) # Error
print(3 + 4j * 5 + 6j)  # Error
print('25' * 3)  # ('252525')
print(3 * '25')  # ('252525')
print('Hyd' * 4)  # ('HydHydHydHyd')
print([10 , 20 , 15] * 2)  # [10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)  #(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # [10 , 20 , 15,10 , 20 , 15,10 , 20 , 15]
print({10 , 20 , 15} * 2)  # Error
print({10 : 20 , 30 : 40} * 2)   # {10 : 20 , 30 : 40,10 : 20 , 30 : 40,10 : 20 , 30 : 40}
print([10] * [20]) # Error