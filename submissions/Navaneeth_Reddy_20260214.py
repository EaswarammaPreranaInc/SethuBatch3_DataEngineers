#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) # (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) # 25 10.8  'Hyd'  True  3+4j  None  'Hyd'  25
print(type(a)) # <class ‘tuple’>
print(len(a)) # 8
print(a[2 : 5]) # ('Hyd' , True , 3+4j)
print(*a[2 : 5]) # 'Hyd'  True  3+4j
a[2] = 'Sec' # Error because tuples are immutable
a . append('Sec') # Error because tuples are immutable, so append() is not supported by tuple
a . remove('Hyd') ## Error because tuples are immutable, so remove() is not supported by tuple
b =  10 , 20 , 30
print(b) # (10 ,20, 30)
print(b * 2) # (10 ,20, 30 , 10 ,20, 30)
c = 40 , 50 , 60,
print(c) # (40 , 50 , 60)
print(type(c)) # <class ‘tuple’>

# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) # <class ‘int’>
print(type(b)) # <class ‘tuple’>
print(type(c)) # <class ‘int’>
print(type(d)) # <class ‘tuple’>
print(a * 4) # 100 , As ‘a’ is int, * is considered as multiplication
print(b * 4) # (25 , 25, 25 , 25), In this as b is tuple, * is considered as repeatator
print(c * 4) # 100
print(d * 4) # (25 , 25, 25, 25)

# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) # (‘H’, ‘y’ , ‘d’)
print(type(a)) # <class ‘tuple’>
print(len(a)) # 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10 , 20 , 15 , 18) here list is converted to tuple
print(tuple(range(5))) # (0, 1, 2, 3, 4) , it creates range with numbers from 0 to 4 , then converted to tuple
print(tuple(25)) # Error, because here 25 is non sequence, where non sequence can not be converted to tuple

# Find  outputs (Home  work)
a = ()
print(type(a)) # < class ‘tuple’>
print(a) # (), it is empty tuple
print(len(a)) # 0
b = tuple()
print(b) # (), empty tuple
print(len(b)) # 0 because as there are no elements in tuple so length is 0




# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # (10 , 20 , 30)
print(id(a)) # Address of a, 147000
a = a * 2  #  Valid / Invalid # It is valid
print(a) # (10 , 20 , 30, 10 , 20 , 30)
print(id(a)) # New address of a , as the new tuple is created 156000
