# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)   # (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))  # <class 'tuple'>
a[3] = 'Sec'    # Error
a[3 : 6] = 60 , 70 , 80   # Error




#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #  (1, 2, 3) Addres of a
a += b    # (1, 2, 3, 4, 5, 6) concatenation
print(a , id(a))  # (1, 2, 3, 4, 5, 6) address of a




#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) # (1 , 2 , 3)  address of a
a = a + b   # (1, 2, 3, 4, 5, 6)
print(a , id(a))  # (1, 2, 3, 4, 5, 6) Address of a  




#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)   # (10,20,30,40)
print(type(a))  # <class 'str'>
b = eval(a)
print(b)  # (10,20,30,40)
print(type(b)) # <class 'tuple'>
print(len(b))  # 4





# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) # (10, [70, 30, 40], 50, 60)
a[1] = [80 , 90 , 100]   
print(a)






# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)  # Error
a[1] = [80 , 90]
print(a)  # Error






# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)     #  (25, 10.8, 'Hyd', True)

print(type(x))   # <class 'tuple'>





# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)  # 25
print(b)   # 10.8
print(c)  # Hyd
print(d)  # True
p , q , r =  x  # Error
a , b , c , d  , e = x  # Error





# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)  # 25
print(b)  # 10.8
print(c)  # ['Hyd', True]
print(type(c))  # <class 'list'>




# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # 25
print(b)  # [10.8, 'Hyd']

print(c) # True




# add()  method  demo  program  (Home  work)
a = set()
a . add(True)
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a)  
a . add(10 , 20 , 30)
a . add([10,20,30])


'''
add()   method
-----------------
1) What  does  add(x)  do ?  --->  Inserts   'x'  any  where  in  the  set  becoz  set  is  unordered

2) How  many  arguments  can  add()  method  take ?  --->  Single

3) Is  set . add(mutable-object)  valid ? --->  No  becoz  set  can  not  hold  mutable  element

4) In  other  words,  argument  of  add()  method  should  be  immutable  object  only

5) What  does  set .  add(sequence)  do  ?  --->
																Inserts  sequence  any  where  in  the  set  but  not  elements  of  sequence
																(Like  append()  method  of  list  class)
'''
    
    
    
    
    






# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)   # {True, 25, 10.8, 'Hyd'}
print(id(a))  # Addres 
a . add(tpl)  
a . add('Sec')
print(a)   # {True, 25, 10.8, 'Hyd', (10, 20, 30), 'Sec'}
print(id(a))  # Address
print(len(a))  # 6
a . add([100 , 200 , 300])
a . add(set())
a . add({ })






# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) 
print(s)  #  {(10, 20, 15, 18)}
print(len(s))  #  1






# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s)      # {10, 20, 15, 18}
s . update(25)


'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  --->  Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                         (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  ---> One  (or)  more
'''




# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)   # {10, 20, 30, 40, 50, 60, 70}
print(len(s)) # 7
s . add(a , b , c)
    
    
    
    
    
# Find  outputs  (Home  work)
a = set() 
a . update('Rama Rao')
print(a)  # {'a', 'o', 'R', ' ', 'm'}
print(len(a))  # 5
a . update(3 + 4j , 10.8 , True)
    
    
    
    
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)   # {10, 20, 15, 18}
b = a . copy()
print(b)   # {10, 20, 15, 18}
print(a  is  b)  # False
print(a  ==  b)  # True
c = a
print(a  is  c)   # True


'''
copy()  method
------------------
1) What  does  copy()  method  do ?  ---> Returns  a  new  set  with  same  elements

2) a = b
    What  does  the  statement  do ?  --->  Reference  copy
																   i.e.  id  is  copied

3) What  is  shallow  clone ?  ---> Reference  copy
     What  is  deep  clone ?  --->  Object  copy
''' 
    
# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25, 10.8, 'Hyd', True}
print(a . pop())   # 25
print(a . pop())   # 10.8
print(a . pop())    # Hyd
print(a . pop())  # True
print(a . pop())   # error
print(a) 
b = {10 , 20 , 30 , 40}
print(b . pop(2))  # erroe


'''
pop()  method
----------------
1) What  does  pop(No-args)  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  ---> Zero
'''
    
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25, 10.8, 'Hyd', True}
a . remove('Hyd')
print(a)   # {25, 10.8, True}
a . remove('Sec')    # Error


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
''' 
    
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
a . discard('Hyd')
print(a) # {25, 10.8, True}
a . discard('Sec')
print(a)  # {25, 10.8, True}
a . remove('Sec')


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''
      
    
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10, 20, 15, 18}
a . clear()
print(a) # set()
print(len(a)) # 0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''
    
    
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))
print(a | b)
print(b . union(a))
print(a + b)





#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)
print(type(c))
d = a & b
print(d)
print(type(d))
print(c  is  d)
print(c  ==  d)


'''
intersection()  method
---------------------------
1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

2) Is  set . intersection(list)  valid  ?  --->
							Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  another  way  to  obtain  common  elements ?  ---> a & b

4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

5) Is  list . intersection(set)  valid ?  --->  No  becoz  there  is  no  intersection()  method  in  list  class
'''


# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)  # {10, 20}
print(type(c))  # <class 'set'>
d = a - b
print(d)  # {10, 20}
print(type(d)) # <class 'set'>
print(c  is  d)  # False
print(c  ==  d)  # True


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->  
										Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''



# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)  # {10, 20, 50, 60}
print(type(c))  # <class 'set'>
d = a ^ b
print(d)  # {10, 20, 50, 60}
print(type(d))  # <class 'set'>
print(c   is   d)  # False
print(c  ==   d)   # True


'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
						                                                              without  common  elements																				  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_…
[1:04 pm, 14/3/2026] +91 99482 50500: # Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)
print(type(a))
'''


#(Home  work)Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
'''
1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''

s = input("Enter String : ")
st = set(s)        
res = ''.join(st)  
print(res)




'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''


a = eval(input("Enter List : "))
s = set(a)        
res = list(s)    
print(res)


'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

a = eval(input("Enter 1st List : "))
b = eval(input("Enter 2nd List : "))
s1 = set(a)
s2 = set(b)
res = list(s1 & s2)
print(res)