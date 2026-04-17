Meghana Gangalapudi



#  Find  outputs  (Home  work)

a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)                     #(25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25)
print(*a)                    #25 10.8 Hyd True (3+4j) None Hyd 25   (Unpacks the tuple)
print(type(a))               #<class 'tuple'>
print(len(a))                #8
print(a[2 : 5])              #('Hyd', True, (3+4j))
print(*a[2 : 5])             #Hyd True (3+4j)
a[2] = 'Sec'                 # Error -  because tuples are immutable.
a . append('Sec')            # Error -  because tuple has no attribute append() as tuple or it is immutable.
a . remove('Hyd')            # Error -  because tuple has no attribute remove() as tuple or it is immutable.
b =  10 , 20 , 30
print(b)                     #(10, 20, 30)
print(b * 2)                 #(10, 20, 30, 10, 20, 30)
c = 40 , 50 , 60,
print(c)                     #(40, 50, 60)
print(type(c))               #<class 'tuple'>




#Find  outputs  (Home  work)

a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))               #<class 'int'>
print(type(b))               #<class 'tuple'>
print(type(c))               #<class 'int'>
print(type(d))               #<class 'tuple'>
print(a * 4)                 #100
print(b * 4)                 #(25, 25, 25, 25)
print(c * 4)                 #100
print(d * 4)                 #(25, 25, 25, 25)


# tuple()  function  demo  program  (Home  work)

a = tuple('Hyd')
print(a)#('H', 'y', 'd')
print(type(a))               #<class 'tuple'>
print(len(a))                #3
b = [10 , 20 , 15 , 18]
print(tuple(b))              #(10, 20, 15, 18)
print(tuple(range(5)))       #(0, 1, 2, 3, 4)
print(tuple(25))             #Error - because 'int' object is not iterable.



# Find  outputs (Home  work)

a = ()
print(type(a))               #<class 'tuple'>
print(a)                     #()
print(len(a))                #0
b = tuple()
print(b)                     #()
print(len(b))                #0



# Tricky program
# Find  outputs (Home  work)

a = (10 , 20 , 30)
print(a)                     #(10, 20, 30)
print(id(a))                 #1234567899999
a = a * 2                    #  Valid / Invalid - Valid
print(a)                     #(10, 20, 30, 10, 20, 30)
print(id(a))                 #0987654321 ( different address ).








