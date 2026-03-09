'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
n=input("Enter input : ")
a=n[:1]
b=n[1:].replace(a,'*')
result=a+b
print(result)
-----------------------------------------------------------------------------
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))#[15 36 48]
print(a)#'15:36:48'
------------------------------------------------------------------------------
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#error
print(a . split())
print(a . split('green'))
print(a . split(''))
----------------------------------------------------------------------------
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))['www','gmail','com']
---------------------------------------------------------------------
'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''
n=input("ENter expression : ")
a=n.split('+')
sum=0
for i in a:
    sum=sum+int(i)
print(sum)
----------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))#15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#error
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))#15:36:48
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#error
g = range(5)
print('-' . join(g))#0_1_2_3_4
--------------------------------------------------------------
#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper())#HYD IS GREEN CITY
print(a . lower())#hyd is green city
print(a . capitalize())#Hyd is green city
print(a . title())# Hyd Is Green City
print(a . swapcase())#HYd Is GReEN CitY
print(a)#hyD  iS  grEen  cITy
print('A7$a' . upper())#error


'''
1) What  does  upper()  method  do ?  --->  Returns  an  upper  case  string

2) What  does  lower()  method  do ?  --->  Returns  a  lower  case  string

3) What  does  capitalize()  method  do ?  --->  Returns  a  string  where  1st  char  is  uppercase  and  the  rest  in  lower  case

4) What  does  title()  method  do ?  --->  Returns  a  string  where  1st  char  of  each  word  is  uppercase  and  the  rest  in  lowercase

5) What  does  swapcase()  method  do ?  --->  Returns  a  string  where  upper  case  alphabets  are  converted  to
																         lower  case  and   vice-versa
'''
--------------------------------------------------------------------------------
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))#True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#True
print(a . endswith(' ' , 3 , 13))#True
-------------------------------------------------------------------------------
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself

4) Hint:  Use  endswith()  method
'''
n="intrest"
if len(n)<3:
    print(s)
elif n.endswith('intrest'):
    print(n+'ly')
else:
    print(n+'ing')
----------------------------------------------------------------------------------
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())#True
print('Rama  Rao'  . isalpha())#True
print('Hyd4'  . isalpha())#False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha())#False
print('+-$'    .  isalpha())#False
print('A2#'  .   isalpha())#False
print(''  .  isalpha())  #  False
print(' '  .  isalpha())#False


'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  an  alphabet

2) When  does  it  return  False  ?  --->  When  at  least  one  character  of  the  string  is  non-alphabet  i.e. digit (or) special  character
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''
---------------------------------------------------------------------------------
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())#True
print('92a47' . isdigit())#False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False#False
print('' . isdigit()) #   False
print(' ' . isdigit())#False
print(9247 . isdigit())#error




'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  a   non-digit  i.e. alphabet  (or) special  character
																					   (or)
															 When  there  are  no  digits  in  the  string
'''
------------------------------------------------------------------------------------
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())#False
print('\n  \t' . isspace())#True
print('\n  7\t' . isspace())#False
print('\n' . isspace())#True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace())#True
print('' . isspace())  #  False
print(' ' . isspace())#True


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  not  a  white  space
															 (i.e.  Alphabet, digit (or)  special  character)
																					(or)
															 When  there  are  no  white  space  characters																					
'''
---------------------------------------------------------------------------------
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