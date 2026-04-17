'''
1) Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
Let  input  be  'babble'
What  is  the  output ?  --->  ba**le
'''
s = input('Enter any string : ')
first = s[0]
rest = s[1:].replace(first, '*')
print(first + rest)

'''
2) Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) # ['15', '36', '48']
print(a) # '15:36:48'
'''
'''
3) Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))  # ['Hyd\nis', 'green\tcity']
print(a . split())  # ['Hyd\nis', 'green\tcity']
print(a . split('green'))  # ['Hyd\nis ', '\tcity']
print(a . split('')) # Error because empty seperator
'''
'''
4) Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd', 'is', 'green', 'city']
print(a . split())     # ['Hyd', 'is', 'green', 'city']
print(a . split(' '))  # ['Hyd\tis\tgreen\tcity']
'''
'''
5) # Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())  # ['Hyd', 'is', 'green', 'city']
print(a . split(' '))  # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']
'''
'''
6) # Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))  # ['www', 'gmail', 'com']
'''
'''
7) Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912
Print  the  sum
Hint:  Use  split()  method
'''
a = input('Enter expression with + : ')
parts = a.split('+')
total = 0
for x in parts:
    total += int(x)
print('Sum :', total)
'''
8) Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))  # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))  # Hyd id green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))  # 10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))  # www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))  # 15:36:48
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))  # SankarDayalSarma
g = range(5)
print('-' . join(g))  # Error because range has integers
'''
'''
9) #  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper())  # HYD IS GREEN CITY
print(a . lower())  # hyd is green city
print(a . capitalize()) # Hyd is green city
print(a . title())  # Hyd Is Green City
print(a . swapcase())  # HYd Is GReEN CitY
print(a)  # hyD  iS  grEen  cITy
print('A7$a' . upper())  # A7$A
'''
'''
10) endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))  # True
print(a . endswith('town'))  # False
print(a . endswith('green' , 3 , 12))  # True
print(a . endswith('green' , 3 , 13))  # False
print(a . endswith(' ' , 3 , 13))  # True
'''
'''
11) Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters
'''
s = input('Please enter string : ')
if len(s) < 3:
    print(s)
elif s.endswith('ing'):
    print(s + 'ly')
else:
    print(s + 'ing')
'''
12) #  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  # False
print('Rama  Rao'  . isalpha())  # True
print('Hyd4'  . isalpha())  # False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha())  # False
print('+-$'    .  isalpha())  # False
print('A2#'  .   isalpha())  # False
print(''  .  isalpha())  #  False
print(' '  .  isalpha())  # False
'''
'''
13) # isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit())  # False
print('+-$' . isdigit())  # False
print('A2#' . isdigit())  # False
print('' . isdigit())  # False
print(' ' . isdigit())  # False
print(9247 . isdigit()) # Error because it should be in quotes
'''
'''
14) # isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  # False
print('\n  \t' . isspace())  # True
print('\n  7\t' . isspace())  # False
print('\n' . isspace())  # True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace())  # True
print('' . isspace())  #  False
print(' ' . isspace())  # True
'''
'''
15) # islower()  method  demo  program  (Home  work)
print('hyD' . islower())  # False
print('hyd' . islower())  # True
print('9247' . islower())  # False
print('rama  rao' . islower())  # True
print('+-$' . islower())  # False
print('hyd+-$' . islower())  # True
print('abc123' . islower())  # True
print('' . islower())  # False
print('a2#' . islower())  # True
'''
'''
16) # Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))  # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))  # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))  # a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))  # a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))  # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))  # a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))  # a  :  25  	  b  :  25  	  c  :  25
'''
'''
17) Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  ---> White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space
'''
ch = input('Enter any character : ')
if ch.isalnum():
    print('Alpha Numeric Character')
    if ch.isalpha():
        print('Alphabet Character')
        if ch.isupper():
            print('Upper case Alphabet')
        else:
            print('Lower case Alphabet')
    elif ch.isdigit():
        print('Digit Character')
elif ch.isspace():
    print('White space')
else:
    print('Special Character')
'''
18) Write  a  program  to  reverse  a  string  without  slice
1) Let  input  be   Hyd
    What  is  the  output ?  --->  dyH
'''
a = input('Enter any string : ')
b = ''
for i in range(1, len(a)+1):
    b = b + a[-i]
print('Reverse String :', b)

'''
19) Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd
'''
a = input('Enter any sentence : ')
b = a.split()   # split words
c = ''
for i in range(1, len(b)+1):
    c = c + b[-i] + ' '
print('Reverse order of words :', c.strip())

'''
20) Write  a  program  to  reverse  each  word  of  the  sentence
1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic
'''
a = input('Enter any sentence : ')
b = a.split()
for x in b:
    print(x[::-1], end=' ')

'''
21) Write  a  program  to  sort  string  in  alphabetical  order
Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
a = input('Enter any string : ')
b = sorted(a)
c = ''.join(b)
print('Sorted string :', c)

'''
22) Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579
'''
a = input('Enter string with alphabets and digits : ')
b = sorted(a)
alpha = ''
digit = ''
for x in b:
    if x.isalpha():
        alpha += x
    else:
        digit += x
print('Result :', alpha + digit)