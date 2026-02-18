#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd}
print(type(a)) # class 'set'
print(len(a)) # 8
print(a[2]) # error bez set doesn't have indexes
print(a[1 : 4]) # error bez set doesn't have indexes
a[2] = 'Sec' # error
print(a * 2) # 
print(a * a) # error bez set cant have the multiple elements




# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(len(a)) # 8
print(type(a)) # class 'set'



#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R''a''m''a' 'r''A''o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25,10.8,'Hyd'}
print(set(range(10 , 20 , 3))) # {10,13,16,19}
print(set(25)) # error
print(set([25 , 10.8 , [] , 'Hyd'])) # error


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
print(type(a)) # class 'list'
print(type(b)) # class 'tuple'
print(type(c)) # class 'dict'
print(type(d)) # class 'set'
print(a) # []
print(b) # ()
print(c) # {}
print(d) # {}




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
print(a) # {25,10.8,'Hyd', True,None,'Hyd', 1}
print(len(a)) # 7
a . remove(25) # {10.8,'Hyd', True,None,'Hyd', 1}
print(a)  # {10.8,'Hyd', True,None,'Hyd', 1}
a . append(100) # error because set doesn't have the append method bez set is unordered
a . add(set()) # {10.8,'Hyd', True,None,'Hyd', 1,()}
a . add(()) # 
a . add([]) # error
print(a) # {10.8,'Hyd', True,None,'Hyd', 1,()}
a . add({}) # {10.8,'Hyd', True,None,'Hyd', 1,(),{}}





# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8} 
print('set  with  print  function') # 'set  with  print  function'
print(???) # ???
print('Iterate  thru  set  with  for  loop') # 'Iterate  thru  set  with  for  loop'
How  to  iterate  thru  set  with  for  loop #






# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} 
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))# class 'dict'
print(How  to  print  value  key  10) # Ramesh
print(How  to  print  value  key  20) # Kiran
print(How  to  print  value  key  15) # amar
print(How  to  print  value  key  18) # sita
print(a[19]) # error because there is no key value 19
print(a[0]) # error
print(a['Amar']) # 
How  to  moify  value  of   key  15  to  'Krishna' # a[15]= 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25]='vamsi'
print(a) # {10 : 'Ramesh' , 15 : 'krishna' , 18 : 'Sita', 25: 'vamsi'} 
print(len(a)) # 4
print(a * 2) # error bez dict dont accept duplicate elements





# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10:'sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b)) 4






#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # 
print(len(a))






# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b) # error
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8}





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
print('Dictionary  with  print  function') # print (a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary') # 
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
		print('Hyd') , # Hyd
		print('Sec') , # sec
		print('Cyb')  # Cyb
	}
print(type(a)) class 'set'
print(a)
print(len(a))




#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # class 'int'
a , _ , c = 10 , 20 , 30 
print(a) # 
print(_)
print(c)
for  _  in  range(5):
	print(_ , 'Hello')