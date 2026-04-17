#  Find  outputs
a = 25
print(id(a))  # address of object 25
a = 35
print(id(a)) # address of object 35



# Find  outputs (Home  work)
a = 25.7
print(id(a)) # address of object float25.7
print(a) # 25.7
a = 35.6
print(id(a)) # address of new object float 35.6
print(a) #35.6
b = True
print(id(b)) # address of object bool True
b = False
print(id(b)) # address of object bool False
c = None
print(id(c)) # address of object None
c = None
print(id(c)) # address of same object None



#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # address of object 'Hyd'
a[1] = 'e' # error bcoz 'str' are immutable
a = 'Sec'
print(id(a)) # address of object 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))
b[2] = 19 #error tuple are immmutable
b = (30 , 40 , 35 , 32)
print(id(b))
c = range(5)
print(id(c))
c[3] = 10
c = range(5)
print(id(c))



# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) # True  bcox reference 'a' and 'b' points to the same object 25
c = 'Hyd'
d = 'Hyd'
print(c  is  d) #True
e = False
f = False
print(e  is  f) # True
g = range(10)
h = range(10)
print(g  is  h) # false becoz range creates new object each time it is iterated



#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # false becoz, reference 'a' and 'b' points to different lists
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # false dict are mutable i.e,reference 'c' and 'd' points to different dictionary
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)# True bcoz,tuples are immutable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)# False sets are mutable i.e,reference 'g' and 'h' points to different sets





# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # 8+10j
print(True + False) # 1
print('Hyder' + 'abad') #Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')# sankarDayalsarma
print('10' + '20') #1020
print([10 , 20 , 30] + [1 , 2 , 3]) # 10,20,30,1,2,3
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40}) #error sets 
print({10 : 'Hyd'} + {20 : 'Sec'}) #error dict do not support +
print(range(4) + range(5)) #error range do not support +
print(10 + '20') #error 
print([10 , 20 , 30] + 5) #error
print([10 , 20 , 30] + (40 , 50 , 60))#error



# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) #276.48
print(True * False) #0
print((3 + 4j) * (5 + 6j)) #true 
print(3 + 4j * 5 + 6j) #true
print('25' * 3)# '252525'
print(3 * '25') #'252525'
print('Hyd' * 4) #'HydHydHydHyd'
print([10 , 20 , 15] * 2) # [10 , 20 , 15 ,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) #(25, 10.8, 'Hyd', True ,25, 10.8, 'Hyd', True ,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) #[10 , 20 , 15 ,10 , 20 , 15 ,10 , 20 , 15]
print({10 , 20 , 15} * 2) #error bcoz set is non seq
print({10 : 20 , 30 : 40} * 2) error bcoz dict is non seq
print([10] * [20]) #error second object cant be list