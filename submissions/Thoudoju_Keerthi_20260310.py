 #  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) #True
print(a  ==  b) #True
b[2] = 12
print(a) #[10, 20, 12, 15,18]

 #  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[10 , 20 , 15 , 18,100 , 200 , 150]
print(a + 5) #Error
print(a + '5') #Error
print([10 , 20] + (30 , 40))#Error

 # Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) #[1 , 2 , 3] <address of list a(1000)>
a += b
print(a , id(a)) #[1 , 2 , 3, 4 , 5 , 6] <address of list a (1000)>

 # Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) #[1 , 2 , 3] <address of list a(1000)>
a  = a + b
print(a , id(a)) #[1 , 2 , 3, 4 , 5 , 6] <address of list a (2000)>

 # Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) # : 25
print('b : ' , b) # [10.8 , 'Hyd' ]
print('c : ' , c) # True
print(type(b)) # <class 'list'>
x , *y = list
print('x : ' , x) # x: 25
print('y : ' , y) # y: [10.8 , 'Hyd' ,  True]
*p , q = list 
print('p : ' , p) #[25 , 10.8 , 'Hyd']
print('q : ' , q)# True

 # all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #False
d = [10 , 0 , 20]
print(all(d)) #False
e = []
print(all(e)) #False


'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''
 # any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) #False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) #True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) #False
e = []
print(any(e)) #False


'''
any()   function
-------------------
1) What  does  any(list)  do ?  --->  Returns  True  when  at  least  one  element  of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  every  element  of  the  list  is  false

3) if  cond1  or  cond2  or  cond3  or  cond4:
     How  to  reduce  the  four  conditions  to  a  single  condition ?  ---> if  any([cond1 , cond2 , cond3 , cond4]):

4) all()  and  any()  functions  are  used  as  an  alternative  when  there  are  too  many  conditions  in  if  and  while
'''
 # del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
del    a[2]
print(a) #[10 , 20  , 18]
del  a[3]
del  a
print(a) #[]

 #  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . append(19)
print(list) #[10 , 20 , 15 , 18,19]

 #  Find  outputs (Home  work)
list = []
print(list) #[]
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) # [25,10.8 , 'Hyd', True]

# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) #[0, 9, 19, 29, 39,49]

 #  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) #[10 , 20 , 30, 'Hyd']
print(len(a)) #4
print(How  to  print  4th  element  of  list  'a') # print(a[3])
print(How  to  print  'H') # print(a[4][0])
print(How  to  print  'y') # print(a[3][1])
print(How  to  print  'd') # print(a[3][2])

 #  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b) 
print(a) # [10 , 20 ,[50 , 60 , 70], 30 , 40]
print(len(a)) #5
print(How  to  print  inner  list) #print(a[2])
print(How  to  print  50) #print(a[2][0])
print(How  to  print  60)#print(a[2][1])
print(How  to  print  70)#print(a[2][2])

 # remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list) # [10 , 20 , 18 , 15 , 12 , 15 , 19]
	list . remove(25)
except:
	print('25  is   not  in  the  list') #25  is   not  in  the  list


'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  ---> Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Raises  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->  Call  remove()  method  in  a  loop
'''
 '''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

a=[10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
try:
	while True:
		a.remove(15)
except:
	print(a)
		
		
'''
 #  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2)) #15
print(a) #[10 , 20 , 18 , 12]
print(a . pop(len(a))) #ERROR
print(a . pop(-3)) #20
print(a) #[10 , 18 ,12]
print(a . pop(-4)) # Error
print(a . pop()) #12
print(a) #[10 , 18]
b = []
b . pop() # Error


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
'''
 # clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . clear()
print(list) #[]


'''
clear()  method
------------------
1) What  does  clear()  method  do ?  ---> Removes  all  the  elements  of  the  list  and  list  becomes  empty

2) What  about  remove()  and  pop()  methods  ?  --->  They  remove  single  element  of  the  list
'''
 # reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
a . reverse()
print(a) #[18 , 15 , 20 , 10]


'''
reverse()  method
---------------------
1) What  does  reverse()  method  do ?  --->  Reverses  all  the  elements  of  list

2) Where  are  the  results  stored ?  ---> In  the  same  list  replacing  existing  elements (List  is  mutable)
'''
   sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) #[10 , 20 , 15 , 18 , 5]
list . sort()
print(list) #[5, 10, 15, 18, 20]
list . sort(reverse = True)
print(list) ##[20, 18, 15, 10, 5]

 # Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) #['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a) #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']

 # Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() #Error

 #  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3
print(a . count(25)) #0
print(len(a)) # 9


'''
What  does  list . count(x)  do ?  --->  Returns  number  of  times  'x'  is  in  the  list
'''

 '''
Tricky  program
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
'''
 '''
a=[10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
try:
	for i in a:
		a.count(i)>1:
			try:
				while i in a:
					a.remove(i)
			except:
				print('Error')
	print(a)
except:
	print('Error')


Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  --->  All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->  All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3
'''
a=eval(input('Enter any list'))
try:
	if(len(set(a)) ==1):
		print('All elements are identical')
	else:
		print('List elements are not identical')
except:
	print('error')

# or
a=eval(input('Enter any list'))
try:
	if(len(a) ==a.count(a[0])):
		print('All elements are identical')
	else:
		print('List elements are not identical')
except:
	print('error')

	