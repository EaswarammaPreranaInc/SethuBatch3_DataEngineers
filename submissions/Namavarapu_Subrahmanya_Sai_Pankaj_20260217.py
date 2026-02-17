#1) Set object demo
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}

print(a)            # duplicates removed (order not fixed)
print(type(a))      # <class 'set'>
print(len(a))       # 6  (25 & 'Hyd' repeated removed)

#print(a[2])         # TypeError (set not subscriptable)
#print(a[1 : 4])     # TypeError (no slicing)

#a[2] = 'Sec'        # TypeError (no indexing)

#print(a * 2)        # TypeError
#print(a * a)        # TypeError

#Tricky set
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}

print(a)            # {1, 'Hyd', False, ''}  (order not fixed)
print(len(a))       # 4
print(type(a))      # <class 'set'>

# 3) set() function
a = set('Rama rAo')
print(a)            # unique characters (space included)
print(len(a))       # count of unique chars

print(set([10 , 20 , 15 , 20]))      # {10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25,10.8,'Hyd'}
print(set(range(10 , 20 , 3)))       # {10,13,16,19}

#print(set(25))       # TypeError
#print(set([25 , 10.8 , [] , 'Hyd'])) # TypeError (list inside list not hashable)


# Types
a = [ ]
b = ( )
c = {}
d = set()

print(type(a))      # <class 'list'>
print(type(b))      # <class 'tuple'>
print(type(c))      # <class 'dict'>
print(type(d))      # <class 'set'>

print(a)            # []
print(b)            # ()
print(c)            # {}
print(d)            # set()


#5) add() and remove()

a = set()
a.add(25)
a.add(10.8)
a.add('Hyd')
a.add(True)
a.add(None)
a.add('Hyd')
a.add(1)

print(a)            # True & 1 same → only one kept
print(len(a))

a.remove(25)
print(a)

#a.append(100)       # AttributeError (no append in set)

#a.add(set())        # TypeError (set not hashable)
a.add(())           # added (tuple allowed)
#a.add([])           # TypeError

print(a)

#a.add({})           # TypeError


#6) Print set two ways
a = {25 , True , 'Hyd' , 10.8}

print('set with print function')
print(a)

print('Iterate thru set with for loop')
for x in a:
    print(x)


# 7) Dictionary
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}

print(a)
print(type(a))              # <class 'dict'>

print(a[10])                # Ramesh
print(a[20])                # Kiran
print(a[15])                # Amar
print(a[18])                # Sita

#print(a[19])                # KeyError
#print(a[0])                 # KeyError
#print(a['Amar'])            # KeyError

a[15] = 'Krishna'           # modify
a.pop(20)                   # remove key 20
a[25] = 'Vamsi'             # add new pair

print(a)
print(len(a))

#print(a * 2)                # TypeError


# 8) Duplicate keys

a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)        # {10:'Sec'}
print(len(a))   # 1
b = {'R':'Red','G':'Green','B':'Blue','Y':'Yellow','G':'Gray','B':'Black'}
print(b)        # last values kept
print(len(b))   # 4


#9) Tricky dict
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}

print(a)        # {True:'May  be'}
print(len(a))   # 1

# 10) Hashable keys
#a = { [ ] : 25}     # TypeError
b = { ( ) : 25}
print(b)            # {():25}

#c = { { } : 25}     # TypeError

d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)
print(len(d))       # 1

#e = {set() : 10.8}  # TypeError

# 11) Empty dict
a = {}
print(type(a))      # <class 'dict'>
print(len(a))       # 0
print(a)            # {}

b = dict()
print(type(b))      # <class 'dict'>
print(len(b))       # 0
print(b)            # {}

# 12) Print dictionary ways
a = {10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}

print('Dictionary with print function')
print(a)
# Dictionary with print function
# {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

print('Keys')
for k in a:
    print(k)
# Keys
# 10
# 20
# 15
# 18

print('Values')
for v in a.values():
    print(v)
# Values
# Ramesh
# Kiran
# Amar
# Sita



#13) Tricky set with prints
a = {
        print('Hyd'),
        print('Sec'),
        print('Cyb')
    }

# Hyd
# Sec
# Cyb

print(type(a))      # <class 'set'>
print(a)            # {None}
print(len(a))       # 1

# 14) Anonymous object _
_ = 25
print(_)            # 25
print(type(_))      # <class 'int'>

a , _ , c = 10 , 20 , 30
print(a)            # 10
print(_)            # 20
print(c)            # 30

for _ in range(5):
    print(_ , 'Hello')

# 0 Hello
# 1 Hello
# 2 Hello
# 3 Hello
# 4 Hello