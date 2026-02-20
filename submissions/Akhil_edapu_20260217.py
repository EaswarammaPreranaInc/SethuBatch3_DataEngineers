a = {25,10.8,'hyd',True,3+4j,None,25,'hyd'}

print(a) #set object with elements are printed.
print(type(a)) #class set 
print(len(a)) # 6 length, elements of objects a.
#print(a[2]) # error 
#print(a[1:4]) # Error we cannot slice the object.
#a[2] = 'sec' # we cannot modify the element of set.
#print(a*2) #No repeating of object is allowed due to duplicate of elements.
#print(a*a) #error no repeatation of object elements

# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #prints the objects of set
print(len(a)) #4
print(type(a)) #class 'set'

#  set()  function demo  program
a = set('Rama rAo') 
print(a) #{'R','a','m','' ,'r','A','o'}is printed
print(len(a)) #length is 7.
print(set([10 , 20 , 15 , 20])) #list is converted to set without duplicates.
print(set((25 , 10.8 , 'Hyd' , 10.8))) #tuple is converted to set without duplicates.
print(set(range(10 , 20 , 3))) #range is converted to set.
print(set(25)) #Error
print(set([25 , 10.8 , [] , 'Hyd'])) #mutable is cannot converted into set.


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
'''
# Find  outputs  (Home  work)
a =   [ ] #list
b =   ( ) #tuple
c =   {} #dict
d =   set() #set
print(type(a)) #class 'list'
print(type(b)) #class 'tuple'
print(type(c)) #class 'dict'
print(type(d)) #class 'set'
print(a) #[]
print(b)#()
print(c)#{}
print(d)#set()




print(a) # Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)  #{None, true, 'hyd', 10.8,25}
print(len(a)) #length is 5
a . remove(25) #removes 25 from set.
print(a)  #{None, true, 'hyd', 10.8}
a . append(100) #we use add method or function to insert element to set.
a . add(set()) #Error
a . add(()) #we can add tuple object to a set
a . add([]) Error 
print(a) #{None, true, 'hyd', 10.8,()}

 # How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop


# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #packed dict object is printed.
print(type(a)) #class 'dict'
print(How  to  print  value  key  10) 
#print(a[10])
print(How  to  print  value  key  20)
#print(a[20])
print(How  to  print  value  key  15)
#print(a[15])
print(How  to  print  value  key  18)
#print(a[18])
print(a[19]) #No key values of 19 in dictionary.
print(a[0]) #no key 0 in dict.
print(a['Amar']) #Error we cannot get key by using value in dict.
How  to  moify  value  of   key  15  to  'Krishna' 
#a[15]='krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'
#del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'
#a[25]='vami';
print(a) #{10:'Ramesh', 15:'Amar', 18:'Sita' 25:'krishna'}
print(len(a)) #length is 4
print(a * 2) #error cannot repeat dict.


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10:'sec'}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #{'R' :'Red', 'G':'Gray', 'Y':'Yellow', 'B':'Blacl'}
print(len(b)) #4


#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{True:'may be'}
print(len(a)) #1


# Find  outputs
a = { [ ] : 25} #Error
b = { ( ) : 25} #we can use tuple as dict key
print(b) # {():25}
c = { { } : 25} # cannot use dict as dict key
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #{'ramesh':[9948250500, 9848565090, 9440250404]}
print(len(d)) #1
e = {set() : 10.8} #Error


# Find  outputs
a = {}
print(type(a)) class 'dict'
print(len(a)) #0
print(a) {}
b = dict() 
print(type(b)) #class 'dict'
print(len(b)) #0
print(b) {}

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') --> #print(a)
How  to  print  dictionary  with  print()  function --> #print(a)
print('Keys  of  dictionary')  ---> # print(a.keys)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop   ---> for x in a.keys():
                                                                              print(x)
print('Values  of  dictionary')  --->  # print(a.values)
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop   --->#  for x in a.values():
                                                                                      print(x)
print('Tuples  of  dict_items   object') 
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')  
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')   ----> for x,y in a.items()
                                                        print('key':x, 'value':y)
How  to  print  each  key  and  corresponding  value  in  dict  'a' ------>  #print(a)


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) #class 'dict'
print(a) #prints hyd, sec, cyb, and last None on screen
print(len(a)) #1


#  Anonymous  object  demo  program
_ = 25
print(_) #25 prints
print(type(_)) #class 'int'
a , _ , c = 10 , 20 , 30
print(a) #10
print(_) #20
print(c) #30
for  _  in  range(5): 
	print(_ , 'Hello')
#prints 0, hello
#prints 1,hello
#prints 2,hello
#prints 3,hello
#prints 4,hello
