#  Find  Outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) #Output: (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25) 
print(*a) #Output: 25 10.8 Hyd True 3+4j None 'Hyd' 25
print(type(a)) #Output: <class 'tuple'>
print(len(a)) #Output: 8
print(a[2 : 5]) #Output: ('Hyd' , True , (3+4j))
print(*a[2 : 5]) #Output: Hyd True 3+4j
a[2] = 'Sec' #Output: Error
a . append('Sec') #Output: Error
a . remove('Hyd') #Output: Error
b =  10 , 20 , 30
print(b) #Output:(10,20,30) 
print(b * 2) #Output:(10,20,30,10,20,30)
c = 40 , 50 , 60,
print(c) #Output: 40,50,60
print(type(c)) #Output: Address of an object
# Find  Outputs  (Home  work)
a = (25) 
b = 25,
c = 25
d = (25,)
print(type(a)) #Output: <class 'tuple'> 
print(type(b)) #Output: <class 'int'>
print(type(c)) #Output: <class 'int'>
print(type(d)) #Output: <class 'tuple'>
print(a * 4) #Output: 100
print(b * 4) #Output: (25,25,25,25)
print(c * 4) #Output: 100
print(d * 4) #Output: (25,25,25,25)
# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) #Output: ('H' 'y' 'd')
print(type(a)) #Output: <class 'tuple'>
print(len(a)) #Output: 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) #Output:(10, 20, 15, 18)
print(tuple(range(5))) #Output: (0, 1, 2, 3, 4)
print(tuple(25)) #Output: Error
# Find  Outputs (Home  work)
a = ()
print(type(a)) #Output:<class 'tuple'>
print(a) #Output:()
print(len(a)) #Output:0
b = tuple()
print(b) #Output:()
print(len(b)) #Output:0
# Tricky program
# Find  Outputs (Home  work)
a = (10 , 20 , 30)
print(a) #Output:(10,20,30)
print(id(a)) #Output:Address of an object
a = a * 2  #  Valid / Invalid
print(a) #Output:(10,20,30,10,20,30)
print(id(a)) #Output:Address of an object