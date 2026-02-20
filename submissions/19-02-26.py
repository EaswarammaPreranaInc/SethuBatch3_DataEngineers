print(7 / 0) # Error (division by zero)
print(7 // 0) # Error (division by zero)
print(7 % 0) # Error (division by zero)


***
print(9 >= 5) # True
print(9 >= 9) # True
print(9 >= 12) # False


print(6 <= 8) # True
print(6 <= 6) # True
print(6 <= 4) # False


print(9 != 7) # True
print(6 == 8) # False


print(True > False) # True (1 > 0)


print(3 + 4j == 3 + 4j) # True
print(3 + 4j == 5 + 6j) # False
print(3 + 4j != 5 + 6j) # True


print(10 == 10.0) # True


print(3 + 4j > 3 + 4j) # Error (complex numbers cannot use >)


***


print('Rama' > 'Rajesh') # True
print('Rama' < 'Sita') # True
print('Hyd' == 'Hyd') # True
print('Rama' <= 'Ramana') # True
print('Rama Rao' >= 'Rama') # True
print('Hyd' != 'Sec') # True
print('HYD' < 'hyd') # True


***


print(10 < 20 < 30) # True
print(10 >= 20 < 30) # False
print(10 < 20 > 30) # False
print(1 < 2 < 3 < 4) # True
print(1 < 2 > 3 > 1) # False
print(4 > 3 >= 3 > 2) # True




***


a = b = c = 25


print(id(a)) # Same address
print(id(b)) # Same address
print(id(c)) # Same address


print(a , b , c) # 25 25 25


***


x , y , z = 25 , 10.8 , 'Hyd'


print(x) # 25
print(y) # 10.8
print(z) # Hyd


***


a , b , c = 3 , 4 , 5
a *= b + c
print(a) # 27 (3 * 9)


***


a = 20
a %= 3 + 2 * 4
print(a) # 9 (20 % 11)


***


a = 3
a **= 4
print(a) # 81






***


a = 25
b = 25.0


print(a is b) # False
print(a is not b) # True
print(a == b) # True


***


x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]


print(x is y) # False
print(x is not y) # True
print(x == y) # True


***


m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)


print(m is n) # True
print(m is not n) # False
print(m == n) # True
print(x == m) # False


***


x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # False


a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b) # False


p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) # True


m = range(5)
n = range(5)
print(m == n) # True


***


list = [10 , 20 , 15 , 12 , 18]


print(15 in list) # True
print(19 in list) # False
print(14 not in list) # True
print(15 not in list) # False


***


s = 'Hyd is green city'


print('is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) # True
print('' in s) # True
print('' not in s) # False