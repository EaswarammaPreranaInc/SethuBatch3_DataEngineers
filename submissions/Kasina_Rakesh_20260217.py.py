#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a)) # class<set>
print(len(a)) # 8
print(a[2])  # 'Hyd'
print(a[1 : 4]) # 10.8 , 'Hyd' , True
a[2] = 'Sec'  #error
print(a * 2) #error
print(a * a) #error



# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # 1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0 
print(len(a)) # 8
print(type(a)) # class<set>



#  set()  function demo  program
a = set('Rama rAo')
print(a)  # r,a ,m ,o repeating elements can be ignored
print(len(a)) # 4
print(set([10 , 20 , 15 , 20])) #
print(set((25 , 10.8 , 'Hyd' , 10.8))) # error cant be sequence
print(set(range(10 , 20 , 3))) # 10 13 16 19
print(set(25)) # 25
print(set([25 , 10.8 , [] , 'Hyd'])) # 25 , 10.8 , [] , 'Hyd'


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set




# Find  outputs  (Home  work)
a =   [ ] # empty
b =   ( ) # empty
c =   {} # empty
d =   set()
print(type(a)) # class list
print(type(b)) # class tuple
print(type(c)) # class dict
print(type(d)) #class set
print(a) #empty
print(b) #empty
print(c) #empty
print(d) #empty





# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)  #{25}
a . add(10.8) #{25 ,10.8}
a . add('Hyd') #{25 ,10.8,'Hyd'}
a . add(True) #{25 ,10.8,'Hyd',True}
a . add(None) #{25 ,10.8,'Hyd',True,None}
a . add('Hyd') #{25 ,10.8,'Hyd',True,None,'Hyd'}
a . add(1) #{25 ,10.8,'Hyd',True,None,'Hyd',1}
print(a) # 25 ,10.8,'Hyd',True,None,'Hyd',1
print(len(a)) #7
a . remove(25) #{10.8,'Hyd',True,None,'Hyd',1}
print(a) #10.8,'Hyd',True,None,'Hyd',1
a . append(100) #error
a . add(set()) #error 
a . add(()) #empty
a . add([])
print(a)
a . add({})






# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop




# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # 10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'
print(type(a)) # class <Dict>
print(How  to  print  value  key  10) #a[10] = 'Ramesh'
print(How  to  print  value  key  20) #a[20] = 'Kiran'
print(How  to  print  value  key  15) #a[15] = 'Amar'
print(How  to  print  value  key  18) #a[18] = 'sita'
print(a[19]) #error
print(a[0]) # error
print(a['Amar']) #error
How  to  moify  value  of   key  15  to  'Krishna' # a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # a.remove[25]
How  to  append  25 : 'Vamsi'  to  dict  'a' # error
print(a) # 10 : 'Ramesh' , 20 : 'Krishna' , 15 : 'Amar' , 18 : 'Sita'
print(len(a)) #4
print(a * 2) #error





# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # 10 : 'Sec'
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'
print(len(b) # 6







#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'
print(len(a)) #3





# Find  outputs
a = { [ ] : 25} #error list cant be
b = { ( ) : 25} 
print(b) # ( ) : 25
c = { { } : 25} #error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # 'Ramesh' : [9948250500, 9848565090, 9440250404
print(len(d))  #1
e = {set() : 10.8}





# Find  outputs
a = {}
print(type(a)) # class dict
print(len(a)) #1
print(a) #<empty >
b = dict()
print(type(b)) #class dict
print(len(b))# 0
print(b) <empty>




#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) # class <Suite>
print(a) # 'Hyd'
	   'Sec'
	   'Cyb' 
print(len(a)) #3