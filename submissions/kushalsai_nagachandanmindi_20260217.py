#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {25 , 10.8 , 'Hyd' , True , 3+4j , None }
print(type(a)) # class 'set'
print(len(a)) # 6
print(a[2]) # Error in set no index
print(a[1 : 4]) # Error as no index slice cannot be done
a[2] = 'Sec' # Error unordered so no index
print(a * 2) # Error dupilicate elements not possible in set 
print(a * a) # Error this operation not possible in set


# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False , True , '' }
print(len(a)) # 5
print(type(a)) # class 'set'

#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R', 'a', 'm', 'r', 'A', 'o'}
print(len(a)) # 6
print(set([10 , 20 , 15 , 20])) # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25 , 10.8 , 'Hyd'}
print(set(range(10 , 20 , 3))) # {10, 13, 16, 19}
print(set(25)) # Error argument  should  be  sequence  only
print(set([25 , 10.8 , [] , 'Hyd'])) # Error

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # class 'list'
print(type(b)) # class 'tuple'
print(type(c)) # class 'set'
print(type(d)) # class 'set'
print(a) # [ ]
print(b) # empty
print(c) # empty
print(d) # empty

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
print(a) # {'Hyd', None, True, 10.8, 25}
print(len(a)) # 5
a . remove(25) 
print(a) # {'Hyd', None, True, 10.8}
a . append(100) # Error append not possible
a . add(set()) # Error
a . add(()) 
a . add([]) # Error
print(a) # {'Hyd', None, True, 10.8, ()}
a . add({}) # Error

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(a)
print(*a)
for i in a:
	print(i)
How  to  iterate  thru  set  with  for  loop

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # class dict
print(a[10]) # 'Ramesh'
print(a[20]) # 'Kiran'
print(a[15]) # 'Amar'
print(a[18]) # 'Sita'
print(a[19]) # Error no key as 19
print(a[0]) # Error no key as 0
print(a['Amar']) # Error no key as 'Amar'
How  to  moify  value  of   key  15  to  'Krishna' # a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25]='Vamsi'
print(a) # {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) # 4
print(a * 2) # Error 

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) # 3

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True: 'May  be'}
print(len(a)) # 1
# Find  outputs 
a = { [ ] : 25} 
b = { ( ) : 25} 
print(b) # {(): 25}
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # Error

# Find  outputs
a = {}
print(type(a)) # class 'dict'
print(len(a)) # 0
print(a) # {}
b = dict() 
print(type(b)) # class 'dict' 
print(len(b)) # 0
print(b) # {}

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') # print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary') # for key in a:
					print(key)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary') # for value in a.values():
				  	print(value)
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object') # for item in a.items():
						print(item)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple') # for item in a.items():
					    print(item[0], item[1])
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary') # for key, value in a.items():
						print(key, value)
How  to  print  each  key  and  corresponding  value  in  dict  'a'

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) # class 'set'
print(a) # None
print(len(a)) # 1

#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # class int 
a , _ , c = 10 , 20 , 30 
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # 0 Hello
			     1 Hello
			     2 Hello
			     3 Hello
			     4 Hello