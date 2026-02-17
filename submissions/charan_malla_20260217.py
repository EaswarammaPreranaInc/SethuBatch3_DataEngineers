#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)  # {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a)) # <class 'set'>
print(len(a))  # 6
print(a[2]) # error, indexing not there in set
print(a[1 : 4]) # error, slicing cannot performed in set
a[2] = 'Sec' # error, we cant modify elements in set
print(a * 2) #Error, because repeatiblity is not supported by set
print(a * a) #Error, because repeatiblity is not supported by set


a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)  # {1 , 'Hyd' , False , ''}
print(len(a)) # 4
print(type(a)) # <class 'set'> 


#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'A', 'a', 'm', ' ', 'R', 'r', 'o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10 , 20 , 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))  # {25 , 10.8 ,'Hyd'}
print(set(range(10 , 20 , 3))) # {10 , 13 , 16 , 19}
print(set(25)) # error, argument cannot be non-sequence
print(set([25 , 10.8 , [] , 'Hyd']))


a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # [ ]
print(b) # ( )
print(c) # {}
print(d) # set()


a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a) # { 25 , 10.8 , 'Hyd' , True , None }
print(len(a)) # 5
a . remove(25) 
print(a) # { 10.8 , 'Hyd' , True , None }
a . append(100)  # error, append method is not used in set
a . add(set()) # Error, because set elements should be immutable, where here set is mutable
a . add(()) # Here it is allowed because tuple is immutable
a . add([]) # Error, because again list is mutable , so it can not be added as element to set
print(a) # {25, 10.8, 'Hyd', True. None , ()}
a . add({}) # Error


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # It will print whole set   {25 , True , 'Hyd' , 10.8}
print('Iterate  thru  set  with  for  loop')
#How  to  iterate  thru  set  with  for  loop
''' for x in a:
	print(x)
"'


# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(How  to  print  value  key  10)  # print(a[10]) 
print(How  to  print  value  key  20)  # print(a[20])
print(How  to  print  value  key  15)  # print(a[15])
print(How  to  print  value  key  18)  # print(a[18])
print(a[19])  # Error because there is no key 19 present in given dict
print(a[0]) # Error because there is no key 0 present in given dict
print(a['Amar']) # Error because we cannot use a value of dict as key
#How  to  modify  value  of   key  15  to  'Krishna' # a[15] = 'Krishna'
# How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
# How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25] = 'Vamsi'
print(a) # {10 : 'Ramesh'  , 15 : 'Krishna' , 18 : 'Sita' , 25 : 'Vamsi'}
print(len(a)) # 4
print(a * 2) # Error, duplicates are supported by dict


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow' }
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # { True : 'May be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25} # Error, List can not be in dictionary as it is mutable
b = { ( ) : 25} 
print(b) # {() :25}
c = { { } : 25} # Error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # Error, because key value in dict should be immutable object

# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0, zero elements in dict
print(a) # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) # 0
print(b) # {}


# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') # print(a) , {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
# How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
"'for x in a.keys() :
	print(x)
"'
# How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')
"' for x in a.values() :
	print(x)
"'
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
print(type(a)) # <class 'dict'>
print(a)
print(len(a))


#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello')  "' 0 Hello
				      1 Hello
 				      2 Hello
				      3 Hello
				      4 Hello "'



