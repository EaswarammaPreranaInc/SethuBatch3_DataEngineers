#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)  # {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a))  # class set
print(len(a))   # 8
print(a[2])   #  Error
print(a[1 : 4]) # Error
a[2] = 'Sec'  # Error
print(a * 2)  # Error
print(a * a)  # Error


#  set()  function demo  program
a = set('Rama rAo')
print(a)  # ('Rama rAo')
print(len(a))  # 1
print(set([10 , 20 , 15 , 20]))  # {10 , 20 , 15 , 20}
print(set((25 , 10.8 , 'Hyd' , 10.8)))  # (25 , 'Hyd' , 10.8)
print(set(range(10 , 20 , 3)))  # {10, 13, 16, 19}
print(set(25))   # Error
print(set([25 , 10.8 , [] , 'Hyd']))  # {25 , 10.8 , [] , 'Hyd'}


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
print(a)  #  {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}

print(len(a))  # 7
print(type(a))  # class set




# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))  #  class list
print(type(b))  #  class Tuple
print(type(c)) # class set
print(type(d))  # class set
print(a) #  []
print(b) # ()
print(c)  # {}
print(d)  # {}




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
print(a) {25, 10.8, 'Hyd', True,  None, 1}
print(len(a)) # 6
a . remove(25)  
print(a)  #  {10.8, 'Hyd', True,  None, 1}
a . append(100)
a . add(set())
a . add(())
a . add([])
print(a) # {10.8, 'Hyd', True,  None, 1, 100, )
a . add({})





# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
# for i in a
	print(i)




# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))  # class int
print(How  to  print  value  key  10)  # print(a.[10])
print(How  to  print  value  key  20)  #print(a.[20])
print(How  to  print  value  key  15)  #print(a.[15])
print(How  to  print  value  key  18)  #print(a.[18])
print(a[19]) # Error
print(a[0])  # Error
print(a['Amar'])  # Error
How  to  modify  value  of   key  15  to  'Krishna'  # a.[15]='krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'      #a.del[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'         # a.add[25:'vamsi']
print(a)  # {10 : 'Ramesh' , 25 : 'vamsi' , 15 : 'Krishna' , 18 : 'Sita'}
print(len(a))  # 4
print(a * 2)  # Error




# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)  #  {10 : 'Hyd' , 10 : 'Sec'}
print(len(a))  # 2
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)   #  {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))  # 6




#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)  # {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(len(a))  # 3




# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b) # { ( ) : 25}
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)  # {'Ramesh' : [9948250500, 9848565090, 9440250404]} 
print(len(d))  # 1
e = {set() : 10.8} # 







# Find  outputs
a = {}
print(type(a))# class set
print(len(a)) # 0
print(a)   # {}
b = dict()  
print(type(b))  # class dict
print(len(b))  # 0
print(b) # {}





#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_))  # class int
a , _ , c = 10 , 20 , 30
print(a)  # 10
print(_)   #20
print(c)  #30
for  _  in  range(5):
	print(_ , 'Hello')  # 20, Hello 20, Hello 20, Hello 20,Hello