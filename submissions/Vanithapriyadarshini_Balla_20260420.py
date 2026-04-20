# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))# <class zip>
print(z1)# type and address
print('Iterate  thru  zip  object  with   next()   function')
while True:
    try:
        print(next(z1))
        print(time.sleep(1))
    except:
        break
    print()
print('Iterate  thru  zip  object  with  _next_()  method')
z2 = zip(a , b)
while True:
    try:
        print(z2.__next__())
        print(time.sleep(1))
    except:
        break
    print()
print('Iterate  thru  zip  object  with   for  loop')
z3 = zip(a , b)
for i in z3:
    print(i)
    print(time.sleep(1))
print()
print('Elements  of  each  tuple  in  zip  object')
z4=zip(a,b)
for x,y in z4:
    print(x,y)
    print(time.sleep(1))
print()
z5=zip(a,b)
print('Unpacks  zip  object  with   *  operator  :  ' , *z5)
print()
z6=zip(a,b)
list=[*z6]
print('zip   object  in  the  form  of   list  :  ' ,  print(list))
print()
z6=list(zip(a,b))
print('zip   object  in  the  form  of   dictionary :  ' ,  print())


#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z))# ('Empno',25)('Empname','Rama Rao')('Salary',10000.0)
		time . sleep(1)
	except  StopIteration:
		break

#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)#('Te','Hy',5cr)('AP','Am',4cr)('Ka','Bng',7cr)('TN','CH',6cr)('Mh','Mum',3cr)
	time . sleep(1)


# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  # 5 7 9
	time . sleep(1)

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
disp(z1)#(10,1)(20,3)(30,5)
z2 = zip(a , b . values())
disp(z2)#(10,2)(20,4)(30,6)
z3 = zip(a , b . items())
disp(z3)# #(10,(1,2)) (20,(3,4)) (30,(5,6))
z4 = zip(a , b)
disp(z4)#(10,1)(20,3)(30,5)
z5 = zip(a)
disp(z5)#(10,)(20,)(30,)
z6 = zip(b)
disp(z6)# (1,)(3,)(5,)
z7 = zip()
disp(z7)# nothing


# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)#[[0,20],[1,21],[2,22],[3,23],[4,24]]


#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))# <class 'reversed'>
print(r1)#type and address
print('Iterate  thru  reversed  object  with   next   function')
while True:
    try:
        print(next(r1))
        print(time.sleep(1))
    except:
        break
    print()
print('Iterate  thru  reversed  object  with   _next_   method')
r2=reversed(a)
print('Iterate  thru  reversed  object  with   next   function')
while True:
    try:
        print(r2.__next__())
        time.sleep(1)
    except:
        break
    print()
print('Iterate  thru  reversed  object  with   for  loop')
r3=reversed(a)
for i in r3:
    print(i)
print()
r4=reversed(a)
print('Unpack  reversed  object  : ' ,  *r4)
r5=reversed(a)
print('List  of  chars  in  reverse  order  :  ' ,  list(r5))
r6=reversed(a)
rev=''
for i in r6:
    rev+=i
print('Reverse  string   :   ' , rev)


# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))# class 'reversed'>
print(b)#type and address
print(id(b))# Address
print(*b)# d y H
#print(b[0])# error bcz obj is empty
#print(b[1 : 3])# error no slicing
#print(b * 2)# error no repetition
#print(len(b))# error no len func 
# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))
print(b)
print(id(b))
print(*b)
print(b[0])
print(b[1 : 3])
print(b * 2)
print(len(b))


# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))# <class 'reversed'>
for  x  in   b:
	print(x)# True 'Hyd' 10.8 25
	time . sleep(1)


#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))
print(r1)
print('next()   function  iterates   thru  list_reverseiterator  object')
while True:
    try:
        print(next(r1))
    except:
        break
print('_next_()   method  iterates   thru  list_reverseiterator  object')
r2=reversed(list)
while True:
    try:
        print(r2.__next__())
    except:
        break
print('for  loop  iterates  thru  list_reverseiterator  object')
r3=reversed(list)
revlist=[]
for i in r3:
    revlist+=i
print('Reverse  list  :  '  ,  revlist)
r4=reversed(list)
print('Unpack  list_reverseiterator  object  :  ' ,  *r4)


#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}# no
r = reversed(a)

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
disp(r1)# 18 15 20 10
r2 = reversed(a . values())
disp(r2)# Amar Kiran Sita Rama
r3 = reversed(a . items())
disp(r3)# (18,'Amar') (15,'Kiran') (20,'Sita') (10,'Rama')
r4 = reversed(a)
disp(r4)# 18 15 20 10


#Tricky  program
#Write  a  program  to  reverse  a  dictionary ?
dic=eval(input("Enter dictionary : "))
d={}
revdic=reversed(dic.items())
for x,y in revdic:
    d[x]=y
print(d)



# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
d1=reversed(a)
for k in d1:
    print(k)
    time.sleep(1)
print('Values  in  reverse  order')
d2=reversed(a.values())
for v in d2:
    print(v)
    time.sleep(1)
print('Tuples  in   reverse  order')
d3=reversed(a.items())
for t in d3:
    print(t)
    time.sleep(1)
print('Elements  of  each   tuple  in  reverse  order')
d4=reversed(a.items())
for k,v in d4:
    print(k,v)
    time.sleep(1)
print('Keys  and  values  in   reverse   order')
d5=reversed(a.values())
for p in d5:
    print(p)
    time.sleep(1)


# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for i in list:
    print(i)
#print(next(list)) Error
list_itr1 = iter(list)
print(type(list_itr1))#<class 'list_iterator'>
print(list_itr1)# Type and address
print('Iterate   thru  list_iterator  with  next()  function')
while True:
    try:
        print(next(list_itr1))
        time.sleep(1)
    except:
        break
print('Iterate  thru  list_iterator  with   _next_()  method')
ll2=iter(list)
while True:
    try:
        print(ll2.__next__())
        time.sleep(1)
    except:
        break
print('Iterate   thru  list_iterator  with   for    loop')
ll3=iter(list)
for x in ll3:
    print(x)
    time.sleep(1)
ll4=iter(list)
print('Unpacks  List_iterator   :    ' ,  ll4)



# Find  outputs
a = 25
print(a)# 25
#for  x   in   a:# error
	#print(x)
#print(iter(a))error
# #print(next(a))error
