#Set object demo program(home work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}

print(a)          # {25, 10.8, 'Hyd', True, (3+4j), None} (duplicates removed)
print(type(a))    # <class 'set'>
print(len(a))     # 6

#print(a[2])       # Error: sets do not have index numbers
#print(a[1:4])     # Error: sets cannot be sliced
#a[2] = 'Sec'      # Error: cannot change set using index
#print(a * 2)      # Error: sets cannot be multiplied
#print(a * a)      # Error: sets cannot be multiplied


#Tricky program
#Find outputs(home work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)          # {1, 'Hyd', False, ''} (True=1=1.0 same, False=0=0.0 same)
print(len(a))     # 4
print(type(a))    # <class 'set'>

#set() function demo program
a = set('Rama rAo')
print(a)          # {'R', 'a', 'o', ' ', 'm', 'A', 'r'}
print(len(a))     # 7
print(set([10 , 20 , 15 , 20]))        # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))         # {10, 13, 16, 19}
print(set(25)) #Error: single number is not a collection of items
print(set([25 , 10.8 , [] , 'Hyd']))   # Error: list inside set is not allowed

#find outputs(home work)
a = []
b = ()
c = {}
d = set()
print(type(a))    # <class 'list'>
print(type(b))    # <class 'tuple'>
print(type(c))    # <class 'dict'>
print(type(d))    # <class 'set'>
print(a)          # []
print(b)          # ()
print(c)          # {}
print(d)          # set()

#Tricky program
#add() and remove() methods(home work)
a = set()
a.add(25)
a.add(10.8)
a.add('Hyd')
a.add(True)
a.add(None)
a.add('Hyd')
a.add(1)

print(a)      # {25, 10.8, 'Hyd', True, None} 
print(len(a)) # 5

a.remove(25)
print(a)      # {None, True, 10.8, 'Hyd'}

a.append(100)     #Error: sets do not have append method 

a.add(set())      #Error: cannot put one set inside another set

a.add(())         # allowed 
a.add([])         #Error: list cannot be added to set

print(a)          # {None, True, 10.8, 'Hyd'}
a.add({})         # Error: dictionary cannot be added to set

#how to print set in two different ways (home work)
a = {25 , True , 'Hyd' , 10.8}

print(a)          # {25 , True , 'Hyd' , 10.8}

for x in a:
    print(x)      
# 25 
# 10.8 
# True 
#Hyd
    
#find the outputs(home work)

a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}

print(a)          # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18:'Sita'}
print(type(a))    # <class 'dict'>
print(a[10])      # Ramesh
print(a[20])      # Kiran
print(a[15])      # Amar
print(a[18])      # Sita
print(a[19])      # Error: key 19 not present in dictionary
print(a[0])       # Error: key 0 not present in dictionary
print(a['Amar'])  # Error: 'Amar' is a value, not a key
a[15] = 'Krishna'     
del a[20]            
a[25] = 'Vamsi'       
print(a)        # {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a))     # 4
print(a * 2)     # Error: dictionaries cannot be multiplied

#find outputs(home work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)          # {10: 'Sec'} (last value kept)
print(len(a))     # 1
b = {'R':'Red','G':'Green','B':'Blue','Y':'Yellow','G':'Gray','B':'Black'}
print(b)          # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))     # 4

#Tricky program
#Find outputs(home work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May be'}
print(a)          # {True: 'May be'} 
print(len(a))     # 1


#Find outputs(home work)
a = { [] : 25}    # Error: list cannot be dictionary key 
b = { () : 25}
print(b)          # {(): 25}
c = { {} : 25}    # Error: dictionary cannot be key
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)          # {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))#1
e={set():10.8} #Error




#  Find Outputs
a = {}
print(type(a))   # <class 'dict'>
print(len(a))    # 0
print(a)         # {}

b = dict()
print(type(b))   # <class 'dict'>
print(len(b))    # 0
print(b)         # {}




#  Print Dictionary in Different Ways

a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

# Dictionary with print function
print(a)
# {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

# Keys of dictionary
for key in a:
    print(key)
# 10
# 20
# 15
# 18

# Values of dictionary
for value in a.values():
    print(value)
# Ramesh
# Kiran
# Amar
# Sita

# Tuples of dict_items object
for item in a.items():
    print(item)
# (10, 'Ramesh')
# (20, 'Kiran')
# (15, 'Amar')
# (18, 'Sita')

# Elements of each tuple
for item in a.items():
    print(item[0], item[1])
# 10 Ramesh
# 20 Kiran
# 15 Amar
# 18 Sita

# Keys and values of dictionary
for key, value in a.items():
    print(key, value)
# 10 Ramesh
# 20 Kiran
# 15 Amar
# 18 Sita



# Find Outputs (Homework)

a = {
        print('Hyd'),   # Hyd
        print('Sec'),   # Sec
        print('Cyb')    # Cyb
    }

print(type(a))   # <class 'set'>
print(a)         # {None}
print(len(a))    # 1



# Anonymous Object Demo Program
_ = 25
print(_)         # 25
print(type(_))   # <class 'int'>

a, _, c = 10, 20, 30
print(a)         # 10
print(_)         # 20
print(c)         # 30

for _ in range(5):
    print(_, 'Hello')
# 0 Hello
# 1 Hello
# 2 Hello
# 3 Hello
# 4 Hello
