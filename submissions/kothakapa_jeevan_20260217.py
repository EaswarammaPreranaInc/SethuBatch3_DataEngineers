#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)  ----> {25 , 10.8 , Hyd, True , 3+4j , None , 25 , Hyd}
print(type(a)) --> Class Set
print(len(a)) ---> 8
print(a[2]) ---> error
print(a[1 : 4]) ---> error (set object cannot be sliced because objects in set are unordered)
a[2] = 'Sec'---> error 
print(a * 2)---> error
print(a * a)---> error


# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) ----> {1 , Hyd , False , True , 0.0 , '' , 1.0 ,  0}
print(len(a)) ---> 8
print(type(a)) ---> Class Set

#  set()  function demo  program
a = set('Rama rAo')
print(a)  ---> {R,a,m,'',o} (in case of duplicates set will gives only unique values)
print(len(a))--> 5
print(set([10 , 20 , 15 , 20])) --> error
print(set((25 , 10.8 , 'Hyd' , 10.8))) --> error
print(set(range(10 , 20 , 3)))
print(set(25))
print(set([25 , 10.8 , [] , 'Hyd']))


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) ----> class list
print(type(b)) ----> class tuple
print(type(c)) ---> class dict
print(type(d)) ---> class set
print(a) ----> []
print(b) ----> ()
print(c) ----> {}
print(d) ----> set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)  --->{25}
a . add(10.8) ---> {10.8,25}
a . add('Hyd') --->{10.8,'Hyd',25}
a . add(True) ---> {'Hyd',True,10.8,25}
a . add(None) ---> {None,'Hyd',True,10.8,25}
a . add('Hyd') --->{None,'Hyd',True,10.8,25}
a . add(1) ----> {None,'Hyd',True,1,10.8,25}
print(a) ----> {None,'Hyd',True,1,10.8,25}
print(len(a)) ---> 6
a . remove(25)
print(a) ---> {None,'Hyd',True,1,10.8}
a . append(100) ---> error (there is no append method in set)
a . add(set()) ----> error
a . add(()) ----> error
a . add([]) ---> error
print(a) ---> {None,'Hyd',True,1,10.8}
a . add({}) ---> error

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) ----> class Dict
print(How  to  print  value  key  10) ---> a[10]
print(How  to  print  value  key  20) ---> a[20]
print(How  to  print  value  key  15) ---> a[15]
print(How  to  print  value  key  18) ---> a[18]
print(a[19]) ----> error
print(a[0]) ----> error
print(a['Amar']) ---> error 
How  to  moify  value  of   key  15  to  'Krishna' ---> a[15]='krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' ----> del(a[20])
How  to  append  25 : 'Vamsi'  to  dict  'a' ----> a[25]='Vamsi'
print(a) ---> {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita',20 : 'Vamsi'}
print(len(a)) ---> 4
print(a * 2) ---> error (repetition not allowed in dict)



# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)
print(len(a))
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)
print(len(b))


#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) ---> { True :'may be'}
print(len(a)) ---> 1



# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b)  ----> { ( ) : 25}
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) ---> {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) ---> 1
e = {set() : 10.8} ---> error


# Find  outputs
a = {}
print(type(a)) ---> class set
print(len(a)) ---> 0
print(a) ---> {}
b = dict()
print(type(b)) ---> class dict
print(len(b)) ---> 0
print(b) ---> {}

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') ----> print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary') ---> a.(keys)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')a.(values)
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a'


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))---> class set
print(a)    ---> empty
print(len(a))---> 0



#  Anonymous  object  demo  program
_ = 25
print(_) ---> _
print(type(_)) ---> Anonymus object  
a , _ , c = 10 , 20 , 30
print(a) ---> 10
print(_) ---> 20
print(c) ---> 30
for  _  in  range(5):
	print(_ , 'Hello')














