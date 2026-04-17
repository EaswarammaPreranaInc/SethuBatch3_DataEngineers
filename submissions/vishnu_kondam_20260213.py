# Find  outputs    (Home  work)

a = range(10 , 50 , 5)
print(type(a))              # <class 'range'>   
print(a)                    # range(10, 50, 5) 
print(*a)                   # 10 15 20 25 30 35 40 45   unpacking prints elements
print(id(a))                # memory address or address of object a  
print(len(a))               # 8 

print(*a[2 : 7] , sep = ' , ')
# 20 , 25 , 30 , 35 , 40  slicing works on range

print(*a[ : : -1])          
# 45 40 35 30 25 20 15 10  reversed using negative step

a[4] = 32                   
# range object does not support item assignment range is immutable

print(a * 2)                
# range does not support multiplication because it doesn't support duplicates



#  Find  outputs  (Home  work)

a = range(10 , 20)
print(*a , sep = ',')  
# 10,11,12,13,14,15,16,17,18,19

b = range(5)
print(*b)                  
# 0 1 2 3 4

c = range(10 , 1 , -1)
print(*c , sep = '...')  
# 10...9...8...7...6...5...4...3...2

d = range(-10 , 0)
print(*d)                 
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

e = range(-10)
print(*e)                 
# (no output)  range(0,-10) empty

f = range(2 , 2)
print(*f)                 
# (no output)  start == stop empty

g = range(10 , 11 , 0.1)
# step must be integer

h = range('A' , 'F')
# arguments must be integers


#  Find  outputs  (Home  work)


r = range(10 , 17 , 3)     # 10 13 16
a , b , c = r              
print(a , b , c)           # 10 13 16

r = range(3)               # 0 1 2
x , y = r                  
# too many values to unpack (3 values)

p , q , r , s = r          
# not enough values (only 3)

a , b , c = *r             
# cannot unpack using *

m = r                      
print(id(r))               # same id
print(id(m))               # same id  both refer to same object



#  Find  outputs  (Home  work)


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)        # prints full list
print(*a)       # prints elements separated by space
print(type(a))  # <class 'list'>
print(id(a))    # memory address
print(len(a))   # 8 

a[2] = 'Sec'    
print(a)        # 'Hyd' replaced by 'Sec'
print(a[2 : 5]) # ['Sec', True, (3+4j)]


#  Find  outputs  (Home  work)


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)        # prints full list
print(*a)       # prints elements separated by space
print(type(a))  # <class 'list'>
print(id(a))    # memory address
print(len(a))   # 8 

a[2] = 'Sec'    
print(a)        # 'Hyd' replaced by 'Sec'
print(a[2 : 5]) # ['Sec', True, (3+4j)]


#  Find  outputs  (Home  work)


a = []
print(a)            # []

a.append(25)
a.append(10.8)
a.append('Hyd')
a.append(True)
print(a)            # [25, 10.8, 'Hyd', True]

a.remove('Hyd')
print(a)            # [25, 10.8, True]

a.remove('25')      
#'25' not found (string ≠ integer 25)


#  Find  outputs  (Home  work)


a = []
print(a)            # []

a.append(25)
a.append(10.8)
a.append('Hyd')
a.append(True)
print(a)            # [25, 10.8, 'Hyd', True]

a.remove('Hyd')
print(a)            # [25, 10.8, True]

a.remove('25')      
# '25' not found (string ≠ integer 25)



#  Find  outputs  (Home  work)


a = [25 , 10.8 , 'Hyd']
print(a)            # [25, 10.8, 'Hyd']
print(id(a))        # memory id

print(a * 3)        # list repeated 3 times [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2)        #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1)        #[25 , 10.8 , 'Hyd']
print(a * 0)        # []
print(a * -1)       # []

print(a * 4.0)      
#can't multiply list by float

a = a * 3
print(a)            # tripled list
print(id(a))        # new id (new object created)

a = [25]
print(a , id(a))    # [25] and new id

print(a * a)        
# list * list not allowed


#  Find  outputs  (Home  work)


a = list('Hyd')
print(a)        # ['H','y','d']
print(type(a))  # <class 'list'>
print(len(a))   # 3

b = (10 , 20 , 15 , 18)
print(list(b))  # converts tuple to list

print(list(range(5)))  # [0,1,2,3,4]

print(list(25))        
# 25 is not sequence i think these might gives an output ?



#  Find  outputs  (Home  work)

a = []
print(type(a))  # <class 'list'>
print(a)        # []
print(len(a))   # 0

b = list()
print(b)        # []
print(len(b))   # 0




#  Find  outputs  (Home  work)

list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']

print(list[2 : 7])     
# [(3+4j), 'Hyd', True, None, 10.8]

print(list[:])         
# full list [(3+4j), 'Hyd', True, None, 10.8]

print(list[ : : -1])   
# reversed list [10.8, NONE, True, 'Hyd', (3+4j)]

print(list[ : : 2])    
# [25, (3+4j), True, 10.8]

print(list[1 : : 2])   
# [10.8, 'Hyd', None, 'Hyd']

print(list[ : : -2])   
# ['Hyd', None, 'Hyd', 10.8]

print(list[-2 : : -2]) 
# [10.8, True, (3+4j), 25]

print(list[1 : 4])     
# [10.8, (3+4j), 'Hyd']

print(list[-4 : -1])   
# [True, None, 10.8]

print(list[3 : -3])    
# ['Hyd', True]

print(list[2 : -5])    
# [(3+4j)]

print(list[-1:-5]) 
    
# [] invalid direction (needs - step)





#  Find  outputs  (Home  work)


list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']

x , y = list[3 : 5]
print('x : ' , x)   # Hyd
print('y : ' , y)   # True

for x in list[2:7]:
    print(x)
# (3+4j)
# Hyd
# True
# None
# 10.8


#  Find  outputs  (Home  work)

a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))

a[1 : 4] = [60 , 70]
print(a , id(a))  
# [10, 60, 70, 50]  replaced 3 elements with 2

a[2: 4] = [100 , 200 , 300]
print(a , id(a))  
# [10, 60, 100, 200, 300]
# same id list modified in-place






#  Find  outputs  (Home  work)

a = [25]

print(a[1])   
# index out of range

print(a[1:])  
# []  slicing never gives error



















