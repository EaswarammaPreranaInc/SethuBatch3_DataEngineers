#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)  # {25, 10.8, 'Hyd', True, 3+4j, None}
print(type(a))  # <class 'set'>
print(len(a))  # 6
print(a[2])  # error #indexing is not possible in set
print(a[1 : 4])  # error #slicing is not permitted
a[2] = 'Sec'  # error #modifing is not permitted because set is unordered
print(a * 2)  # error #repetation is not permitted because set don't allow duplicates
print(a * a)  # error


# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)  # {False , 1 , '' , 'Hyd'}
print(len(a))  # 4
print(type(a))  # <class 'set'>


#  set()  function demo  program
a = set('Rama rAo')
print(a)  # {'R', 'a', 'm', ' ', 'r', 'o', 'A'}
print(len(a))  # 7
print(set([10 , 20 , 15 , 20]))  # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))  # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))  # {10, 13, 16, 19}
print(set(25))  >>  error #non-sequence element is not converted to set
print(set([25 , 10.8 , [] , 'Hyd']))  # error becoz list is mutable, set doesn't allow mutable objects during conversion


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a)  # []
print(b)  # ()
print(c)  # {}
print(d)  # set()


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
print(a)  # {25, 10.8, 'Hyd', True, None}  #True == 1
print(len(a))  # 5
a . remove(25) 
print(a)  # {10.8, 'Hyd', True, None}
a . append(100)  # error append is permitted only in list
a . add(set())  #  error nested set is not permitted
a . add(())  # {10.8, 'Hyd', True, None, ()}
a . add([])  # error list is mutable set doesn't allow mutable objects 
print(a)  # {10.8, 'Hyd', True, None, ()}
a . add({}) # error  set is mutable so set is not permitted



# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')   # print(a)
print(a)  >>  {25, True, 'Hyd', 10.8}
print('Iterate  thru  set  with  for  loop')  # for i in a:
How  to  iterate  thru  set  with  for  loop           print(i)  # 25
                                                                   True
                                                                   Hyd
                                                                   10.8



# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)  # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))  # <class 'dict'>
print(How  to  print  value  key  10)  #  a[10]
print(How  to  print  value  key  20)  #  a[20] 
print(How  to  print  value  key  15)  #  a[15]
print(How  to  print  value  key  18)  #  a[18]
print(a[19])  >>  error #there is no 19 key
print(a[0])  >>  error #there is no 0 key
print(a['Amar'])  >>  error #because by using value key is not return 
How  to  modify  value  of   key  15  to  'Krishna'  # a[15] = 'Krishna' 
How  to  remove  20 :  'Kiran'  from  dict  'a'  # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'  # a[25] = 'Vamsi'
print(a)  #  {10 : 'Ramesh' ,  15 : 'Krishna' , 18 : 'Sita', 25 : 'Vamsi'}
print(len(a))  #  4
print(a * 2)  #  error #repetation is not permitted



# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)  #  {10 : 'Sec'}
print(len(a))  #  1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)  #  {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow' }
print(len(b))  #  4


#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)   # {True : 'May be'}
print(len(a))  #  1


# Find  outputs
a = { [ ] : 25}  #error key should be immutable
b = { ( ) : 25} 
print(b)  #  {() : 25}
c = { { } : 25}  #  error #set is mutable so dict keys must be immutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)  #  {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))  #  1
e = {set() : 10.8}  # error


# Find  outputs
a = {}
print(type(a))  # <class 'dict'>
print(len(a))  #  0
print(a)  # {}
b = dict()
print(type(b))  # <class 'dict'>
print(len(b))  #  0
print(b)  #  {}



# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')  #  print(dict())
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')  #  dict_keys([10 , 20 , 15 , 18])
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop   # for i in a.keys():
                                                                             print(i)
                                                                                   10
                                                                                   20
                                                                                   15
                                                                                   18

print('Values  of  dictionary')  >>  dict_values(['Ramesh' , 'Kiran' , 'Amar' , 'Sita'])
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop  # for i in a.values():
                                                                             print(i)
                                                                                   Ramesh
                                                                                   Kiran
                                                                                   Amar
                                                                                   Sita

print('Tuples  of  dict_items   object')  dict_items([(10,'Ramesh') , (20,'Kiran') , (15,'Amar') , (18,'Sita')])
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop  # for i in a.items():
                                                                             print(i)
                                                                                   10 Ramesh
                                                                                   20 Kiran
                                                                                   15 Amar
                                                                                   18 Sita

print('Elements  of  each   tuple')  # (10,'Ramesh') , (20,'Kiran') , (15,'Amar') , (18,'Sita')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object  # print(a.items())
print('Keys  and  values  of  dictionary')  #  for i,j in a.items():
                                                        print(i,j)
                                                              10 Ramesh
                                                              20 Kiran
                                                              15 Amar
                                                              18 Sita
How  to  print  each  key  and  corresponding  value  in  dict  'a'  # print()
                                                


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))  # <class 'set'>
print(a)  # 'Hyd'
            'Sec'
            'Cyb'
             None
print(len(a)) # 1



#  Anonymous  object  demo  program
_ = 25
print(_)  # 25
print(type(_))  # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a)  #  10
print(_)  # 20
print(c)  #  30
for  _  in  range(5):
	print(_ , 'Hello')  #   0 Hello
                                1 Hello
                                2 Hello
                                3 Hello
                                4 Hello