a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}


print(a) # {25, 10.8, 'Hyd', True, (3+4j), None} (duplicates removed, order may vary)
print(type(a)) # <class 'set'>
print(len(a)) # 6


print(a[2]) # Error (set does not support indexing)
print(a[1 : 4]) # Error (set does not support slicing)


a[2] = 'Sec' # Error (set does not support item assignment)


print(a * 2) # Error (set cannot be multiplied)
print(a * a) # Error


***


a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 , 0}


print(a)      
# {1, 'Hyd', False, ''} (since 1, True, 1.0 are same and 0, False, 0.0 are same)


print(len(a)) # 4
print(type(a)) # <class 'set'>


***


a = set('Rama rAo')
print(a) # {'R', 'a', 'm', ' ', 'r', 'A', 'o'} (order may vary)
print(len(a)) # 7


print(set([10 , 20 , 15 , 20])) # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) # {10, 13, 16, 19}


print(set(25)) # Error (int is not iterable)
print(set([25 , 10.8 , [] , 'Hyd'])) # Error (list inside set is unhashable)


***


a = []
b = ()
c = {}
d = set()


print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>


print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()


***


a = set()


a.add(25)
a.add(10.8)
a.add('Hyd')
a.add(True)
a.add(None)
a.add('Hyd')
a.add(1)


print(a) # {25, 10.8, 'Hyd', True, None} (1 and True are same)
print(len(a)) # 5


a.remove(25)
print(a)


a.append(100) # Error (set has no append method)


a.add(set()) # Error (set is unhashable)
a.add(()) # Valid (empty tuple allowed)
a.add([]) # Error (list is unhashable)


print(a)


a.add({}) # Error (dict is unhashable)


***


a = {25 , True , 'Hyd' , 10.8}


print('set with print function')
print(a)   
# Example: {25, True, 'Hyd', 10.8}


print('Iterate thru set with for loop')
for x in a:
    print(x)
# 25
# True
# Hyd
# 10.8


***


a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}


print(a)
print(type(a)) # <class 'dict'>


print(a[10]) # Ramesh
print(a[20]) # Kiran
print(a[15]) # Amar
print(a[18]) # Sita


print(a[19]) # Error (Key not found)
print(a[0]) # Error
print(a['Amar']) # Error (value cannot be key)


a[15] = 'Krishna'
del a[20]
a[25] = 'Vamsi'


print(a)
print(len(a))
print(a * 2) # Error (dict cannot be multiplied)


***


a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10: 'Sec'}
print(len(a)) # 1


b = {'R':'Red','G':'Green','B':'Blue','Y':'Yellow','G':'Gray','B':'Black'}
print(b) # {'R':'Red','G':'Gray','B':'Black','Y':'Yellow'}
print(len(b)) # 4




***


a = { [] : 25} # Error (list is unhashable)
b = { () : 25}
print(b) # {(): 25}


c = { {} : 25} # Error (dict is unhashable)


d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)
print(len(d)) # 1


e = {set() : 10.8} # Error (set is unhashable)




***




a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}


b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) # 0
print(b) # {}




***


a = {10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}


print('Dictionary with print function')
print(a)


print('Keys of dictionary')
for k in a:
    print(k)


print('Values of dictionary')
for v in a.values():
    print(v)


print('Tuples of dict_items object')
for t in a.items():
    print(t)


print('Elements of each tuple')
for t in a.items():
    print(t[0], t[1])


print('Keys and values of dictionary')
for k, v in a.items():
    print(k, v)




***


_ = 25
print(_) # 25
print(type(_)) # <class 'int'>


a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30


for _ in range(5):
    print(_ , 'Hello')


# 0 Hello
# 1 Hello
# 2 Hello
# 3 Hello
# 4 Hello