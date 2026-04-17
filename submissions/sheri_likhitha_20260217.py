#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)          #{25,10.8,'Hyd',True,3+4j,None}
print(type(a))    #class set
print(len(a))     #6
print(a[2])       #error because set is unordered 
print(a[1 : 4])   #error because set is unordered
a[2] = 'Sec'      #error because set does not support item assignment
print(a * 2)      #error because set has unique elements
print(a * a)      #error because set has unique elements


# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)          #{1,'Hyd',False,''}
print(len(a))     #4
print(type(a))    #class set


#  set()  function demo  program
a = set('Rama rAo')
print(a)           #{R,a,m,r,A,o,''}
print(len(a))      #7
print(set([10 , 20 , 15 , 20]))       #{10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))  #{25,10.8,'Hyd'}
print(set(range(10 , 20 , 3)))           #{16,10,19,13}
print(set(25))                           #error because int object is not iterable
print(set([25 , 10.8 , [] , 'Hyd']))     #error because set will not hold sub set



# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))   #class list
print(type(b))   #class tuple
print(type(c))   #class dict
print(type(d))   #class set
print(a)         #[ ]
print(b)         #( )
print(c)         #{ }
print(d)         #set()


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
print(a)          #{25,10.8,'Hyd',True,None}
print(len(a))     #5
a . remove(25)    
print(a)          #{10.8,'Hyd',True,None}
a . append(100)   #error set has no append attribute
a . add(set())    #error 
a . add(())       #error
a . add([])       #error
print(a)          #{None,True,10.8,'Hyd'}
a . add({})       #error


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(a)
for x in a:
   print(x)



# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)                                #{10:'Ramesh',20:'Kiran',15:'Amar',18:'sita'}
print(type(a))                          #class dict
print(How  to  print  value  key  10)   #a[10]
print(How  to  print  value  key  20)   #a[20]
print(How  to  print  value  key  15)   #a[15]
print(How  to  print  value  key  18)   #a[18]
print(a[19])                            #error key does not exist in the dictionary
print(a[0])                             #error
print(a['Amar'])                        #key error
How  to  moify  value  of   key  15  to  'Krishna'  #a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'     #a'.pop(20)
How  to  append  25 : 'Vamsi'  to  dict  'a'        #a[25]='Vamsi'
print(a)                                            #{10:'Ramesh',15:'Krishna',18:'sita',25:'Vamsi'}
print(len(a))                                       #4
print(a * 2)                                        #error because operator does not support in dict



# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)                 #{10:'Sec'}
print(len(a))            #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)                 #{'R':'Red','y':'Yellow','G':Grey,'B':'Black'}
print(len(b))            #4


#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)            #{True:'May be'}         
print(len(a))       #1


# Find  outputs
a = { [ ] : 25}     #error
b = { ( ) : 25}    #error
print(b)
c = { { } : 25}    #error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)                    #{'Ramesh':[9948250500,9848565090,9440250404]}
print(len(d))               #1
e = {set() : 10.8}          #error
 

# Find  outputs
a = {}
print(type(a))      #class dict
print(len(a))       #0
print(a)            #{}
b = dict()          
print(type(b))      #class dict
print(len(b))       #0
print(b)            #{}


# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)
How  to  print  dictionary  with  print()  function
print("keys of dictionary")
for key in a:
   print(key)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')
for value in a.values():
    print(value)
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')
for item in a.items():
    print(item)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')
for item in a.items():
    print(item[0],item[1])
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
for key,value in a.items():
   print(f"key:{key},value:{value}")


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,  #Hyd
		print('Sec') ,  #Sec
		print('Cyb')    #Cyb
	}
print(type(a))     #class set
print(a)           #None
print(len(a))      #1

#  Anonymous  object  demo  program
_ = 25
print(_)                     #25
print(type(_))               #class int
a , _ , c = 10 , 20 , 30     
print(a)                     #10
print(_)                     #20
print(c)                     #30
for  _  in  range(5):
	print(_ , 'Hello')   #0 Hello
                             #1 Hello
                             #2 Hello
                             #3 Hello
                             #4 Hello