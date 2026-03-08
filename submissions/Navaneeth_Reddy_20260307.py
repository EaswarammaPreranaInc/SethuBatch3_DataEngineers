'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''

a = input("Enter the String : ")

f = a[0]
ao = a[1:]

ao = ao.replace(f , '*')

res = ao + f

print("Result : ",res)

'''
Output :
Enter the String : babble
Result :  ba**le
'''

#-----------------------------------------------------------

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) 
print(a) # ['15','36','48']

#---------------------------------------------------------------

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis','green\tcity']
print(a . split()) # ['Hyd, 'is', 'green', 'city']
print(a . split('green')) # ['Hyd\nis','\tcity']
print(a . split('')) # Error

#-------------------------------------------------------------------

# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd', 'is', 'green', 'city']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd\tis\tgreen\tcity']

#-----------------------------------------------------------------

# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd', 'is', 'green', 'city']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd\tis\tgreen\tcity']

#---------------------------------------------------------------------
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

#---------------------------------------------------------------------------

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) # ['www', 'gmail', 'com']

#------------------------------------------------------------------------

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''

a = input("Enter the input : ")

res = a.split('+')
  
s = 0

for i in res:
    s = s + int(i)
    
print("Sum : ",s)

'''
Output :
Enter the input : 6+3+5+8+2
Sum :  24
'''

#------------------------------------------------------------------

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # 10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d)) # www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) # Error, elements are integers
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # SankarDayalSarma
g = range(5)
print('-' . join(g)) # Error

#----------------------------------------------------------------------

#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) # HYD  IS  GREEN  CITY
print(a . lower()) # hyd  is  green  city
print(a . capitalize()) # Hyd  is  green  city
print(a . title()) # Hyd  Is  Green  City
print(a . swapcase()) # HYd  Is  GReEN  CitY
print(a) # HYd  Is  GReEN  CitY
print('A7$a' . upper()) # A7$A

#-----------------------------------------------------------------------

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) # True
print(a . endswith('town')) # False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13)) # False
print(a . endswith(' ' , 3 , 13)) # True

#---------------------------------------------------------------
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself

4) Hint:  Use  endswith()  method
'''

i1 = input("Enter the string : ")

if len(i1) < 3:
    print(i1)
elif i1.endswith('ing'):
    print(i1 + 'ly')
else :
    print(i1 + 'ing')
    
'''
Output :
Enter the string : Suddenly
Suddenlying
Enter the string : Sudden
Suddening
'''

#-----------------------------------------------------------------------

#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha()) # True
print('Rama  Rao'  . isalpha()) # False 
print('Hyd4'  . isalpha()) # False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha()) # False
print('+-$'    .  isalpha()) # False
print('A2#'  .   isalpha()) # False
print(''  .  isalpha())  #  False
print(' '  .  isalpha()) # False

#-----------------------------------------------------------------------

# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) # True
print('92a47' . isdigit()) # False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit()) # False
print('+-$' . isdigit()) # False
print('A2#' . isdigit()) # False
print('' . isdigit()) #   False
print(' ' . isdigit()) # False
print(9247 . isdigit()) # Error

#------------------------------------------------------------------------

# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) # False
print('\n  \t' . isspace()) # True
print('\n  7\t' . isspace()) # False
print('\n' . isspace()) # True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace()) # True
print('' . isspace())  #  False
print(' ' . isspace()) # True

#-----------------------------------------------------------------------

# islower()  method  demo  program  (Home  work)
print('hyD' . islower()) # False
print('hyd' . islower()) # True
print('9247' . islower()) # False
print('rama  rao' . islower()) # True
print('+-$' . islower()) # False
print('hyd+-$' . islower()) # True
print('abc123' . islower()) # True
print('' . islower()) # False
print('a2#' . islower()) # True

#-----------------------------------------------------------------------

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a  :  25  	b  :  10.8  	c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a  :  25  	b  :  10.8  	c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # a  :  Hyd  	b  :  10.8  	c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a  :  Hyd  	b  :  Hyd  	c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # a  :  25  	b  :  10.8  	c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  Hyd  	b  :  10.8  	c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  25  	b  :  25  	c  :  25

#------------------------------------------------------------------------

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
c = input("Enter a character: ")

if c.isalnum():
    print("Alphanumeric character")

    if c.isalpha():
        print("Alphabet character")

        if c.isupper():
            print("Upper case alphabet")
        elif c.islower():
            print("Lower case alphabet")

    elif c.isdigit():
        print("Digit character")

elif c.isspace():
    print("White space")

else:
    print("Special character")
'''
Output :
Enter a character: B
Alphanumeric character
Alphabet character
Upper case alphabet
'''

#------------------------------------------------------

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
a = input("Enter the string: ")

b = ''

for i in range(1, len(a) + 1):
    b = b + a[-i]

print("Reverse string:", b)

#-------------------------------------------------------------------

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

a = input("Enter the sentence: ")

b = a.split()

c = ''

for i in range(1, len(b) + 1):
    c = c + b[-i] + ' '

print(c)

#-----------------------------------------------------------------------
'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''

a = input("Enter the sentence: ")

b = a.split()

for x in b:
    print(x[::-1], end=" ")
    
#--------------------------------------------------------------------------

'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''

a = input("Enter the string: ")

b = sorted(a)

c = ''.join(b)

print(c)

#----------------------------------------------------------------------

'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
a = input("Enter the string: ")

b = sorted(a)

alp = ''
dig = ''

for i in b:
    if i.isalpha():
        alp = alp + i
    elif i.isdigit():
        dig = dig + i

print(alp + dig)

'''
Output :
Enter the string: 56AZ89BG604
ABGZ0456689
'''







