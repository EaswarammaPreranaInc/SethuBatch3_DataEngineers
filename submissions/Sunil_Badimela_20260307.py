'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''

s = "babble"

first = s[0]            # first character
rest = s[1:]            # remaining string

rest = rest.replace(first, '*')

result = first + rest

print(result)

0utput
ba**le


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)

0utput
15:36:48
['15', '36', '48']

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))
print(a . split())
print(a . split('green'))
print(a . split(''))

output
['Hyd\nis', 'green\tcity']
['Hyd', 'is', 'green', 'city']
['Hyd\nis ', '\tcity']
ValueError: empty separator



# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))
print(a . split())
print(a . split(' '))

output
['Hyd', 'is', 'green', 'city']
['Hyd', 'is', 'green', 'city']
['Hyd\tis\tgreen\tcity']





# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())
print(a . split(' '))

output
['Hyd', 'is', 'green', 'city']
['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']




'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''
expr = "23 + 456 + 7 + 8912"

# split the expression using '+'
parts = expr.split('+')

total = 0

for num in parts:
    total += int(num)

print(total)

output

9398


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

output

15:36:48
Hyd is green city
10,20,15,25,52   (order may vary)
www.gmail.com
TypeError
SankarDayalSarma
TypeError



#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper())
print(a . lower())
print(a . capitalize())
print(a . title())
print(a . swapcase())
print(a)
print('A7$a' . upper())


'''
1) What  does  upper()  method  do ?  --->  Returns  an  upper  case  string

2) What  does  lower()  method  do ?  --->  Returns  a  lower  case  string

3) What  does  capitalize()  method  do ?  --->  Returns  a  string  where  1st  char  is  uppercase  and  the  rest  in  lower  case

4) What  does  title()  method  do ?  --->  Returns  a  string  where  1st  char  of  each  word  is  uppercase  and  the  rest  in  lowercase

5) What  does  swapcase()  method  do ?  --->  Returns  a  string  where  upper  case  alphabets  are  converted  to
																         lower  case  and   vice-versa
'''
output

HYD  IS  GREEN  CITY
hyd  is  green  city
Hyd  is  green  city
Hyd  Is  Green  City
HYd  Is  GReEN  CitY
hyD  iS  grEen  cITy
A7$A




# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))
print(a . endswith('town'))
print(a . endswith('green' , 3 , 12))
print(a . endswith('green' , 3 , 13))
print(a . endswith(' ' , 3 , 13))


otput
True
False
True
False
True


'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself

4) Hint:  Use  endswith()  method
'''


s = input("Enter a string: ")

if len(s) < 3:
    print(s)
elif s.endswith("ing"):
    print(s + "ly")
else:
    print(s + "ing")


output
interest
interesting

interesting
interestingly

Hi
Hi




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


'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  an  alphabet

2) When  does  it  return  False  ?  --->  When  at  least  one  character  of  the  string  is  non-alphabet  i.e. digit (or) special  character
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''

print('Hyd'.isalpha())
print('Rama  Rao'.isalpha())
print('Hyd4'.isalpha())
print('Hyd$'.isalpha())
print('9247'.isalpha())
print('+-$'.isalpha())
print('A2#'.isalpha())
print(''.isalpha())
print(' '.isalpha())

output

True
False
False
False
False
False
False
False
False



# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())
print('\n  \t' . isspace())
print('\n  7\t' . isspace())
print('\n' . isspace())
print('\n  $\t' . isspace())  #  False
print('\t' . isspace())
print('' . isspace())  #  False
print(' ' . isspace())


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  not  a  white  space
															 (i.e.  Alphabet, digit (or)  special  character)
																					(or)
															 When  there  are  no  white  space  characters																					
'''
output

False
True
False
True
False
True
False
True


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

output

False
True
False
True
False
True
True
False
True


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))


output
a  :  25  	b  :  10.8  	c  :  Hyd
a  :  25  	b  :  10.8  	c  :  Hyd
a  :  Hyd  	b  :  10.8  	c  :  25
a  :  Hyd  	b  :  Hyd  	c  :  Hyd
a  :  25  	b  :  10.8  	c  :  Hyd
a  :  Hyd  	b  :  10.8  	c  :  25
a  :  25  	b  :  25  	c  :  25




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

ch = input("Enter a character: ")

if ch.isalnum():
    print("Alphanumeric character")
    
    if ch.isalpha():
        print("Alphabet character")
        
        if ch.isupper():
            print("Upper case alphabet")
        elif ch.islower():
            print("Lower case alphabet")
            
    elif ch.isdigit():
        print("Digit character")

elif ch.isspace():
    print("White space")

else:
    print("Special character")

output
Alphanumeric character
Alphabet character
Upper case alphabet
Alphanumeric character
Alphabet character
Lower case alphabet

Alphanumeric character
Digit character
Special character

Special character
White space




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

a = input("Enter a string: ")
b = ''

for i in range(1, len(a)+1):
    b = b + a[-i]

print("Reversed string:", b)

output
Hyd
Reversed string: dyH

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


a = input("Enter a sentence: ")

b = a.split()      # split words into list
c = ''             # result string

for i in range(1, len(b)+1):
    c = c + b[-i] + ' '

print("Reversed order:", c)

output
Hyd is green city
city green is Hyd


'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''

a = input("Enter a string: ")

b = sorted(a)   # sorts characters

c = ''          # result string

for ch in b:
    c = c + ch

print("Sorted string:", c)

output
RAJESH
AEHJRS



'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''

a = input("Enter a string: ")

b = sorted(a)     # sort characters

alpha = ''
digit = ''

for ch in b:
    if ch.isalpha():
        alpha = alpha + ch
    elif ch.isdigit():
        digit = digit + ch

result = alpha + digit

print("Output:", result)

output
Z9K3PA7D51
b = '13579ADKPZ'

ADKPZ13579
ADKPZ13579
















