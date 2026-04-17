# Find outputs (Home work)
a = range(10 , 50 , 5)
print(type(a)) 				# <class 'range'>
print(a) 				# range(10, 50, 5)
print(*a) 				# 10 15 20 25 30 35 40 45
print(id(a)) 				# some integer (memory address)
print(len(a)) 				# 8
print(*a[2 : 7] , sep = ' , ') 		# 20 , 25 , 30 , 35 , 40
print(*a[ : : -1]) 			# 45 40 35 30 25 20 15 10
a[4] = 32 				# error
print(a * 2) 				# error

# Find outputs (Home work)
a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) # (no output)
f = range(2 , 2)
print(*f) # (no output)
g = range(10 , 11 , 0.1) # TypeError: 'float' object cannot be interpreted as an integeh = range('A' , 'F') # TypeError: 'str' object cannot be interpreted as an integer

# Find outputs (Home work)
r = range(10 , 17 , 3) # 10,13,16
a , b , c = r
print(a , b , c) # 10 13 16
r = range(3) # 0,1,2
x , y = r # ValueError: too many values to unpack
p , q , r , s = r # ValueError
a , b , c = *r # SyntaxError
m = r
print(id(r)) # some integer
print(id(m)) # same integer

# Find outputs (Home Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a) # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a)) # <class 'list'>
print(id(a)) # some integer
print(len(a)) # 8
a[2] = 'Sec'
print(a) # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5]) # ['Sec', True, (3+4j)]

# append() and remove()
a = [ ]
print(a) # []
a.append(25)
a.append(10.8)
a.append('Hyd')
a.append(True)
print(a) # [25, 10.8, 'Hyd', True]
a.remove('Hyd')
print(a) # [25, 10.8, True]
a.remove('25') # ValueError: list.remove(x): x not in list

# Find outputs
a = [25 , 10.8 , 'Hyd']
print(a) # [25, 10.8, 'Hyd']
print(id(a)) # some integer
print(a * 3) # [25,10.8,'Hyd',25,10.8,'Hyd',25,10.8,'Hyd']
print(a * 2) # repeated twice
print(a * 1) # same list
print(a * 0) # []
print(a * -1) # []
print(a * 4.0) # TypeError
a = a * 3
print(a) # repeated 3 times
print(id(a)) # new integer
a = [25]
print(a , id(a)) # [25] some integer
print(a * a) # TypeError

# list() demo
a = list('Hyd')
print(a) # ['H','y','d']
print(type(a)) # <class 'list'>
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10,20,15,18]
print(list(range(5))) # [0,1,2,3,4]
print(list(25)) # TypeError

# Empty list
a = [ ]
print(type(a)) # <class 'list'>
print(a) # []
print(len(a)) # 0
b = list()
print(b) # []
print(len(b)) # 0

# Slicing outputs (major ones)

print(list[2 : 7]) # [(3+4j),'Hyd',True,None,10.8]
print(list[ : : ]) # full list
print(list[ : : -1]) # reversed list
print(list[ : : 2]) # [25,3+4j,True,10.8]
print(list[1 : : 2]) # [10.8,'Hyd',None,'Hyd']
print(list[ : : -2]) # ['Hyd',None,'Hyd',10.8]
print(list[-2 : : -2]) # [10.8,True,(3+4j),25]
print(list[1 : 4]) # [10.8,3+4j,'Hyd']
print(list[-4 : -1]) # [True,None,10.8]
print(list[3 : -3]) # ['Hyd',True]
print(list[2 : -5]) # [3+4j]
print(list[-1:-5]) # []

# More outputs
x , y = list[3 : 5]
print('x : ' , x) # x : Hyd
print('y : ' , y) # y : True
for x in list[2:7]:
 print(x) # (3+4j) Hyd True None 10.8
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # original id
a[1 : 4] = [60 , 70]
print(a , id(a)) # [10,60,70,50] same id
a[2: 4] = [100 , 200 , 300]
print(a , id(a)) # [10,60,100,200,300] same id
a = [25]
print(a[1]) # IndexError
print(a[1:]) # []