
# Find  outputs    (Home  work)

a = range(10, 50, 5)
print(type(a)) # <class 'range'>
print(a) # range(10, 50, 5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # 6000
print(len(a)) # 8 
print(*a[2 : 7] , sep = ' , ') # 20, 25, 30, 35, 40
print(*a[ : : -1]) # 45 40 35 30 25 20 15 10
#a[4] = 32 # Error range object is immutable hence cannot change values
#print(a * 2) # Error because range object does not support multiplication


#  Find  outputs  (Home  work)

a = range(10, 20)
print(*a , sep = ',') # 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
b = range(5) 
print(*b) # 0 1 2 3 4
c = range(10, 1, -1)
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2
d = range(-10, 0)
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
e = range(-10)
print(*e) # '' 
f = range(2, 2)
print(*f) # ''
#g = range(10, 11, 0.1) # Error because step value must be integer (0.1 is float)
#h = range('A', 'F') # Error because range() works only with integers (not strings)



#  Find  outputs  (Home  work)

r = range(10, 17, 3) 
a, b, c = r  
print(a, b, c) # 10, 13, 16
r = range(3)   
#x, y = r # Error because range(3) gives 3 values (0,1,2) but only 2 variables given
#p, q, r, s = r # Error because range(3) gives 3 values but 4 variables given
#a, b, c = *r # Error because * unpacking cannot be used alone on right side like this (invalid syntax)
m = r  
print(id(r)) # 7000
print(id(m)) # 7000


#  Find  outputs  (Home  Work)

a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Hyd', 25]
print(a) # [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Hyd', 25]
print(*a) # 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a)) # <class 'list'>
print(id(a)) # 3000 address of 'a' 
print(len(a)) # 8
a[2] = 'Sec'
print(a) # [25, 10.8, 'Sec', True, 3 + 4j, None, 'Hyd', 25]
print(a[2 : 5]) # ['Sec', True, 3 + 4j]


# append()  and  remove()  methods  (Home  work)

a = [ ]
print(a) # []
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) # [25, 10.8, 'Hyd', True]
a . remove('Hyd')
print(a) # [25, 10.8, True]
a . remove('25')
#print(a) # Error because '25' (string) is not in the list



#  Find  outputs  (Home  work)

a = [25, 10.8, 'Hyd']
print(a) # [25, 10.8, 'Hyd']
print(id(a)) # 8000
print(a * 3) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1) # [25, 10.8, 'Hyd']
print(a * 0) # []
print(a * -1) # []
#print(a * 4.0) # Error because list can multiply only with integer (4.0 is float)
a = a * 3
print(a) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a)) # 9000
a = [25]
print(a , id(a)) # [25] 8000
#print(a * a) # Error because list cannot multiply with another list (only integer allowed)



# list()  function  demo  program

a = list('Hyd')
print(a) # ['H', 'y', 'd']
print(type(a)) # <class 'list'>
print(len(a)) # 3
b = (10, 20, 15, 18)
print(list(b)) # [10, 20, 15, 18]
print(list(range(5))) # [0, 1, 2, 3, 4]
#print(list(25)) # Error because 'int' object is not iterable



# Find  outputs

a = [ ]
print(type(a)) # <class 'list'>
print(a) # [ ]
print(len(a)) # 0
b = list()
print(b) # [ ]
print(len(b)) # 0



# Slice  demo  program (Home  work)

#       0     1     2       3     4      5     6     7
#list =  [25, 10.8, 3 + 4j, 'Hyd', True, None, 10.8, 'Hyd']
#      -8    -7    -6      -5    -4     -3    -2    -1

print(list[2 : 7]) # [3+4j, 'Hyd', True, None, 10.8]
print(list[ : : ]) # [25, 10.8, 3 + 4j, 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) # [25, 10.8, 3 + 4j, 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : -1]) # ['Hyd', 10.8, None, True, 'Hyd', 3+4j, 10.8, 25]
print(list[ : : 2]) # [25, 3+4j, True, 10.8]
print(list[1 : : 2]) # [ 10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) # ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2]) # [10.8, True, 3+4j, 25]
print(list[1 : 4]) # [10.8, 3 + 4j, 'Hyd']
print(list[-4 : -1]) # [True, None, 10.8]
print(list[3 : -3]) # ['Hyd', True]
print(list[2 : -5]) # [3+4j]
print(list[-1:-5]) # []


#  Find  outputs  (Home  work)

#        0   1     2      3      4     5     6     7
#list = [25, 10.8, 3+4j, 'Hyd', True, None, 10.8, 'Hyd']

x ,  y = list[3 : 5] # ['Hyd', True]
print('x : ', x) # x : Hyd
print('y : ', y) # y : True
for  x  in  list[2:7]: # [3+4j, 'Hyd', True, None, 10.8]
	print(x) # 3+4j     (for loop )
                 # 'Hyd'
                 # True 
                 # None
                 # 10.8



#  Find  outputs  (Home  work)

#     0  1    2   3   4
a = [10, 20, 30, 40, 50]

print(a , id(a)) # [10, 20, 30, 40, 50] 3000
a[1 : 4] = [60, 70] 
print(a , id(a)) # [10, 60, 70, 50] 3000
a[2: 4] =   # [100, 200, 300]
print(a , id(a))   #[10, 60, 100, 200, 300] 3000



#Find  outputs  (Home  work)

a =  [25]
#print(a[1]) # Error because index 1 does not exist in the list (list has only one element at index 0) 
print(a[1:]) # []




