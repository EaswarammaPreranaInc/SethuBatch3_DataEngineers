#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)
print(type(a)) # <class 'set'>
print(len(a)) # 6
print(a[2]) # Error as set is not indexed
print(a[1 : 4]) # Error as set is not indexed
a[2] = 'Sec' # Invlaid
print(a * 2)
print(a * a)

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {False,1,'','Hyd'}
print(len(a)) # 4
print(type(a)) # <class 'set'>

#  set()  function demo  program
a = set('Rama rAo')
print(a) # { 'R','r','a','o','m','A',' '}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25,10.8,'Hyd'}
print(set(range(10 , 20 , 3))) # {10,16,13,19}
print(set(25)) # Error as int is a non-sequence
print(set([25 , 10.8 , [] , 'Hyd'])) #


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
'''

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'set'>
print(type(d)) # <class 'set'>
print(a) # [ ]
print(b) # ( )
print(c) # { }
print(d) # set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) # {25}
a . add(10.8) # {10.8,25}
a . add('Hyd') # { 25, 'Hyd',10.8}
a . add(True) #{ True,10.8,25,'Hyd'}
a . add(None) # {True,10.8,None,25,'Hyd'}
a . add('Hyd')
a . add(1)
print(a) # {True,10.8,None,25,'Hyd'}
print(len(a)) # 5
a . remove(25) # {True,10.8,None,'Hyd'}
print(a) # {True,10.8,None,'Hyd'}
a . append(100) # Error set does not have an append function
a . add(set()) # Error as nested set is not allowed
a . add(()) # {True,10.8,None,(),'Hyd'}
a . add([]) # Error adding a tuple is not possible
print(a)# {True,10.8,None,(),'Hyd'}
a . add({}) #Error 

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???) # print(a) 
                {25 , True , 'Hyd' , 10.8}
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop # for item in a:
                                                    print(item)
                                                    25
                                                    Hyd
                                                    True
                                                    10.8

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(How  to  print  value  key  10) # print(a[10])
print(How  to  print  value  key  20) # print(a[20])
print(How  to  print  value  key  15) # print(a[15])
print(How  to  print  value  key  18) # print(a[18])
print(a[19]) #Error no key '19'
print(a[0]) #Error no key '0'
print(a['Amar'])#Error 'Amar' is a value not a key
How  to  moify  value  of   key  15  to  'Krishna' # a[15]=Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25]='Vamsi'
print(a) {10 : 'Ramesh' , 20 : 'Kiran' , 18 : 'Sita' , 25 : 'Vamsi' }
print(len(a)) # 4
print(a * 2) # Error as dict cannot be repeated as it cannot have duplicate

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b){'R' : 'Red' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) #4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True : 'May be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b) # { ( ) : 25}
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8}

# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) # 0 
print(b) # {}

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
How  to  print  dictionary  with  print()  function # print(a)
print('Keys  of  dictionary')
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop # for key in a:
    print(key)
print('Values  of  dictionary')
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop # for value in a:
    print(value)
print('Tuples  of  dict_items   object')
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop # for item in a:
    print(item)
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object # for element in a:
                        print(elemrnt)
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a' # print(a)

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) # <class 'set'>
print(a)
print(len(a))

#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) #<class 'int'>
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