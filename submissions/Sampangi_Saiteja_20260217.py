#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#{25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a))#<class 'set'>
print(len(a))#6
print(a[2])#error due to set did not support the Indexing and slicing
print(a[1 : 4])#error due to set did not support the Indexing and slicing
a[2] = 'Sec'
print(a * 2)#error due to Set do not accept duplicate values 
print(a * a)#error due to Set do not accept duplicate values 


#  set()  function demo  program
a = set('Rama rAo')
print(a)# {'R','a','m','a', 'r','A','o'}
print(len(a))#''
print(set([10 , 20 , 15 , 20]))#{20,15,10}
print(set((25 , 10.8 , 'Hyd', 10.8)))#{10.8,'hyd',25}
print(set(range(10 , 20 , 3)))#{10,19,16,13}
print(set(25))# Error due to it is non sequence
print(set([25 , 10.8 , [] , 'Hyd']))#{'Hyd',10.8,[],25}


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))#<class 'list'>
print(type(b))#<class 'tuple'>
print(type(c))#<class 'set'>
print(type(d))#<class 'set>
print(a)#[ ]
print(b)#( )
print(c)#{}
print(d)#{}


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
print(a)#{25,1,10.8,True,None,'Hyd', ,'Hyd'}
print(len(a))#7
a . remove(25)
print(a)#{1,10.8,True,None,'Hyd', ,'Hyd'}
a . append(100)# Error due to It did not have append matter
a . add(set())
a . add(())
a . add([])
print(a){ , , ,}
a . add({})# Error due Both the set will not be 


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')#print(a)
print(???)#???
print('Iterate  thru  set  with  for  loop')#'Iterate  thru  set  with  for  loop'


# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)#{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))#<class 'dictionary'>
print(How  to  print  value  key  10)#a[10]
print(How  to  print  value  key  20)#a[20]
print(How  to  print  value  key  15)#a[15]
print(How  to  print  value  key  18)#a[18]
print(a[19])#error due to it is not present in dictionary
print(a[0])#error due to it is not present in dictionary
print(a['Amar'])#error due to It can access only key  Not value
How  to  moify  value  of   key  15  to  'Krishna' #a[15]='moify'
How  to  remove  20 :  'Kiran'  from  dict  'a'#
How  to  append  25 : 'Vamsi'  to  dict  'a'#a[25]='Vamsi'
print(a)#{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(len(a))#4
print(a * 2)#error due to 


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10 : 'Hyd' , 10 : 'Sec'}
print(len(a))#2
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))#6

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)#{True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(len(a))#3


# Find  outputs
a = { [ ] : 25}#{ :25}
b = { ( ) : 25}#{ :25}
print(b)#{ :25}
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)#{'Ramesh' : 9948250500, 9848565090, 9440250404}
print(len(d))#1
e = {set() : 10.8}#{ :10.8}


# Find  outputs
a = {}
print(type(a))<class 'set'>
print(len(a))#0
print(a)#<space>
b = dict()
print(type(b))#<class ' Dictionary'>
print(len(b))#0
print(b)#<space>

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')#print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
#key=a.keys()
#print(key)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')
# error due to It cannot access the values
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')#print(items)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')#
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
#items=a.items()
#print(items)
How  to  print  each  key  and  corresponding  value  in  dict  'a'


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))#error due to space and tab and also {}
print(a)#error due to space and tab and also {}
print(len(a))#error due to space and tab and also {}


#  Anonymous  object  demo  program
_ = 25
print(_)#25
print(type(_))<class 'int'>
a , _ , c = 10 , 20 , 30
print(a)#10
print(_)#20
print(c)#30
for  _  in  range(5):
	print(_ , 'Hello')
#20,'Hello'
#20,'Hello'
#20,'Hello'
#20,'Hello'
#20,'Hello'
