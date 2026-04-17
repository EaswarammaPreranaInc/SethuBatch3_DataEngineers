# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a)) # <class 'Range'>
print(a) # (10, 50, 5) 
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # Address of the object (10, 50, 5)
print(len(a)) # 8
print(*a[2 : 7] , sep = ' , ') # 20, 25, 30, 35, 40
print(*a[ : : -1]) # 45, 40, 35, 30, 25, 20, 15, 10
a[4] = 32 # Error due to range cannot be modified
print(a * 2) # Error due to range does not support multiplication

#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
b = range(5)
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) # -10, -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) # Empty
f = range(2 , 2)
print(*f) # Empty
g = range(10 , 11 , 0.1) # Error due to can't hold float objects
h = range('A' , 'F') # Error due to invalid range objects

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c)  # (10, 13, 16)
r = range(3)   
x , y = r   
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r)) # Address of object r
print(id(m)) # Address of object m

#  Find  outputs  (Home  Work)
a = [25 , 10.8, 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25, 10.8, 'Hyd', True, 3+4j, None, 'Hyd', 25]
print(*a) 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a)) #<class 'List'>
print(id(a)) # Address of the object 'a'
print(len(a)) # 8
a[2] = 'Sec'
print(a) # [25 , 10.8, 'Sec', True, 3 + 4j, None, 'Hyd', 25]
print(a[2 : 5]) ['Sec', True, 3+4j]

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # []
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) #[25, 10.8, 'Hyd', True]
a . remove('Hyd')
print(a) # [25, 10.8, True] 
a . remove('25')
print(a) # Error due to invalid List object

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) #[25, 10.8, 'Hyd']
print(id(a)) # Address of the object 'a'
print(a * 3) # [25 , 10.8, 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2) # [25 , 10.8, 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1) # [25 , 10.8, 'Hyd']
print(a * 0) # [] 
print(a * -1) # []
print(a * 4.0) # Error due to float object can't be multiply
a = a * 3
print(a) # [25 , 10.8, 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a)) # Address of the object 'a'
a = [25] 
print(a , id(a)) # [25] Address of the object 'a'
print(a * a) # Error due to can't multiply sequence

# list()  function  demo  program
a = list('Hyd')
print(a) # ['H', 'y', 'd']
print(type(a)) #<class 'List'>
print(len(a)) #<3>
b = (10 , 20 , 15 , 18)
print(list(b)) #[10, 20, 15, 18]
print(list(range(5))) # Error due to int object is not iterable 
print(list(25)) # Error due to int object is not iterable 


# Find  outputs
a = [ ]
print(type(a)) # < class 'List'>
print(a) #[]
print(len(a)) # 0
b = list()
print(b) # []
print(len(b)) # 0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # list [2 : 8 :1] ---> List  from  indexes  2  to  7  in steps  of  1  i.e.   [3 + 4j, 'Hyd' , True , None , 10.8]
print(list[ : : ]) # list[0 : 8 : 1]   --->  List  from  indexes  0  to  7  in steps  of  1  i.e.   [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) # list[0 : 8 : 1]   --->  List  from  indexes  0  to  7  in steps  of  1  i.e.   [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # list [0 : 8 : -1]  --->  List  from  indexes  0  to  7  in steps  of  1  i.e.   ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # list [1 : 8 : 2] ---> List  from  indexes  1  to  7  in steps  of  2  i.e.   [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) # list [0 : 8 : -2 ] --->  List  from  indexes  1  to  7  in steps  of  2  i.e. ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])  # list[1 : 4 : 1]   --->  List  from  indexes  1  to  5  in steps  of  1  i.e.   [10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1]) # list[-4 : -1 : 1]   --->  List  from  indexes  -4  to  -1  in steps  of  1  i.e. [True, None, 10.8]
print(list[3 : -3]) # list[3 : -3 : 1]   --->  List  from  indexes  3  to  -3  in steps  of  1  i.e. ['Hyd', True]
print(list[2 : -5])  # list[2 : -5 : 1]   --->  List  from  indexes  2  to  -5  in steps  of  1  i.e. [3+4j]
print(list[-1:-5]) # list[-1: -5 : 1]   --->  List  from  indexes  -1  to  -5  in steps  of  1  i.e. []


#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) # 'Hyd'
print('y : ' , y) #True
for  x  in  list[2:7]:
	print(x) # 3+4j 
                 #'Hyd' 
                 # True  
                 # None 
                 # 10.8    

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10, 20, 30, 40, 50] Address of the object 'a'
a[1 : 4] = [60 , 70]
print(a , id(a)) #[10, 60, 70, 50]  Address of the object 'a'
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [10, 60, 100, 200, 300]  Address of the object 'a'

#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # Error due to index is out of range
print(a[1:]) # []