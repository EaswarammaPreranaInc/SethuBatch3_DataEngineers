#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)  ---> # (25, 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) ---> # 25  10.8  'Hyd'  True  3+4j  None  'Hyd'  25
print(type(a))----> # string object
print(len(a)) ---> # 8
print(a[2 : 5]) ---> # print(a[2 : 5 : 1]) ---> #  ['Hyd' , True , 3+4j] 
print(*a[2 : 5]) ---> # print(*a[2 : 5 : 1]) ---> ['Hyd'  True  3+4j]
a[2] = 'Sec'---> # (25 , 10.8 , 'Sec' , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
a . append('Sec') ---> # (25 , 10.8  , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
a . remove('Hyd') ---> #  (25 , 10.8  , True , 3+4j , None , 'Hyd' , 25) 
b =  10 , 20 , 30 
print(b) ---> # 10  20  30 
print(b * 2) ---> # 10 , 20 , 30 , 10 , 20 , 30
c = 40 , 50 , 60,
print(c) ---> # 40 , 50 , 60,
print(type(c)) ----> # 40  50  60


# Find  outputs  (Home  work)
a = (25) 
b = 25,
c = 25
d = (25,)
print(type(a)) ---> # int
print(type(b)) ---> # tuple & list
print(type(c)) ---> # string
print(type(d)) ---> # tuple
print(a * 4) ---> # 25 25 25 25
print(b * 4) ---> # 25 25 25 25
print(c * 4) ---> # 25 25 25 25
print(d * 4) ---> # 25 25 25 25


# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd') 
print(a) ---> # Hyd
print(type(a)) ---> tuple
print(len(a))---> 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) ---> # 10 20 15 18
print(tuple(range(5))) ---> # 3
print(tuple(25)) ---> # Error

# Find  outputs (Home  work)
a = ()
print(type(a)) ---> # tuple
print(a) ---> # empty
print(len(a)) ---> 0
b = tuple() 
print(b) ---> tuple()
print(len(b)) ---> 7

# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) ---> 10 , 20 , 30
print(id(a)) ---> Address of tuple 
a = a * 2 ---> #  Valid / Invalid ---> valid
print(a) ---> # 10 , 20 , 30 ,10 , 20 , 30
print(id(a)) ---> # address of a