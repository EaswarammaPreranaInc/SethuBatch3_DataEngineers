#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)   #  (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a)  # (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(type(a))  # Class Tuple
print(len(a))   # 8
print(a[2 : 5])  # ('Hyd', True, 3+4j)
print(*a[2 : 5]) # ('Hyd', True, 3+4j)
a[2] = 'Sec'    # Error
a . append('Sec') # Error
a . remove('Hyd')  # # Error
b =  10 , 20 , 30
print(b)  #  (10 , 20 , 30)
print(b * 2) # Error
c = 40 , 50 , 60, 
print(c)  #  (40 , 50 , 60)
print(type(c))  # Class Tuple







# Find  outputs  (Home  work)
a = (25) 
b = 25,
c = 25
d = (25,)
print(type(a))  # Class Int 
print(type(b))   # class Tuple
print(type(c))   # Class Int
print(type(d))  # Class Tuple
print(a * 4)  # Error
print(b * 4)  # Error
print(c * 4)  # Error
print(d * 4)   # Error



# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)  # ('Hyd')
print(type(a))  # Class List
print(len(a))  # 1
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10 , 20 , 15 , 18)
print(tuple(range(5)))   # (10 , 20 , 15 , 18)
print(tuple(25))  (5,)





# Find  outputs (Home  work)
a = ()
print(type(a)) # Error
print(a)   # ()  
print(len(a))  # 0
b = tuple() 
print(b)  #  ()
print(len(b))  #0



# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)  # (10 , 20 , 30)
print(id(a))  # Address of the object tuple
a = a * 2  #  Valid / Invalid  # Invalid
print(a)  # Error
print(id(a))  # Address of the object tuple