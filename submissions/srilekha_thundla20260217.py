#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#{25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a))#<class 'set'>
print(len(a))#6
print(a[2])#error because set is not indexed
print(a[1 : 4])#error because set is not indexed
a[2] = 'Sec'#error because set is not indexed
print(a * 2)#error because set is not allowed duplication

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#{1,'Hyd',0.0,''}
print(len(a))#4
print(type(a))#class set
#  set()  function demo  program
a = set('Rama rAo')
print(a)#{'R','a','m',' ','r','A','o'}
print(len(a))#1
print(set([10 , 20 , 15 , 20]))#{10 , 20 , 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))#{25 , 10.8 , 'Hyd'}
print(set(range(10 , 20 , 3)))#{10,13,16,19}
print(set(25))#{25}
print(set([25 , 10.8 , [] , 'Hyd']))#error because set can't have mutable 


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
print(type(a))#class list
print(type(b))#empty tuple
print(type(c))#empty set
print(type(d))#empty set
print(a)#[]
print(b)#()
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
print(a)#{25,10.8,'Hyd',True,None}
print(len(a))#5
a . remove(25)
print(a)#{10.8,'Hyd',True,None}
a . append(100)
a . add(set())#error not possible because set can't be in set
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')#set  with  print  function
print(???)#error
print('Iterate  thru  set  with  for  loop')#Iterate  thru  set  with  for  loop
How  to  iterate  thru  set  with  for  loop # for s in a:
                                                   #print(s)
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)#{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))#class 'dict'
print(How  to  print  value  key  10)#print(a[10])
print(How  to  print  value  key  20)#print(a[20])
print(How  to  print  value  key  15)#print(a[15])
print(How  to  print  value  key  18)#print(a[18])
print(a[19])#error because there is no key 19
print(a[0])#error because there is no key 0
print(a['Amar'])#error  because there is no key 'Amar'
How  to  moify  value  of   key  15  to  'Krishna'#a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'#a.remove[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'#a[25]='Vamsi'
print(a)#{10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita', 25:'Vamsi'}
print(len(a))#4
print(a * 2)#error
# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10 : 'Hyd' , 10 : 'Sec'}
print(len(a))#2
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' }
print(len(b))#4
#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)#{True : 'Yes' , 1 : 'No' }
print(len(a))#2
# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b)#{ ( ) : 25}

c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)#{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))#1
e = {set() : 10.8}
# Find  outputs
a = {}
print(type(a))#class set
print(len(a))#0
print(a)#{}
b = dict()
print(type(b))#class dict
print(len(b))#0
print(b)#{}
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')#
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')#print(a.key())
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop #for s,a in a:
                                                                     #print(s,a)
print('Values  of  dictionary')#print(a.value())
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop #for i in a.value():
                                                                         #print(i)
print('Tuples  of  dict_items   object')#
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
print(type(a))#class set
print(a)#error
print(len(a))#1
#  Anonymous  object  demo  program
_ = 25
print(_)#25
print(type(_))#class int
a , _ , c = 10 , 20 , 30
print(a)#10
print(_)#20
print(c)#30
for  _  in  range(5):
	print(_ , 'Hello')''' 0 'Hello'
                              1 'Hello'
                              2 'Hello'
                              3 'Hello'
                              4 'Hello'
                                '''