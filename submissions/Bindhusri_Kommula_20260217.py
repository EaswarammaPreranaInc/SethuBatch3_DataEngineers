#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)            # {25 , 10.8 , 'Hyd' , True , 3+4j , None} and order may vary because set is unordered
print(type(a))      # <class 'set'>
print(len(a))       # 6
print(a[2])         # error because set does not have indexing because of unordered
print(a[1 : 4])     # cannot be sliced as it does not have indexes
a[2] = 'Sec'        # error because it is unordered
print(a * 2)        # No repetation because it does not have duplicate elements
print(a * a)        # Error 


# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0} 
print(a)        # {'Hyd' , False , True , ''} and it printed in any order
print(len(a))   # 4
print(type(a))  # <class 'set'>


#  set()  function demo  program
a = set('Rama rAo')
print(a)                                   # {'R', 'a', 'm',' ', 'r', 'A', 'o'}
print(len(a))                              # 7
print(set([10 , 20 , 15 , 20]))            # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))     # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))             # {10, 13, 16,19}
print(set(25))                             # Error because argument should  be sequence only but it is int
print(set([25 , 10.8 , [] , 'Hyd']))       # error because it has no mutable elements


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))  # <class 'list'>
print(type(b))  # <class 'tuple'>
print(type(c))  # <class 'dict'>
print(type(d))  # <class 'set'>
print(a)        # [ ]
print(b)        # ( )
print(c)        # {}
print(d)        # set()


# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)     # {25}
a . add(10.8)   # {25, 10.8}
a . add('Hyd')  # {25, 10.8. 'Hyd'}
a . add(True)   # {25, 10.8. 'Hyd', True}
a . add(None)   # {25, 10.8. 'Hyd', True, None}
a . add('Hyd')  # Already 'Hyd' is present in set, now 'Hyd' is ignored
a . add(1)      # 1 is ignored as it is equal to True
print(a)        # {25, 10.8. 'Hyd', True, None}
print(len(a))   # 5
a . remove(25)  # it will remove 25 from set
print(a)        # {10.8. 'Hyd', True, None}
a . append(100) # No append method in set
a . add(set())  # error because no mutable elements
a . add(())     # {10.8. 'Hyd', True, None, ()}
a . add([])     # error because no mutable elements
print(a)        # {10.8. 'Hyd', True, None,()}
a . add({})     # error because no mutable elements 


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???)  # print(a)
print('Iterate  thru  set  with  for  loop')
for x in a:
    print(x)


# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)         # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))   # <class 'dict'>
print(How  to  print  value  key  10) # a[10]
print(How  to  print  value  key  20) # a[20]
print(How  to  print  value  key  15) # a[15]
print(How  to  print  value  key  18) # a[18]
print(a[19]) # error because of invalid key
print(a[0])  # error because of invalid key
print(a['Amar']) # error because we cannot use value
How  to  moify  value  of   key  15  to  'Krishna'  # a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'     # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'        # a[25]='Vamsi'
print(a)       # {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita', 25 : 'Vamsi'}
print(len(a))  # 4
print(a * 2)   # No repeatation because we get duplicate keys 


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)        # {10 : 'Sec'}
print(len(a))   # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)  # {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black', 'Y' : 'Yellow'}
print(len(b))  #  4


#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)      # {True : 'May  be'}
print(len(a)) # 1


# Find  outputs
a = { [ ] : 25} # error
b = { ( ) : 25}
print(b)   # { ( ) : 25}
c = { { } : 25} # error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)  # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # error


# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a))  # 0
print(a)       # {}
b = dict()     # {}
print(type(b)) # <class 'dict'>
print(len(b))  # 0
print(b)       # {}


# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')    # print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')                 # print(a.keys())
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
# for key in a:
    print(key)
print('Values  of  dictionary')               # print(a.values())
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
# for value in a.values():
      print(value)
print('Tuples  of  dict_items   object')     # print(a.items())
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop                  
# for item in a.items():
      print(item)
print('Elements  of  each   tuple')                                               
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
# for key, value in a.items():
      print(key, value)
print('Keys  and  values  of  dictionary')                 
# for key, value in a.items():
      print(key, value)
How  to  print  each  key  and  corresponding  value  in  dict  'a'


#  Find  outputs (Home  work)
a = {
		print('Hyd') , 
		print('Sec') ,
		print('Cyb')
	}
print(type(a))  # <class 'set'>
print(a)        
print(len(a))   # 1


#  Anonymous  object  demo  program
_ = 25
print(_)      # 25
print(type(_)) # int
a , _ , c = 10 , 20 , 30
print(a)  # 10
print(_)  # 20
print(c)  # 30
for  _  in  range(5):
	print(_ , 'Hello')  # 0, Hello
                             1, Hello
                             2, Hello
                             3, Hello
                             4, Hello