# Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

str = input("Enter string: ")
first = str[0]
rest = str[1:]
rest = rest.replace(first, '*')
print(first + rest)

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) 
print(a) # 15 36 48

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))
print(a . split())
print(a . split('green'))
print(a . split(''))
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))
print(a . split())
print(a . split(' '))
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())
print(a . split(' '))
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))

#Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))
d = ['www' , 'gmail', 'com']
print('.' . join(d))
e = [15 , 36 , 48]
print(':' . join(e))
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))
g = range(5)
print('-' . join(g))
#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper())
print(a . lower())
print(a . capitalize())
print(a . title())
print(a . swapcase())
print(a)
print('A7$a' . upper())

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))
print(a . endswith('town'))
print(a . endswith('green' , 3 , 12))
print(a . endswith('green' , 3 , 13))
print(a . endswith(' ' , 3 , 13))

#Write  a  program  to  append  'ing'  to  input  string. Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'. Leave  the  string  unchanged  if  string  has  lessthan  three  characters

#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())
print('Rama  Rao'  . isalpha())
print('Hyd4'  . isalpha())
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha())
print('+-$'    .  isalpha())
print('A2#'  .   isalpha())
print(''  .  isalpha())  #  False
print(' '  .  isalpha())

# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())
print('92a47' . isdigit())
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit())
print('+-$' . isdigit())
print('A2#' . isdigit())
print('' . isdigit()) #   False
print(' ' . isdigit())
print(9247 . isdigit())

# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())
print('\n  \t' . isspace())
print('\n  7\t' . isspace())
print('\n' . isspace())
print('\n  $\t' . isspace())  #  False
print('\t' . isspace())
print('' . isspace())  #  False
print(' ' . isspace())

# islower()  method  demo  program  (Home  work)
print('hyD' . islower())
print('hyd' . islower())
print('9247' . islower())
print('rama  rao' . islower())
print('+-$' . islower())
print('hyd+-$' . islower())
print('abc123' . islower())
print('' . islower())
print('a2#' . islower())

[13:01, 07/03/2026] +91 99482 50500: # Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))

# Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

# Write  a  program  to  reverse  a  string  without  slice

# Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

# Write  a  program  to  reverse  each  word  of  the  sentence

#Write  a  program  to  sort  string  in  alphabetical  order

#Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
