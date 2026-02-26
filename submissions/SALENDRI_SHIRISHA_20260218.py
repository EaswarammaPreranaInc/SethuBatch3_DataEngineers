#  Find  outputs
a = 25
print(id(a))  # Address of the object 25
a = 35
print(id(a))  # Address of the object 35, because object 25 is deleted


# Find  outputs (Home  work)
a = 25.7
print(id(a))  # Address of the object 25.7
print(a)  # 25.7
a = 35.6
print(id(a))  # Address of the object 35.6
print(a)  # 35.6
b = True
print(id(b))  # Address of the object True
b = False
print(id(b))  # Address of the object False
c = None
print(id(c))  # Address of the object None
c = None
print(id(c))  # Same address of the object None


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))  # Address of the object Hyd
#a[1] = 'e'  # Error due to a string is immutable
a = 'Sec'
print(id(a))  # Address of the object Sec
b = (10 , 20 , 15 , 18)
print(id(b))  # Address of the tuple (10 , 20 , 15 ,18)
#b[2] = 19  # Error due  a tuple is immutable 
b = (30 , 40 , 35 , 32)
print(id(b))  # Address of the tuple (30 , 40 , 35 ,32)
c = range(5)
print(id(c))  # Address of the range (0 , 5 , 1)
#c[3] = 10  # Error due to indexing in range , immutable
c = range(5) 
print(id(c)) # Address of the range (0 , 5 , 1)

# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)  # True 
c = 'Hyd'
d = 'Hyd'
print(c  is  d)  # True
e = False
f = False
print(e  is  f)  # True
g = range(10)
h = range(10)
print(g  is  h)  # False

#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)  # false
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)  # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)  # True 
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  # True

# Find outputs (Home work)
print(10 + 20)  # 30
print(10.8 + 20.6)  # 31.4
print(3 + 4j + 5 + 6j)  # 8 + 10j
print(True + False)  # True
print('Hyder' + 'abad')  # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')  # SankarDayalSarma
print('10' + '20')  # 1020
print([10 , 20 , 30] + [1 , 2 , 3])  # [10 , 20 , 30 , 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  # (25 , 10.8 , 'Hyd' , 3+4j , True , None)
#print({10 , 20} + {30 , 40})  # Error due to '+' operator in sets
#print({10 : 'Hyd'} + {20 : 'Sec'})  # Error due to '+' operator in dictionary
#print(range(4) + range(5))  # Error due to range is neither done in plus nor pipe
#print(10 + '20')  # Error due to non seq + seq
#print([10 , 20 , 30] + 5)  # Error due to non seq + seq
#print([10 , 20 , 30] + (40 , 50 , 60))  # Error due to list + tuple

# Find outputs (Home work)
print(25 * 3)  # 75 
print(10.8 * 25.6)  # 276.48
print(True * False)  # 0 
print((3 + 4j) * (5 + 6j))  # 3 * 5 + 3 * 6j + 4j * 5 + 4j * 6j  =  15 + 18j + 20j - 24j  =  -9 + 38j
print(3 + 4j * 5 + 6j)  # 3 + 20j + 6j  =  3 + 26j
print('25' * 3)  # '252525'
print(3 * '25')  # '252525'
print('Hyd' * 4)  # 'HydHydHydHyd'
print([10 , 20 , 15] * 2)  # [ 10 , 20 , 15 , 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)  # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0)  # Error due to float
#print({10 , 20 , 15} * 2)  # Error due to no duplicates in set
#print({10 : 20 , 30 : 40} * 2)  # Error due to no duplicates in dictionary
#print([10] * [20])  # Error due to List * List can't do

