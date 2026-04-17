
# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))        #3
b = {}
print(len(b))        #0


#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))               #10+30+50=90
print(sum(a . values()))             #20+40+60=120
print(sum(a))                        #90(default keys are taken)
print(sum(a . items()))              #error due to + between int and tuple


# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))                         #40
print(min(a . keys()))                         #7
print(max(a . values()))                       #50
print(min(a . values()))                       #5
print(max(a . items()))                        #(40,5)
print(min(a . items()))                        #(7,28)
print(max(a))                                  #40
print(min(a))                                  #7

# dict()  function  demo program (Home  work)

a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b)                  # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}

c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)                  # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}

e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
# print(dict(e))          #error because dictionary update sequence element #0 has length 3; 2 is required

f = [[10] , [20] , [30]]
# print(dict(f))          #error because dictionary update sequence element #0 has length 1; 2 is required

# print(dict([10 , 20]))  #error because cannot convert dictionary update sequence element #0 to a sequence

g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))           #{10: [20, 30], 40: [50, 60], 70: [80, 90]}

h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
# print(dict(h))         #error because unhashable type: 'list'

i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))           #{(10, 20): 30, (40, 50): 60, (70, 80): 90}



'''
dict()  function
------------------
1) What  is  the  argument  of  dict()  function ?  ---> Nested  sequence  such  as  list  of  tuples, list  of  lists, etc.
'''



# sorted()  function  (Home  work)

a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}

b = sorted(a.keys())
print(b)                    #[5, 10, 15, 18, 20]

c = sorted(a.values())
print(c)                    #['Blue', 'Green', 'Red', 'White', 'Yellow']

d = sorted(a.items())
print(d)        #[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]

f = sorted(a, reverse=True)
print(f)                 #[20, 18, 15, 10, 5]

print(a)                 #{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}



'''


Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
   What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}
2) Both  input  and  output  are  dictionaries
3) Hint:  Use  sorted()  function
'''

CODE:

x = input("enter dictionary :")
y = eval(x)
z = dict(sorted(y.items()))
print(z) # {5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}



# clear()  method  demo  program (Home  work)

a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)                         #{10: 20, 30: 40, 50: 60}
a.clear() 
print(a)                         #{}

del a
print(a)                       #error because name 'a' is not defined



# copy()  method demo  program  (Home  work)

a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a.copy()
print(b)                     #{'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a is b)                #False
print(a == b)                #True



# keys()  method  demo  program

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a.keys()
print(b)                      #dict_keys([10, 20, 15, 18])
print(type(b))                #<class 'dict_keys'>

for x in b:
    print(x) # 10
             # 20
             # 15
             # 18

'''
1) What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys
'''



# values()  method  demo  program

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a.values()
print(b) # dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) # <class 'dict_values'>

for x in b:
    print(x) # 'Hyd'
             # 'Sec'
             # 'Cyb'
             # 'Pune'

# 1) What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values



# items()  method  demo  program

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a.items()
print(b)              #dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))        #<class 'dict_items'>

for x in b:
    print(x) # (10, 'Hyd')
             # (20, 'Sec')
             # (15, 'Cyb')
             # (18, 'Pune')

for x , y  in b:
    print(x , y , sep = ' ... ') # 10 ... Hyd
                                 # 20 ... Sec
                                 # 15 ... Cyb
                                 # 18 ... Pune

# 1) What  does  items()  method  do  ---> Returns  dict_items  object  which  has  list  of  tuples
# 2) What  are  the  two  elements  of  each  tuple ?  ---> (key , value)



# Find  outputs (Home  work)

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}

for x , y  in a.items():
    print(x , y , sep = ' ... ') # 10 ... Hyd
                                 # 20 ... Sec
                                 # 15 ... Cyb
                                 # 18 ... Pune

for x , y  in a.keys(): 
    print(x , y , sep =' ... ')    #error because cannot unpack non-iterable int object
for x , y  in a.values():
 print(x,y , sep = '...')         #error because not enough values to unpack
for x , y  in a:
 print(x,y , sep = '...')       #error because cannot unpack non-iterable int object


# Find  outputs  (Home  work)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}

x , y , z = a.keys()
print(x)                    #10
print(y)                    #20
print(z)                    #15

x , y , z = a.values()
print(x)                    #'Rama'
print(y)                    #'Sita'
print(z)                    #'Rajesh'

x , y , z = a.items()
print(x)                    #(10, 'Rama')
print(y)                    #(20, 'Sita')
print(z)                    #(15, 'Rajesh')

(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a.items()
print(rno1 , sname1)        #10 Rama
print(rno2 , sname2)        #20 Sita
print(rno3 , sname3)        #15 Rajesh



'''
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order
(ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  --->  {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

1) String to uppercase: 'RAMA RAO'
2) Result of sorted('RAMA RAO'): [' ' , 'A' , 'A' , 'A' , 'M' , 'O' , 'R' , 'R']
3) Initially a = {}
... (Logic steps follow)
'''

CODE:

s = input("enter a string:")
s = s.upper()
l = sorted(s)

a = {}
for i in l:
    if i.isalpha():
        a[i] = a.get(i, 0) + 1

print("result:", a) 

Output: {'A': 3, 'M': 1, 'O': 1, 'R': 2}



# Find outputs (Home  work)

a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b.update(a)
print(b)               #{'Y': 'Yellow', 'G': 'Green', 'B': 'Blue', 'R': 'Red'}

a.update(b)            #error because 'list' object has no attribute 'update'



# Find  outputs  (Home  work)

a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)           #error because dictionary update sequence element #0 has length 3; 2 is required

c = [(10,) , (20,) , (30,)]
b.update(c)           #error because dictionary update sequence element #0 has length 1; 2 is required



# Find outputs (Home  work)

d = {x : x ** 3   for    x    in  range(5)}
print(d)                   #{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))             #<class 'dict'>



# Find outputs   (Home  work)

d = { x :  2 * x    for    x    in   range(5) }
print(d)                   #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}



# Find outputs  (Home  work)

a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}

b = { k :  v  for   k , v  in   a.items()   if    k % 2 != 0}
print(b)                     #{15: 'Sita', 17: 'Kiran'}

c = {k : a[k]   for   k   in    a    if   a[k].startswith('R')}
print(c)                     #{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}



