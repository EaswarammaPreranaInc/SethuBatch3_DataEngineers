# Find outputs  (Home  work)
print('green' in 'Hyd  is  green  city')  # True
print('day' in 'Sankar  dayal  sarma')  # True
print('Green' in 'Hyd  is  green  city')  # False
print('d  is' in 'Hyd  is  green  city')  # True
print('dis' in 'Hyd  is  green  city')  # False
print('iniv' in 'Srinivas')  # True
print('iniv' not in 'Srinivas')  # False

# -----------------------------------------------------------------------------------------

'''
1) What  does  in  and  not  in  operators  do ?  --->  Searches  for  a  string  in  another  string

2) What  does  str1  in  str2  do ? --->  Returns  True  if  str1  is  in  str2  and  False  otherwise

3) What  does  str1  not  in  str2  do ? --->  Returns  True  if  str1  is  not  in  str2  and  False  otherwise

4) not  in  operator  is  quite  opposite  to  in  operator
'''

# -----------------------------------------------------------------------------------------

'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''

a = 'Rama Rao'

print(a[:7:2])  # Rm a
print(a[:7])  # Rama Ra
print(a[2:4])  # ma
print(a[2:])  # ma Rao
print(a[:4])  # Rama
print(a[::2])  # Rm a
print(a[-6:-1])  # ma Ra
print(a[-6:])  # ma Rao
print(a[:-4:-1])  # oaR
print(a[-3:-1])  # Ra
print(a[-3:])  # Rao
print(a[::])  # Rama Rao
print(a[:])  # Rama Rao
print(a[::-1])  # oaR amaR
print(a[::-2])  # oRaa
print(a[-2::-2])  # a mR
print(a[2:8])  # ma Rao
print(a[2:8:-1])  # '' (empty string because step is negative but start < stop)
print(a[:-6:-1])  # oaR a
print(a[2:-3])  # ma 
print(a[1:6:2])  # aaR
print(a[:-5:-5])  # o
print(a[2:-5])  # m
print(a[2:-5:2])  # m
print(a[:0:-1])  # oaR ama
print(a[-5:0:-2])  # aa

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice
'''

h = input('Enter first string: ')  # Enter first string: Java
p = input('Enter second string: ')  # Enter second string: Python

x = p[:2] + h[2:] + ' ' + h[:2] + p[2:]

print('Result:', x)  # Result: Pyva Jathon

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''

x = input('Enter any string: ')  # Enter any string: PYTHON

if len(x) > 4:
    print(x[:2] + x[-2:])  # PYON
else:
    print('')

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice
'''

x = input('Enter the string: ')  # Enter the string: VAMSI

for i in range(len(x)):
    print(F'Character at index {i} : {x[i]}')

for i in range(1, len(x) + 1):
    print(F'Character at index {-i} : {x[-i]}')

# -----------------------------------------------------------------------------------------

x = input('Enter a string: ')  # Enter a string: HYDERABAD

odd = ''
even = ''

for i in range(len(x)):
    if i % 2 == 0:
        even += x[i]
    else:
        odd += x[i]

print('String at even indexes:', even)
print('String at odd indexes:', odd)

# -----------------------------------------------------------------------------------------

'''
Let  input  be    A   4   B   3   C   2   $   5
What  is  the  output ?  --->  AAAABBBCC$$$$$
'''

try:
    x = input('Enter a string with alternate character and digit : ')  # Enter: A4B3C2$5
    y = ''

    for i in range(0, len(x), 2):
        y += x[i] * int(x[i + 1])

    print('RESULT:', y)  # RESULT: AAAABBBCC$$$$$

except ValueError:
    print('String should have alternate character and digit')

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  merge  two  strings  to  form  a  new  string
'''

x = input('Enter first string: ')  # HYD
y = input('Enter second string: ')  # VAMSI

z = ''
i = 0

while i < len(x) and i < len(y):
    z += x[i] + y[i]
    i += 1

z = z + x[i:] + y[i:]

print('Result:', z)  # Result: HVYADMSI

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
'''

x = input('Enter any string: ')  # RAMA RAO
y = ''

for i in x:
    if i not in y:
        y += i

print('String without duplicates:', y)  # RAM O

# -----------------------------------------------------------------------------------------

# len()  function  demo  program  (Home  work)

print(len('Hyd'))  # 3
print(len('Rama Rao'))  # 8
print(len('9247'))  # 4
print(len('+-$'))  # 3
print(len(''))  # 0
print(len(' '))  # 1
print(len('A2#'))  # 3

# print(len(3456))  # Error because len() argument must be a sequence
# print('Sec'.len())  # Error because string has no len() method

# -----------------------------------------------------------------------------------------

# chr()  function  demo  program

print(chr(65))  # A
print(chr(90))  # Z
print(chr(97))  # a
print(chr(122))  # z
print(chr(48))  # 0
print(chr(57))  # 9
print(chr(36))  # $
print(chr(32))  # <space>

# -----------------------------------------------------------------------------------------

# ord()  function  demo  program

print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32

# -----------------------------------------------------------------------------------------

'''
Let  input  be  A4M3Z5D2
What  is  the  output ?  --->  AEMPZ_DF
'''

try:
    x = input('Enter a string with alternate character and digit: ')  # A4M3Z5D2
    z = ''

    for i in range(0, len(x), 2):
        z += x[i] + chr(ord(x[i]) + int(x[i + 1]))

    print('Result:', z)  # Result: AEMPZ_DF

except ValueError:
    print('Please enter a string with alternate character and digit')

# -----------------------------------------------------------------------------------------

'''
Modify  following  program  with  walrus  operator
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = a.find('is')

while index != -1:
    print(index)
    index = a.find('is', index + 1)

print('End')

# -----------------------------------------------------------------------------------------

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = 0

while (index := a.find('is', index + 1)) != -1:
    print(index)

print('End')

# -----------------------------------------------------------------------------------------

# count()  method  demo  program

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

print(a.count('is'))  # 4
print(a.count('is', 19, 48))  # 3
print(a.count('was'))  # 0

# -----------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'

print(a.count(' '))  # 3
print(a.count('\t'))  # 3
print(a.count('\n'))  # 3