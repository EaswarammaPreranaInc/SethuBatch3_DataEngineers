Assignment-5

#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)  (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a). 25  10.8  'Hyd'  True  3+4j  None  'Hyd'  25
print(type(a)) tuple
print(len(a))  8
print(a[2 : 5])  (‘Hyd’, True, 3+4j)
print(*a[2 : 5]) Hyd  True 3+4j
a[2] = 'Sec'
a . append('Sec') error
a . remove('Hyd') error
b =  10 , 20 , 30 
print(b) 10, 20, 30
print(b * 2) error
c = 40 , 50 , 60,
print(c) 40, 50, 60
print(type(c)) class tuple


# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) < class range>
print(type(b)) class tuple
print(type(c)) class int
print(type(d)) class tuple 
print(a * 4) error
print(b * 4) error
print(c * 4) 100
print(d * 4) error


# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) (Hyd,)
print(type(a)) class tuple
print(len(a)) 1
b = [10 , 20 , 15 , 18] 
print(tuple(b)) (10,20,15,18)
print(tuple(range(5))) 5,
print(tuple(25)) 25,


# Find  outputs (Home  work)
a = ()
print(type(a)) range
print(a) ()
print(len(a)) 0
b = tuple() 
print(b) 
print(len(b)) 0


# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)  10, 20,30
print(id(a)) address of object a
a = a * 2  #  Valid / Invalid invalid no duplicates in tuple
print(a) 20,40,60
print(id(a)) same address 