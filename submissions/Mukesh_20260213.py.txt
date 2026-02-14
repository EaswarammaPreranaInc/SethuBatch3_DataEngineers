 #  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) #(25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) # 25 10.8 hyd True 3+4j none hyd 25
print(type(a)) <class 'Tuple'>
print(len(a)) # 8
print(a[2 : 5]) # ( Hyd , True , 3+4j)
print(*a[2 : 5]) # Hyd  True  3+4j
a[2] = 'Sec' # Error it is immutable
a . append('Sec')  # Error it is immutable
a . remove('Hyd') # Error it is immutable
b =  10 , 20 , 30
print(b)  #10 , 20 , 30
print(b * 2) # 10 , 20 , 30 , 10 , 20 , 30
c = 40 , 50 , 60,
print(c) 40 , 50 , 60,
print(type(c)) <class 'Tuple'>

 # Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) # <class 'Tuple'>
print(type(b)) # <class 'Tuple'>
print(type(c))# <class 'int'>
print(type(d)) # <class 'Tuple'>
print(a * 4)  # (25,25,25,25)
print(b * 4)  # (25,25,25,25,)
print(c * 4) # 100
print(d * 4)  # (25,25,25,25)

 # tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) #('H','y','d')
print(type(a)) # <Class 'Tuple'>
print(len(a)) #2 
b = [10 , 20 , 15 , 18]
print(tuple(b)) #(10,20,15,18)
print(tuple(range(5))) # (0,1,2,3,4)
print(tuple(25)) # int is not non sequenes

 # Find  outputs (Home  work)
a = ()
print(type(a)) #<Class 'Tuple'>
print(a) 
print(len(a)) #()
b = tuple()
print(b) # ()
print(len(b)) #0


 # Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) #(10,20,30)
print(id(a)) #Addres of object 3 elements
a = a * 2  #  Valid 
print(a) # 10,20,30,10,20,30
print(id(a)) Addres of object of 6 elemts