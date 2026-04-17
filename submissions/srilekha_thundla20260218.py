#  Find  outputs
a = 25
print(id(a)) #Address of object 25
a = 35
print(id(a))#Address of object 35 both adresses are different


# Find  outputs (Home  work)
a = 25.7
print(id(a))#Address of object 25.7
print(a)#25.7
a = 35.6
print(id(a))#Address of object 35.6
print(a)# 35.6
b = True
print(id(b))# address of object True
b = False
print(id(b))# address of object False

c = None
print(id(c))# address of object None
c = None
print(id(c))# Same address as above c



#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))# address of object 'Hyd'
a[1] = 'e'  #error 
a = 'Sec' 
print(id(a))# address of object 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))# address of tuple (10,20,15,18)
b[2] = 19 #error because tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b))# address of the second tuple (30 , 40 , 35 , 32)
c = range(5)
print(id(c))#address of range oject
c[3] = 10 # error because range obj is immutable
c = range(5)# reference is modified
print(id(c))#address of the second range object




# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)#True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)#True
e = False
f = False
print(e  is  f)#True
g = range(10)
h = range(10)
print(g  is  h)#False



#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)#False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)#False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)# True because tuple is immutable and reusable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)#False


# Find outputs (Home work)
print(10 + 20)#30
print(10.8 + 20.6)#31.4
print(3 + 4j + 5 + 6j)#8+10j
print(True + False)#1
print('Hyder' + 'abad')# Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')#SankarDayalSarma
print('10' + '20')#1020
print([10 , 20 , 30] + [1 , 2 , 3])#[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))#(25,10.8,'Hyd',3+4j,True,None)
print({10 , 20} + {30 , 40})#error
print({10 : 'Hyd'} + {20 : 'Sec'})#error
print(range(4) + range(5))#error
print(10 + '20')#error
print([10 , 20 , 30] + 5)#error
print([10 , 20 , 30] + (40 , 50 , 60))#error both are not same type



# Find outputs (Home work)
print(25 * 3)#75
print(10.8 * 25.6)#
print(True * False)#0
print((3 + 4j) * (5 + 6j))#multiplacation of complex numbers
print(3 + 4j * 5 + 6j)#3+26j
print('25' * 3)#252525 repeatation
print(3 * '25')#252525 repeatation
print('Hyd' * 4)#HydHydHydHyd
print([10 , 20 , 15] * 2)#[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)#(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)#error operand 2 should integer
print({10 , 20 , 15} * 2)#error because if you repeat the set duplication will occur
print({10 : 20 , 30 : 40} * 2)#erroe duplication is not allowed
print([10] * [20])#error operand 2 should integer
