#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #  {25 , 10.8 , 'Hyd' , True , 3+4j , None } in any order
print(type(a)) # class set
print(len(a)) # 6 
print(a[2]) # Error
print(a[1 : 4]) # Error
a[2] = 'Sec' # Error
print(a * 2) # Error
print(a * a) #Error

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False , '' } in any order
print(len(a)) # 4
print(type(a)) # class set

#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R' , 'a' , 'm' , ' ' , 'r' , 'A' , 'o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10 , 20 , 30} in any order
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25 , 10.8 , 'Hyd'} in any order
print(set(range(10 , 20 , 3))) # {10 ,13 , 16 , 19} in any order
print(set(25)) # Error
print(set([25 , 10.8 , [] , 'Hyd'])) # Error

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # class list
print(type(b)) # #class tuple
print(type(c)) # class dictionary
print(type(d)) # class set
print(a) #[ ]
print(b) # ( )
print(c) # { } 
print(d) # set( )

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set() #empty set
a . add(25)  # {25}
a . add(10.8) # {25 , 10.8}
a . add('Hyd') # {25 , 10.8 , 'Hyd'}
a . add(True) # {25 , 10.8 , 'Hyd' , True}
a . add(None) # {25 , 10.8 , 'Hyd' , True}
a . add('Hyd') # {25 , 10.8 , 'Hyd' , True}
a . add(1) #{25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True} in order 
print(len(a)) # 5
a . remove(25) #{ 10.8 , 'Hyd' , True}
print(a) {25 , 10.8 , 'Hyd' , True}
a . append(100) # Error
a . add(set()) # Error 
a . add(()) # {25 , 10.8 , 'Hyd' , True ,( )}
a . add([]) # Error
print(a) # {25 , 10.8 , 'Hyd' , True , ( )}
a . add({}) # Error 

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???) #print(a) ## {25 , True , 'Hyd' , 10.8} in any order
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
for x in a: # How  to  iterate  thru  set  with  for  loop
    print(x)

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #  {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # class dictionary
print(How  to  print  value  key  10) # a[10]
print(How  to  print  value  key  20) # a[20]
print(How  to  print  value  key  15) # a[15]
print(How  to  print  value  key  18)  #a[18]
print(a[19]) #Error
print(a[0]) # Error
print(a['Amar']) # Error
#a[15]='Krishna' - How  to  moify  value  of   key  15  to  'Krishna'
#del a[20] ## How  to  remove  20 :  'Kiran'  from  dict  'a'
#a[25] = 'vamsi" ##How  to  append  25 : 'Vamsi'  to  dict  'a'
print(a)  {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita' ,25 : 'vamsi'}
print(len(a)) 4
print(a * 2) # Error

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #  {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow' }
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True : 'May  be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25} # Error
b = { ( ) : 25} # valid
print(b) # { ( ) : 25}
c = { { } : 25} # Error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]} # valid 
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1 
e = {set() : 10.8} # Error

# Find  outputs
a = {} 
print(type(a)) # class dict
print(len(a)) # 0
print(a) # { }
b = dict() 
print(type(b)) # class dict 
print(len(b)) # 0
print(b) # { }

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
#print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
#for x in a.keys():
   # print(x)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')
#for x in a.values():
   # print(x)
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')
#for x in a.items():
   # print(x)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')
#for x,y in a.items():
   #  print(x,y,sep='...")
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a'
# for x in a.keys():
    # print(x,a[x],sep=':')
#  Find  outputs (Home  work)
a = {
		print('Hyd') , #none
		print('Sec') , #none
		print('Cyb') #None 
	} #print s object and returns None that is 
# Hyd
# Sec
# Cyb
print(type(a)) # class set
print(a) # {none}
print(len(a))# 1

#  Anonymous  object  demo  program
_ = 25
print(_) #25
print(type(_)) #class int
a , _ , c = 10 , 20 , 30
print(a) #10
print(_) #20
print(c) #30
for  _  in  range(5):
	print(_ , 'hello')
#0,hello
1,hello
  2,hello
  3,hello
  4,hello
