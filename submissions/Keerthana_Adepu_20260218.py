#Outputs Homework #1
a = 25
print(id(a)) # address of the int object a 
a = 35
print(id(a)) # address of the new int object a


#Outputs Homework #2
a = 25.7
print(id(a)) # address of the float object a
print(a) # 25.7
a = 35.6
print(id(a)) # address of the new float object a
print(a) # 35.6
b = True
print(id(b)) # address of the bool object b
b = False
print(id(b)) # address of the new bool object b
c = None
print(id(c)) # address of the NoneType object b
c = None
print(id(c)) # address of the NoneType object b


#Outputs Homework #3
a = 'Hyd'
print(id(a)) # address of the str object a
a[1] = 'e' # error because str object is immutable   
a = 'Sec'
print(id(a)) # address of the new str object a
b = (10 , 20 , 15 , 18)
print(id(b)) # address of the tuple object b
b[2] = 19 # error because tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b)) # address of the new tuple object b
c = range(5) # 0 , 1 , 2 , 3 , 4
print(id(c)) # address of the range object c
c[3] = 10 # error because range is immutable
c = range(5)
print(id(c)) # address of the range object c


#Outputs Homework #4
a = 25
b = 25
print(a  is  b) # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True
e = False
f = False
print(e  is  f) # True
g = range(10)
h = range(10)
print(g  is  h) # False


#Outputs Homework #5
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) # False


#Outputs Homework #6
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # 8 + 10j
print(True + False) # 1
print('Hyder' + 'abad') # 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma') # 'SankarDayalSarma'
print('10' + '20') # '1020'
print([10 , 20 , 30] + [1 , 2 , 3]) # [10 , 20 , 30 , 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25 , 10.8 , 'Hyd' , 3 + 4j , True , None)
print({10 , 20} + {30 , 40}) # error because set cannot be concatenated with the '+' operator
print({10 : 'Hyd'} + {20 : 'Sec'}) # error because dictionary cannot be concatenated with the '+' operator
print(range(4) + range(5)) # error because range cannot be concatenated with the '+' operator
print(10 + '20') # error because non-sequence + sequence is not permitted
print([10 , 20 , 30] + 5) # error because non-sequence + sequence is not permitted
print([10 , 20 , 30] + (40 , 50 , 60)) # error because a list and a tuple cannot be added


#Outputs Homework #7
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # -9 + 38j
print(3 + 4j * 5 + 6j) # 3 + 26j
print('25' * 3) # '252525'
print(3 * '25') # '252525'
print('Hyd' * 4) # 'HydHydHydHyd'
print([10 , 20 , 15] * 2) # [10 , 20 , 15 , 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True , 25, 10.8, 'Hyd', True , 25, 10.8, 'Hyd', True))
print([10 , 20 , 15] * 3.0) # error when using * as a repition tool only integer can be used for the argument
print({10 , 20 , 15} * 2) # {10 , 20 , 15} # the doubles values in a set are ignored and not printed
print({10 : 20 , 30 : 40} * 2) # error because keys in dictionary can't have duplicate objects and repeition will make it have duplicates
print([10] * [20]) # [10 , 20]
