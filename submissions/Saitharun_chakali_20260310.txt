Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)
print(a  ==  b)
b[2] = 12
print(a)

output:
True
True
[10, 20, 12, 18]


2.  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)
print(a + 5)                # Error
print(a + '5')              # Error
print([10 , 20] + (30 , 40))# Error

output:
[10, 20, 15, 18, 100, 200, 150]



3.Tricky  program
# Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a))
a += b
print(a , id(a))

output:
[1, 2, 3]          #address of a
[1, 2, 3, 4, 5, 6] #address of a




4.Tricky  program
# Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a))
a  = a + b
print(a , id(a))

output:
[1 , 2 , 3]  address of a
[1 , 2 , 3, 4 , 5 , 6]  address of another a 




5. Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print(type(b))
x , *y = list
print('x : ' , x)
print('y : ' , y)
*p , q = list
print('p : ' , p)
print('q : ' , q)

output:
a :  25
b :  [10.8, 'Hyd']
c :  True
<class 'list'>
x :  25
y :  [10.8, 'Hyd', True]
p :  [25, 10.8, 'Hyd']
q :  True



6.Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list               # Error
a , b , *c , d , e = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
a , b , *c , d , e , f = list          # Error


output:

a :  25
b :  10.8
c :  []
d :  Hyd
e :  True





7.Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)
print('b : ' , b)
print('_ :  ' , _)
print('d : ' , d)


output:
a :  25
b :  10.8
_ :   Hyd
d :  True



8.Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)
print('b : ' , b)
print('d : ' , d)

output:
a :  (3+4j)
b :  10.8
d :  True


9.Tricky  program
 Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)
print('b : ' , b)
print('_ : ' , _)
print('d : ' , d)
print('_: ' , _)

output:
a :  25
b :  10.8
_ :  (3+4j)
d :  True
_:  (3+4j)



10.# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list


output:
Error



11.# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)
print('b :  ' , b)
print('c :  ' , c)

output:
a :   [25, 10.8]
b :   Hyd
c :   True


12.# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
a , b , c , d = list    # Error


output:
a :  25
b :  10.8
c :  Hyd
d :  True


13.# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)
print(a  is   b)
print(a < c)
print(a > d)
print(a >= c)
print(a <= d)
print(a != c)
print(a != b)
print(a == c)


output:
True
False
True
True
False
False
True
False
False



14.# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)
print(a  is   b)

output:
False
False


15.#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))
b = []
print(len(b))
c = [[10 , 20] , 30 , 40]
print(len(c))

'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''

output:
4
0
3


16.# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))
b= [3 + 4j , 5 + 6j]
print(sum(b))
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))
d = [10 , 20 , 15 , 18]
print(sum(d))
e = [25 , 10.8 , 'Hyd' , True]   
print(sum(e))                   # Error


'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements



output:
36.8
(8+10j)
(39.8+4j)
63



17.#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a))
print(sum(a[0]))
print(How  to  determine  sum  of  inner  list  elements  in  another  way)



18.# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))
print(min(a))
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))
print(min(b))
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))                         # Error
d = [25 , '35']
#print(max(d))                         # Error
#print(max([]))                        # Error
#print(min([]))                        # Error


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''
output:
30
5
Vamsi
Amar



19.# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)
print(type(b))
print(a  is  b)
print(a == b)


output:
[10, 20, 15, 18]
<class 'list'>
False
False


20.#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)
print(type(b))
a = list('Vamsi')
print(a)
a = list()
print(a)
print(list(25))      # Error
print(list(10.8))    # Error
print(list(True))    # Error
print(list(None))    # Error



'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  --->  Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error

output:

[4, 6, 8]
<class 'list'>
['V', 'a', 'm', 's', 'i']
[]





21.# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))

output:
[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
[[10, 20], (30, 40), {50, 60}]



22.# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b)
print(type(b))
c = sorted(a , reverse = True)
print(c)
print(a)



'''
sorted()  function
---------------------
1) What  does  sorted(list)  do  ?  --->  Sorts  elements  of  the  list  in  ascending  order

2) Where  are  the  results  stored  ?  --->  In  another  list

3) Is  argument  list  modified ?  --->  No  and  it  remains  unchanged

4) How  to  sort  list  in  descending  order ?  --->  sorted(list , reverse = True)

5) What  are  the  two  arguments  of  sorted()  function ?  ---> List  to  be  sorted
																												and
																					                 reverse = True  which  is  an  optional  argument


output:
[5, 10, 12, 15, 20]
<class 'list'>
[20, 15, 12, 10, 5]
[10, 20, 15, 5, 12]


23.# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)
c = sorted(a , reverse = True)
print(c)
print(a)

output:
['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']


24.# all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))
d = [10 , 0 , 20]
print(all(d))
e = []
print(all(e))


'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):'''


output:
True
False
False
False
True


25.# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))
e = []
print(any(e))


'''
any()   function
-------------------
1) What  does  any(list)  do ?  --->  Returns  True  when  at  least  one  element  of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  every  element  of  the  list  is  false

3) if  cond1  or  cond2  or  cond3  or  cond4:
     How  to  reduce  the  four  conditions  to  a  single  condition ?  ---> if  any([cond1 , cond2 , cond3 , cond4]):

4) all()  and  any()  functions  are  used  as  an  alternative  when  there  are  too  many  conditions  in  if  and  while
'''



output:

True
False
True
False
False




26.# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)
del    a[2]
print(a)
del  a[3]         # Error
del  a            # Error
print(a)

output:
[10, 20, 15, 18]
[10, 20, 18]



27.#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)
list . append(19)
print(list)

output:
[10, 20, 15, 18]
[10, 20, 15, 18, 19]


28.#  Find  outputs (Home  work)
list = []
print(list)
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list)

output:
[]
[25, 10.8, 'Hyd', True]

29.# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)

output:
[0, 10, 20, 30, 40]


30.#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a)
print(len(a))
print(How  to  print  4th  element  of  list  'a')
print(How  to  print  'H')
print(How  to  print  'y')
print(How  to  print  'd')

output:





31.#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)
print(len(a))
print(How  to  print  inner  list)
print(How  to  print  50)
print(How  to  print  60)
print(How  to  print  70)





32.# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)
	list . remove(25)
except:
	print('25  is   not  in  the  list')
output:
[10, 20, 18, 15, 12, 15, 19]
25  is   not  in  the  list



'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  ---> Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Raises  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->  Call  remove()  method  in  a  loop
'''






33.Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]


code:
a = [10, 20, 15, 18, 19, 15, 17, 20, 15, 14]
x = 15

result = []

for i in a:
    if i != x:     
       result.append(i)

print("Original list :", a)
print("After deleting", x, ":", result)



34.#  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2))
print(a)
print(a . pop(len(a)))
print(a . pop(-3))
print(a)
print(a . pop(-4))
print(a . pop())
print(a)
b = []
b . pop()



'''
pop()   method
------------------
1) What  does  pop(index)  do ?  --->  Removes  element  at  the  specified  index  and  returns  the  deleted   element

2) What  does  pop(invalid-index)  do  ?  --->  Raises  IndexError

3) What  does  pop(No-args)  do ?  --->  Removes  last  element  of  the  list  and  returns  the  deleted  element

4) How  many  arguments  can  pop()  method  take ?  --->  1  (or)  0

5) What  does  pop(No-args)  do  when  list  is  empty ?  --->  Raises  error

6) del  list[index]
    list . pop(index)
    What  is  the  difference  between  the  two  statements ?  --->
											del  operator  removes  element  but  does  not  return  the  deleted  element
											whereas  pop()  method  not  only  deletes  element  but  also  returns  the  deleted  element





35.# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)
list . clear()
print(list)

output:
[10, 20, 15, 18]
[]

'''
clear()  method
------------------
1) What  does  clear()  method  do ?  ---> Removes  all  the  elements  of  the  list  and  list  becomes  empty

2) What  about  remove()  and  pop()  methods  ?  --->  They  remove  single  element  of  the  list
'''


# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)
a . reverse()
print(a)

output:
[10, 20, 15, 18]
[18, 15, 20, 10]


'''
reverse()  method
---------------------
1) What  does  reverse()  method  do ?  --->  Reverses  all  the  elements  of  list

2) Where  are  the  results  stored ?  ---> In  the  same  list  replacing  existing  elements (List  is  mutable)






36.#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)
list . sort()
print(list)
list . sort(reverse = True)
print(list)

output:
[10, 20, 15, 18, 5]
[5, 10, 15, 18, 20]
[20, 18, 15, 10, 5]



37.# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)
a . sort()
print(a)
a . sort(reverse = True)
print(a)

output:
['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']



38.# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()                             # Error




39.#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))
print(a . count(25))
print(len(a))

'''
What  does  list . count(x)  do ?  --->  Returns  number  of  times  'x'  is  in  the  list
'''

code:
3
0
9



40.tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  --->  [15 , 14 , 18 , 19]

Element         count               Action
---------------------------------------------
  10                  3                       Ignore
  
  20                  2                       Ignore
  
  15                  1                       [15]
  
  14                  1                       [15 , 14]
  
  18                  1                       [15 , 14 , 18]
  
  19                  1                       [15 , 14 , 18 , 19]

code:

lst = [10, 20, 15, 10, 14, 10, 18, 20, 19]

result = []

for i in lst:
    if lst.count(i) == 1:   
        result.append(i)

print("Original List :", lst)
print("Output List   :", result)





41.Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  --->  All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->  All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3
'''



code:

lst = eval(input("Enter the list: "))
total_elements = len(lst)
first_element_count = lst.count(lst[0])
if total_elements == first_element_count:
    print("All the elements are identical")
else:
    print("All the elements are not identical")

print("Number of elements in the list:", total_elements)
print("First element is repeated:", first_element_count, "times")













