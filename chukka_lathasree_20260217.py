#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)  ----> # 25  10.8  'Hyd'  True  3+4j  None 
print(type(a)) ---> # <class 'set'>
print(len(a)) ---> # 6
print(a[2]) ---> # it is unordered no indexes
print(a[1 : 4]) --->  # it is unordered no indexes
a[2] = 'Sec' ---> # Error
print(a * 2) ---> # Error
print(a * a) ---> # Error

#  set()  function demo  program
a = set('Rama rAo') 
print(a)---> # 'Rama rAo'
print(len(a)) ---> # 
print(set([10 , 20 , 15 , 20])) ---> # 10 , 20 , 15
print(set((25 , 10.8 , 'Hyd' , 10.8))) ---> # 25 , 10.8 , Hyd 
print(set(range(10 , 20 , 3))) ---> # set is unordered it doesn't have range
print(set(25)) ---> # 25
print(set([25 , 10.8 , [] , 'Hyd'])) ---> # 25 , 10.8 , [] , Hyd


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
'''


# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) ---> # 1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0
print(len(a)) ---> # 8
print(type(a)) ---> <class 'set'>

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) ---> # list
print(type(b)) ---> # tuple
print(type(c)) ---> # set
print(type(d)) ---> # set 
print(a) ---> # [] empty
print(b) ---> # () empty
print(c) ---> # {} empty
print(d) ---> # empty set

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set() 
a . add(25) ---> # set(25)
a . add(10.8) ---> # set(25 , 10.8)
a . add('Hyd')---> # set(25 , 10.8 , 'Hyd')
a . add(True)---> # set(25 , 10.8 , 'Hyd' , True)
a . add(None)---> # set(25 , 10.8 , 'Hyd' , True , None)
a . add('Hyd') ---> # set(25 , 10.8 , 'Hyd' , True , None , 'Hyd')
a . add(1)  ---> # set(25 , 10.8 , 'Hyd' , True , None , 'Hyd' , 1)
print(a) ---> # (25 , 10.8 , 'Hyd' , True , None  , 1)
print(len(a)) ---> # 6
a . remove(25)  ---> # ( 10.8 , 'Hyd' , True , None  , 1)
print(a) ---> # ( 10.8 , 'Hyd' , True , None  , 1)
a . append(100) ---> # Error
a . add(set()) ---> # (set( 10.8 , 'Hyd' , True , None  , () , 1))
a . add(()) ----> # ( 10.8  , 'Hyd' , True , None  , () , 1)
a . add([])----> # ( 10.8  , 'Hyd' , [] , True , None  , () , 1)
print(a) ---> # ( 10.8  , 'Hyd' , [] , True , None  , () , 1)
a . add({})---> # ( 10.8  , {} , 'Hyd' , [] , True , None  , () , 1)


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') ----> # 25 True  'Hyd'  10.8
print(???) ---> # Error no elements in set
print('Iterate  thru  set  with  for  loop') ---> for x in set : 
                                                        print
How  to  iterate  thru  set  with  for  loop   --->    for x in set : 
                                                        print     

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) ---> Ramesh Kiran Amar Sita
print(type(a)) ---> # class dict
print(How  to  print  value  key  10)---> # a[10]
print(How  to  print  value  key  20)----> # a[20]
print(How  to  print  value  key  15)---> # a[15]
print(How  to  print  value  key  18)----> # a[18]
print(a[19]) ---> # Error
print(a[0]) ---> # Error
print(a['Amar']) ----> # Error
How  to  moidfy  value  of   key  15  to  'Krishna'---> # dict(10)= Krishna
How  to  remove  20 :  'Kiran'  from  dict  'a' ---> # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'----> # dict[new key] = Vamsi
print(a) ----> # Krishna Vamsi Amar Sita
print(len(a)) ---> # 4 
print(a * 2) ---> # Error

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) ---> # 'Sec' 
print(len(a)) ---> # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) ---> # Red Green Blue yellow  Gray Black
print(len(b)) ---> # 6

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) ---> # Yes No May be
print(len(a))---> # 3

# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b) ----> # (): 25
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) ---> # Ramesh : [9948250500, 9848565090, 9440250404]
print(len(d)) ---> # 4
e = {set() : 10.8}

# Find  outputs
a = {} 
print(type(a)) ---> # class dict or set
print(len(a)) ---> # o
print(a) ---> empty
b = dict() 
print(type(b)) ----> # class dict 
print(len(b)) ---> # 0
print(b) ---> # Empty

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')
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
print(type(a)) ---> # dict
print(a) ---> invalid 
print(len(a)) ---> invalid

#  Anonymous  object  demo  program
_ = 25
print(_) ----> # 25 
print(type(_))---> # int
a , _ , c = 10 , 20 , 30
print(a) ---> # Error no object
print(_) ---> # 0
print(c) ---> # 10
for  _  in  range(5):
	print(_ , 'Hello')




