#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j , None }
print(type(a))#<class 'set'>
print(len(a))#6
print(a[2])#error-we can't access the elements of set using indexes 
print(a[1 : 4])#error-set is not indexed so slicing is not posssible
a[2] = 'Sec'#error-set doesn't perform modification because set doesnot have index
print(a * 2)#error-set is not repeated because set doesn't contain duplicate elements
print(a * a)#error-set is not repeated because set doesn't contain duplicate elements

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#{1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(len(a))#8
print(type(a))#<class 'set'>

#  set()  function demo  program
a = set('Rama rAo')
print(a)#{'R','a','m','o'}
print(len(a))#4
print(set([10 , 20 , 15 , 20]))#error-set should have immutable objects
print(set((25 , 10.8 , 'Hyd' , 10.8)))#{25,10.8,'Hyd'}
print(set(range(10 , 20 , 3)))#{10,13,16,19}
print(set(25))#error-arguments should be sequence only 
print(set([25 , 10.8 , [] , 'Hyd']))#error-set should have immutable objects


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) #<class 'list'>
print(type(b))#<class 'tuple'>
print(type(c))#<class 'set'>
print(type(d))#<class 'set'>
print(a)#empty list
print(b)#empty tuple
print(c)#empty set
print(d)#empty set

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)#{25}
a . add(10.8)#{10.8,25}
a . add('Hyd')#{'Hyd',10.8,25}
a . add(True)#{'Hyd',10.8,True,25}
a . add(None)#{'Hyd',None,10.8,25}
a . add('Hyd')#Ignored or error because element is already present in set 
a . add(1)#{'Hyd',1,None,10.8,25}
print(a)#{'Hyd',1,None,10.8,25}
print(len(a))#5
a . remove(25)#{'Hyd',1,None,10.8}
print(a)#{'Hyd',1,None,10.8}
a . append(100)#error-no append method is present in set
a . add(set())#error-nested set is not possible
a . add(())#{'Hyd',1,None,10.8,()}
a . add([])#error-set cannot contain mutable elements
print(a)#{'Hyd',1,None,10.8,()}
a . add({})#error-nested set is not possible

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')#print(a)
print(???)#print(a)
print('Iterate  thru  set  with  for  loop')#for x in range a:
				     print(x)
How  to  iterate  thru  set  with  for  loop#for x in range a:
				     print(x)

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)#{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))#<class 'dict'>
print(How  to  print  value  key  10)#print(a[10])
print(How  to  print  value  key  20)#print(a[20])
print(How  to  print  value  key  15)#print(a[15])
print(How  to  print  value  key  18)#print(a[18])
print(a[19])#error-no key is present with number 19
print(a[0])#error-no key is present with number 0
print(a['Amar'])#error-we can't acess key using value
How  to  moify  value  of   key  15  to  'Krishna'#a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'#a.remove[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'#error we cannot use append method in set. however,we can use add method to add the key value pair by using a.add[25: 'Vamshi']
print(a){10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita' , 25: 'Krishna'}
print(len(a))#4
print(a * 2)#error-the repetation is not allowed because of duplicate elements

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10 : 'Sec'}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R' : 'Red' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))#4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)#{True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(len(a))#3

# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b)#{ ( ) : 25}
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #{'Ramesh' : [9440250404]}
print(len(d))#1
e = {set() : 10.8}#error-dictionary cannot have immutable objects

# Find  outputs
a = {}
print(type(a))#<class 'set'>
print(len(a))#0
print(a)#empty set or {}
b = dict()
print(type(b))#<class 'dict'>
print(len(b))#0
print(b)#{ : }

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')#print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')#print(a.keys())
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')#print(a.values())
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')#print(a.items())
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')#for x in range a:
                                                                print(x)
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary') #error
How  to  print  each  key  and  corresponding  value  in  dict  'a'#print(a)

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))#<class 'str'>
print(a)#error
print(len(a))#3

#  Anonymous  object  demo  program
_ = 25
print(_)#25
print(type(_))#<class 'int'>
a , _ , c = 10 , 20 , 30
print(a)#10
print(_)#20
print(c)#30
for  _  in  range(5):
	print(_ , 'Hello')#