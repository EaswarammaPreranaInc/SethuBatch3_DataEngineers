#  set  object  demo  program  
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # { 25, 10.8, 'Hyd', True, 3+4j, None, 25, 'Hyd'}
print(type(a)) # <class 'set'>
print(len(a)) # 6
print(a[2]) # 'set' object is not subscriptable
print(a[1 : 4]) # 'set' object is not subscriptable
a[2] = 'Sec' # Error assignment is not supported
print(a * 2) # unsupported operand type(s) for *: 'set' and 'int'
print(a * a) # unsupported operand type(s) for *: 'set' and 'int'

#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R', 'a', 'm', ' ', 'r', 'A', 'o'} 
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) #  {10, 15, 20} 
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) # {10, 13, 16, 19}
print(set(25)) # 'int' object is not iterable
print(set([25 , 10.8 , [] , 'Hyd'])) # unhashable type: 'list'

# Tricky  program
# Find  outputs 
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {False, 1, '', 'Hyd'}
print(len(a)) # 4
print(type(a)) # <class 'set'>

# Find  outputs  
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()

# Tricky  program
# add()  and  remove()  methods  
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a) # { 25, 10.8, 'Hyd', True, None}
print(len(a)) # 5 
a . remove(25)  
print(a) # {10.8, 'Hyd', True, None}
a . append(100) # Error 'set' object has no attribute 'append'
a . add(set()) # Error unhashable type: 'set'
a . add(()) # Error unhashable type: 'list'
a . add([]) # error unhashable type: 'list'
print(a) # {None, True, 10.8, 'Hyd', ()}
a . add({}) # Error unhashable type: 'dict'

# Find  outputs  
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) <class 'dict'>
print(How  to  print  value  key  10) # to print value key 10 -> a[10]
print(How  to  print  value  key  20) # to print value key 20 -> a[20]
print(How  to  print  value  key  15) # to print value key 15 -> a[15]
print(How  to  print  value  key  18) # to print value key 18 -> a[18]
print(a[19]) # Error there is no key '19'
print(a[0]) # Error there is no key '0'
print(a['Amar']) # Error, can only access value with key but not key with vlaue
How  to  moify  value  of   key  15  to  'Krishna' # a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25] = 'Vamsi'
print(a) {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) # 4
print(a * 2) # unsupported operand type(s) for *: 'dict' and 'int' 


# Find  outputs  
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b)) # 4

#  Tricky  program
# Find output  
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # { True: 'May be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25} # unhashable type: 'list'
b = { ( ) : 25}
print(b) # {() : 25}
c = { { } : 25} # unhashable type: 'dict'
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # unhashable type: 'set'

# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) # 0
print(b) # {}

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) # <class 'Set'>
print(a) # Hyd Sec Cyb
print(len(a)) # 1 

#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) #<class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10 
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # 0 Hello 1 Hello 2 Hello 3 Hello 4 Hello
