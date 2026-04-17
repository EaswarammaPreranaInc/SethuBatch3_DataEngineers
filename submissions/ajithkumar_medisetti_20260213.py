# Find  outputs (Home  work)
a = range(10 , 50 , 5)
print(type(a))  # < class 'range'>
print(a) # range(10, 50, 5)
print(*a) # 10 15 20 25 30 35 40 45 
print(id(a)) # Address of the object a
print(len(a)) # 8
print(*a[2 : 7] , sep = ' , ') # 20 , 25 , 30 , 35 , 40 
print(*a[ : : -1]) # ( )
a[4] = 32 # Syntax Error Beacause Are Immutable 
print(a * 2) # Syntax Error



#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5) 
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0
f = range(2 , 2)
print(*f) # Empty 
g = range(10 , 11 , 0.1) # Syntax Error Because Float Objects can not Interpreted As An Integer
h = range('A' , 'F') # Syntax Error Because Range Objects Are Only  Integers Can Hold String Objects 


#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) # 10 13 16
r = range(3)   # 0 1 2
x , y = r   # Syntax Error
p , q  , r , s = r # Syntax Error
a , b , c = *r  # Syntax Error
m = r 
print(id(r)) # Memory Address Of Range Objects 
print(id(m)) # Same Memory  Address 



#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25  10.8  'Hyd'  True  3 + 4j  None  'Hyd'  25
print(type(a)) # <Class'list'>
print(id(a)) # Adress Of the Object a
print(len(a)) # 8
a[2] = 'Sec'
print(a) # [25, 10.8, 'Sec', True, (3+4j)] 
print(a[2 : 5]) # ['Sec', True, (3+4j)]



# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # []
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) # [25 10.8 'Hyd' True]
a . remove('Hyd')
print(a) # [25 10.8 True]
a . remove('25')
print(a) # [10.8 True]




#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # [25, 10.8, 'Hyd']
print(id(a)) # Address Of Object a 
print(a * 3) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1) # [25, 10.8, 'Hyd']
print(a * 0) # []
print(a * -1) #[]
print(a * 4.0) #Syntax Error
a = a * 3
print(a) # [75, 30.4, 'HydHydHyd']
print(id(a)) # Address Of The Object A
a = [25]
print(a , id(a)) #[25] Address Of a
print(a * a) # Syntax Error Because It Can Not Multiply



# list()  function  demo  program
a = list('Hyd')
print(a) # ['H', 'y', 'd']
print(type(a)) # <class 'list'>
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10, 20, 15, 18]
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(25)) # Syntax Error Because Int object Is Not iterable




# Find  outputs
a = [ ]
print(type(a)) # <class 'list'>
print(a) # []
print(len(a)) # 0
b = list()
print(b) # []
print(len(b)) # 0




# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ]) # [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:])# [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : -1]) #['Hyd']
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # [10.8]
print(list[ : : -2]) # ['Hyd', True, None]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) # [True, None, 10.8]
print(list[3 : -3]) # ['Hyd', True, None]
print(list[2 : -5]) # ['Hyd']
print(list[-1:-5]) # []




#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) # x : Hyd
print('y : ' , y) # y : True
for  x  in  list[2:7]:
	print(x)  # (3+4j)
                  # Hyd
                  # True
                  # None
                  # 10.8
                


#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10, 20, 30, 40, 50] Address Of The Object a For Ex: 10000
a[1 : 4] = [60 , 70]
print(a , id(a)) # [10, 60, 70, 50] Address Of the Object a For Ex 10000
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [10, 60, 100, 200, 300, 50] Address Of The Object a




#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # Syntax Error Because There Is no Any Index Of a[1]
print(a[1:]) # Syntax Error Because There Is No Any Range Object 







