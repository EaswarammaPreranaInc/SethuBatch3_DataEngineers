#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)                     # {25, 10.8, 'Hyd', True, (3+4j), None}
print(type(a))               # <class 'set'>
print(len(a))                # 6
print(a[2])                  # TypeError: 'set' object is not subscriptable
print(a[1 : 4])              # TypeError: 'set' object is not subscriptable
a[2] = 'Sec'                 # TypeError: 'set' object does not support item assignment
print(a * 2)                 # TypeError: unsupported operand type(s) for *
print(a * a)                 # TypeError: unsupported operand type(s) for *


# Tricky  program
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)                     # {False, 1, 'Hyd', ''}
print(len(a))                # 4
print(type(a))               # <class 'set'>


#  set()  function demo  program
a = set('Rama rAo')
print(a)                     # {'R', 'a', 'm', ' ', 'r', 'A', 'o'}
print(len(a))                # 7
print(set([10 , 20 , 15 , 20]))          # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))   # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))           # {10, 13, 16, 19}
print(set(25))              # TypeError: 'int' object is not iterable
print(set([25 , 10.8 , [] , 'Hyd']))     # TypeError: unhashable type: 'list'


# Find  outputs
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))               # <class 'list'>
print(type(b))               # <class 'tuple'>
print(type(c))               # <class 'dict'>
print(type(d))               # <class 'set'>
print(a)                     # []
print(b)                     # ()
print(c)                     # {}
print(d)                     # set()


# Tricky  program
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)                     # {25, 10.8, 'Hyd', True, None}
print(len(a))                # 5
a . remove(25)
print(a)                     # {10.8, 'Hyd', True, None}
a . append(100)              # AttributeError: 'set' object has no attribute 'append'
a . add(set())               # TypeError: unhashable type: 'set'
a . add(())
a . add([])
print(a)                     # TypeError: unhashable type: 'list'
a . add({})                  # TypeError: unhashable type: 'dict'


# How  to  print  set  in  two  different ways
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)                     # {25, True, 'Hyd', 10.8}
print('Iterate  thru  set  with  for  loop')
for i in a: print(i)         # prints each element one by one


# Find  outputs
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)                     # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a))               # <class 'dict'>
print(a[10])                 # Ramesh
print(a[20])                 # Kiran
print(a[15])                 # Amar
print(a[18])                 # Sita
print(a[19])                 # KeyError: 19
print(a[0])                  # KeyError: 0
print(a['Amar'])             # KeyError: 'Amar'
a[15] = 'Krishna'            # modifies value
del a[20]                    # removes 20:'Kiran'
a[25] = 'Vamsi'              # appends 25:'Vamsi'
print(a)                     # {10:'Ramesh',15:'Krishna',18:'Sita',25:'Vamsi'}
print(len(a))                # 4
print(a * 2)                 # TypeError: unsupported operand type(s) for *


# Find  outputs
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)                     # {10: 'Sec'}
print(len(a))                # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)                     # {'R':'Red','G':'Gray','B':'Black','Y':'Yellow'}
print(len(b))                # 4


#  Tricky  program
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)                     # {True: 'May  be'}
print(len(a))                # 1


# Find  outputs
a = { [ ] : 25}              # TypeError: unhashable type: 'list'
b = { ( ) : 25}
print(b)                     # {(): 25}
c = { { } : 25}              # TypeError: unhashable type: 'dict'
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)                     # {'Ramesh':[9948250500,9848565090,9440250404]}
print(len(d))                # 1
e = {set() : 10.8}           # TypeError: unhashable type: 'set'


# Find  outputs
a = {}
print(type(a))               # <class 'dict'>
print(len(a))                # 0
print(a)                     # {}
b = dict()
print(type(b))               # <class 'dict'>
print(len(b))                # 0
print(b)                     # {}


# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a)                     # prints complete dictionary
print('Keys  of  dictionary')
for k in a: print(k)         # prints each key
print('Values  of  dictionary')
for v in a.values(): print(v)   # prints each value
print('Tuples  of  dict_items   object')
for t in a.items(): print(t)    # prints (key,value) tuples
print('Elements  of  each   tuple')
for k,v in a.items(): print(k,v) # prints elements of each tuple
print('Keys  and  values  of  dictionary')
for k in a: print(k,a[k])     # prints key and corresponding value


#  Find  outputs
a = {
        print('Hyd') ,
        print('Sec') ,
        print('Cyb')
    }
# Output:
# Hyd
# Sec
# Cyb
print(type(a))               # <class 'set'>
print(a)                     # {None}
print(len(a))                # 1


#  Anonymous  object  demo  program
_ = 25
print(_)                     # 25
print(type(_))               # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a)                     # 10
print(_)                     # 20
print(c)                     # 30
for  _  in  range(5):
    print(_ , 'Hello')       # 0 Hello ... 4 Hello
