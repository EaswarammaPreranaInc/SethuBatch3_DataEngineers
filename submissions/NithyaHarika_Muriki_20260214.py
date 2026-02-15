#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) #OUTPUT:(25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) #OUTPUT:25  10.8  'Hyd'  True  3+4j  None  'Hyd'  25
print(type(a)) #OUTPUT:<class 'tuple'>
print(len(a)) #OUTPUT:8
print(a[2 : 5]) #OUTPUT:('Hyd' , True , 3+4j)
print(*a[2 : 5]) #OUTPUT: Hyd  True  3+4j
a[2] = 'Sec'
a . append('Sec')  #OUTPUT:Error, tuple neither growable nor shrinkable
a . remove('Hyd')  #OUTPUT:Error, tuple neither growable nor shrinkable
b =  10 , 20 , 30
print(b)#OUTPUT:(10 , 20 , 30)
print(b * 2)#OUTPUT:Error, tuple does not contain duplicate values
c = 40 , 50 , 60,
print(c)#OUTPUT:(40 , 50 , 60,)
print(type(c))#OUTPUT:<class 'tuple'>


# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))#OUTPUT:<class 'int'>
print(type(b))#OUTPUT:<class 'tuple'>
print(type(c))#OUTPUT:<class 'int'>
print(type(d))#OUTPUT:<class 'tuple'>
print(a * 4)#OUTPUT:#OUTPUT:100
print(b * 4)#OUTPUT:#OUTPUT:Error, tuple does not contain duplicate values
print(c * 4)#OUTPUT:#OUTPUT:100
print(d * 4)#OUTPUT:#OUTPUT:Error, tuple does not contain duplicate values



# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)#OUTPUT:('H' , 'y', 'd')
print(type(a))#OUTPUT:<class 'tuple'>
print(len(a))#OUTPUT:3
b = [10 , 20 , 15 , 18]
print(tuple(b))#OUTPUT:(10 , 20 , 15 , 18)
print(tuple(range(5)))#OUTPUT:(0,1,2,3,4)
print(tuple(25))#OUTPUT:error, int object is not iterable



# Find  outputs (Home  work)
a = ()
print(type(a))#OUTPUT:()
print(a)#OUTPUT:
print(len(a))#OUTPUT:0
b = tuple()
print(b)#OUTPUT:()
print(len(b))#OUTPUT:0



# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)#OUTPUT:
print(id(a))#OUTPUT:
a = a * 2  #  Valid / Invalid
print(a)#OUTPUT:
print(id(a))#OUTPUT: