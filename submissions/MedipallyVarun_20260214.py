# Name : Medipally Varun 


#  Find  outputs  (Home  work)
a =(25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) # (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) # 25 10.8  'Hyd' True 3+4j None 'Hyd' 25
print(type(a)) # class 'tuple'
print(len(a)) # 8
print(a[2 : 5]) # ('Hyd' , True , 3+4j)
print(*a[2 : 5])# 'Hyd' , True , 3+4j
a[2] = 'Sec' # Error tuple is immutable 
a . append('Sec') # Error tuple is immutable
a . remove('Hyd')# Error tuple is immutable
b =  10 , 20 , 30
print(b) # (10, 20 ,30)
print(b * 2) # (10, 20 ,30 , 10, 20 ,30)
c = 40 , 50 , 60,
print(c) # (40,50,60)
print(type(c)) # class'tuple'





# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) # class'tuple'
print(type(b)) # class'tuple' 
print(type(c)) # class'int'
print(type(d)) # class 'tuple'
print(a * 4) # 100
print(b * 4) # 100
print(c * 4)# 100
print(d * 4)# 100



# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) # tuple('Hyd')
print(type(a)) # class 'tuple'
print(len(a)) # 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) # b(10,20,15,18)
print(tuple(range(5))) # Error 
print(tuple(25)) # Error 


# Find  outputs (Home  work)
a = ()
print(type(a)) # class 'tuple'
print(a) # ()
print(len(a)) # emplty
b = tuple()
print(b) # tuple()
print(len(b)) # empty 





# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # (10,20,30)
print(id(a)) # Address of the a
a = a * 2  #  Valid 
print(a) # (10 , 20 , 30, 10 , 20 , 30)
print(id(a)) # same address 