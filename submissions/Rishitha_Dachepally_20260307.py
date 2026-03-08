'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''

x = input('Enter a string: ')  # Enter a string: babble
z = x[0] + x[1:].replace(x[0], '*')
print(z)  # ba**le

# -----------------------------------------------------------------------------------------

#  Find  outputs  (Home  work)

a = '15:36:48'

print(a.split(':'))  # ['15', '36', '48']
print(a)  # 15:36:48

# -----------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

a = 'Hyd\nis green\tcity'

print(a.split(' '))  # ['Hyd\nis', 'green\tcity']
print(a.split())  # ['Hyd', 'is', 'green', 'city']
print(a.split('green'))  # ['Hyd\nis ', '\tcity']

# print(a.split(''))  # Error because delimiter cannot be empty string

# -----------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

a = 'Hyd\tis\tgreen\tcity'  #  There  is  tab  between  the  words

print(a.split('\t'))  # ['Hyd', 'is', 'green', 'city']
print(a.split())  # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))  # ['Hyd\tis\tgreen\tcity']

# -----------------------------------------------------------------------------------------

# Find  outputs (Home  work)

a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words

print(a.split())  # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))  # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

# -----------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

a = 'www.gmail.com'

print(a.split('.'))  # ['www', 'gmail', 'com']

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''

x = input('Enter a expression with + symbols: ')  # 23+456+7+8912
y = x.split('+')
z = []

for i in y:
    z.append(int(i))

print(sum(z))  # 9398

# -----------------------------------------------------------------------------------------

#  Find  outputs  (Home  work)

a = ['15', '36', '48']
print(':'.join(a))  # 15:36:48

b = ('Hyd', 'is', 'green', 'city')
print(' '.join(b))  # Hyd is green city

c = {'10', '20', '15', '25', '52'}
print(','.join(c))  # Order may vary because set is unordered

d = ['www', 'gmail', 'com']
print('.'.join(d))  # www.gmail.com

e = [15, 36, 48]
# print(':'.join(e))  # Error because join() requires string elements

f = ['Sankar', 'Dayal', 'Sarma']
print(''.join(f))  # SankarDayalSarma

g = range(5)
# print('-'.join(g))  # Error because join() requires string elements

# -----------------------------------------------------------------------------------------

#  Case  conversion  methods  (Home  work)

a = 'hyD  iS  grEen  cITy'

print(a.upper())  # HYD  IS  GREEN  CITY
print(a.lower())  # hyd  is  green  city
print(a.capitalize())  # Hyd  is  green  city
print(a.title())  # Hyd  Is  Green  City
print(a.swapcase())  # HYd  Is  GReEN  CitY
print(a)  # hyD  iS  grEen  cITy
print('A7$a'.upper())  # A7$A

# -----------------------------------------------------------------------------------------

# endswith()  method  demo  program

a = 'Hyd is green city'

print(a.endswith('city'))  # True
print(a.endswith('town'))  # False
print(a.endswith('green', 3, 12))  # True
print(a.endswith('green', 3, 13))  # False
print(a.endswith(' ', 3, 13))  # True

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters
'''

x = input('Enter a string: ')  # interest

if len(x) < 3:
    print(x)
else:
    if x.endswith('ing'):
        x += 'ly'
    else:
        x += 'ing'

    print(x)  # interesting

# -----------------------------------------------------------------------------------------

#  isalpha()  method  demo  program

print('Hyd'.isalpha())  # True
print('Rama Rao'.isalpha())  # False
print('Hyd4'.isalpha())  # False
print('Hyd$'.isalpha())  # False
print('9247'.isalpha())  # False
print('+-$'.isalpha())  # False
print('A2#'.isalpha())  # False
print(''.isalpha())  # False
print(' '.isalpha())  # False

# -----------------------------------------------------------------------------------------

# isdigit()  method  demo  program

print('9247'.isdigit())  # True
print('92a47'.isdigit())  # False
print('92$47'.isdigit())  # False
print('Hyd'.isdigit())  # False
print('+-$'.isdigit())  # False
print('A2#'.isdigit())  # False
print(''.isdigit())  # False
print(' '.isdigit())  # False

# print(9247.isdigit())  # Error because int object has no isdigit() method

# -----------------------------------------------------------------------------------------

# isspace()  method  demo  program

print('\n  A\t'.isspace())  # False
print('\n  \t'.isspace())  # True
print('\n  7\t'.isspace())  # False
print('\n'.isspace())  # True
print('\n  $\t'.isspace())  # False
print('\t'.isspace())  # True
print(''.isspace())  # False
print(' '.isspace())  # True

# -----------------------------------------------------------------------------------------

# islower()  method  demo  program

print('hyD'.islower())  # False
print('hyd'.islower())  # True
print('9247'.islower())  # False
print('rama  rao'.islower())  # True
print('+-$'.islower())  # False
print('hyd+-$'.islower())  # True
print('abc123'.islower())  # True
print(''.islower())  # False
print('a2#'.islower())  # True

# -----------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

a, b, c = 25, 10.8, 'Hyd'

print('a  :  {}  \t  b  :  {}  \t  c  :  {}'.format(a, b, c))  # a  :  25  b  :  10.8  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}'.format(a, b, c))  # a  :  25  b  :  10.8  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}'.format(a, b, c))  # a  :  Hyd  b  :  10.8  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}'.format(a, b, c))  # a  :  Hyd  b  :  Hyd  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}'.format(x=a, y=b, z=c))  # a  :  25  b  :  10.8  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}'.format(z=a, y=b, x=c))  # a  :  Hyd  b  :  10.8  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}'.format(z=a, y=b, x=c))  # a  :  25  b  :  25  c  :  25

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  reverse  a  string  without  slice
'''

a = input('Enter a string: ')  # Hyd

z = ''

for i in range(1, len(a) + 1):
    z += a[-i]

print('reverse string:', z)  # dyH

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
'''

a = input('Enter a sentence: ')  # Hyd is green city

b = a.split()

c = ''

for i in range(1, len(b) + 1):
    c += b[-i] + ' '

print('Reverse order of words', c)  # city green is Hyd

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  reverse  each  word  of  the  sentence
'''

a = input('Enter a string: ')  # Hyd is green city

b = a.split()

c = ''

for word in b:
    c += word[::-1] + ' '

print(c)  # dyH si neerg ytic

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
'''

a = input('Enter a string with alphabets and digits: ')  # Z9K3PA7D51

b = ''
c = ''

for i in range(len(a)):
    if a[i].isalpha():
        b += a[i]

    if a[i].isdigit():
        c += a[i]

b = ''.join(sorted(b))
c = ''.join(sorted(c))

print('Result:', b + c)  # ADKPZ13579