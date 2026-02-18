# Set Object Homework
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # prints set object a in any order with unique elements
print(type(a)) # <class 'set'>
print(len(a)) # 6
print(a[2]) # error as indexing is not supported by sets given that they are not ordered
print(a[1 : 4]) # error as slicinng is not supported by sets given that they cannot be indexed
a[2] = 'Sec' # error because while set is mutable, it only supports inserton and deletion, not modification
print(a * 2) # error because set does not allow duplicates, it cannot be repeated
print(a * a) # error because set does not allow duplicates, it cannot be repeated but also because repeation can only support int arguments


# Tricky Program Homework
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # prints set object a in any order with unique elements
print(len(a)) # 6
print(type(a)) # <class 'set'>


# set() Function Homework
a = set('Rama rAo')
print(a) # prints each letter of the str in a set in any order with unique elements
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # error because a set can only contain immutable objects
print(set((25 , 10.8 , 'Hyd' , 10.8))) # prints a set with the given elements from the tuple in any order with unique elements
print(set(range(10 , 20 , 3))) # prints the output of the range i.e. (10, 13, 16, 19), in any order with unique elements
print(set(25)) # error because the arguments needs to be a sequence
print(set([25 , 10.8 , [] , 'Hyd'])) # error because a set can only contain immutable objects

'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  because  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
'''


# Find Outputs Homework #1
a =   [ ] 
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # empty list
print(b) # empty tuple
print(c) # empty dict
print(d) # empty set


# Tricky Program add(), remove() Methods Homework
a = set() # empty set
a . add(25) # adds int object 25 to the set
a . add(10.8) # adds float object 10.8 to the set
a . add('Hyd') # adds str object 'Hyd' to the set
a . add(True) # adds bool object True to the set
a . add(None) # adds NoneType object None to the set
a . add('Hyd') # it does not show in the output because an object 'Hyd' already exists
a . add(1)
print(a) # prints set a of any order with unique elements
print(len(a)) # 6
a . remove(25) # removes the element 25
print(a) # prints a set of any order with unique elements
a . append(100) # error because append does not exist in set
a . add(set()) # mutable objects cannot be added to set
a . add(()) # adds an empty tuple to the set
a . add([]) # mutable objects cannot be added to set
print(a) # prints a set of any order with unique elements
a . add({}) # mutable objects cannot be added to set


# Printing Set Homework
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
# for x in set:
      # print(x)


# Find Outputs Homework #2
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(How  to  print  value  key  10) # a[10]
print(How  to  print  value  key  20) # a[20]
print(How  to  print  value  key  15) # a[15]
print(How  to  print  value  key  18) # a[18]
print(a[19]) # error because key 19 does not exist
print(a[0]) # error because key 0 does not exist
print(a['Amar']) # error because only keys print values, not the other way around
How  to  moify  value  of   key  15  to  'Krishna' # a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25] = 'Vamsi'
print(a) # {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita' , 25 : 'Vamsi'}
print(len(a)) # 4
print(a * 2) # error # dictionary cannot be repeated as it cannot contain duplicate elements


# Find Outputs Homework #3
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) # 4


# Tricky Program Homework #2
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True : 'May be'}
print(len(a)) # 1


# Find Outputs Homework #4
a = { [ ] : 25} # empty list cannot be used as a key
b = { ( ) : 25}
print(b) # {() : 25}
c = { { } : 25} # empty dict cannot be used as a key
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # set() cannot be used as a key


# Find Outputs Homework #5
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) # 0 
print(b) # {}


# Printing Dictionary Homeowork
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
How  to  print  dictionary  with  print()  function #print(a)
print('Keys  of  dictionary')
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop # for key in a.keys(): <> print(key)
print('Values  of  dictionary')
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop # for value in a.values(): <> print(value)
print('Tuples  of  dict_items   object')
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop # for tup in a.items(): <> print(tup)
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a' # for key, value in a.items: <> print(key, value)


# Find Outputs Homework #6
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) # <class 'set>
print(a) # prints a set of any order with unique elements
print(len(a)) # 3


# Anonymous Object Homework
_ = 25
print(_) # 25
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # 0, Hello <> 1 Hello <> 2 Hello <> 3 Hello <> 4 Hello
