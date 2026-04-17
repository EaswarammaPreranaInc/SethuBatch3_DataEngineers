***
a = range(10 , 50 , 5)


print(type(a)) # <class 'range'>
print(a) # range(10, 50, 5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # Some memory address (example: 6000)
print(len(a)) # 8


print(*a[2 : 7] , sep = ' , ') # 20 , 25 , 30 , 35 , 40
print(*a[ : : -1]) # 45 40 35 30 25 20 15 10


a[4] = 32 # Error (range object does not support item assignment)
print(a * 2) # Error (range cannot be multiplied)


***


a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19


b = range(5)
print(*b) # 0 1 2 3 4


c = range(10 , 1 , -1)
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2


d = range(-10 , 0)
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


e = range(-10)
print(*e) # 0 -1 -2 -3 -4 -5 -6 -7 -8 -9


f = range(2 , 2)
print(*f) # (Nothing – empty range)


g = range(10 , 11 , 0.1) # Error (step must be integer)
h = range('A' , 'F') # Error (arguments must be integers)


***


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]


print(a) # [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a) # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a)) # <class 'list'>
print(id(a)) # Some memory address
print(len(a)) # 8


a[2] = 'Sec'
print(a) # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5]) # ['Sec', True, (3+4j)]


***


a = []
print(a) # []


a.append(25)
a.append(10.8)
a.append('Hyd')
a.append(True)


print(a) # [25, 10.8, 'Hyd', True]


a.remove('Hyd')
print(a) # [25, 10.8, True]


a.remove('25') # Error (Value not found in list)
print(a)


***


a = []
print(a) # []


a.append(25)
a.append(10.8)
a.append('Hyd')
a.append(True)


print(a) # [25, 10.8, 'Hyd', True]


a.remove('Hyd')
print(a) # [25, 10.8, True]


a.remove('25') # Error (Value not found in list)
print(a)


***
.a = [25 , 10.8 , 'Hyd']


print(a) # [25, 10.8, 'Hyd']
print(id(a)) # Some memory address


print(a * 3) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1) # [25, 10.8, 'Hyd']
print(a * 0) # []
print(a * -1) # []
print(a * 4.0) # Error (Cannot multiply list by float)


a = a * 3
print(a) # Repeated 3 times
print(id(a)) # New memory address


a = [25]
print(a , id(a)) # [25] Some address
print(a * a) # Error (Cannot multiply list by list)




***


a = list('Hyd')
print(a) # ['H', 'y', 'd']
print(type(a)) # <class 'list'>
print(len(a)) # 3


b = (10 , 20 , 15 , 18)
print(list(b)) # [10, 20, 15, 18]
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(25)) # Error (Integer is not iterable)


***


a = []
print(type(a)) # <class 'list'>
print(a) # []
print(len(a)) # 0


b = list()
print(b) # []
print(len(b)) # 0


***


list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']


print(list[2 : 7]) # [(3+4j), 'Hyd', True, None, 10.8]
print(list[: : ]) # Full list
print(list[:]) # Full list
print(list[: : -1]) # Reverse list
print(list[: : 2]) # [25, (3+4j), True, 10.8]
print(list[1 : : 2]) # [10.8, 'Hyd', None, 'Hyd']
print(list[: : -2]) # ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2]) # [10.8, True, (3+4j), 25]
print(list[1 : 4]) # [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) # [True, None, 10.8]
print(list[3 : -3]) # ['Hyd', True]
print(list[2 : -5]) # [(3+4j)]
print(list[-1:-5]) # []


***


a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))  
# [10, 20, 30, 40, 50] Some address


a[1 : 4] = [60 , 70]
print(a , id(a))  
# [10, 60, 70, 50] Same address


a[2: 4] = [100 , 200 , 300]
print(a , id(a))  
# [10, 60, 100, 200, 300] Same address


***


a = [25]


print(a[1]) # Error (Index out of range)
print(a[1:]) # []



