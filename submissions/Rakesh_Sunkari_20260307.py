'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
##
a=input('enter a string: ')
output=''
for i in range(len(a)):
    if a[i] not in a[:i]:
        output+=a[i]
    else:
        output+='*'
print(output)

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) # ['15','36','48']
print(a) #15:36:48
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity' 
print(a . split(' ')) #['Hyd\nis', 'green\tcity']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split('green')) #['Hyd\nis ', '\tcity']
print(a . split(''))
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) #['Hyd', 'is', 'green', 'city']
print(a . split()) #['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd\tis\tgreen\tcity']
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) #['Hyd', 'is', 'green', 'city']
print(a . split(' ')) #['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))['www', 'gmail', 'com']

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) # [15:36:48]
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) #Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # 10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d)) #www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))#Error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) #SankarDayalSarma
g = range(5)
print('-' . join(g)) #Error

#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) #HYD IS GREEN CITY
print(a . lower()) #hyd is green city
print(a . capitalize()) #Hyd is green city
print(a . title())  #Hyd Is Green City
print(a . swapcase()) HYd  Is  GReEN  CitY
print(a) #hyD  iS  grEen  cITy
print('A7$a' . upper()) #A7$A


'''
1) What  does  upper()  method  do ?  --->  Returns  an  upper  case  string

2) What  does  lower()  method  do ?  --->  Returns  a  lower  case  string

3) What  does  capitalize()  method  do ?  --->  Returns  a  string  where  1st  char  is  uppercase  and  the  rest  in  lower  case

4) What  does  title()  method  do ?  --->  Returns  a  string  where  1st  char  of  each  word  is  uppercase  and  the  rest  in  lowercase

5) What  does  swapcase()  method  do ?  --->  Returns  a  string  where  upper  case  alphabets  are  converted  to lower  case  and   vice-versa
'''
# endswith()  method  demo  progrram (Home  work)

a = 'Hyd is green city'
print(a . endswith('city')) #True
print(a . endswith('town')) #False
print(a . endswith('green' , 3 , 12)) #True
print(a . endswith('green' , 3 , 13)) #False
print(a . endswith(' ' , 3 , 13)) #True

[12:26 pm, 07/03/2026] +91 99482 50500: #  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())#True
print('Rama  Rao'  . isalpha()) #True
print('Hyd4'  . isalpha()) #False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha()) #False
print('+-$'    .  isalpha()) #False
print('A2#'  .   isalpha()) #False
print(''  .  isalpha())  #  False
print(' '  .  isalpha()) #False


'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  an  alphabet

2) When  does  it  return  False  ?  --->  When  at  least  one  character  of  the  string  is  non-alphabet  i.e. digit (or) special  character
  (or) When  there  are  no  alphabets  in  the  string
'''
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) #True
print('92a47' . isdigit()) #False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit()) #False
print('+-$' . isdigit()) #False
print('A2#' . isdigit()) #false
print('' . isdigit()) #   False
print(' ' . isdigit()) #False
print(9247 . isdigit()) #Error


'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  a   non-digit  i.e. alphabet  (or) special  character
 (or)When  there  are  no  digits  in  the  string
'''


# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) #False
print('\n  \t' . isspace()) # True
print('\n  7\t' . isspace()) #False
print('\n' . isspace()) #True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace()) True
print('' . isspace())  #  False
print(' ' . isspace()) #Ture


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  not  a  white  space
 (i.e.  Alphabet, digit (or)  special  character) (or) When  there  are  no  white  space  characters																					
'''
# islower()  method  demo  program  (Home  work)
print('hyD' . islower()) #False
print('hyd' . islower()) #True
print('9247' . islower()) #False
print('rama  rao' . islower()) #True
print('+-$' . islower()) #False
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower()) #False
print('a2#' . islower()) #True


'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  ---> When  at  least  one  character  of  the  string  is  uppercase  alphabet (or)When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  ---> When  there  are  no  uppercase  alphabets  in  the  string and at  least  one  character  is  lowercase  alphabet

Note:
1) What  are  upper()  and  lower()  called ?  --->  Conversion  methods

2) What  are  isupper()  and  islower()  called ?  --->  Conditional  methods  becoz  they  return  True  (or)  False
'''
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))  #a  :  25  	  b  :  10.8  	  c  :  Hyd  
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) #a  :  25  	  b  :  10.8  	  c  :  Hyd  
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # a  :  Hyd  	  b  :  10.8  	  c  :  25  
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) #a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd  
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) #a  :  25  	  b  :  10.8  	  c  :  Hyd  
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #a  :  Hyd  	  b  :  10.8  	  c  :  25  
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #a  :  25  	  b  :  25  	  c  :  25  

'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
##
a = input("Enter a string:")
print(sorted(a))


'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself

4) Hint:  Use  endswith()  method
'''

a = input("Enter: ")
d =" "
if len(a) > 2:
    if a[-2:]!='ly':
        d = a + 'ly'
        print(d)
    elif a[-2:] =='ly':
        d =a[0:-2] +'ing' + a[-2:]
        print(d)
else:
    print(a)


Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''
b= "23 + 456 + 7 + 8912"
d = b.split("+")
c =0
print(d)
for i in range(1,len(d)+1):
    c += int(d[-i])
print(c,sep=" ",end=" ")


'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    **What  is  the  output ?  ---> city   green   is   Hyd**

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
---------------------------------------------
                              **''**

    **1        'city'        '' + 'city' + ' ' = 'city '**							  

    **2        'green'     'city ' + 'green' + ' ' = 'city green '**							  

    **3        'is'            'city green ' + 'is' + ' ' = 'city green is '**							  

    **4        'Hyd'        'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '**							  

-------------------------------------------------------
'''
b="Hyd  is  green  city "
d = b.split()
c = " "

for i in range(1,len(d)+1):
    c += d[-i]+ " "
print(c,sep=" ",end=" ")

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
a = input("Enter")
b = ""
for i in range(len(a)):
    b = a[-i] +b
print(b)

''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
b="Hyd  is  green  city"
c = b.split(" ")

for x in c:
    print(x[-1::-1],end=" ")


