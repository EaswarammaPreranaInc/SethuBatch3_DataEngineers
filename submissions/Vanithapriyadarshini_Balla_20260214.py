#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) # (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) # 25  10.8  'Hyd'  True  3+4j  None  'Hyd'  25
print(type(a)) # <class 'tuple'>
print(len(a)) # 8
print(a[2 : 5]) # ('Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a[2 : 5]) # 'Hyd' True 3+4j None 'Hyd' 25
a[2] = 'Sec' # Error, bcz tuple is immutable.
a . append('Sec') # Error, bcz tuple is immutable.
a . remove('Hyd') # Error, bcz tuple is immutable.
b =  10 , 20 , 30
print(b) # (10, 20, 30)
print(b * 2) # (10, 20, 30, 10, 20, 30)
c = 40 , 50 , 60,
print(c) # (40, 50, 60)
print(type(c)) # <class 'tuple'>

# Find  outputs  (Home  work)
a = (25) # invalid tuple
b = 25, # valid, bcz tuple should be separeted by ',' when there is single element
c = 25 # invalid tuple
d = (25,) # valid
print(type(a)) # <class 'int'>
print(type(b)) # <class 'tuple'>
print(type(c)) #<class 'int'>
print(type(d)) #<class 'tuple'>
print(a * 4) # 100
print(b * 4) # (25, 25, 25, 25)
print(c * 4) 100
print(d * 4) # (25, 25, 25, 25)

# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) # ('H', 'y', 'd')
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10, 20, 15, 18)
print(tuple(range(5))) # (0, 1, 2, 3, 4)
print(tuple(25)) # Error ,bcz tuple args should be sequence.

# Find  outputs (Home  work)
a = ()
print(type(a)) # <class 'tuple'>
print(a) # ()
print(len(a)) # 0
b = tuple() 
print(b) # ()
print(len(b)) # 0

# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # (10 , 20 , 30)
print(id(a)) # Address of tuple obj (10, 20, 30)
a = a * 2  #  Valid / Invalid # valid
print(a) # (10 , 20 , 30, 10 , 20 , 30)
print(id(a)) # Address of tuple obj (10, 20, 30, 10, 20, 30)