# 1.set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)         # {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a))   # <class 'set'>
print(len(a))    # 6
print(a[2])      # Error we can not access a set
print(a[1 : 4])  # Error the set not allow to slicing concept
a[2] = 'Sec'     # Error we can not replace the elements in set
print(a * 2)     # Error if we multiply two times the same list will be appeared but in set duplicates are not allowed
print(a * a)     # Error


# 2.Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)       # {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(len(a))  # 8
print(type(a)) # <class 'set'>


# 3.set()  function demo  program
a = set('Rama rAo')
print(a)                               # {'R','a','m',' ','r','A','o'}
print(len(a))                          # 7
print(set([10 , 20 , 15 , 20]))        # {10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25,10.8,'Hyd'}
print(set(range(10 , 20 , 3)))         # {10,13,16,19}
print(set(25))                         # Error
print(set([25 , 10.8 , [] , 'Hyd']))   # {25 , 10.8 , [] , 'Hyd'}


# 4.Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))  # <class 'list'>
print(type(b))  # <class 'tuple'>
print(type(c))  # <class 'dict'>
print(type(d))  # <class 'set'>
print(a)        # []
print(b)        # ()
print(c)        # {}
print(d)        # {}


# 5.Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)     # {25}
a . add(10.8)   # {25,10.8}
a . add('Hyd')  # {25,10.8,'Hyd'}
a . add(True)   # {25,10.8,'Hyd',True}
a . add(None)   # {25,10.8,'Hyd',True,None}
a . add('Hyd')  # {25,10.8,'Hyd',True,None}
a . add(1)      # {25,10.8,'Hyd',True,None,1}
print(a)        # {25,10.8,'Hyd',True,None,1}
print(len(a))   # 6
a . remove(25)   
print(a)        # {10.8,'Hyd',True,None,1}
a . append(100) # Error
a . add(set())  # Error
a . add(())     # You can add 
a . add([])     # Error
print(a)        # {10.8,'Hyd',True,None,1,()}
a . add({})     # Error the tuple is immutuable


# 6.How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  thru  set  with  for  loop')
for i in a:
   print(i)



# 7.Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)          # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))    # <class 'dict'>
print(a[10])
print(a[20])
print(a[15])
print(a[18])
print(a[19])      # Error 
print(a[0])       # Error
print(a['Amar'])  # Error
a[15] = 'Krishna'
del a[20]
a[25] = 'Vamsi'
print(a)          # {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita' , 25 : 'Vamsi'}
print(len(a))     # 4
print(a * 2)      # Error Becoz The keys get Duplicated so the dict does not allow



# 8.Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)                # {10 : 'Sec'}
print(len(a))           # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)                # {'R' : Red , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow'}
print(len(b))           # 4




# 9.Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)      # {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(len(a)) # 3



# 10.Find  outputs
a = { [ ] : 25}    # Error
b = { ( ) : 25}  
print(b)           # {( ) : 25}
c = { { } : 25}    # Error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)           # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))      # 1
e = {set() : 10.8} # # Error


# 11.# Find  outputs
a = {}
print(type(a))  # <class 'dict'>
print(len(a))   # 0
print(a)        # {}
b = dict()      
print(type(b))  # <class 'dict'>
print(len(b))   # 0
print(b)        # {}
 


# 12.How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')   
print(a)
print('Keys  of  dictionary')
print(a.keys())
print('Values  of  dictionary')
print(a.values())
print('Tuples  of  dict_items   object')
print(a.items()) 
print('Elements  of  each   tuple')
print(a.items.tuple.list())
print('Keys  and  values  of  dictionary')
print(a)


# 13.Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
    }
print(type(a))  # <class 'set'>
print(a)        # {'Hyd','Sec','Cyb'}
print(len(a))   # 3



# #  Anonymous  object  demo  program
_ = 25
print(_)                  # 25
print(type(_))            # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a)                  # 10
print(_)                  # 20
print(c)                  # 30
for  _  in  range(5):
	print(_ , 'Hello') 
''' 0 Hello
    1 Hello
    2 Hello
    3 Hello
    4 Hello
'''

