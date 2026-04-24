import   time
d=  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
dic=reversed(d.items())
print(f"dictionary reversed {dict(dic)}")
time.sleep(5)


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
{10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
18
15
20
10
Amar
kiran
sita
Rama
( 18 , 'Amar')
(15 , 'Kiran')
(20 , 'Sita')
(10 , 'Rama')
18
15
20
10
'''

lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst) 
print(type(r1)) #<class 'list_reversed'>
print(r1)       # type and address
print('next()   function  iterates   thru  list_reverseiterator  object')
while(True):
	try:
		print(next(r1))
		time.sleep(1)
	except StopIteration:
		break
r2 = reversed(lst) 
print('_next_()   method  iterates   thru  list_reverseiterator  object')
while(True):
	try:
		print(r2.__next__())
		time.sleep(1)
	except StopIteration:
		break
print('for  loop  iterates  thru  list_reverseiterator  object')
r3 = reversed(lst)
for i in r3:
	print(i) 
	time.sleep(1)
r4 = reversed(lst) 
print('Unpack  list_reverseiterator  object  :  ' , *r4 )
r5 = reversed(lst) 
print('Reverse  list  :  '  ,  list(r5))


a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
'''
True
Hyd
10.8
25
'''
a = 'HYD'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b)       #
print(id(b))   # Adress
print(*b)      #DYH
#print(b[0])    # error
#print(b[1 : 3]) # error
#print(b * 2)    # error
#print(len(b))    #error

a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate  thru  reversed  object  with   next   function')
while(True):
	try:
		print(next(r1))
		time.sleep(1)
	except StopIteration:
		break
r2=reversed(a)
print('Iterate  thru  reversed  object  with   _next_   method')
while(True):
	try:
		print(r2.__next__())
		time.sleep(1)
	except StopIteration:
		break
r3=reversed(a)
print('Iterate  thru  reversed  object  with   for  loop')
for i in r3:
	print(i)
	time.sleep(1)
r4=reversed(a)
print('Unpack  reversed  object  : ' ,  *r4)
r5=reversed(a)
print('List  of  chars  in  reverse  order  :  ' ,list(r5))

a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print('Iterate  thru  zip  object  with   next()   function')
while(True):
    try:
        print(next(z1))
    except StopIteration:
        print("end of elements")
        break
z2=zip(a,b)
print('Iterate  thru  zip  object  with  _next_()  method')
while(True):
    try:
        print(z2.__next__())
    except StopIteration:
        print("end of elements")
        break
z3=zip(a,b)
print('Iterate  thru  zip  object  with   for  loop')
for i in z3:
    print(i)

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
('empno',25)
('empname','Rama Rao')
('salary',10000)

'''

a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
'''
('Telangana','Hyderabad',50000000)
('Andhra Pradesh','Amarvathi',40000000)
('karnataka','banglore',7000000)
('tamil nadu','chennai',600000)
('Maharastra','mumbai',3000000)

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
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
(10,1) (20,3) (30,5)
(10,2) (20,4) (30,6)
(10,(1,2)) (20,(3,4)) (30,(5,6))
(10,1) (20,3) (30,5)
(10,) (20,) (30,)
(1,) (3,) (5,)


'''


z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)

#[[0,20],[1,21],[2,22],[3,23],[4,24]]



#print('Reverse  string   :   ' , ???)