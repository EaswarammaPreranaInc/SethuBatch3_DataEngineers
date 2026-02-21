'''s
#  Find  outputs
a = 25
print(id(a)) #1010
a = 35
print(id(a)) #2010

 The id of a changes 2 times because

--> 1st time the reference a contain the address of objest 25 that is 1010

--> 2nd time the refernece a is points to adress of object 35 that is 2010 


# Find  outputs (Home  work)
a = 25.7
print(id(a)) #--> The reference a contain the address of objest 25.7 that is 1010
print(a) # 25.7
a = 35.6
print(id(a)) #--> The reference a contain the address of objest 35.6 that is 2010
print(a) # 35.6
b = True
print(id(b))# --> The reference b contain the address of objest True that is 3010
b = False
print(id(b)) # --> The reference a contain the address of objest False that is 4010
c = None
print(id(c)) # The reference a contain the address of objest None that is 6010
c = None
print(id(c)) # The reference a contain the address of objest None that is 6010

a = 'Hyd'
print(id(a))# The reference a contain the address of objest Hyd that is 1010
# a[1] = 'e'  = ERROR

a = 'Sec'  
print(id(a)) # The reference a contain the address of objest Sec that is 2010

b = (10 , 20 , 15 , 18)
print(id(b)) # The reference b contain the address of objest tuple that is 1000010
# b[2] = 19 # ERROR

b = (30 , 40 , 35 , 32)
print(id(b)) # The reference a contain the address of tuple object that is 3000010

c = range(5)
print(c)  # range object is printed instead of numbers like range(0,5)
print(id(c)) # The reference c contain the address of range objest that is 2078685
# c[3] = 10 = ERROR NE INDEXING  IT IS IMMUTABLE

a = 25
b = 25
print(a  is  b) # TRUE
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # TRUE
e = False
f = False
print(e  is  f) # TRUE
g = range(10)
h = range(10)
print(g  is  h) # FALSE

a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)         # FALSE References  'a'  and  'b'  point  to  different  lists
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)         #FALSE References  'c'  and  'd'  point  to  different  lists
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)         # TRUE References  'e'  and  'f'  point  to  same  lists
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)         # FALSE References  'g'  and  'h'  point  to  different  lists
'''
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4 
print(3 + 4j + 5 + 6j) # (8+10j)
print(True + False)  # 1
print('Hyder' + 'abad') # hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # sankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3] creates the list of 6 elements 
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd', (3+4j), True, None) creates the tuple of 6 elements 
# print({10 , 20} + {30 , 40}) = ERROR BECAUSE 2 SETS CANNOT BE ADDED
#print({10 : 'Hyd'} + {20 : 'Sec'}) = ERROR 2 DICTONARIES CANNOT BE ADDED
#print(range(4) + range(5)) = ERROE 2 RANGE OBJECTS CANNOT BE ADDED
#print(10 + '20') = ERROR ONE STRING AND ONE INT CANNOT BE ADDED
#print([10 , 20 , 30] + 5) = ERROR LIST CAN ONLU CONCATINATE ONLUY LIST NOT INT
#print([10 , 20 , 30] + (40 , 50 , 60)) = ERROR ERROR LIST CAN ONLU CONCATINATE ONLUY LIST NOT TUPLE



print(25 * 3)   # 75
print(10.8 * 25.6)  #276.48
print(True * False) #0
print((3 + 4j) * (5 + 6j))#(-9+38j)
print(3 + 4j * 5 + 6j) #(3+26j)
print('25' * 3) 
print(3 * '25')# 252525
print('Hyd' * 4) #HydHydHydHyd
print([10 , 20 , 15] * 2) #[10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) #(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0) = ERROR REPETATION WITH ONLY INT TYPE NOT FLOAT 
#print({10 , 20 , 15} * 2) = IGNORED BECAUSE SET DOESNT CONTAIN THE DUPLICATES
#print({10 : 20 , 30 : 40} * 2) = ERROR DICT DOES NOT INT OR REPETATION
#print([10] * [20])  = WE ACN MULTIPLY THE LIST WITH INT BUT NOT LIST
