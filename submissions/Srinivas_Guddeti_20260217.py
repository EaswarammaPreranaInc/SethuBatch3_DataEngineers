#----- Set Object Demo Program -----

a = {25, 10.8, 'Hyd', True, 3+4j, None, 25, 'Hyd'}
print(a) # {None, True, 10.8, 25, 'Hyd', (3+4j)}
print(type(a)) # <class 'set'>
print(len(a)) # 6
#print(a[2]) # Error because set does not support indexing
#print(a[1 : 4]) # Error because set does not support slicing
#a[2] = 'Sec' # Error because set does not support item assignment
#print(a * 2) # Error because set does not support multiplication
#print(a * a) # Error because set does not support multiplication


#----- Tricky Program -----

a = {1, 'Hyd', False, True, 0.0, '', 1.0, 0}
print(a) # {False, '', 'Hyd', 1}
print(len(a)) # 4
print(type(a)) # <class 'set'>


#----- Set() Function Demo Program -----

a = set('Rama rAo')
print(a) # {'R', 'a', 'm', ' ', 'r', 'A', 'o'}
print(len(a)) # 7
print(set([10, 20, 15, 20])) # {10, 20, 15}
print(set((25, 10.8, 'Hyd', 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10, 20, 3))) # {10, 13, 16, 19}
#print(set(25)) # Error because int is not iterable
#print(set([25, 10.8, [], 'Hyd'])) # Error because list inside set is not allowed


#----- Find Outputs -----

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


#----- Tricky Program -----

a = set()
a.add(25)
a.add(10.8)
a.add('Hyd')
a.add(True)
a.add(None)
a.add('Hyd')
a.add(1)
print(a) # {25, 10.8, 'Hyd', True, None}
print(len(a)) # 5
a.remove(25)
print(a) # {10.8, 'Hyd', True, None}
#a.append(100) # Error because set has no append method
#a.add(set()) # Error because set is not allowed inside set
a.add(())
#a.add([]) # Error because list is not allowed inside set
print(a) # {10.8, 'Hyd', True, None, ()}
#a.add({}) # Error because dict is not allowed inside set


#----- How to print set in two different ways -----

a = {25, True, 'Hyd', 10.8}
print('set  with  print  function') # set  with  print  function
print(a) # {25, True, 'Hyd', 10.8}
print('Iterate  thru  set  with  for  loop') # Iterate  thru  set  with  for  loop
#How  to  iterate  thru  set  with  for  loop # Error because this is not valid python statement


#----- Find Outputs -----

a = {10 : 'Ramesh', 20 : 'Kiran', 15 : 'Amar', 18 : 'Sita'}
print(a) # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a)) # <class 'dict'>
#print(How  to  print  value  key  10) # Error because invalid python syntax
#print(How  to  print  value  key  20) # Error because invalid python syntax
#print(How  to  print  value  key  15) # Error because invalid python syntax
#print(How  to  print  value  key  18) # Error because invalid python syntax
#print(a[19]) # Error because key 19 is not present in dictionary
#print(a[0]) # Error because key 0 is not present in dictionary
#print(a['Amar']) # Error because Amar is value not key
#How  to  moify  value  of   key  15  to  'Krishna' # Error because this is not valid python statement
#How  to  remove  20 :  'Kiran'  from  dict  'a' # Error because this is not valid python statement
#How  to  append  25 : 'Vamsi'  to  dict  'a' # Error because this is not valid python statement
print(a) # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(len(a)) # 4
#print(a * 2) # Error because dictionary does not support multiplication


#----- Find Outputs -----

a = {10 : 'Hyd', 10 : 'Sec'}
print(a) # {10: 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red', 'G' : 'Green', 'B' : 'Blue', 'Y' : 'Yellow', 'G' : 'Gray', 'B' : 'Black'}
print(b) # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b)) # 4


#----- Tricky Program -----

a = {True : 'Yes', 1 : 'No', 1.0 : 'May  be'}
print(a) # {True: 'May  be'}
print(len(a)) # 1


#----- Find Outputs -----

#a = { [] : 25} # Error because list cannot be dictionary key
b = {() : 25}
print(b) # {(): 25}
#c = { {} : 25} # Error because dict cannot be dictionary key
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
#e = {set() : 10.8} # Error because set cannot be dictionary key


#----- Find Outputs -----

a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) # 0
print(b) # {}


#----- How to print dictionary in different ways -----

a = {10 : 'Ramesh', 20 : 'Kiran', 15 : 'Amar', 18 : 'Sita'}
print('Dictionary  with  print  function') # Dictionary  with  print  function
#How  to  print  dictionary  with  print()  function # Error because this is not valid python statement
print('Keys  of  dictionary') # Keys  of  dictionary
#How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop # Error because this is not valid python statement
print('Values  of  dictionary') # Values  of  dictionary
#How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop # Error because this is not valid python statement
print('Tuples  of  dict_items   object') # Tuples  of  dict_items   object
#How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop # Error because this is not valid python statement
print('Elements  of  each   tuple') # Elements  of  each   tuple
#How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object # Error because this is not valid python statement
print('Keys  and  values  of  dictionary') # Keys  and  values  of  dictionary
#How  to  print  each  key  and  corresponding  value  in  dict  'a' # Error because this is not valid python statement


#----- Find Outputs -----

a = {print('Hyd'), print('Sec'), print('Cyb')} # Hyd Sec Cyb
print(type(a)) # <class 'set'>
print(a) # {None}
print(len(a)) # 1


#----- Anonymous Object Demo Program -----

_ = 25
print(_) # 25
print(type(_)) # <class 'int'>
a , _ , c = 10, 20, 30
print(a) # 10
print(_) # 20
print(c) # 30
for _ in range(5):
    print(_, 'Hello') # 0 Hello 1 Hello 2 Hello 3 Hello 4 Hello