# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1)) # <class 'iterator'>
print(z1) # type and address
print('Iterate  thru  zip  object  with   next()   function')
while True:
    try:
        print(next(z1))
        time . sleep(1)
    except StopIteration:
        break
    
z2 = zip(a , b)
print('Iterate  thru  zip  object  with  __next__()  method')
while True:
    try:
        print(z2.__next__())
        time . sleep(1)
    except StopIteration:
        break

z3 = zip(a , b)
print('Iterate  thru  zip  object  with   for  loop')
for x in z3:
    print(x)
    time . sleep(1)

z4 = zip(a , b)
print('Elements  of  each  tuple  in  zip  object')
for a , b in z4:
    print(f'{a} _ {b}')
    time . sleep(1)

z5 = zip(a , b)
print('Unpacks  zip  object  with   *  operator  :  ' , *z5)
print()

z6 = zip(a , b)
print('zip   object  in  the  form  of   list  :  ' ,  list(z6))
print()

z7 = zip(a , b)
print('zip   object  in  the  form  of   dictionary :  ' , dict(z7))



#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z))
		time . sleep(1)
	except  StopIteration:
		break
'''
('Empno' , 25)
('Emp Name' , 'Rama Rao')
('Salary' , 10000.0)
'''


#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
'''
('Telangana' , 'Hyderabad' , 50000000)
('Andhra Pradesh' , 'Amaravathi' , 40000000)
('Karnataka' , 'Banglore' , 70000000)
('TamilNadu' , 'Chennai' , 60000000)
('Maharastra' , 'Mumbai' , 30000000)
'''



# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  
	time . sleep(1)
'''
5
7
9
'''



# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
z1 = zip(a , b . keys())
disp(z1)
z2 = zip(a , b . values())
disp(z2)
z3 = zip(a , b . items())
disp(z3)
z4 = zip(a , b)
disp(z4)
z5 = zip(a)
disp(z5)
z6 = zip(b)
disp(z6)
z7 = zip()
disp(z7)
'''
(10 , 1)
(20 , 3)
(30 , 5)

(10 , 2)
(20 , 4)
(30 , 6)

(10 , (1 , 2))
(20 , (3 , 4))
(30 , (5 , 6))

(10 , 1)
(20 , 3)
(30 , 5)

(10 ,)
(20 ,)
(30 ,)

(1 ,)
(3 ,)
(5 ,)

<nextline>
'''


# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a) # [[0 , 20] , [1 , 21] , [2 , 22] , [3 , 23] , [4 , 24]]



#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1)) # <class 'reversed'>
print(r1) # type and address
print('Iterate  thru  reversed  object  with   next   function')
while True:
    try:
        print(next(r1))
        time . sleep(1)
    except StopIteration:
        break

r2 = reversed(a)
print('Iterate  thru  reversed  object  with   __next__   method')
while True:
    try:
        print(r2.__next__())
        time . sleep(1)
    except StopIteration:
        break


r3 = reversed(a)
print('Iterate  thru  reversed  object  with   for  loop')
for x in r3:
    print(x)
    time . sleep(1)

r4 = reversed(a)
print('Unpack  reversed  object  : ' , *r4)

r5 = reversed(a)
print('List  of  chars  in  reverse  order  :  ' , list(r5))
print('Reverse  string   :   ' , a[::-1])



# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b) # type and address
print(id(b)) # decimal address
print(*b) # D Y H
print(b[0]) # error , iterators are not indexed
print(b[1 : 3]) # error , iterators cannot be sliced
print(b * 2) # error , iterators cannot be repeated
print(len(b)) # error , len() function argument should be sequence



# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) # <class 'reversed'>
for  x  in b:
	print(x)
	time . sleep(1)
'''
True
Hyd
10.8
25
'''



#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1)) # <class 'list_reverseiterator'>
print(r1) # type and address
print('next()   function  iterates   thru  list_reverseiterator  object')
while True:
    try:
        print(next(r1))
        time . sleep(1)
    except:
        break

r2 = reversed(lst)
print('__next__()   method  iterates   thru  list_reverseiterator  object')
while True:
    try:
        print(r2.__next__())
        time . sleep(1)
    except:
        break

r3 = reversed(lst)
print('for  loop  iterates  thru  list_reverseiterator  object')
for x in r3:
    print(x)

r4 = reversed(lst)
print('Unpack  list_reverseiterator  object  :  ' ,  *r4)

lst.reverse()
print('Reverse  list  :  '  ,  lst)



#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a) # error , set is unordered



# Can  dictionary  be  reversed  ? (Home  work)
import   time
def   disp(r):
	while  True:
		try:
			print(next(r))
			time . sleep(0.5)
		except  StopIteration:
			break
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
r1 = reversed(a . keys())
disp(r1)
r2 = reversed(a . values())
disp(r2)
r3 = reversed(a . items())
disp(r3)
r4 = reversed(a)
disp(r4)
'''
18
15
20
10
Amar
Kiran
Sita
Rama
(18 , 'Amar')
(15 , 'Kiran')
(20 , 'Sita')
(10 , 'Rama')
18
15
20
10
'''


#1
'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''
d = eval(input('Enter a dictionary:'))
a = {}
b = reversed(d)

for x in b:
    a[x] = d[x]

print(a)


# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}

b = reversed(a . keys())
print('Keys  in   reverse   order')
for x in b:
    print(x)
    time . sleep(1)

b = reversed(a . values())
print('Values  in  reverse  order')
for x in b:
    print(x)
    time . sleep(1)

b = reversed(a . items())
print('Tuples  in   reverse  order')
for x in b:
    print(x)
    time . sleep(1)

print('Elements  of  each   tuple  in  reverse  order')
for x , y in a . items():
    b = (y , x)
    print(b)


print('Keys  and  values  in   reverse   order')
b = {}
c = reversed(a)

for x in c:
    b[x] = a[x]

print(b)




# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for x in list:
    print(x)

print(next(list)) # error , next function argument should be an iterator
list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)
print('Iterate   thru  list_iterator  with  next()  function')
while True:
    try:
        print(next(list_itr1))
        time . sleep(1)
    except StopIteration:
        break

list_itr2 = iter(list)
print('Iterate  thru  list_iterator  with   __next__()  method')
while True:
    try:
        print(list_itr2.__next__())
        time . sleep(1)
    except StopIteration:
        break


list_itr3 = iter(list)
print('Iterate   thru  list_iterator  with   for    loop')
for x in list_itr3:
    print(x)
    time . sleep(1)

list_itr4 = iter(list)
print('Unpacks  List_iterator   :    ' , *list_itr4)




# Find  outputs
a = 25
print(a) # 25
for  x   in   a:
	print(x) # error , cannot iterate an integer
print(iter(a)) # error , iter() function argument should be an iterable/sequence
print(next(a)) # error , next() function argument should be an iterator
