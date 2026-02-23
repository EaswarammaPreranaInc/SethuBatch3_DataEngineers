# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a)) # class range
print(a) # range(10,50,5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # address of range object
print(len(a)) # 8
print(*a[2 : 7] , sep = ' , ') # 20,25,30,35,40
print(*a[ : : -1]) # 45 40 35 30 25 20 15 10 
a[4] = 32 # Error range cannot be modified
print(a * 2) # Error range cannot be duplicated
#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) # 0,1,2,3,4
c = range(10 , 1 , -1)
print(*c , sep = '...') #10…9…8..7…5…5…4…3…2
d = range(-10 , 0) 
print(*d) # -10,-9.-8,-7,-6,-5,-4,-3,-2,-1
e = range(-10) # Error default starts from 0
print(*e) # () # Error
f = range(2 , 2)
print(*f) # ()
g = range(10 , 11 , 0.1) # Error step should be in int
h = range('A' , 'F') # Error numbers should only perform the range function
#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c)  # 10,13,16
r = range(3)   
x , y = r   
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r)) # Error 
print(id(m)) # Error
#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25  10.8  'Hyd'  True  3 + 4j  None  'Hyd'  25
print(type(a)) # class list
print(id(a)) # Address of the list object
print(len(a)) # 8
a[2] = 'Sec'
print(a) #  [25 , 10.8 ,’Sec’ , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) # [Sec,True,3+4j]
# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # []
a . append(25) # [25]
a . append(10.8) # [25, 10.8
a . append('Hyd') # [25, 10.8, 'Hyd']
a . append(True) # [25, 10.8, 'Hyd', True]
print(a) # [25,10.8,’Hyd’,True]
a . remove('Hyd') # [25, 10.8 ,True]
print(a) # [25,10.8,True]
a . remove('25') # Errror str 25 is not in list
print(a) # [25,10.8,True]
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # [25 , 10.8 , 'Hyd']
print(id(a)) # Address of the list object
print(a * 3) # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2) # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1) # [25 , 10.8 , 'Hyd']
print(a * 0) # []
print(a * -1) # []
print(a * 4.0) # Error cannot 
a = a * 3
print(a) # Error value is not assigned to a
print(id(a)) # Error 
a = [25]
print(a , id(a)) # [25],Address of the list
print(a * a) # Error value not defined
# list()  function  demo  program
a = list('Hyd')
print(a) # [‘H’,’Y’,’d’]
print(type(a)) # Address of the list should be stored
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10,20,15,18]
print(list(range(5)))  # [0,1,2,3,4]
print(list(25)) # [25]

# Find  outputs
a = [ ]
print(type(a)) # class list
print(a) # []
print(len(a)) # 0
b = list()
print(b) #[]
print(len(b)) #0
# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # [3+4j,’Hyd’,True,None,10.8]
print(list[ : : ]) # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # [‘Hyd’ ,10.8 ,None ,True ,’Hyd’, 3+4j ,10.8, 25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # [10.8 , ’Hyd’, None , ‘Hyd’]
print(list[ : : -2]) # [‘Hyd’ ,None, ’Hyd , 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # [10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1]) # [True , None , 10.8]
print(list[3 : -3]) # [‘Hyd’ , True]
print(list[2 : -5]) # [3+4j]
print(list[-1:-5]) # []
#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) # ['Hyd' ]
print('y : ' , y) # [ True]
for  x  in  list[2:7]:
	print(x) # (3+4j) <next line> Hyd <next line> True  <ne 10.8xt line> None <next line>

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10,20,30,40,50] , Address of the list object
a[1 : 4] = [60 , 70]
print(a , id(a)) # [10,60,70,50] , Address of the same list object with modified elements
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [10 , 60 , 100 ,200, 300] , Address of the same list object with modified elements
#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # Error inddex out of the range
print(a[1:]) # []
