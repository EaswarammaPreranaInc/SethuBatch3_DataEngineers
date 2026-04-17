# Set Object Demo Program (Home Work)

a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}

print(a).    # Output: {25, 10.8, 'Hyd', True, (3+4j), None}

print(type(a))     # <class 'set'>

print(len(a))      # 6

print(a[2])        # Error: 'set' object is not subscriptable

print(a[1 : 4])     # Error: 'set' object is not subscriptable

a[2] = 'Sec'          #Error: 'set' object does not support item assignment

print(a * 2)          # Error: unsupported operand type(s) for *: 'set' and 'int'

print(a * a)           # Error: unsupported operand type(s) for *: 'set' and 'set'





# Tricky Program
# Find Outputs (Home Work)

a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 , 0}

print(a) #{1, 'Hyd', False, ''}

print(len(a)) # 4

print(type(a)) # <class 'set'>





# set() function demo program

a = set('Rama rAo')
print(a)    # {'R', 'a', 'm', ' ', 'r', 'A', 'o'}

print(len(a))    #  7

print(set([10 , 20 , 15 , 20]))       #  {10, 20, 15}

print(set((25 , 10.8 , 'Hyd' , 10.8)))    #  {25, 10.8, 'Hyd'}

print(set(range(10 , 20 , 3)))   # range(10,20,3) → 10, 13, 16, 19
                                 #  {10, 13, 16, 19}

print(set(25))   # Error: 'int' object is not iterable

print(set([25 , 10.8 , [] , 'Hyd']))      # Error: unhashable type: 'list'

'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set





# Find outputs (Home Work)

a = []
b = ()
c = {}
d = set()

print(type(a))   # <class 'list'>
print(type(b))   # <class 'tuple'>
print(type(c))   # <class 'dict'>
print(type(d))   # <class 'set'>

print(a)         # []
print(b)         # ()
print(c)         # {}
print(d)         # set()





# Tricky program
# add() and remove() methods (Home Work)

a = set()

a.add(25)
a.add(10.8)
a.add('Hyd')
a.add(True)
a.add(None)
a.add('Hyd')
a.add(1)

print(a)         # {25, 10.8, 'Hyd', True, None}

print(len(a))    # 5

a.remove(25)
print(a)         # {10.8, 'Hyd', True, None}

a.append(100)    # AttributeError: 'set' object has no attribute 'append'
 
a.add(set())     # Error: unhashable type: 'set'

a.add(())       # Allowed (tuple is immutable)
               # Adds empty tuple ()

a.add([])        # Error: unhashable type: 'list'

print(a)

a.add({})   # Error: unhashable type: 'dict'





# How to print set in two different ways (Home Work)

a = {25, True, 'Hyd', 10.8}

print('Set with print function')
print(a)   # First way

print('Iterate thru set with for loop')
for x in a:    # Second way
    print(x)






# Find outputs (Home Work)

a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

print(a)     # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

print(type(a))  # <class 'dict'>

print(a[10])   # Ramesh

print(a[20])   # Kiran

print(a[15])   # Amar

print(a[18])   # Sita

print(a[19])  # Error: 19 (Key not found)

print(a[0])  # Error: 0 (Key not found)

print(a['Amar'])   # Error: 'Amar'






# Find outputs (Home Work)

a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)     # {10: 'Sec'}

print(len(a))  # 1

b = {
    'R': 'Red',
    'G': 'Green',
    'B': 'Blue',
    'Y': 'Yellow',
    'G': 'Gray',
    'B': 'Black'
}

print(b)          # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}

print(len(b))      # 4







# Tricky program
# Find output (Home Work)

a = {True: 'Yes', 1: 'No', 1.0: 'May be'}

print(a)     # {True: 'May be'}

print(len(a))     # 1






# Find outputs

a = {[]: 25}   # Error: unhashable type: 'list'

b = {(): 25}
print(b)  # {(): 25}

c = {{}: 25}    # Error: unhashable type: 'dict'

d = {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(d)   # {'Ramesh': [9948250500, 9848565090, 9440250404]}

print(len(d))       # 1

e = {set(): 10.8}    # Error: unhashable type: 'set'






# Find outputs

a = {}

print(type(a))     # <class 'dict'>
print(len(a))    # 0
print(a)          # {}

b = dict()

print(type(b))   # <class 'dict'>
print(len(b))     # 0
print(b)          # {}





# Find outputs (Home Work)

a = {
        print('Hyd'),
        print('Sec'),
        print('Cyb')
    }
# Hyd
# Sec
# Cyb

print(type(a))   # <class 'set'>
print(a)          # {None}
print(len(a))    # 1



# Anonymous object demo program

_ = 25
print(_)            # 25
print(type(_))      # <class 'int'>

a, _, c = 10, 20, 30
print(a)            # 10
print(_)            # 20
print(c)            # 30

for _ in range(5):
    print(_, 'Hello')


