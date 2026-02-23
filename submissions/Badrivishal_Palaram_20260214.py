#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) O/P: (25 , 10.8 , 'Hyd' , True , 3+4j , None, , 'Hyd' , 25)
print(*a)  O/P:25  10.8 'Hyd' True 3+4j 'Hyd'  25
print(type(a)) O/P: <class ‘tuple’> 
print(len(a)) O/P: 8
print(a[2 : 5]) O/P: ('Hyd' , True , (3+4j) , None)
print(*a[2 : 5]) O/P : 'Hyd' True  3+4j  None
a[2] = 'Sec'   O/P: error tuple is immutable
a . append('Sec') O/P: error tuple is immutable
a . remove('Hyd') O/P: error tuple is immutable
b =  10 , 20 , 30
print(b) O/P:(10 , 20 , 30)
print(b * 2) O/P:(10 , 20 , 30,10 , 20 , 30)
c = 40 , 50 , 60,
print(c) O/P : (40 , 50 , 60)
print(type(c)) O/P: <class ‘tuple’>

# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) O/P: <class ‘int’>
print(type(b)) O/P: <class ‘tuple’>
print(type(c)) O/P: <class ‘int’>
print(type(d)) O/P: <class ‘tuple’>
print(a * 4) O/P: 100
print(b * 4) O/P: (25,25,25,25)
print(c * 4) O/P: 100
print(d * 4) O/P: (25,25,25,25)

# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) O/P: (‘H’,’y’,’d’)
print(type(a)) O/P: <class ‘tuple’>
print(len(a)) O/P: 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) O/P: (10 , 20 , 15 , 18)
print(tuple(range(5)))  O/P: (0,1,2,3,4)
print(tuple(25)) O/P: error , tuple is immutable





# Find  outputs (Home  work)
a = ()
print(type(a)) O/P: <class ‘tuple’>
print(a) O/P: ()
print(len(a)  O/P: 0
b = tuple()
print(b) O/P: ()
print(len(b)) O/P: 0

# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) O/P: (10,20,30)
print(id(a)) O/P: some system generated address say 1000
a = a * 2  #  Valid / Invalid O/P: Valid
print(a) O/P: (10,20,30,10,20,30)
print(id(a)) O/P: some system generated address say 2000
