1'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
Let  input  be  'babble'
What  is  the  output ?  --->  ba**le
Hint : Use  replace()  method
'''
str=input("Enter any string : ")
Result=str[0]
str1=str[1:]
str1=str1.replace(str[0],'*')
print(Result+str1)
'''
output
Enter any string : babble
ba**le
'''
=======================================================================================================================================================
2#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))#['15':'36':'48']
print(a)#15:36:48
=======================================================================================================================================================
3# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis','green\tcity']
print(a . split())#['Hyd','is','green''tcity']
print(a . split('green'))#['Hyd\nis','\tcity']
print(a . split(''))#error
=======================================================================================================================================================
4# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#['Hyd', 'is', 'green', 'city']
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd\tis\tgreen\tcity']
=======================================================================================================================================================
5# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']
=======================================================================================================================================================
6# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#[www,gmail,com]
=======================================================================================================================================================
7'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912
Print  the  sum
Hint:  Use  split()  method
'''
m=input("Enter : ")
n=m.split('+')
sum=0
for i in n:
    sum+=int(i)
print("SUM : ",sum)
'''
output
Enter : 23 + 456 + 7 + 8912
SUM :  9398
'''
=======================================================================================================================================================
8#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))#15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))# Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))#error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#SankarDayalSarma
g = range(5)
print('-' . join(g))#error
=======================================================================================================================================================
9#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper())#HYD IS GREEN CITY
print(a . lower())#hyd is green city
print(a . capitalize())#Hyd is green city
print(a . title())#Hyd Is Green City
print(a . swapcase())#HYd  Is  GReEN  CitY
print(a)#hyD  iS  grEen  cITy
print('A7$a' . upper())#A7$A
=======================================================================================================================================================
10# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))#True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#False
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))True
=======================================================================================================================================================
11'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters
1) What  is  the  output  if  input  is  'interest' ?  ---> interesting
2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly
3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself
4) Hint:  Use  endswith()  method
'''
x=input("Please enter string : ")
if len(x)<3:
    print(x)
elif x.endswith('ing'):
    print(x+'ly')
else:
    print(x+'ing')
'''
output
Please enter string : interest
interesting
Please enter string : Hi
Hi
Please enter string : interesting
interestingly
'''
=======================================================================================================================================================
12#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())#True
print('Rama  Rao'  . isalpha())#False
print('Hyd4'  . isalpha())#False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha())#False
print('+-$'    .  isalpha())#False
print('A2#'  .   isalpha())#False
print(''  .  isalpha())  #  False
print(' '  .  isalpha())#False
=======================================================================================================================================================
13# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())#True
print('92a47' . isdigit())#False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False
print('' . isdigit()) #   False
print(' ' . isdigit())#False
print(9247 . isdigit())Error
=======================================================================================================================================================
14# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())#False
print('\n  \t' . isspace())#True
print('\n  7\t' . isspace())#False
print('\n' . isspace())#True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace())#True
print('' . isspace())  #  False
print(' ' . isspace())#True
=======================================================================================================================================================
15# islower()  method  demo  program  (Home  work)
print('hyD' . islower())#False
print('hyd' . islower())#True
print('9247' . islower())#False
print('rama  rao' . islower())#True
print('+-$' . islower())#False
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower())#False
print('a2#' . islower())#True
=======================================================================================================================================================
16# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))#a  :  25          b  :  10.8      c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))#a  :  25          b  :  10.8      c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))#a  :  Hyd         b  :  10.8      c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))#a  :  Hyd         b  :  Hyd      c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))#a  :  25          b  :  10.8      c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a  :  Hyd         b  :  10.8      c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a  :  25         b  :  25      c  :  25
=======================================================================================================================================================
17'''
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
char = input("please enter a single character:")
if char.isalnum():
    print("Alphanumeric character")
    if char.isalpha():
        print("Alphabet character")
        if char.isupper():
            print("Upper case alphabet")
        elif char.islower():
            print("Lower case alphabet")
    elif char.isdigit():
        print("Digit character")
elif char.isspace():
    print("White space")
else:
    print("Special character")		
'''
output
Please enter a single character: A
Alphanumeric character
Alphabet character
Upper case alphabet
'''
=======================================================================================================================================================
18'''
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
x=input("Enter any string : ")
Reverse=''
for i in range(1,len(x)+1):
    Reverse+=x[-i]
print("Reverse String : ",Reverse)

'''
output
Enter any string : RAMA RAO
Reverse String :  OAR AMAR
'''
=======================================================================================================================================================
19'''
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
str1=input("Enter any sequence : ")
str2=str1.split()
reverse=''
for i in range(1,len(str2)+1):
    reverse+=str2[-i]+' '
print("Reverse order of words : ",reverse)
'''
output
Enter any sequence : Pls write todays exam well
Reverse order of words :  well exam todays write Pls 
'''
=======================================================================================================================================================
20'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic
2) Hint: Use  for  each  loop  and  also  slice
'''
str1=input("Enter any sequence : ")
str2=str1.split()
reverse=[]
for i in str2:
    reverse.append(i[::-1])
print(' '.join(reverse),end='')
'''
output
Enter any sequence : Hyd is green city
dyH si neerg ytic
'''
=======================================================================================================================================================
21'''
Write  a  program  to  sort  string  in  alphabetical  order
Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
st=input("Enter any string : ")
sorted_string=''
for i in sorted(st):
    sorted_string+=i
print("Sorted string : ",sorted_string)
'''
output
Enter any string : RAJESH
Sorted string :  AEHJRS
'''
=======================================================================================================================================================
22'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579
1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'
2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'
3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
st = input("Enter string with alphabets and digits : ")
sorted_str = "".join(sorted(st))
digit = ""
alpha = ""
for ch in sorted_str:
    if ch.isalpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch
result = alpha + digit
print("Result : ", result)
'''
Enter string with alphabets and digits : Z9K3PA7D51
Result :  ADKPZ13579
'''







