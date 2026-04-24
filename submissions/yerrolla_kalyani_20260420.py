 # How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))#<class 'zip'>
print(z1)#type and address of the z1
print('Iterate  thru  zip  object  with   next()   function')
next(z1)#How  to   iterate  thru  zip  object  with  next()  function
print('Iterate  thru  zip  object  with  __next__()  method')
print(z1.__next__())#How  to   iterate  thru  zip  object  with  _next_()  method
print('Iterate  thru  zip  object  with   for  loop')
for x in z1:
    print(next(z1))#How  to   iterate  thru  zip  object  with  for  loop
print('Elements  of  each  tuple  in  zip  object')
z1 = zip(a, b)
for x, y in z1:
    print(x, '-', y)#How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
z1 = zip(a, b)   
print('Unpacks  zip  object  with   *  operator  :  ' , *z1)
print()#nothing 
z1 = zip(a, b)
print('zip   object  in  the  form  of   list  :  ' , list(z1))
print()#nothing 
z1 = zip(a, b)
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(z1))


#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z))#('Empno',25)<nxt>('Emp Name','Rama Rao')<nxt>('Salary',10000.0)
		time . sleep(1)#elements are yielded one at a time interwel 1 sec 
	except  StopIteration:
		break


#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)#('Telangana' , Hyderabad', 50000000)<next>('Andhra  Pradesh' , 'Amaravathi', 40000000)<next>('Karnataka' ,'Banglore', 70000000)<next>('TamilNadu' ,'Chennai', 60000000)<next>('Maharastra , 'Mumbai', 30000000)
	time . sleep(1)#elements are yielded one at a time interwel 1 sec 



# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y) #5 <nxt>7<nxt>9
	time . sleep(1)#elements are yielded one at a time interwel 1 sec 


# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)#elements are yielded one at a time interwel 1 se
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
z1 = zip(a , b . keys())
disp(z1)#(10,1)<NEXT>(20,3)<NEXT>(30,5)
z2 = zip(a , b . values())
disp(z2)##(10,2)<NEXT>(20,4)<NEXT>(30,6)
z3 = zip(a , b . items())
disp(z3)##(10,(1 , 2))<NEXT>(20,( 3 , 4))<NEXT>(30,(5 , 6))
z4 = zip(a , b)
disp(z4)#(10,1)<NEXT>(20,3)<NEXT>(30,5)
z5 = zip(a)
disp(z5)#(10,)<nxt>(20,)<nxt>(30,)
z6 = zip(b)
disp(z6)#(1,)<nxt>(3,)<nxt>(5,)
z7 = zip()
disp(z7)#no output 1 iteration only stop iteration error and break loop


# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)#[[0,20],[1,21],[2,22],[3,23],[4,24]]

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))#<class 'reversed'>
print(r1)#type and address of the onject r1
print('Iterate  thru  reversed  object  with   next   function')
print(next(r1))#How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   __next__   method')
print(r1.__next__())#How  to  iterate  reversed  object   with  _next_()   method
print('Iterate  thru  reversed  object  with   for  loop')
for x in r1:
    print(next(r1))#How  to  iterate  reversed  object   with  for  loop
r1=reversed(a)
print('Unpack  reversed  object  : ' ,  *r1)
print('List  of  chars  in  reverse  order  :  ' , list(r1))
print('Reverse  string   :   ' , a[::-1])



# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))#<class 'reversed'>
print(b)#type and address(in hexa_decimal) of the object b
print(id(b))#address if the object in decimal formate 
print(*b)#
print(b[0])#error iterators are empty they are not indexed
print(b[1 : 3])#error iterators are not indexed and cannot be sliced 
print(b * 2)#error ,repeation is not allowed not supported 
print(len(b))#error ,len function demands argument as sequence but not iterator 
#



 # Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))#<class 'reverse'>
for  x  in   b:
	print(x)#Ture , 'Hyd' , 10.8 , 25
	time . sleep(1)


#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))#<class 'reverse'>
print(r1)#type and address of the object r1
print('next()   function  iterates   thru  list_reverseiterator  object')
while True:
    try:
        print(next(r1))
    except StopIteration:
        break#How  to  iterate   list_reverseiterator  object  with   next()   function
print('_next_()   method  iterates   thru  list_reverseiterator  object')
r1 = reversed(lst)
while True:
    try:
        print((r1.__next__()))
    except StopIteration:
        break#How  to  iterate   list_reverseiterator  object  with   _next_()   method
print('for  loop  iterates  thru  list_reverseiterator  object')
r1 = reversed(lst)
while True:
    try:
        print(next(r1))
    except StopIteration:
        break#How  to  iterate   list_reverseiterator  object  with   for  loop
r1 = reversed(lst)
print('Unpack  list_reverseiterator  object  :  ' ,   *r1)
print('Reverse  list  :  '  ,  list(reversed(lst)))
# 

#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)
#no set  object is not reversible


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
disp(r1)#18<nxt>15<nxt>20<nxt>10
r2 = reversed(a . values())
disp(r2)#'Amar'<nxt>'Kiran'<nxt>'Sita'<nxt>'Rama'
r3 = reversed(a . items())
disp(r3)#(18 ,'Amar')<nxt>(15 , 'Kiran') <nxt>(20 , 'Sita') <nxt>(10 ,'Rama')
r4 = reversed(a)
disp(r4)#18<nxt>15<nxt>20<nxt>10



# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
r=reversed(list(a.keys))
for i in r:
    print(next(r))#Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
r=reversed(list(a.values))#Write  for  loop  to  reverse  values  of  dictionary
for i in r:
    print(next(r))
print('Tuples  in   reverse  order')
r=reversed(list(a.items))
for i in r:
    print(next(r))#Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
r=reversed(list(a.items))
for k, v in a.items():
    print((v, k))#Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
r=reversed(a)
for k in r:#Write  for  loop  to  reverse  keys  and 
    print(k)
 

# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
r=iter(list)
for x in r:#How  to  iterate  list  with  for  loop
    print(x)
print(next(r))#stop iteration error as we gortje 5 iteration as si error and we get out of loop .
list_itr1 = iter(list)
print(type(list_itr1))#<class 'list_iterator')
print(list_itr1)#type and addres of the object list_itr1
print('Iterate   thru  list_iterator  with  next()  function')
r=iter(list)
print((next(r)))#How  to  iterate  list_iterator  with  next()  function
print('Iterate  thru  list_iterator  with   _next_()  method')
print(r.__next__())#How  to  iterate  list_iterator  with   _next_  method
print('Iterate   thru  list_iterator  with   for    loop')
r=iter(list)
for x in r:#How  to  iterate  list_iterator  with  for  loop
    print(x)
r=iter(list)
print('Unpacks  List_iterator   :    ' ,  *r)


 # Find  outputs
a = 25
print(a)#25
for  x   in   a:#error cannot loop the non sequence 
	print(x)
print(iter(a))#error iter function takes only the sequence as the argument not allowes the other as argument so error cannot loop int object 
print(next(a))#error for above reason 

'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''
a={'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
r=reversed(a.keys())
b={}
for k in reversed(list(a.keys())):
    b[k] = a[k]

print(b)