
 # 1 . # len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # output : 3
b = {}
print(len(b)) # output : 0 empty dictionary

# '''
# What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary


#---------------------------------------------------------------------------------------------

# 2 . #  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # output : 90
print(sum(a . values())) # output : 120
print(sum(a)) # output : output : 90
print(sum(a . items())) # output : Typerror 

# ----------------------------------------------------------------------------------------------

# 3 . # max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # output : 40
print(min(a . keys())) # output : 7
print(max(a . values())) # output : 50
print(min(a . values())) # output : 5
print(max(a . items())) # output : (40,5)
print(min(a . items())) # output : (7, 28)
print(max(a)) # output : 40
print(min(a)) # output : 7

#---------------------------------------------------------------------------------------------

# 4 . #  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b) # output : {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) # output : {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e)) # output : value error
f = [[10] , [20] , [30]]
print(dict(f)) # output : valueerror
print(dict([10 , 20])) # output : Typeerror
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) # output : {10: [20, 30], 40: [50, 60], 70: [80, 90]}
# h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
# print(dict(h)) # output : Typeerror
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # output : {(10, 20): 30, (40, 50): 60, (70, 80): 90}

# dict()  function
# ------------------
# 1) What  is  the  argument  of  dict()  function ?  --->
# 											Nested  sequence  such  as  list  of  tuples , list  of  lists , tuple  of  tuples , tuple  of  lists,
# 											set  of  tuples  and  so  on

# 2) What  does  dict(nested-sequence)  do ?  --->  Converts  nested  sequence  to  dictionary

# 3) How  many  elements  can  be  in  each  inner  sequence ?  ---> Exactly  two  elements
#     What  are  the  two  elements  of   each  inner  sequence ?  ---> key  and   value

# 4) Is  dict(sequence)  valid ?  --->  No  becoz  argument  is  not  a  nested  sequence


# -------------------------------------------------------------------------------------------------

# 5 . # sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) # output : [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c) # output : ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d) # output : [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f) # output : [20, 18, 15, 10, 5]
print(a) # output : {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

# ---------------------------------------------------------------------------------------------------

# 6 . Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

# 1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
#     What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

# 2) Both  input  and  output  are  dictionaries

# 3) Hint:  Use  sorted()  function

#output : 
a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
b = sorted(a.items())
c = dict(b) 
print(c)
  #(or)
a = eval(input('Enter a dictionary: ')) # {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
b = sorted(a.items())
c = dict(b)
print(c) # output : {5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}


# -------------------------------------------------------------------------------------------------------------

# 7  # clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # output : {10 : 20 , 30 : 40 , 50 : 60}
a . clear() 
print(a) # output : {}
del  a
print(a) # output : Nameerror 'a' is not defined

# -----------------------------------------------------------------------------------------------------------


# 8 . # copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) # output : {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) # output : False
print(a  ==  b) # ouptut : True

# -------------------------------------------------------------------------------------------------------

# 9 . #  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) #  output : dict_keys([10 ,20, 15, 18])
print(type(b)) # output : <class 'dict_keys'>
for  x  in   b:
        print(x) # output : 10 next 20 next 15 next 18

# '''
# 1) What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys
 
# ----------------------------------------------------------------------------------------------------

# 10 .# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) # output : dict_values(['Hyd','Sec','Cyb', 'Pune'])
print(type(b)) # <class 'dict_values'>
for  x   in   b:
	print(x) # output : 'Hyd' next 'Sec' next 'Cyb' next 'Pune'


# '''
# 1) What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values

#---------------------------------------------------------------------------------------------------

# 11 . #  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) # output : dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) # output : <class 'dict_items'>
for  x   in   b:
        print(x)# output : (10, 'Hyd')
                        #    (20, 'Sec')
                        #    (15, 'Cyb')
                        #    (18, 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ') # output : 10 ... Hyd
                                                # 20 ... Sec
                                                # 15 ... Cyb
                                                # 18 ... Pune

# '''
# 1) What  does  items()  method  do  ---> Returns  dict_items  object  which  has  list  of  tuples

# 2) What  are  the  two  elements  of  each  tuple ?  ---> (key , value)
# '''

#-----------------------------------------------------------------------------------------------------------------

# 12 . # Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
# for  x , y   in  a . items():
#        print(x , y , sep = ' ... ') # output : 10 ... Hyd
# 20 ... Sec
# 15 ... Cyb
# 18 ... Pune
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ') # output : TypeError
for  x , y   in  a . values():
      print(x , y , sep = ' ... ') # output : Error
for  x , y   in  a:
       print(x , y , sep = ' ... ') # output : Typeerror


# -----------------------------------------------------------------------------------------------------

# 13 . #  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # output : 10
print(y) # output : 20
print(z) # output : 15
print()
x , y , z = a . values()
print(x) # output : Rama
print(y) # output : Sita
print(z) # output : Rajesh
print()
x , y ,  z = a . items()
print(x) # output : (10,'Rama')
print(y) # output : (20, 'sita')
print(z) # output : (15, 'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) # output : 10 Rama
print(rno2 , sname2) # output : 20 Sita
print(rno3 , sname3) # output : 15 Rajesh

#--------------------------------------------------------------------------------------------

# # 14 .# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b) # output : {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
#a . update(b)

# ----------------------------------------------------------------------------------

# 15 . #  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a)
print(b) # output : {}
c = [(10,) , (20,) , (30,)]
#b . update(c)
print(b) # output : {}

# -----------------------------------------------------------------------------------------------------

# 16 . #  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) # output : {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))  # output : <class'dict'>

#----------------------------------------------------------------------------

# # 17 . # Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) # output : {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# ----------------------------------------------------------------------

# 18 . # Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # output : {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # output : {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}