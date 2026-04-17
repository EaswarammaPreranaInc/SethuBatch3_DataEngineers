#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a)) # < class'set'>
print(len(a)) # 8
print(a[2]) # Error Because There Is No Index In Set
print(a[1 : 4]) # Error Because There Is No Slice In Set
a[2] = 'Sec' # Error Because its not 
print(a * 2) # Error Because There Is No Reputation In Set
print(a * a) # Error



# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1.0, 'Hyd', 0, False}
print(len(a)) # 3
print(type(a)) # < class 'set'>


#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R', ' ', 'a', 'm', 'o'} 
print(len(a)) # 6
print(set([10 , 20 , 15 , 20])) # {10, 15, 20}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # (10.8, 25, 'Hyd')
print(set(range(10 , 20 , 3))) # {10, 13, 16, 19}
print(set(25)) # Error Because Integer Is not a Sequence or iterable 
print(set([25 , 10.8 , [] , 'Hyd'])) # Error Because Sets only accept immutable elements: numbers, strings, tuples


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # []
print(b) # ()
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
a . add('Hyd')# Error Because The Element Is Already Exists
a . add(1)
print(a) # {25, 10.8, None, True, 'Hyd', 1}
print(len(a)) # 6
a . remove(25)
print(a) # {10.8, None, True, 'Hyd',1}
a . append(100) #  Error There Is no append method in set
a . add(set()) # Error Because set is Immutable
a . add(()) # Added
a . add([]) # Error Because Ser Is Immutable
print(a) # {10.8, None, 'Hyd', True, 1,()}
a . add({}) # Error Because The Set Contains Only Immutable Objects



# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???) # print(a) 
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
# a = {25 , True , 'Hyd' , 10.8}
# for i in a:
#    print(i)


# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(a[10]) # (How  to  print  value  key  10)
print(a[20]) # (How  to  print  value  key  20)
print(a[15]) # (How  to  print  value  key  15)
print(a[18]) # (How  to  print  value  key  18)
print(a[19]) # Error Invalid Key 
print(a[0]) # Error Invalid Key
print(a['Amar']) # Error Invalid key
How  to  moify  value  of   key  15  to  'Krishna' # a[15] ='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25] = 'Vamsi'
print(a) # {10 : 'Ramesh', 15 :'Krishna', 18 : 'Sita', 25: 'Vamsi'} 
print(len(a)) # 4
print(a * 2) # error because keys cannot be duplicate




# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # { 10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) # 4




#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #  { True : ' 'May  be'}
print(len(a)) # 1




# Find  outputs
a = { [ ] : 25}  # Error Key Can not be mutable object Such as list
b = { ( ) : 25}
print(b) #  { ( ) : 25}
c = { { } : 25} # Error Key Can not be mutable object Such as dict
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} #  Error Key Can not be mutable object Such as set



# Find  outputs
a = {} # Empty dictionary
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
print(a) #  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Keys  of  dictionary')
for  x   in  a . keys():  
    print(x)  # 10  <next  line>  20  <next  line>  15  <next  line>  18 <next  line>
print('Values  of  dictionary')
for  x   in  a . values(): 
    print(x)   #  Ramesh  <next  line>  Kiran  <next  line>  Amar  <next  line>   Sita  <next  line>
print('All  the  tuples  of  dict_items   object')
for   x  in  a . items():  
	print(x)  #  (10 , 'Ramesh')  <next  line>  (20 , 'Kiran')  <next  line>  (15 , 'Amar')  <next  line>  (18 , 'Sita')  <next  line>
print('Elements  of  each   tuple')
for  x , y  in  a . items(): 
		print(x , y , sep = '...')   #  10  ...  Ramesh  <next  line>  20  ...  Kiran  <next  line>  15  ... Amar  <next  line>  18   ... Sita  <next  line>
print('Keys  and  values  of  dictionary')
for   x  in a . keys(): 
	print(x , a[x] , sep = ':')   #  10  :  Ramesh  <next  line>  20  :  Kiran  <next  line>  15 :  Amar  <next  line>  18 :  Sita  <next  line>


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	} # Hyd
          # Sec
          # Cyb
print(type(a)) # < class 'set'>
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
	print(_ , 'Hello')
      # 0 Hello
      # 1 Hello
      # 2 Hello
      # 3 Hello
      # 4 Hello

