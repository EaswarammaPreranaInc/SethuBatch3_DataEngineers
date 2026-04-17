#  Find  outputs
a = 25
print(id(a)) # address of a reffering object (int)  25
a = 35
print(id(a)) # address of a reffering object (int)  35



# Find  outputs (Home  work)
a = 25.7
print(id(a)) # address of a reffering object (float) 25.7
print(a) # 25.7
a = 35.6
print(id(a)) # address of a reffering object (float) 35.6 
print(a) # 35.6
b = True
print(id(b)) # address of b reffering object (bool) True
b = False
print(id(b)) # address of b reffering object (bool) False
c = None
print(id(c)) # address of c reffering object (None type)
c = None
print(id(c)) # address of c reffering object (None type) same None


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # address of a refering object (str) Hyd
a[1] = 'e' # error bcz str is immutable   
a = 'Sec'
print(id(a)) # address of a refering object(str) Sec
b = (10 , 20 , 15 , 18)
print(id(b)) # address of b refering object(tuple) (10 , 20 , 15 , 18)
b[2] = 19  # error bcz tuple is immutable   
b = (30 , 40 , 35 , 32)
print(id(b)) # address of b refering object(tuple) (30 , 40 , 35 , 32)
c = range(5) # 0,1,2,3,4
print(id(c)) # address of b refering object(range)
c[3] = 10 # error becaz range is immutable
c = range(5)
print(id(c)) # address of b refering object(range) same



# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True
e = False
f = False
print(e  is  f) # True
g = range(10)
h = range(10)
print(g  is  h) # Flase



#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)  # Flase
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)  # Flase
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  # Flase



# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # 8+10j
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25 , 10.8 , 'Hyd',3 + 4j , True , None)
print({10 , 20} + {30 , 40}) #error for set + set is not support
print({10 : 'Hyd'} + {20 : 'Sec'}) #error for dict + dict is not support
print(range(4) + range(5)) #error range is immutable and dupicates are not allowed
print(10 + '20') # error int and str not addable
print([10 , 20 , 30] + 5) # error list and int not addable
print([10 , 20 , 30] + (40 , 50 , 60)) # error list and tuple not addable



# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 10.8*25.6=276.48
print(True * False) # Flase =0
print((3 + 4j) * (5 + 6j)) # (3+4j)(5+6j)=(-9+38j)
print(3 + 4j * 5 + 6j) # 3+26j
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # error float times are not repetable
print({10 , 20 , 15} * 2)  #error set does not contain dupilicate elements
print({10 : 20 , 30 : 40} * 2)  #error set does not contain dupilicate elements
print([10] * [20])  #error range does not allowed mutiplication bcz range is immutable
