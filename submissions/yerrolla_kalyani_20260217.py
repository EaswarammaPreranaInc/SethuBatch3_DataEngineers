 #  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)		#{ 10.8 , 'Hyd' , True , 3+4j , None , 25 }in any order
print(type(a))		#<class 'set'>
print(len(a))		#6
print(a[2])		# error set is not indexed so we cant access to the a[2]
print(a[1 : 4])		# error set is not indexed so we random accessing is not possible
a[2] = 'Sec'		#  error modifications are not possible in set they are not indented
print(a * 2)		# error reapeatation is not allowed in set i.e,set not contain duplicate values
print(a * a)		#error in repeatation the 2nd arg should be non int and set ,so doesn't support the repeation


#  set()  function demo  program
a = set('Rama rAo')
print(a)				#{'R','a','m','r','A','o',''}
print(len(a))				#7
print(set([10 , 20 , 15 , 20]))		#{10 , 20 , 15 }in any order
print(set((25 , 10.8 , 'Hyd' , 10.8)))	#{25 , 10.8 , 'Hyd' }in any order
print(set(range(10 , 20 , 3)))		#{10,16,13,19}in any order
print(set(25))				#error  becoz  argument  should  be  sequence  only
print(set([25 , 10.8 , [] , 'Hyd']))	#error set should not contain sequences like list,dict,tuple.


# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)			# {1,'Hyd','',false}in any order
print(len(a))			#4
print(type(a))			#<class 'set'>


 # Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))		#<class 'list'>
print(type(b))		#<class 'tuple'>
print(type(c))		#<class 'set'>
print(type(d))		#<class 'set'>
print(a)		#[]
print(b)		#()
print(c)		#{}
print(d)		#set()


 # Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)		#{25}
a . add(10.8)		#{25,10.8}in any order
a . add('Hyd')		#{25,10.8,'Hyd'}in any order 
a . add(True)		#{25,10.8,'Hyd',1}in any order 
a . add(None)		#{25,10.8,'Hyd',1,None}in any order
a . add('Hyd')		#error set does not take duplicate values
a . add(1)		#{25,10.8,'Hyd',1,None}
print(a)		#{25,10.8,'Hyd',1,None}in any order
print(len(a))		#5
a.remove(25)		#{10.8,'Hyd',1,None}in any order
print(a)		#{10.8,'Hyd',1,None}in any order
a . append(100)		#append method is not allowed in set only add() method
a . add(set())		#error becoz nested set is not allowed .set contain only immutable elements
a . add(())		#{10.8,'Hyd',1,None,()}
a . add([])		#error set cannot contain mutable elements.like list ,tuple ,dict 
print(a)		# {10.8,'Hyd',1,True,None}in any order
a . add({})		#error because set does not contain mutable elements like dictionary


 # How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')			#print(a)
print(???)#print(a)
print('Iterate  thru  set  with  for  loop') 		#sequential accessing
							#for x in a
							#print(x)
How  to  iterate  thru  set  with  for  loop 		#sequentioal access
 # Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)						#{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))						#<class'dict'>
print(How  to  print  value  key  10)			#a[10]
print(How  to  print  value  key  20)			#a[20]
print(How  to  print  value  key  15)			#a[15]
print(How  to  print  value  key  18)			#a[18]
print(a[19])						#error no key 19 present in dictionary a
print(a[0])						#error no key 0 present in dictionary a
print(a['Amar'])					#error becoz based on key we can get value .Amar is not a key
How  to  moify  value  of   key  15  to  'Krishna'	#a[15]='Krishna'#{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'krishna' , 18 : 'Sita'}
How  to  remove  20 :  'Kiran'  from  dict  'a'		#del a[20]#{10 : 'Ramesh' ,  15 : 'krishna' , 18 : 'Sita'}
How  to  append  25 : 'Vamsi'  to  dict  'a'		#a[25]='Vamsi'
print(a)						##{10 : 'Ramesh' ,  15 : 'krishna' , 18 : 'Sita', 25 :'vamsi'}
print(len(a))						##4
print(a * 2)						#repeation is not allowed in dictionary bcoz duplicates of keys  are not allowed
 

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)						#{ 10 : 'Sec'}
print(len(a))						#1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) 						#{'R' : 'Red'   , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow' }
print(len(b))						#4
 

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)						#{True : 'May  be'}
print(len(a))						#1
 # Find  outputs
a = { [ ] : 25}						#error becoz keys should be immutable  but list is mutable 
b = { ( ) : 25}						#{():25} becoz tuple is immutable.
print(b)						##{():25}
c = { { } : 25}						#error becoz keys should be immutable  but set is mutable 
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)						#{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))						#1
e = {set() : 10.8}					# error becoz keys must be immutable but set is mutable


 # Find  outputs
a = {}
print(type(a))				#<class 'dict'>
print(len(a))				#0
print(a)				#{}
b = dict()
print(type(b))				#<class 'dict'>
print(len(b))				#0
print(b)				#{}
 

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')				#print(a)
How  to  print  dictionary  with  print()  function			#print(a)
print('Keys  of  dictionary')						#print(a.keys())#dict_keys([10,20,15,18])
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop	#for x in a.keys():
									#print(x)
print('Values  of  dictionary')						#print(a.values())ie.,  #dict_keys([ 'Ramesh' , 'Kiran' , 'Amar' ,'Sita'])
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop	#for x in a.values():
									#print(x)


print('Tuples  of  dict_items   object')					#print(a.items()) #ie.,dict_items([(10 : 'Ramesh' ),  (20 : 'Kiran' )(, 15 : 'Amar') , (18 : 'Sita')])
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop		#for x in a.items():
										#print(x)
print('Elements  of  each   tuple')					
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object#for x,y in a.items()
										#print(x,y,sep='_')

print('Keys  and  values  of  dictionary')					
How  to  print  each  key  and  corresponding  value  in  dict  'a'		#for key,value in a.items():
										#print (key,":",value)
 


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))				#<class 'set'>
print(a)				#{none}
print(len(a))				#1


 #  Anonymous  object  demo  program
_ = 25
print(_)				#25
print(type(_))				#<class 'int'>
a , _ , c = 10 , 20 , 30
print(a)				#10
print(_)				#20
print(c)				#30
for  _  in  range(5):
	print(_ , 'Hello')		#0 Hello
					#1 Hello
					#2 Hello
					#3 Hello
					#4 Hello