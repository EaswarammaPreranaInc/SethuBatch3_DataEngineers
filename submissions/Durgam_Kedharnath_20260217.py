
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #  {25, 10.8, 'Hyd', True, 3+4j, None}
print(type(a)) # class set
print(len(a)) # 6
print(a[2]) # Error set cannot has indexed
print(a[1 : 4]) # Error set cannot has indexed so it cannot be sliced
a[2] = 'Sec' # Error set cannot be modified
print(a * 2) # Error set cannot have duplicate values
print(a * a) # Error set cannot have duplicate values
# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1, 'Hyd', False, ''}
print(len(a)) # 4
print(type(a)) # class set
#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R', 'a', 'm', ' ', 'r' ,'A', 'o'}
print(len(a)) # 4
print(set([10 , 20 , 15 , 20])) # {10,20,15,}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, "Hyd"}
print(set(range(10 , 20 , 3))) # {10,13,16,19}
print(set(25)) # 25
print(set([25 , 10.8 , [] , 'Hyd'])) # Error set object cannot contain list


# Find  outputs  (Home  work)
a =   [ ] # class list
b =   ( ) # class tuple
c =   {} # class dict
d =   set() # class set
print(type(a)) # class list
print(type(b)) # class tuple
print(type(c)) # class dict 
print(type(d)) # class set
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()
# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) # {25}
a . add(10.8) # {25, 10.8}
a . add('Hyd') # {25, 10.8 ,'Hyd'}
a . add(True) # {25, 10.8 , 'Hyd', True} 
a . add(None) # {25, 10.8 , 'Hyd', True , None} 
a . add('Hyd') # Error set cannot contain duplicates
a . add(1) # {25, 10.8 , 'Hyd', True , None} 
print(a) # {25, 10.8 , 'Hyd', True , None} 
print(len(a)) # 5
a . remove(25)
print(a) # {10.8 , 'Hyd', True , None} 
a . append(100) # Error append cannot works in set
a . add(set()) # Error set is mutable
a . add(()) # {10.8 , 'Hyd', True , None, ()}
a . add([]) # Error list is mutable 
print(a) # {10.8 , 'Hyd', True , None, ()}
a . add({}) # Error dict is mutable

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') # {25 , True , 'Hyd' , 10.8} it's print in any order
print(???) # print(a)
print('Iterate  thru  set  with  for  loop') # for i in a:  
                                                 print(i) = Hyd ,nextline 25, nextline 10.8, nextline True

How  to  iterate  thru  set  with  for  loop
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # class dict
print(How  to  print  value  key  10) # print(a[10])
print(How  to  print  value  key  20) # print(a[20])
print(How  to  print  value  key  15) # print(a[15])
print(How  to  print  value  key  18) # print(a[18])
print(a[19]) # Error invalid key
print(a[0]) # Error invalid key
print(a['Amar']) # Error invalid key
How  to  moify  value  of   key  15  to  'Krishna' # a[15]='krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25]='vamsi'
print(a) # {10 : 'Ramesh' , 15 : 'krishna' , 18 : 'Sita', 25: 'vamsi'}
print(len(a)) # 4
print(a * 2) # Error dict cannot be repeated

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10: 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red', 'G' : 'Gray', 'B' : 'Black', 'Y': 'Yellow'}
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'} 
print(a) # {True : 'May be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25} # Error key should be immutable
b = { ( ) : 25} 
print(b) # { ():25}
c = { { } : 25} # Error key should be immutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # { 'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # Error key should be immutable

# Find  outputs
a = {}
print(type(a)) # class dict
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # class dict
print(len(b)) # 0
print(b) # {}

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') # print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary') # for i in a.keys():
                                     print(i)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary') # for i in a.values():
                                      print(i)

How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object') # for i in a.item():
                                                 print(i)

How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple') # for x,y in a.items():
                                        print(x,y sep=',')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary') # for i in a.keys():
                                                   print(i,a[i],sep=':')
How  to  print  each  key  and  corresponding  value  in  dict  'a'

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) # class set
print(a) # None
print(len(a)) # 1

#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) class int
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # 0 Hello nextliine  1 Hello nextline 2 Hello nextline 3 Hello nextline 4 Hello
