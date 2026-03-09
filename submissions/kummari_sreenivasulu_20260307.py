1.
'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le
Hint : Use  replace()  method
'''
x = input ("Enter a string :")
y = x[0]
z = x.replace(y, "*")
z = y + z[1:]
print(z)


2.

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) # ['15', '36', '48']
print(a) # 15:36:48


3.
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis', 'green\tcity']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split('green')) # ['Hyd\nis ', '\tcity']
#print(a . split('')) # ValueError: empty separator



4.
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd', 'is', 'green', 'city']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd\tis\tgreen\tcity']



5.
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # ['Hyd', 'is', 'green', 'city'] 
print(a . split(' ')) # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']



6.
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) # ['www', 'gmail', 'com']


7.
'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''
x = input ("Enter an expression :")
y = x.split('+')
z = 0
for i in y:
    z = z + int(i)
    print(z)


8.
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))# 10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d)) # www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) # TypeError: sequence item 0: expected str instance, int found
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # sankarDayalSarma
g = range(5)
print('-' . join(g)) # TypeError: sequence item 0: expected str instance, int found


9.
#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) # HYD  IS GREEN CITY
print(a . lower()) # hyd is green city
print(a . capitalize()) # Hyd is green city
print(a . title()) # Hyd Is Green City
print(a . swapcase()) # HYd Is GRrEEN CIty
print(a)
print('A7$a' . upper()) # A7$A
'''
1) What  does  upper()  method  do ?  --->  Returns  an  upper  case  string

2) What  does  lower()  method  do ?  --->  Returns  a  lower  case  string

3) What  does  capitalize()  method  do ?  --->  Returns  a  string  where  1st  char  is  uppercase  and  the  rest  in  lower  case

4) What  does  title()  method  do ?  --->  Returns  a  string  where  1st  char  of  each  word  is  uppercase  and  the  rest  in  lowercase

5) What  does  swapcase()  method  do ?  --->  Returns  a  string  where  upper  case  alphabets  are  converted  to
																         lower  case  and   vice-versa
'''


10.
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) # True
print(a . endswith('town')) # False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13)) # False
print(a . endswith(' ' , 3 , 13)) # True


11.
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself

4) Hint:  Use  endswith()  method
'''
x = input ("Enter a string :")
if x.endswith('inh'):
    print(x + 'ly')
elif x.endswith('ing'):
    print(x + 'ly')
elif len(x) < 3:
    print(x)
else:
    print(x + 'ing')



12.
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha()) # True
print('Rama  Rao'  . isalpha()) # False Because of space
print('Hyd4'  . isalpha()) # False Because of digit
print('Hyd$'  . isalpha())  #   False because of special character
print('9247'  .  isalpha()) # False because of digits
print('+-$'    .  isalpha()) # False because of special charactrers
print('A2#'  .   isalpha()) # Flase because of digits and special charactres
print(''  .  isalpha())  #  False because of empty string
print(' '  .  isalpha()) # False because of space
'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  an  alphabet

2) When  does  it  return  False  ?  --->  When  at  least  one  character  of  the  string  is  non-alphabet  i.e. digit (or) special  character
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''


13.
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) #  alse because of A
print('\n  \t' . isspace()) # True  because of \n and \t
print('\n  7\t' . isspace()) # False because of 7
print('\n' . isspace()) # True because of \n
print('\n  $\t' . isspace())  #  False because of $
print('\t' . isspace()) # True because of \t
print('' . isspace())  #  False because of empty string
print(' ' . isspace()) # True because of space
'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  not  a  white  space
															 (i.e.  Alphabet, digit (or)  special  character)
																					(or)
															 When  there  are  no  white  space  characters																					
'''


14.
# islower()  method  demo  program  (Home  work)
print('hyD' . islower()) # False because of D
print('hyd' . islower()) # True because of all lowercase
print('9247' . islower()) # False because of digits
print('rama  rao' . islower()) # False because of space
print('+-$' . islower()) # False because of special characters
print('hyd+-$' . islower()) # False because of special characters
print('abc123' . islower()) # False because of digits
print('' . islower()) # False because of empty string
print('a2#' . islower()) # False because of digits and special characters
'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  ---> When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
																			 When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  ---> When  there  are  no  uppercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  lowercase  alphabet

Note:
1) What  are  upper()  and  lower()  called ?  --->  Conversion  methods

2) What  are  isupper()  and  islower()  called ?  --->  Conditional  methods  becoz  they  return  True  (or)  False
'''


15.
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  25  	  b  :  25  	  c  :  25


16.
'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  ---> White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods

9) Hint2:  Use  nested  if  and   elif
'''

x = input("Enter a character :")
if x.isalnum():
    print("Alphanumeric character")
    if x.isalpha():
        print("Alphabet character")
        if x.isupper():
            print("Upper case alphabet")
        else:
            print("Lower case alphabet")
    else:
        print("Digit character")
elif x.isspace():
    print("White space")
else:
    print("Special character")


17.
'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  --->  dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1        'd'             '' + 'd' = 'd'								
     2       'y'             'd' + 'y' = 'dy'								
     3       'H'            'dy' + 'H' = 'dyH'								
  ---------------------------------------------
'''
x = input ("Enter a string :")
y = ''
for i in range(1, len(x) + 1):
    y = y + x[-i]
    print(y)



18.
'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
    1        'city'        '' + 'city' + ' ' = 'city '							  
    2        'green'     'city ' + 'green' + ' ' = 'city green '							  
    3        'is'            'city green ' + 'is' + ' ' = 'city green is '							  
    4        'Hyd'        'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '							  
   -------------------------------------------------------
'''
x = input("Enter a sentence :")
y = ''
z = x.split()
for i in range(1, len(z) + 1):
    y = y + z[-i] + ' '
    print(y)



19.
'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
x = input("Enter a sentence :")
y = ''
z = x.split()
for i in z:
    y = y + i[::-1] + ' '
    print(y)


20.
'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
x = input("Enter a string :")
y = sorted(x)
z = ''
for i in y:
    z = z + i
    print(z)



21.
'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
x = input("Enter a string :")
y = sorted(x)
alpha  = ''
digit = ''
for i in y:
    if i.isalpha():
        alpha = alpha + i
    elif i.isdigit():
        digit = digit + i
z = alpha + digit
print(z)
