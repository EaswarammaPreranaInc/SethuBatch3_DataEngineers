#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)   #  {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a))  # <class 'set'>
print(len(a)) # 6
print(a[2])    # error as there is no indexing in set
print(a[1 : 4])  # error as there is no slicing in set
a[2] = 'Sec'  # error since set is not modifiable
print(a * 2) # error as set doesn't have duplicates
print(a * a)  # error as set is not used for multiplication 


 # Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {False, 1, 'Hyd', ''}
print(len(a)) # 4
print(type(a)) # <class 'set'>

#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R','a','m',' ','r','A','o'} 
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10,15,20}
print(set((25 , 10.8 , 'Hyd' , 10.8)))  # {25,10.8,'Hyd'}
print(set(range(10 , 20 , 3)))  # {10,13,16,19}
print(set(25)) # error as arg should be sequence only
print(set([25 , 10.8 , [] , 'Hyd']))  # {25,10.8,'Hyd'}


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
print(type(b))  # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>

print(a) # [ ]
print(b) # ( )
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
a . add('Hyd')
a . add(1)
print(a)  # {25,10.8,'Hyd',True,None}
print(len(a)) # 5
a . remove(25)
print(a) # {10.8,'Hyd',True,None}
a . append(100) 
a . add(set())
a . add(())
a . add([])
print(a) # {10.8,'Hyd',True,(),None}
a . add({})


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
#print(a)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
# for x in a:
      print(x)  

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)  # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(How  to  print  value  key  10) # a[10]
print(How  to  print  value  key  20) # a[20]
print(How  to  print  value  key  15) # a[15]
print(How  to  print  value  key  18) # a[18]
print(a[19]) # error as key is invalid
print(a[0])   # error as key is invalid
print(a['Amar'])  #error as key is invalid

How  to  modify  value  of   key  15  to  'Krishna' # a[15] = 'krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'  # a[25] = 'Vamsi' 
print(a) # {10:'Ramesh',15: 'krishna',18:'Sita',25:'Vamsi'}
print(len(a)) # 4
print(a * 2)  # error


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10:'Sec'}
print(len(a)) # 1..
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red' ,'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))  # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True :'May  be'} 
print(len(a)) # 1

 # Find  outputs
a = { [ ] : 25} # error as keys should be immutable
b = { ( ) : 25}
print(b)  # { ( ) : 25}
c = { { } : 25} # error as keys should be immutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # error as keys should be immutable

# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a))  # 0
print(a)   # {}
b = dict()
print(type(b))  # <class 'dict'>
print(len(b))   # 0
print(b)        # {}



# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
How  to  print  dictionary  with  print()  function # print(a)
print('Keys  of  dictionary') # print(a.keys())
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
# for key in a:
      print(key)
print('Values  of  dictionary')  # print(a.values())
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
#  for x in a:
      print(x,a[x])
print('Tuples  of  dict_items   object')  #print(a.items())
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
# for i in a.items():
      print(i) 
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
# for i,j in a.items():
      print(i,j) 
How  to  print  each  key  and  corresponding  value  in  dict  'a'
# print(a)

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))  # <class 'set'>
print(a)   # {None,None,None} as print does not return anything 
print(len(a)) # 3

#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a)# 10
print(_)# 20
print(c)# 30
for  _  in  range(5):
	print(_ , 'Hello') 
 '''
0 Hello
1 Hello
2 Hello
3 Hello
4 Hello
'''
