Outputs Homework #1

a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) # (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) # 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a)) # <class ‘tuple’>
print(len(a)) # 8
print(a[2 : 5]) # (‘Hyd’ , True , 3+4j)
print(*a[2 : 5]) # Hyd True 3+4j
a[2] = 'Sec' # error because a tuple is immutable
a . append('Sec') # error because a tuple is immutable
a . remove('Hyd') # error because a tuple is immutable
b =  10 , 20 , 30
print(b) # (10 , 20 , 30)
print(b * 2) # (10 , 20 , 30, 10 , 20 , 30)
c = 40 , 50 , 60,
print(c) # (40 , 50 , 60)
print(type(c)) # <class ‘tuple’>



Outputs Homework #2

a = (25) # it is int object 25 because comma is mandatory in a tuple
b = 25, # it is a tuple because ‘()’ is not mandatory for a tuple but ‘,’ is mandatory
c = 25 # it is int object 25 because comma is mandatory in a tuple
d = (25,) # it is a tuple because ‘()’ is not mandatory for a tuple but ‘,’ is mandatory
print(type(a)) # <class ‘int’>
print(type(b)) # <class ‘tuple’>
print(type(c)) # <class ‘int’>
print(type(d)) # <class ‘tuple’>
print(a * 4) # 75
print(b * 4) # (25 , 25 , 25)
print(c * 4) # 75
print(d * 4) # (25 , 25 , 25)



tuple() Function Homework

a = tuple('Hyd')
print(a) # (‘H’ , ‘y’ , ‘d’)
print(type(a)) # <class ‘tuple’>
print(len(a)) # 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10 , 20 , 15 , 18)
print(tuple(range(5))) # (0 , 1 , 2 , 3, 4)
print(tuple(25)) # error because int is not iterable



Outputs Homework #3

a = ()
print(type(a)) # <class ‘tuple’>
print(a) # ()
print(len(a)) # 0
b = tuple() 
print(b) # ()
print(len(b)) # 0



Tricky Program Homework #4

a = (10 , 20 , 30)
print(a) # (10 , 20 , 30)
print(id(a)) # address of the tuple object a
a = a * 2  #  Valid / Invalid # valid
print(a) # (10 , 20 , 30 , 10 , 20 , 30)
print(id(a)) # address of the new tuple object a
