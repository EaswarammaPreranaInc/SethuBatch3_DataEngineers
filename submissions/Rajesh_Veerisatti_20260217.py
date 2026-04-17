#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j , None }
print(type(a))# <class 'set'>
print(len(a)) # 6
#print(a[2]) # error in set elements are unorder
#print(a[1 : 4])# error in set elements are unorder
#a[2] = 'Sec' # error set is not allows replacing
#print(a * 2) # error set have no dupilicate elements so repetation is not allowed
#print(a * a)# error set have no dupilicate elements so repetation is not allowed



# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , '' ,  0}
print(len(a)) # 4
print(type(a)) # <class 'set'>



#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R','a','m',' ','r','A','o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10,15,20}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25,10.8,Hyd}
print(set(range(10 , 20 , 3))) # set(range of indexes from 10to19 in steps of 3)# set(10,13,16,19) # {10,13,16,19}
#print(set(25)) # error int can not consisted in tuple
#print(set([25 , 10.8 , [] , 'Hyd'])) # error in set lists are not allowed bcz list is mutable


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
print(type(a)) #<class 'list'>
print(type(b))  #<class 'tuple'>
print(type(c))  #<class 'set'>
print(type(d))  #<class 'set'>
print(a) # []
print(b) # ()
print(c) #{}
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
print(a) # { 25,10.8,Hyd,1,None}
print(len(a)) # 5
a . remove(25)
print(a) # {10.8,Hyd,1,None}
#a . append(100) #  error append is not allowed in set
#a . add(set()) # error set inside the set is not allowed
a . add(()) #  set inside the tuple is allowed # {10.8,Hyd,1,None,()}
#a . add([]) # error set inside the list is not allowed
print(a)  # {10.8,Hyd,1,None,()}
#a . add({})



# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') # print (a) # print (set(25 , True , 'Hyd' , 10.8)
# print(???) # print (a)
print('Iterate  thru  set  with  for  loop') # for x in a:
                                                  #print(x)
#How  to  iterate  thru  set  with  for  loop



# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class'dict'>
#print(How  to  print  value  key  10) # print a[10]
#print(How  to  print  value  key  20) # print a[20]
# print(How  to  print  value  key  15) # print a[15]
#print(How  to  print  value  key  18) # print a[18]
# print(a[19]) # error dict not having key 19
#print(a[0])  # error dict not having key 0
# print(a['Amar']) # error dict not allow value to key
# How  to  moify  value  of   key  15  to  'Krishna' # a[15]='Krishna'
# How  to  remove  20 :  'Kiran'  from  dict  'a'# a.del[20]
# How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25]='Vamsi'
print(a) #  {10 : 'Ramesh' , 25 : 'Vamsi' , 15 : 'Krishna' , 18 : 'Sita'}
print(len(a)) # 4
# print(a * 2) # error repetation is not allowed bcz dupilicate elements are not exists in dict



# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red'  , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) # 4



#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # { 1.0 : 'May  be'}
print(len(a)) # 1




# Find  outputs
#a = { [ ] : 25} # error list can not exist in dict keys
b = { ( ) : 25}
print(b) # { ( ) : 25}
#c = { { } : 25} # error nested dict are not allowed
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
#e = {set() : 10.8} # error set is not allowed as keys in dict



# Find  outputs
a = {}
print(type(a)) # <class'dict'>
print(len(a)) # 0
print(a) # {}
b = dict() 
print(type(b)) # <class'dict'>
print(len(b)) # 0
print(b) # {}



# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') #  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
 # How  to  print  dictionary  with  print()  function  # print (a)
print('Keys  of  dictionary')  #10
                               #20
                               #15
                               #18
 # How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop # for x in a:
                                                                    # print (x)
print('Values  of  dictionary') #Ramesh
                                #Kiran
                                #Amar
                                #Sita
# How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop # for x in a.values():
                                                                    # print(x)
print('Tuples  of  dict_items   object')#10 Ramesh
                                        #20 Kiran
                                        #15 Amar
                                        #18 Sita
# How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop # for x in a.items():
                                                                     #  print(x)
print('Elements  of  each   tuple')#10 Ramesh
                                   #20 Kiran
                                   #15 Amar
                                   #18 Sita
# How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object # for t in a.items():
                                                                                  # print(x[0], x[1])
print('Keys  and  values  of  dictionary')#10 Ramesh
                                          #20 Kiran
                                          #15 Amar
                                          #18 Sita
# How  to  print  each  key  and  corresponding  value  in  dict  'a'# for k, v in a.items():
                                                                     #print(k, v)




#  Find  outputs (Home  work)
# a = {print('Hyd') ,
# print('Sec') ,
# print('Cyb')
#}
print(type(a)) # <class'set'>
print(a) # {None}
print(len(a)) # 1



#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
  print(_ , 'Hello') #0 Hello
                   #1 Hello
                   #2 Hello
                   #3 Hello
                   #4 Hello