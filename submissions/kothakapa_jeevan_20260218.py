#  Find  outputs
a = 25
print(id(a)) ----> 24555 (id is the reference of int object)
a = 35
print(id(a)) ---->32365 (id is the reference of int object)


# Find  outputs (Home  work)
a = 25.7
print(id(a)) ---> 54856 (id is the reference of float object)
print(a) ----> 25.7
a = 35.6
print(id(a)) ----> 878945 (id is the reference of float object)
print(a) ---> 35.6
b = True
print(id(b)) ---> 31325 (id is the reference of bool object)
b = False
print(id(b)) ---> 0010325 (id is the reference of bool object)
c = None
print(id(c)) ----> 9799636 (id is the reference of none object)
c = None
print(id(c)) ----> 9799636 (id is the reference of none object)


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) ---> 0445652 (id is the reference of str object)
a[1] = 'e'   
a = 'Sec'
print(id(a)) ----> 478880001 (id is the reference of str object)
b = (10 , 20 , 15 , 18)
print(id(b)) ----> 00123333 (id is the reference of tuple object)
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b)) ---->331120 (id is the reference of tuple object)
c = range(5)
print(id(c)) ----> 887799663 (id is the reference of range object)
c[3] = 10
c = range(5) 
print(id(c)) ---> 003355 (id is the reference of range object)


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)  ---> true
c = 'Hyd'
d = 'Hyd'
print(c  is  d) ----> true
e = False
f = False
print(e  is  f) ---> true
g = range(10)
h = range(10)
print(g  is  h) ----> true




#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)		 ----> False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)		 ----> False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) 	 ----> False
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)		 ----> False



# Find outputs (Home work)
print(10 + 20)		----> 30 (int and int will act like addition)
print(10.8 + 20.6)	----> not aware 
print(3 + 4j + 5 + 6j)  ----> not aware 
print(True + False) 	----> 1 (1+0=1)
print('Hyder' + 'abad') ----> (Hyderabad)
print('Sankar' + 'Dayal' + 'Sarma') --> ( Sankar Dayal Sarma)
print('10' + '20') 	----> (1020)
print([10 , 20 , 30] + [1 , 2 , 3]) ---> [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) ---> (25 , 10.8 , 'Hyd') + (3 + 4j , True , None)
print({10 , 20} + {30 , 40}) ----> error
print({10 : 'Hyd'} + {20 : 'Sec'}) ---> error 
print(range(4) + range(5)) ----> (0,1,2,3,0,1,2,3,4)
print(10 + '20') ----> error (int and str cannot concatenate)
print([10 , 20 , 30] + 5)---> error (int and str cannot concatenate)       		
print([10 , 20 , 30] + (40 , 50 , 60)) ---> (10,20,30,40,50,60)


# Find outputs (Home work)

print(25 * 3)		--> 75
print(10.8 * 25.6)	--> error
print(True * False)	--> 0 (1*0=0)
print((3 + 4j) * (5 + 6j))-> not aware 
print(3 + 4j * 5 + 6j)  ---> not aware 
print('25' * 3)	        ---> 252525
print(3 * '25')         ---> 252525
print('Hyd' * 4)	---> (HydHydHydHyd)
print([10 , 20 , 15] * 2) --> [10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3) --> (25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) error ( Using float cannot be multiplied)
print({10 , 20 , 15} * 2) --> error 
print({10 : 20 , 30 : 40} * 2) --> error
print([10] * [20]) ---> error
