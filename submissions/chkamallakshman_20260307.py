
# 1 . Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method

# output : s = input("Enter any string: ")

first = s[0]                 
rest = s[1:]    
rest = rest.replace(first, '*') 
result = first + rest
print("Result :", result)

# 2. Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)

# output : ['15', '36', '48']
            15:36:48


# 3 . # Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))
print(a . split())
print(a . split('green'))
print(a . split(''))

# output : ['Hyd\nis', 'green\tcity']
['Hyd', 'is', 'green', 'city']
['Hyd\nis ', '\tcity']
ValueError: empty separator


# 4 . # Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))
print(a . split())
print(a . split(' '))

# output : ['Hyd', 'is', 'green', 'city']
['Hyd', 'is', 'green', 'city']
['Hyd\tis\tgreen\tcity']


# 5 . # Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())
print(a . split(' '))


# output : ['Hyd', 'is', 'green', 'city']
['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']


# 6 . # Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))

 # output : ['www', 'gmail', 'com']


# 7 . Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method

# output : exp = input("Enter expression: ")

parts = exp.split('+')

total = 0
for i in parts:
    total = total + int(i)

print("Sum =", total)


# 8 . #  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) # => output : 15:36:48

b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) # => output : Hyd is green city

c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # => output : 10,20,15,25,52

d = ['www' , 'gmail', 'com']
print('.' . join(d)) # output : www.gmail.com

e = [15 , 36 , 48]
print(':' . join(e)) # output : TypeError: sequence item 0: expected str instance, int found

f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) #output : SankarDayalSarma

g = range(5)
print('-' . join(g)) # output : TypeError: sequence item 0: expected str instance, int found


# 9 . #  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) #output : HYD  IS  GREEN  CITY
print(a . lower())
print(a . capitalize()) #output : hyd  is  green  city
print(a . title())  # output : Hyd  Is  Green  City
print(a . swapcase())  # output : HYd  Is  GReEN  CitY
print(a)  # output : hyD  iS  grEen  cITy
print('A7$a' . upper()) # output : A7$A

'''
1) What  does  upper()  method  do ?  --->  Returns  an  upper  case  string

2) What  does  lower()  method  do ?  --->  Returns  a  lower  case  string

3) What  does  capitalize()  method  do ?  --->  Returns  a  string  where  1st  char  is  uppercase  and  the  rest  in  lower  case

4) What  does  title()  method  do ?  --->  Returns  a  string  where  1st  char  of  each  word  is  uppercase  and  the  rest  in  lowercase

5) What  does  swapcase()  method  do ?  --->  Returns  a  string  where  upper  case  alphabets  are  converted  to


# 10 . # endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) # output : True
print(a . endswith('town'))# output : False
print(a . endswith('green' , 3 , 12)) # output : True
print(a . endswith('green' , 3 , 13))# output : False
print(a . endswith(' ' , 3 , 13)) # output : True


# 11 . Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself

4) Hint:  Use  endswith()  method

# output : s = input("Enter a string: ")

if len(s) < 3:
    print(s)
elif s.endswith("ing"):
    print(s + "ly")
else:
    print(s + "ing")


# 12 . #  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha()) # output : True
print('Rama  Rao'  . isalpha()) # output : False
print('Hyd4'  . isalpha()) # output : False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha()) # output : False
print('+-$'    .  isalpha()) # output : False
print('A2#'  .   isalpha()) # output : False
print(''  .  isalpha())  #  False
print(' '  .  isalpha())# output : False

'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  an  alphabet

2) When  does  it  return  False  ?  --->  When  at  least  one  character  of  the  string  is  non-alphabet  i.e. digit (or) special  character
																					    (or)
															  When  there  are  no  alphabets  in  the  string
																         lower  case  and   vice-vers
# 13 . # isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) # output : True
print('92a47' . isdigit()) # output : False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit()) # output : False
print('+-$' . isdigit()) # output : False
print('A2#' . isdigit()) # output : False
print('' . isdigit()) #   False
print(' ' . isdigit()) # output : False
print(9247 . isdigit()) # output : Error: 'int' object has no attribute 'isdigit'

'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  a   non-digit  i.e. alphabet  (or) special  character
																					   (or)															 When  there  are  no  digits  in  the  string
'''

# 14 . # isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) # output : False
print('\n  \t' . isspace()) # output : True
print('\n  7\t' . isspace()) # output : False
print('\n' . isspace())  # output : True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace())output : # True
print('' . isspace())  #  False
print(' ' . isspace())  # output : True


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  not  a  white  space
															 (i.e.  Alphabet, digit (or)  special  character)
																					(or)
															 When  there  are  no  white  space  characters


# 15 . # islower()  method  demo  program  (Home  work)
print('hyD' . islower()) # output : False
print('hyd' . islower()) # output : True
print('9247' . islower()) # output : False
print('rama  rao' . islower()) # output : True
print('+-$' . islower()) # output : False
print('hyd+-$' . islower())  # output : True
print('abc123' . islower()) # output : True
print('' . islower()) # output : False
print('a2#' . islower())# output : True


# 16 . # Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # output : a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # output : a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # output : a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # output : a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # output : a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # output : a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))# output : a  :  25  	  b  :  25  	  c  :  25


# 17 . Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  ---> White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods

9) Hint2:  Use  nested  if  and   elif

# output : ch = input("Enter a character: ")

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


# 18 . Write  a  program  to  reverse  a  string  without  slice

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

# output : s = input("Enter a string: ")

b = ''

for i in range(1, len(s) + 1):
    b = b + s[-i]

print("Reversed string:", b)

# 19 . Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

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

# output : s = input("Enter a sentence: ")

b = s.split() 
c = ''

for i in range(1, len(b) + 1):
    c = c + b[-i] + ' '

print("Result:", c)



# 20 . Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice

# output : s = input("Enter a sentence: ")

words = s.split()
result = ''

for w in words:
    result = result + w[::-1] + ' '

print("Result:", result)


# 21 . Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS


# output : s = input("Enter a string: ")

a = list(s)      
a.sort()       
result = ''.join(a)   
print("Sorted string:", result)


# 21 . Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'

# output : s = input("Enter a string: ")

a = sorted(s)  

alpha = ''
digit = ''

for ch in a:
    if ch.isalpha():
        alpha = alpha + ch
    elif ch.isdigit():
        digit = digit + ch

result = alpha + digit
print("Result:", result)