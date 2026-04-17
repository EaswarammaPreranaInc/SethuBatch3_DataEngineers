#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)  # {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a)) # <Class 'set'>
print(len(a))  # 6
print(a[2])    # Error
print(a[1 : 4]) # Error 
a[2] = 'Sec'   # Error
print(a * 2)   # Error
print(a * a)   # Error

#  set()  function demo  program
a = set('Rama rAo')
print(a)   #{ R, a, m, r, A,o , ''}
print(len(a))  #7
print(set([10 , 20 , 15 , 20])) # Error
print(set((25 , 10.8 , 'Hyd' , 10.8))) # { 25, 10.8 , 'Hyd'}
print(set(range(10 , 20 , 3))) # { 13, 16 , 19}
print(set(25))  #Error
print(set([25 , 10.8 , [] , 'Hyd'])) # Error

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #{1 , 'Hyd' , 0.0 , '' , 
print(len(a)) #4
print(type(a)) # <Class 'set'>

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) #<Class 'list'>
print(type(b)) #<Class 'tuple'>
print(type(c)) #<Class 'dict'>
print(type(d)) #<Class 'set'>
print(a)       # []
print(b)       # ()
print(c)       # {}
print(d)       #{}

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)    #{25}
a . add(10.8)  #{25, 10.8}
a . add('Hyd') # {
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)    #{ 25, 10.8, 'Hyd', True, None}
print(len(a)) # 5
a . remove(25) 
print(a)    # { 10.8, 'Hyd', True, None}
a . append(100) #Error
a . add(set()) #error
a . add(()) 
a . add([]) #Error
print(a) { 25, 10.8, 'Hyd', True, None, ()}
a . add({})Error

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') 
print(???)  #a
print('Iterate  thru  set  with  for  loop')  # for x in a:
                                                   print(x)
How  to  iterate  thru  set  with  for  loop

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)  # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <Class ' Dict'>
print(How  to  print  value  key  10) # a[10]
print(How  to  print  value  key  20) # a[20]
print(How  to  print  value  key  15) # a[15] 
print(How  to  print  value  key  18) # a[18]
print(a[19]) #Error
print(a[0])  #Error
print(a['Amar']) #error
How  to  moify  value  of   key  15  to  'Krishna' a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'    del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'       a[25] = 'Vamsi'
print(a) {10 : 'Ramesh'  , 15 : 'Krishna' , 18 : 'Sita' , 25 : 'Vamsi'}
print(len(a))#4
print(a * 2) #Error

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)   # {10 : 'Sec'}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)  {'R' : 'Red' ,  'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{True : 'May  be'}
print(len(a))#1

# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b)  # { ( ) : 25}
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))#1
e = {set() : 10.8} 

# Find  outputs
a = {}
print(type(a))  <Class 'dict'>
print(len(a))   #0
print(a)        #{}
b = dict()
print(type(b)) <Class 'dict'>
print(len(b))   #0
print(b)        #{}

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
How  to  print  dictionary  with  print()  function # print(a)
print('Keys  of  dictionary')  print(a.Keys)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop # for x in a.key():
                                                                       print(x)
print('Values  of  dictionary')                                   # print(a.values)
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop  # for x in a.value():
                                                                         printx
print('Tuples  of  dict_items   object')                           #print(a.items)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop  #for x in a.items():
                                                                         printx
print('Elements  of  each   tuple')                                  # for i in a.items():
                                                                          for x in i:
                                                                             print(x)
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')                            #for key, Value in a.items():
                                                                           print(key , value)
How  to  print  each  key  and  corresponding  value  in  dict  'a' 

  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) #Error
print(a)       #error
print(len(a))  

#  Anonymous  object  demo  program
_ = 25
print(_)  #25
print(type(_))#<Class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30 
for  _  in  range(5):
	print(_ , 'Hello')  # 0 , 'Hello'  1 , 'Hello'   2 , 'Hello'  3 , 'Hello'  4 , 'Hello'
                              
