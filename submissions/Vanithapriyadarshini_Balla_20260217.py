#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {25, 10.8, 'Hyd', True, 3+4j, None}
print(type(a)) # <class 'set'>
print(len(a)) # 6
print(a[2]) # Error, bcz no indexing
print(a[1 : 4]) # Error, bcz no slicing
a[2] = 'Sec' # Error, bcz no assigning 
print(a * 2) # Error, bcz no repition
print(a * a) # Error

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # { 1, 'Hyd', False, ''}
print(len(a)) # 4
print(type(a)) # <class 'set'>

#  set()  function demo  program
a = set('Rama rAo') 
print(a) # {'R', 'a', 'm', '', 'r', 'A', 'o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) # { 10, 13, 16, 19}
print(set(25)) # Error, bcz args should be sequence
print(set([25 , 10.8 , [] , 'Hyd'])) # error ,bcz set can only have immutale elements

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'set'>
print(type(d)) # <class 'dict'>
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) #{25}
a . add(10.8) #{25, 10.8}
a . add('Hyd') #{'Hyd', 25, 10.8}
a . add(True) #{'Hyd', 25, True, 10.8}
a . add(None) #{'Hyd', True, None, 25, 10.8}
a . add('Hyd') # ignore
a . add(1) # ignore
print(a) # {'Hyd', True, None, 25, 10.8}
print(len(a)) # 5
a . remove(25) # {'Hyd', True, None, 10.8}
print(a) # {'Hyd', True, None, 10.8}
a . append(100) # Error, bcz no append method in set
a . add(set()) # error, bcz args should be immutable
a . add(()) # {'Hyd', (), True, None, 10.8}
a . add([]) # error, bcz args should be immutable
print(a) # {'Hyd', (), True, None, 10.8} 
a . add({}) # Error, bcz args should be immutable

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  thru  set  with  for  loop')
# How  to  iterate  thru  set  with  for  loop
for i in a:
print(i)

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print("How  to  print  value  key  10") 
print(a[10])
print("How  to  print  value  key  20")
print(a[20])
print("How  to  print  value  key  15")
print(a[15])
print("How  to  print  value  key  18")
print(a[18])
print(a[0]) # Error, bcz no key 0
print(a['Amar']) # Error, bcz not supported
# How  to  modify  value  of   key  15  to  'Krishna'
a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'
del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'
a[25]='Vamsi'
print(a) # # {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita', 25 : 'Vamsi'}
print(len(a)) # 4
print(a * 2) # Error, bcz no repetition , duplicates are not permitted

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10: 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow'}

print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True: 'May be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25} # Error, bcz key should be immutable
b = { ( ) : 25} 
print(b) # {() : 25}
c = { { } : 25} # Error, bcz key should be immutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8}  # Error, bcz key should be immutable

# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict() 
print(type(b)) #< class 'dict'>
print(len(b)) # 0
print(b) # {}

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
print(a.keys())
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')
print(a.values())
# How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')
# How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')
# How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
# How  to  print  each  key  and  corresponding  value  in  dict  'a'

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) # <class 'set'>
print(a) # {None}
print(len(a)) # 1

#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # 0
                           # 1
                           # 2
                           # 3
                           # 4

