'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Hint : Use  replace()  method

s=input('Enter any string: ')
a=s[0]
print(s[0]+s[1:].replace(a,'*'))

output:
Enter any string: babble
ba**le


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) # ['15','36','48']
print(a) # '15:36:48'

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis','green\tcity']
print(a . split()) # ['Hyd','is','green','city']
print(a . split('green')) # ['Hyd\nis','\tcity']
print(a . split('')) # error


# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd','is','green','city']
print(a . split()) # ['Hyd','is','green','city']
print(a . split(' ')) # ['Hyd','is','green','city']


# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # ['Hyd','is','green','city']
print(a . split(' ')) # ['Hyd','','','is','','','green','','','city']


# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) # ['www','gmail','com']


'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Hint:  Use  split()  method

s=input('Enter any string: ')
s=s.split('+')
sum=0
for x in s:
    sum=sum+int(x)
print(sum)

output:
Enter any string: 23+456+7+8912
9398


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
print(':' . join(e)) # error as 15,36,48 not strings
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # SankarDayalSarma
g = range(5) 
print('-' . join(g)) # error


#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) # HYD IS GREEN CITY
print(a . lower()) # hyd is green city
print(a . capitalize()) # Hyd is green city
print(a . title()) # Hyd Is Green City
print(a . swapcase()) # HYd Is GReEN City
print(a) # hyD  iS  grEen  cITy
print('A7$a' . upper()) # A7$A

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) # True
print(a . endswith('town')) # False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13)) # False
print(a . endswith(' ' , 3 , 13)) # True


Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

s=input('Enter any string: ')
if len(s)<3:
    print(s)
elif s.endswith('ing'):
    s=s+'ly'
    print(s)
else:
    s=s+'ing'
    print(s)

output:
Enter any string: interest
interesting

Enter any string: interesting
interestingly

Enter any string: hi
hi


#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha()) # True
print('Rama  Rao'  . isalpha()) #  False
print('Hyd4'  . isalpha()) #  False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha()) #  False
print('+-$'    .  isalpha()) #  False
print('A2#'  .   isalpha()) #  False
print(''  .  isalpha())  #  False
print(' '  .  isalpha()) #  False


# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) # True
print('92a47' . isdigit()) #  False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit()) #  False
print('+-$' . isdigit()) #  False
print('A2#' . isdigit()) #  False
print('' . isdigit()) #   False
print(' ' . isdigit()) #  False
print(9247 . isdigit()) # error


# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) # False
print('\n  \t' . isspace()) # True
print('\n  7\t' . isspace())  # False
print('\n' . isspace()) # True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace()) # True
print('' . isspace())  #  False
print(' ' . isspace()) # True


# islower()  method  demo  program  (Home  work)
print('hyD' . islower())# False
print('hyd' . islower()) # True
print('9247' . islower()) # False
print('rama  rao' . islower()) # True
print('+-$' . islower()) # False
print('hyd+-$' . islower()) # True
print('abc123' . islower()) # True
print('' . islower()) # False
print('a2#' . islower()) # True


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a : 25 b : 10.8 c:Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a : 25 b : 10.8 c:Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # # a : Hyd b : 10.8  c:25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a: Hyd   b: Hyd  c: Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # a : 25 b : 10.8 c:Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a : Hyd  b : 10.8  c : 25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a : 25  b : 25  c : 25


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

s=input('Enter any character: ')
if s.isalnum():
    print('Alphanumeric Character')
    if s.isalpha():
        print('Alphabet Character')
        if s.isupper():
            print('Upper case character')
        elif s.islower():
            print('Lower case character')
    elif s.digit():
        print('digit character')
elif s.isspace():
    print('white space')
else:
    print('special character')

Output:
Enter any character: A
Alphanumeric Character
Alphabet Character
Upper case character



Write  a  program  to  reverse  a  string  without  slice

s=input('Enter any string: ')
reverse=""
for i in range(1,len(s)+1):
    reverse=reverse+s[-i]
print(reverse)

output:
Enter any string: RAMA RAO
OAR AMAR



Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

s=input('Enter any string: ')
s=s.split(' ')
rev=""
for i in range(1,len(s)+1):
    rev=rev+s[-i]+" "
print('reverse order of words: ',rev)

output:
Enter any string: hyd is green city
reverse order of words:  city green is hyd



Write  a  program  to  reverse  each  word  of  the  sentence

s=input('Enter any sentence: ')
for x in s.split():
    print(x[::-1],end=" ")

output:
Enter any sentence: hyd is green city
dyh si neerg ytic 



Write  a  program  to  sort  string  in  alphabetical  order

s=input('Enter any string: ')
s=sorted(s)
a=""
for x in s:
    a=a+x
print(a)

OUTPUT:
Enter any string: RAJESH
AEHJRS



Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

s=input('Enter any string with alphabets and digit: ')
s=sorted(s)
alpha=""
digit=""
for x in s:
    if x.isalpha():
        alpha=alpha+x 
    else:
        digit=digit+x 
print(alpha+digit)

output:
Enter any string with alphabets and digit: Z9K3PA7D51
ADKPZ13579



    








