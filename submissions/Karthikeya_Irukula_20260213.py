#4.Python H/W (Karthikeya Irukula)

# Find outputs (Home work)
a = range(10 , 50 , 5)
print(type(a)) #<class 'range'>
print(a) #range(10,50,5)
print(*a)#10 15 20 25 30 35 40 45 * indicates unpacked.
print(id(a)) #address of range(10,50,5) object.
print(len(a)) #8
print(*a[2 : 7] , sep = ' , ') # 20, 25, 30, 35, 40
print(*a[ : : -1]) #reverse 45 40 35 30 25 20 15 10
a[4] = 32 #Error object cannot be modified.
print(a * 2) # Error range function cannot be multiplied/modified becoz range obj is immutable and it also cannot be repeated.

# Find outputs (Home work)
a = range(10 , 20)
print(*a , sep = ',') #10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') #10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) #Empty object due to data (0,-10,1) becoz always beginner >= end.
f = range(2 , 2)
print(*f) #Empty due to both are at same point.
g = range(10 , 11 , 0.1) # Error range does not supports float value
h = range('A' , 'F') #Error due to range does not support string values

# Find outputs (Home work)
r = range(10 , 17 , 3)
a , b , c = r
print(a , b , c) #10, 13, 16
r = range(3) #0 1 2
x , y = r #Error due to assign of too many values.
p , q , r , s = r #Error due to assign of too many objects on left side.
a , b , c = *r #Error due to * cannot be used to assign. Becoz it's automatically unpacked.
m = r
print(id(r)) #address of range object
print(id(m)) #address of range(3) same address.

# Find outputs (Home Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25 10.8 Hyd True 3 + 4j None Hyd 25
print(type(a))# <class 'list'>
print(id(a)) #Address of object a or list
print(len(a)) #8
a[2] = 'Sec'
print(a) # [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) #'Sec' ,True ,3+4j

# append() and remove() methods (Home work)
a = [ ]
print(a) #
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) #[ 25, 10.8, 'Hyd', True]
a . remove('Hyd')
print(a) #[ 25, 10.8, True]
a . remove('25') #Error
print(a) #[ 25, 10.8, True]

# Find outputs (Home work)
a = [25 , 10.8 , 'Hyd']
print(a) #[25 , 10.8 , 'Hyd']
print(id(a)) #address of list a
print(a * 3) #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2) #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1) #[25 , 10.8 , 'Hyd']
print(a * 0) #
print(a * -1) #
print(a * 4.0) #Error due to float value
a = a * 3
print(a) #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a)) #address of a*3
a = [25]
print(a , id(a)) # [25] address of 25
print(a * a) # Error list and list multiplication cannot be done.
# list() function demo program
a = list('Hyd')
print(a) #['H', 'y', 'd']
print(type(a)) #<class 'list'>
print(len(a)) #3
b = (10 , 20 , 15 , 18)
print(list(b)) #[10, 20, 15, 18]
print(list(range(5))) #[0,1,2,3,4]
print(list(25)) #Error

# Find outputs
a = [ ]
print(type(a)) #<class 'list'>
print(a) #
print(len(a)) #0
b = list()
print(b)#
print(len(b))#0

# Slice demo program (Home work)
# 0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
# -8 -7 -6 -5 -4 -3 -2 -1
print(list[2 : 7]) #[3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : ])# [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2]) # list[0 : 8 : 2] ---> List from indexes 0 to 7 in steps of 2 i.e. [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) #[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2]) # list[-2 : -9 : -2] ---> List from indexes -2 to -8 in steps of -2 i.e. [10.8 , True , 3+4j , 25]
print(list[1 : 4]) #[10.8, (3+4j), 'Hyd']
print(list[-4 : -1])#[True, None, 10.8]
print(list[3 : -3]) #['Hyd', True]
print(list[2 : -5]) #[(3+4j)]
print(list[-1:-5]) #Empty

# Find outputs (Home work)
# 0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x , y = list[3 : 5]
print('x : ' , x) #x: 'Hyd'
print('y : ' , y) #y: None
for x in list[2:7]:
print(x) #3+4j
Hyd
True
None
10.8

# Find outputs (Home work)
# 0 1 2 3 4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #[10 , 20 , 30 , 40 , 50] , address of object a
a[1 : 4] = [60 , 70]
print(a , id(a)) #[10 , 60, 70, 50] , address of object a contains
a[2: 4] = [100 , 200 , 300]
print(a , id(a)) #[10, 60, 100, 200, 300]

# Find outputs (Home work)
a = [25]
print(a[1]) #Error due to no value in index given
print(a[1:]) #