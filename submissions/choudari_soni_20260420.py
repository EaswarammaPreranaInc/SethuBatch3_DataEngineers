'''How  to  iterate  zip  object  in  differenet  ways  (Home  work)'''
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))#<class 'list_reverseiterate'>
print(z1)#
#print('Iterate  thru  zip  object  with   next()   function')
z1=zip(a,b)
print(next(z1)) # (Telangana,Hyderabad)
print(next(z1)) # (Andhra Pradesh,Amaravathi)
print(next(z1)) # (Karnataka,Bangalore)
print(next(z1)) # (Tamilnadu,Chennai)
print(next(z1)) # stop iteration Error
#print('Iterate  thru  zip  object  with  __next__()  method')
#How  to   iterate  thru  zip  object  with  __next__()  method
z1 = zip(a, b)
print(z1.__next__()) # (Telangana,Hyderabad)
print(z1.__next__()) # (Andhra Pradesh,Amaravathi)
print(z1.__next__()) # (Karnataka,Bangalore)
print(z1.__next__()) # (Tamilnadu,Chennai)
print(z1.__next__()) # stop iteration Error
#print('Iterate  thru  zip  object  with   for  loop')
#How  to   iterate  thru  zip  object  with  for  loop
z1=zip(a,b)
for items  in z1:
    print(item)
#print('Elements  of  each  tuple  in  zip  object')
z1 = zip(a, b)
for x, y in z1:
    print(x, "->", y)
#How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' , *zip(a, b))
print()
print('zip   object  in  the  form  of   list  :  ' ,  list(zip(a, b)))
print()
print('zip   object  in  the  form  of   dictionary :  ' ,dict(zip(a, b))  )
'''Find  outputs  (Home  work)'''
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
'''output'''    
# ('Empno',25)
# ('Emp Name' ,'Rama  Rao' )
# ('Salary' , 10000.0  )
'''Find  outputs  (Home  work)'''
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
'''output'''
# (Telangana , Hyderabad , 50000000)
# (Andhra  Pradesh , Amaravathi ,  40000000)
# (Karnataka , Banglore , 70000000)
# (TamilNadu , Chennai , 60000000 )
# (Maharastra , Mumbai , 30000000)
'''Find  outputs   (Home  work)'''
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)   # (5,) /n   (7,)  /n  (9,)
	time . sleep(1)

'''Find outputs  (Home  work)'''
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
disp(z1) # (10,1)<nextline>(20,3)<nextline>(30 , 5)
z2 = zip(a , b . values())
disp(z2) # (10,2)<nextline>(20,4)<nextline>(30 , 6)
z3 = zip(a , b . items())
disp(z3) # (10,(1 , 2))<nextline>(20,(3,4))<nextline>(30 ,( 5 , 6))
z4 = zip(a , b)
disp(z4)  # (10,1)<nextline>(20,3)<nextline>(30 , 5)
z5 = zip(a)
disp(z5) # (10,)<nextline>(20,)<nextline>(30 ,)
z6 = zip(b)
disp(z6) # (1,)<nextline>(3,)<nextline>(5,)
z7 = zip()
disp(z7) # SI
'''Find  outputs  (Home  work)'''
# z = zip(range(5) , range(20 , 25))
# a = [ [x , y]  for  x , y   in   z]  
# print(a)# (0,20)<nextline> (1,21) <nextline>(2,22)<nextline> (3 , 23)<nextline> (4, 24)
'''How  to  print  reversed  object  in  different  ways  (Home  work)'''
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1) # D<nextline> Y <nextline>H
#print('Iterate  thru  reversed  object  with   next   function')
#How  to  iterate  reversed  object  'r'  with  next()  function
r1 = reversed(a)
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
#print('Iterate  thru  reversed  object  with   __next__   method')
#How  to  iterate  reversed  object   with  __next__()   method
r1 = reversed(a)
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
#print('Iterate  thru  reversed  object  with   for  loop')
#How  to  iterate  reversed  object   with  for  loop
r1 = reversed(a)
for ch in r1:
    print(ch)
print('Unpack  reversed  object  : ' ,  *reversed(a))
print('List  of  chars  in  reverse  order  :  ' ,list(reversed(a))  )
print('Reverse  string   :   ' , ''.join(reversed(a)))


'''Find  outputs (Home  work)'''
a = 'HYD'
b = reversed(a)
print(type(b)) #<class 'reversed'>
print(b)  # DYH
print(id(b))  # Address of an object b
print(*b) #Error
print(b[0]) # Error--- don’t support indexing
print(b[1 : 3]) # Error--- don’t support indexing
print(b * 2) # Error--- don’t support Repetation
print(len(b))  # Error---  don’t support  len
'''Can  tuple  be  reversed ?   (Home  work)'''
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x) # True<nextline> Hyd <nextline> 10.8 <nextline> 25
	time . sleep(1)
'''How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)'''
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))
print(r1)
#print('next()   function  iterates   thru  list_reverseiterator  object')
#How  to  iterate   list_reverseiterator  object  with   next()   function
r1 = reversed(lst)
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1)) # SI
#print('_next_()   method  iterates   thru  list_reverseiterator  object')
#How  to  iterate   list_reverseiterator  object  with   __next__()   method
r1 = reversed(lst)
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
print(r1.__next__()) # SI
#print('for  loop  iterates  thru  list_reverseiterator  object')
#How  to  iterate   list_reverseiterator  object  with   for  loop
r1 = reversed(a)
for x in r1:
    print(x)
print('Unpack  list_reverseiterator  object  :  ' ,  *reversed(lst))
print('Reverse  list  :  '  ,''.join(reversed(lst)) )    

'''Can  set  be  reversed  ?  (Home  work)'''
a = {10, 20, 15 , 18}
r = reversed(a) # Error---'set' object is not reversible

'''Can  dictionary  be  reversed  ? (Home  work)'''
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
disp(r1) # (18,)<nextline> (15,)<nextline> (20,) <nextline>(10,)
r2 = reversed(a . values())
disp(r2) # (Amar,)<nextline> (Kiran,)<nextline>(Sita,) <nextline> (,Rama)
r3 = reversed(a . items())
disp(r3)# (18 ,Amar)<nextline>(15 ,Kiran)<nextline>(15 ,Kiran)(20,Sita)<nextline>(10,Rama)
r4 = reversed(a)
disp(r4) #(18,)<nextline> (15,)<nextline> (20,) <nextline>(10,)

'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''
d = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}

rev_d = dict(reversed(list(d.items())))
print("Original Dictionary:", d)
print("Reversed Dictionary:", rev_d)


'''Find outputs'''
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
#Write  for  loop  to  reverse  keys  of  dictionary
for k in reversed(list(a.keys())):
    print(k)
print('Values  in  reverse  order')
#Write  for  loop  to  reverse  values  of  dictionary
for v in reversed(list(a.values())):
    print(v)
print('Tuples  in   reverse  order')
#Write  for  loop  to  reverse   tuples   of  dictionary
for item in reversed(list(a.items())):
    print(item)
print('Elements  of  each   tuple  in  reverse  order')
#Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
for item in reversed(list(a.items())):
    print((item[1], item[0]))
print('Keys  and  values  in   reverse   order')
#Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary
for k, v in reversed(list(a.items())):
    print(k, v)

'''Find  outputs'''
a = 25
print(a) #25
for  x   in   a:
	print(x)  # Error--Integers are not iterable
print(iter(a)) # Error--Integers are not iterable
print(next(a)) # Error--Integers are not iterable