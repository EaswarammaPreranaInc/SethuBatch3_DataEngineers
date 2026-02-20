# Rathanpalke AkhilKumar 19-02-2026

print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8)  #   True
print(6 <= 6)  #   True
print(6 <= 4)  #   False
print(9 != 7)  #   True
print(6 == 8)  #   False
print(True  >  False) # True 
print(3 + 4j == 3 + 4j) # True
print(3 + 4j == 5 + 6j) # False
print(3 + 4j != 5 + 6j) # True
print(10 == 10.0)        # True
print(3 + 4j >  3 + 4j)   # TypeError: '>' not supported between instances of 'complex' and 'complex'

print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana')  # True :  both strings are equal
print('Rama  Rao'  >=  'Rama') # True : 
print('Hyd'  != 'Sec')  # True   #  different strings
print('HYD'  <   'hyd') # True


print(10 < 20 < 30)  # True : 10 < 20 and 20 < 30 → both True

print(10 >= 20 < 30)  # False : 10 >= 20 is False, so overall False

print(10 < 20 > 30) # False : 10 < 20 is True but 20 > 30 is False

print(1 < 2 < 3 < 4) # True :  all comparisons True

print(1 < 2 > 3 > 1) # False : 2 > 3 is False, so overall False

print(4 > 3 >= 3 > 2) # True :  4 > 3, 3 >= 3, and 3 > 2 → all True

i = 10
i = not  i > 14
print(i) # True i > 14 → 10 > 14 → False 
print(not(6 < 4  or  9 >= 5  and  6 != 6)) # True 


a = 25
print(a)# 25
b =  a # 25
print(b) # 25
print(a  is  b) # True a and b refer to the same object (25)
x = 4
y = 5
z = x + y * 6 # 34
print(z) # 34 
25 = a # SyntaxError
a + b = x + y # SyntaxError

a = b = c = 25
print(id(a)) # same id (memory address)
print(id(b)) # same id as a
print(id(c))# same id as a and b
print(a , b , c) # 25 25 25


x , y , z = 25 , 10.8 , 'Hyd'
print(x) # 25
print(y) #10.8
print(z) # Hyd

a , b , c = 3 , 4 , 5
a *= b + c   
print(a) # 27



a = 25
b = 25.0
print(a is b) # False
print(a is not b) # True
print(a == b) # True

list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True   # 15 is present in the list
print(19 in list) # False  # 19 not present
print(14 not in list)# True   # 14 not present
print(15 not in list)# False  # 15 is present
s = 'Hyd is green city'
print('is' in s) # True   # substring 'is' present
print('was' in s) # False  # not present
print('g' in s)# True   # 'g' present in "green"
print('z' in s)# False  # not present
print(' ' in s)# True   # space exists in string
print('gre' in s) # True   # substring present
print('yd i' in s) # True   # substring exists: "Hyd is"
print('' in s) # True   # empty string always considered present in any string
print('' not in s) # False  # opposite of above


x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # False  
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  # False  
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)  # True  
m = range(5)
n = range(5)
print(m == n) # True 


a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  # False
print(a  ==  b) # False

list = [10 , 20 , 15 , 12 , 18]
print(15 in list)# True   
print(19 in list) # False 
print(14 not in list)# True  
print(15 not in list) # False  
s = 'Hyd is green city'
print('is' in s) # True  
print('was' in s) # False 
print('g' in s) # True   
print('z' in s)# False  
print(' ' in s) # True 
print('gre' in s) # True  
print('yd i' in s) # True 
print('' in s) # True  

print('' not in s)# False 



