
# Find  outputs    
a = range(10 , 50 , 5) 
print(type(a)) # <class 'range'>
print(a) # range(10, 50, 5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # 2041299564272
print(len(a)) # 8
print(*a[2 : 7] , sep = ' , ') # 20 , 25 , 30 , 35 , 40
print(*a[ : : -1]) # 45 40 35 30 25 20 15 10
a[4] = 32 # 'range' object does not support item assignment
print(a * 2) # unsupported operand type(s) for *: 'range' and 'int'
#  Find  outputs  
a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)  
print(*e) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
f = range(2 , 2)
print(*f) # 
g = range(10 , 11 , 0.1) # 'float' object cannot be interpreted as an integer
h = range('A' , 'F') # 'str' object cannot be interpreted as an integer 
#  Find  outputs  
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) # 10 13 16
r = range(3)   
x , y = r   # too many values to unpack (expected 2)
p , q  , r , s = r  # not enough values to unpack (expected 4, got 3)
a , b , c = *r  # can't use starred expression here
m = r  
print(id(r)) # 2546763331168
print(id(m)) # 2546763331168
#  Find  outputs  
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a) # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a)) #  <class 'list'>
print(id(a)) # 2758975754816
print(len(a)) # 8
a[2] = 'Sec' 
print(a) # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5]) #  ['Sec', True, (3+4j)]
# append()  and  remove()  methods  
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
print(a) # list.remove(x): x not in list
#  Find  outputs  
a = [25 , 10.8 , 'Hyd']
print(a) # [25, 10.8, 'Hyd']
print(id(a)) # 2371834614336
print(a * 3) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1) # [25, 10.8, 'Hyd']
print(a * 0) # []
print(a * -1) # []
print(a * 4.0) # can't multiply sequence by non-int of type 'float'
a = a * 3
print(a) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a)) # 1435081961024
a = [25]
print(a , id(a)) # [25] 1435038650944
print(a * a) # can't multiply sequence by non-int of type 'list'
# list()  function  demo  program
a = list('Hyd') 
print(a) # ['H', 'y', 'd']
print(type(a)) # <class 'list'>
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10, 20, 15, 18]
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(25)) #  'int' object is not iterable
# Find  outputs
a = [ ]
print(type(a)) # <class 'list'>
print(a) # []
print(len(a)) # 0
b = list()
print(b) # []
print(len(b)) # 0
#  Find  outputs  
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10, 20, 30, 40, 50] 2034612572736
a[1 : 4] = [60 , 70]
print(a , id(a)) [10, 60, 70, 50] 2034612572736
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [10, 60, 100, 200, 300] 2034612572736
#  Find  outputs  
a =  [25]
print(a[1]) # list index out of range
print(a[1:]) # []




