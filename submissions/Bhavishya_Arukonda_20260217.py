#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)  # {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a))  # <class 'set'>
print(len(a)) # 6
print(a[2])  #  error  because set is not indexed
print(a[1 : 4]) #  error  because set is not indexed
a[2] = 'Sec'# error
print(a * 2) # error set cannot have duplicates
print(a * a) # error 

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)  # {1 , 'Hyd' , False , True , 0.0 , ''}
print(len(a)) # 6
print(type(a))  # <class 'set'>

#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R' , 'a' , 'm' , 'r' , 'A' , 'o' , ''}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10 , 20 , 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25 , 10.8 , 'Hyd'}
print(set(range(10 , 20 , 3))) # {10 , 13 , 16 , 19}
print(set(25)) # errorr
print(set([25 , 10.8 , [] , 'Hyd'])) # error

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'set'>
print(type(d)) # <class 'set'>
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) 
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)  # {25 , 10.8 , 'Hyd' ,'True' , 'None'}
print(len(a)) # 5
a . remove(25)
print(a) # {10.8 , 'Hyd' ,'True' , 'None'}
a . append(100) # error append method is not supported in set
a . add(set()) # error
a . add(())
a . add([]) # error set cannot have list
print(a)
a . add({}) 3 error


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop


# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(How  to  print  value  key  10)  # a[10]
print(How  to  print  value  key  20)  # a[20]
print(How  to  print  value  key  15)  # a[15]
print(How  to  print  value  key  18)  # a[18]
print(a[19]) # error i.e there is key 19
print(a[0]) # error i.e there is key 0
print(a['Amar']) # error 
How  to  moify  value  of   key  15  to  'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # error there is no key 25
print(a) # {10 : 'Ramesh' , 15 : 'Amar' , 18 : 'Sita'}
print(len(a)) # 3
print(a * 2) # error dictionary cannot have duplicates


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # error key must be unique
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow'}
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) {True : 'Yes'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b) # error
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))  1
e = {set() : 10.8}

# Find  outputs
a = {}
print(type(a)) # < class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # < class 'dict'>
print(len(b)) # 0
print(b) # {}

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))
print(a)
print(len(a))


#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # < class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # 0
                             1
                             2
                             3
                             4