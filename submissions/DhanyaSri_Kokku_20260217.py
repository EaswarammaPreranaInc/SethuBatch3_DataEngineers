#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # { 25 , 10.8 , 'Hyd' ,True , 3+4j, None}
print(type(a)) # class<'set'>
print(len(a)) # 6
print(a[2]) # Error set cannot be indexed because it is unordered
print(a[1 : 4]) # Error set cannot be sliced because it is unordered
a[2] = 'Sec' # Error elements in the set are cannot be modified
print(a * 2) # Repetation is not allowed because set cannot have duplicates
print(a * a) # Repetation is not allowed because set cannot have duplicates

#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R' , 'a' , 'm' , ' ', 'r' ,'A' ,'o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) #Error set cannot has mutable elements
print(set((25 , 10.8 , 'Hyd' , 10.8))) # { 25, 10.8 ,'Hyd'}
print(set(range(10 , 20 , 3))) # { 10 , 13 , 16 , 19}
print(set(25)) # Error set cannot have a non sequence as argument
print(set([25 , 10.8 , [] , 'Hyd'])) #Error set cannot has mutable elements


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
'''

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False , '' }
print(len(a)) # 4
print(type(a)) # class<'set'>

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # type<'list'>
print(type(b)) # type<'tuple'>
print(type(c)) # type<'dict'>
print(type(d)) # type<'set'>
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) # Adds element 25 into set a
a . add(10.8) # Adds element 10.8 into set a
a . add('Hyd') # Adds element 'Hyd' into set a
a . add(True) # Adds element True into set a
a . add(None) # Adds element None into set a
a . add('Hyd') # As the set does not allows duplicates the set does not modify
a . add(1) # Adds element 25 into set a
print(a) # { 25, 10.8, 'Hyd', None, 1}
print(len(a)) # 5
a . remove(25) # Removes a element 25
print(a) # { 10.8, 'Hyd', None, 1}
a . append(100) # Set object does not have a append method
a . add(set()) # Error set cannot have mutable objects
a . add(()) # Adds a empty tuple into a
a . add([]) # Error set cannot have mutable objects
print(a) # { 10.8, 'Hyd', None, 1 , ()}
a . add({}) # Error set cannot have mutable objects

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  thru  set  with  for  loop')
#How  to  iterate  thru  set  with  for  loop
for ele in a:
    print(ele)  

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # class<'dict'>
print('How  to  print  value  key  10',a[10])
print('How  to  print  value  key  20',a[20])
print('How  to  print  value  key  15',a[15])
print('How  to  print  value  key  18',a[18])
print(a[19]) # Error the key is not exist in the dictionary
print(a[0]) # Error the key is not exist in the dictionary
print(a['Amar']) # Error the key is not exist
How  to  modify  value  of   key  15  to  'Krishna' # a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25]='Vamsi'
print(a) # {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita',25 : 'Vamsi'}
print(len(a)) # 4
print(a * 2) #  Error Dictionary cannot be repeated

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # { 10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # { True: 'May be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25} # Invalid the key should be immutable objects
b = { ( ) : 25}
print(b) # { ( ) : 25}
c = { { } : 25} # Invalid the key should be immutable objects
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # Invalid the key should be immutable objects

# Find  outputs
a = {}
print(type(a)) # class<'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # class<'dict'>
print(len(b)) # 0
print(b) # {}

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
#How  to  print  dictionary  with  print()  function
print(a)
print('Keys  of  dictionary')
#How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
for key in dict.keys(a):
     print(key)
print('Values  of  dictionary')
#How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
for val in dict.values(a):
     print(val)
print('Tuples  of  dict_items   object')
#How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
for tup in dict.items(a):
     print(tup)
print('Elements  of  each   tuple')
#How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
for tup in dict.items(a):
     print(*tup)
         
print('Keys  and  values  of  dictionary')
#How  to  print  each  key  and  corresponding  value  in  dict  'a'
print(a)

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) # class<'set'>
print(a) # { None }
print(len(a)) # 1

#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # class<'int'>
a , _ , c = 10 , 20 , 30 
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello')
# 0 Hello
# 1 Hello
# 2 Hello
# 3 Hello
# 4 Hello