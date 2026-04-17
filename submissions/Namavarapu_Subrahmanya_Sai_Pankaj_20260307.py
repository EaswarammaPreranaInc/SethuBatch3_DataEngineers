'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
a = 'babble'

first = a[0]
rest = a[1:].replace(first, '*')

result = first + rest

print(result)

a = '15:36:48'
print(a.split(':'))
print(a)

a = 'Hyd\nis green\tcity'

print(a.split(' '))
print(a.split())
print(a.split('green'))
print(a.split(''))


a = 'Hyd	is	green	city'
print(a.split('\t'))
print(a.split())
print(a.split(' '))


a = 'Hyd   is   green   city'
print(a.split())
print(a.split(' '))


a = 'www.gmail.com'
print(a.split('.'))

a = input("Enter expression: ")

parts = a.split('+')

total = 0

for i in parts:
    total += int(i)

print(total)




a = ['15','36','48']
print(':'.join(a))



b = ('Hyd','is','green','city')
print(' '.join(b))



c = {'10','20','15','25','52'}
print(','.join(c))


d = ['www','gmail','com']
print('.'.join(d))


e = [15,36,48]
print(':'.join(e))

f = ['Sankar','Dayal','Sarma']
print(''.join(f))


a = 'hyD  iS  grEen  cITy'
# HYD  IS  GREEN  CITY
# hyd  is  green  city
# Hyd  is  green  city
# Hyd  Is  Green  City
# HYd  Is  GReEN  CitY
# hyD  iS  grEen  cITy
# A7$A

a = 'Hyd is green city'
# True
# False
# False
# True
# False

a = input("Enter string: ")

if len(a) < 3:
    print(a)
elif a.endswith('ing'):
    print(a + 'ly')
else:
    print(a + 'ing')

# interest → interesting
# interesting → interestingly
# Hi → Hi


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

# True
# False
# False
# False
# False
# False
# False
# False
# False


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




'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  a   non-digit  i.e. alphabet  (or) special  character
																					   (or)
															 When  there  are  no  digits  in  the  string
'''

# True
# False
# False
# False
# False
# False
# False
# False
# AttributeError


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
# False
# True
# False
# True
# False
# True
# False
# True


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
# False
# True
# False
# True
# False
# True
# True
# False
# True


# Find  outputs  (Home  work)
# a , b , c = 25 , 10.8 , 'Hyd'
# print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
# print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
# print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
# print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
# print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
# print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
# print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))

# print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '.format(a , b , c))
# a  :  25  	  b  :  10.8  	  c  :  Hyd


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
        else:
            print("Lower case alphabet")

    elif ch.isdigit():
        print("Digit character")

elif ch.isspace():
    print("White space")

else:
    print("Special character")


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

a = input("Enter string: ")

b = ""

for i in range(1, len(a)+1):
    b = b + a[-i]

print(b)


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

a = input("Enter sentence: ")

b = a.split()

c = ""

for i in range(1, len(b)+1):
    c = c + b[-i] + " "

print(c)

'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''


a = input("Enter sentence: ")

b = a.split()

for i in b:
    print(i[::-1], end=" ")


'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''


a = input("Enter string: ")

b = sorted(a)

print("".join(b))


'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
a = input("Enter string: ")

s = sorted(a)

alpha = ""
digit = ""

for i in s:
    if i.isalpha():
        alpha += i
    else:
        digit += i

print(alpha + digit)