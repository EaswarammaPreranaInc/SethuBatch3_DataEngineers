#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)   # { None, 10.8, 25, 'Hyd', 3+4j, True}
print(type(a))  # <class 'set'>
print(len(a))   # 6
print(a[2])   # Error: 'set' object is not indexed
print(a[1 : 4])   # Error: 'set' object is not indexed
a[2] = 'Sec'   # Error: 'set' object does not support item assignment because set is unordered collection of unique elements
print(a * 2)  # Error: 'set' and 'int' because set is unindexed collection of unique elements
print(a * a)  # Error: 'set' and 'set' because set is unindexed collection of unique elements



# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)   # {0, 1, '', False, 'Hyd', 0.0, True, 1.0}
print(len(a))  #  4
print(type(a))  # <class 'set'>




#  set()  function demo  program
a = set('Rama rAo')
print(a)  # {'a', 'm', 'R', ' ', 'o', 'r'}
print(len(a)) # 6
print(set([10 , 20 , 15 , 20]))  # {10, 15, 20}
print(set((25 , 10.8 , 'Hyd' , 10.8)))  # {10.8, 25, 'Hyd'}
print(set(range(10 , 20 , 3)))  # {10, 13, 16, 19}
print(set(25))  # Error: 'int' object is not iterable
print(set([25 , 10.8 , [] , 'Hyd']))  # Error: 'list' because set is unindexed collection of unique elements and list is mutable object






# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b))  # <class 'tuple'>
print(type(c))  # <class 'dict'>
print(type(d))  # <class 'set'>
print(a)  # []
print(b)  # ()
print(c)  # {}
print(d)  # set()  empty set





# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()  # empty set
a . add(25)    # {25}
a . add(10.8)  # {10.8, 25}
a . add('Hyd')  # {10.8, 25, 'Hyd'}
a . add(True)   # {10.8, 25, 'Hyd', True}
a . add(None)   # {None, 10.8, 25, 'Hyd', True}
a . add('Hyd')  # {None, 10.8, 25, 'Hyd', True}  duplicate element is not added to the set
a . add(1)    # {None, 1, 10.8, 25, 'Hyd', True}   not added to the set because True and 1 are considered as same element in the set
print(a)   # {None, 1, 10.8, 25, 'Hyd', True}
print(len(a))  # 6
a . remove(25)  # {None, 1, 10.8, 'Hyd', True}
print(a)  # {None, 1, 10.8, 'Hyd', True}
a . append(100)  # Error: 'set' object has no method 'append'
a . add(set())  # {None, 1, 10.8, 25, 'Hyd', True, set()}  empty set is added to the set because set is unindexed collection of unique elements and empty set is considered as unique element in the set
a . add(())   # {None, 1, 10.8, 25, 'Hyd', True, set(), ()}  empty tuple is added to the set because set is unindexed collection of unique elements and empty tuple is considered as unique element in the set
a . add([])   # Error: 'list' object is unhashable because set is unindexed collection of unique elements and list is mutable object
print(a)    # {None, 1, 10.8, 25, 'Hyd', True, set(), ()}
a . add({})   # Error: 'dict' object is unhashable because set is unindexed collection of unique elements and dict is mutable object



# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')   # {True, 10.8, 25, 'Hyd'}
print(a)  # True 10.8 25 'Hyd'
print('Iterate  thru  set  with  for  loop')  # True 10.8 25 'Hyd'



# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)  # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a))  # <class 'dict'>
print(How  to  print  value  key  10)  # Ramesh 
print(How  to  print  value  key  20)  # Kiran
print(How  to  print  value  key  15)  # Amar
print(How  to  print  value  key  18)  # Sita
print(a[19])  # Error: 19 because key 19 is not present in the dictionary a
print(a[0])   # Error: 0 because key 0 is not present in the dictionary a
print(a['Amar'])  # Error: 'Amar' because key 'Amar' is not present in the dictionary a
How  to  moify  value  of   key  15  to  'Krishna'  # a[15] = 'Krishna' 
How  to  remove  20 :  'Kiran'  from  dict  'a'    # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'    # a[25] = 'Vamsi'
print(a)   # {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a))  # 4
print(a * 2)  # Error: 'dict' and 'int' because dict is unindexed collection of unique elements





# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)   # {10: 'Sec'} because duplicate key is not allowed in the dictionary and last value of the duplicate key is considered as value of the key in the dictionary
print(len(a))  # 1 because duplicate key is not allowed in the dictionary and last value of the duplicate key is considered as value of the key in the dictionary
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)  # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'} because duplicate keys are not allowed in the dictionary and last value of the duplicate key is considered as value of the key in the dictionary
print(len(b))  # 4 because duplicate keys are not allowed in the dictionary and last value of the duplicate key is considered as value of the key in the dictionary



#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)  # {True: 'May  be'} because True and 1 and 1.0 are considered as same key in the dictionary and last value of the duplicate key is considered as value of the key in the dictionary
print(len(a))  # 1 because True and 1 and 1.0 are considered as same key in the dictionary and last value of the duplicate key is considered as value of the key in the dictionary



# Find  outputs
a = { [ ] : 25}  # Error: 'list'  set is unindexed collection of unique elements and list is mutable object
b = { ( ) : 25}   # {(): 25} because empty tuple is added to the dictionary as key because set is unindexed collection of unique elements and empty tuple is considered as unique element in the set
print(b)  # {(): 25}
c = { { } : 25}  # Error: 'dict'  set is unindexed collection of unique elements and dict is mutable object
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}   # {'Ramesh': [9948250500, 9848565090, 9440250404]} because list is added to the dictionary as value because set is unindexed collection of unique elements and list is mutable object
print(d)  # {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))   # 1
e = {set() : 10.8}  # Error: 'set'  set is unindexed collection of unique elements



# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a))  # 0
print(a)   # {}  empty dictionary
b = dict()    
print(type(b))  # <class 'dict'>
print(len(b))  # 0
print(b)   # {}  empty dictionary



# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')  # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')  # dict_keys([10, 20, 15, 18])
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')  # dict_values(['Ramesh', 'Kiran', 'Amar', 'Sita'])
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')  # dict_items([(10, 'Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')])
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')  # 10 Ramesh 20 Kiran 15 Amar 18 Sita
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')  # 10 : Ramesh 20 : Kiran 15 : Amar 18 : Sita
How  to  print  each  key  and  corresponding  value  in  dict  'a'




#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))  # <class 'set'>
print(a)  # {None} because print() function returns None
print(len(a))  # 1 because print() function returns None 




#  Anonymous  object  demo  program
_ = 25
print(_)  # 25
print(type(_))   # <class 'int'>
a , _ , c = 10 , 20 , 30   
print(a)   # 10
print(_)  # 20
print(c)  # 30
for  _  in  range(5):
	print(_ , 'Hello')  # 0 Hello 1 Hello 2 Hello 3 Hello 4 Hello
	

    