#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {10.8 , True , 3+4j , None , 25 , 'Hyd'}
print(type(a)) # <class 'set'>
print(len(a)) # 6 
print(a[2]) # Error due to there is no indexes
print(a[1 : 4]) # Error due to there is no slicing 
a[2] = 'Sec' # Error due to there is no modify
print(a * 2) # Error due to there is no reptition 
print(a * a) # Error due to there is no dulipcate 

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False , '' ,}
print(len(a)) # 4
print(type(a)) # <class 'set'>

#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'a', 'R', 'm', 'a', 'A', 'r', 'o'}
print(len(a)) # 7 
print(set([10 , 20 , 15 , 20])) # { 20, 15, 10} 
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25 , 10.8 , 'Hyd' , 10.8}
print(set(range(10 , 20 , 3))) # {16, 10, 13, 19}
print(set(25)) # Error due to 'int' object can't be iterable 
print(set([25 , 10.8 , [] , 'Hyd'])) #Error due to 'list' object 

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b))  # <class 'tuple'>
print(type(c))  # <class 'dict'>
print(type(d))  # <class 'set'>
print(a) # [ ]
print(b) # ( )
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
print(a) # {25, 10.8, 'Hyd', True, None, } 
print(len(a)) # 5
a . remove(25) 
print(a) # {10.8, True, None, 'Hyd}
a . append(100) # Error due to there is no append method 
a . add(set())  # Error due to hasble element
a . add(()) 
a . add([]) # Error due to hasble element
print(a) # {10.8, True, None, 'Hyd', ()}
a . add({}) # Error due to hashable element

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set with print function')
print(a)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop # for i in a : 
                                                   print(i) 

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(How  to  print  value  key  10) # Ramesh
print(How  to  print  value  key  20) # Kiran 
print(How  to  print  value  key  15) # Amar 
print(How  to  print  value  key  18) # Sita 
print(a[19]) # Error due to there is no Key '19' 
print(a[0]) # Error due to  there is no Key '0'
print(a['Amar']) # Error due to Values can't be used in 'dict'
How  to  moify  value  of   key  15  to  'Krishna' # a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20] 
How  to  append  25 : 'Vamsi'  to  dict  'a' # Error due to there is no append method
print(a) # {10 : 'Ramesh' , 15 : 'Amar' , 18 : 'Sita'}
print(len(a)) # 3
print(a * 2) # Error due to there is no dulipcates in keys 

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # { 10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black', 'R' : 'Red'}
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{True : May  be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25} # Error due to there is no list key 
b = { ( ) : 25}
print(b) # Error due to there is no tuple key
c = { { } : 25} # Error due to there is no dict key
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1 
e = {set() : 10.8} # Error due to there is no set key

# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) #  0 
print(b) # {}

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary') #  for Keys in a :
                                       print(Keys) 
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary') # for value in a.Values() :
                                       print(value)    
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object') # for dict_item in a.dict_items() : 
                                                 print(dict_item)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple') # for Element in a.Elements() :
                                                      print(Element)
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary') # for key, value in a.items() :
                                                        print(key, value)
How  to  print  each  key  and  corresponding  value  in  dict  'a' # print(item[0], item [1] ... 

#  Find  outputs (Home  work)
a = {
		print('Hyd') , # Hyd
		print('Sec') , # Sec 
		print('Cyb')   # Cyb 
	}
print(type(a)) # <class 'set'>
print(a) # {None}
print(len(a)) # 1 

#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # < class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10 
print(_) # 20 
print(c) # 30 
for  _  in  range(5):
	print(_ , 'Hello') #  0 Hello
                           # 1 Hello
                           # 2 Hello
                           # 3 Hello
                           # 4 Hello 
_ = 25
print(_) # 25  
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20 
print(c) # 30 
for  _  in  range(5):
	print(_ , 'Hello') #  0 Hello
                           # 1 Hello
                           # 2 Hello
                           # 3 Hello
                           # 4 Hello 