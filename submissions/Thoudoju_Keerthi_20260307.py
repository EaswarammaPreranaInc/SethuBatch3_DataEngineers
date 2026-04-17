 '''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
try:
	s=input('Enter a string')
	res=s[0]
	s=s.replace(res,'*')
	print(res+s[1:])
except:
	print('Error')


try:
	s=input('Enter a string')
	res=s[0]
	for i in range(1,len(s)):
		if(s[i]==s[0]):
			res+="*"
		else:
			res+=s[i]
	print(res)
except:
	print('Error')



#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a) # ['15', ‘36’, ‘48’]

 # Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) #[’Hyd\nis’, ‘green\tcity’]
print(a . split())##[’Hyd’, ‘is’, ‘green’, ‘city’]
print(a . split('green'))#[’Hyd\nis’ ‘\tcity’]
print(a . split(''))#Error

 # Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#[’Hyd’, ‘is’, ‘green’, ‘city’]
print(a . split())##[’Hyd’, ‘is’, ‘green’, ‘city’]
print(a . split(' '))#[’Hyd	is	green	cityy’]

 # Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())#[’Hyd’, ‘is’, ‘green’, ‘city’]
print(a . split(' '))#[’Hyd’, '','', ‘is’, '', '', ‘green’, '','', ‘city’]

 # Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#[’www’, ‘gmail’, ‘com’]

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''
try:
	s=input('Enter a string')
	a=s.split('+')
	s=0
	for i in a:
		s+=eval(i)
	print(s)
except:
	print('Error')

 #  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) #15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))#15:36:48
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#SankarDayalSarma
g = range(5)
print('-' . join(g))#0-1-2-3-4-5

 #  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) # HYD IS GREEN CITY
print(a . lower())# hyd is green city
print(a . capitalize())#Hyd is green city
print(a . title())##Hyd Is Green City
print(a . swapcase())#HYd Is GReEN CitY
print(a)#hyD  iS  grEen  cITy
print('A7$a' . upper())#Error


'''
1) What  does  upper()  method  do ?  --->  Returns  an  upper  case  string

2) What  does  lower()  method  do ?  --->  Returns  a  lower  case  string

3) What  does  capitalize()  method  do ?  --->  Returns  a  string  where  1st  char  is  uppercase  and  the  rest  in  lower  case

4) What  does  title()  method  do ?  --->  Returns  a  string  where  1st  char  of  each  word  is  uppercase  and  the  rest  in  lowercase

5) What  does  swapcase()  method  do ?  --->  Returns  a  string  where  upper  case  alphabets  are  converted  to
																         lower  case  and   vice-versa
'''

 # endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) #True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#False
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#False

'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself

4) Hint:  Use  endswith()  method
'''
try:
	s=input('Enter a string')
	if(len(s) <3):
		print(s)
	elif(s.endswith('ing')):
		print(s+'ly')
	else:
		print(s+'ing')
except:
	print('Error')
	
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha()) #True
print('Rama  Rao'  . isalpha()) #False
print('Hyd4'  . isalpha())#True
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha()) #True
print('+-$'    .  isalpha())#   False
print('A2#'  .   isalpha())#   False
print(''  .  isalpha())  #  False
print(' '  .  isalpha())#   False



'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  an  alphabet

2) When  does  it  return  False  ?  --->  When  at  least  one  character  of  the  string  is  non-alphabet  i.e. digit (or) special  character
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) #True
print('92a47' . isdigit())#  False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit())#  False
print('+-$' . isdigit())#  False
print('A2#' . isdigit())#  False
print('' . isdigit()) #   False
print(' ' . isdigit())#  False
print(9247 . isdigit())#  False



'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  a   non-digit  i.e. alphabet  (or) special  character
																					   (or)
															 When  there  are  no  digits  in  the  string
'''
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())#  False
print('\n  \t' . isspace())#True
print('\n  7\t' . isspace())#  False
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
 # islower()  method  demo  program  (Home  work)
print('hyD' . islower()) #False
print('hyd' . islower()) #True
print('9247' . islower()) #False
print('rama  rao' . islower()) #True
print('+-$' . islower()) #False
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower()) #False
print('a2#' . islower())#True



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
 # Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a : 25	b : 10.8  c : Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a : 25	b : 10.8  c : Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # a : Hyd   b : 10.8   c : 25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a : Hyd   b : Hyd   c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))# a : 25	b : 10.8  c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))# a : hyd	b : 10.8  c : 25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))# a : Hyd   b : Hyd   c : Hyd

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

ch = input("Enter a character : ")

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
try:
	s=input('Enter a string')
	res=''
	for i in range(1, len(s)+1):
		res+=s[-i]
	print(res)
except:
	print('error')
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
try:
	s=input('Enter a string')
	a=s.split(' ')
	res=''
	for i in range(1,len(a)+1):
		res+=a[-i]+ ' '
	print(res)
except:
	print('error')

 '''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
try:
	s=input('Enter a string')
	a=s.split(' ')
	res=''
	for i in range(len(a)):
		res+=a[i][::-1]+ ' '
	print(res)
except:
	print('error')

 '''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''

try:
	s=input('Enter a string')
	res=sorted(s)
	print(''.join(res))
except:
	print('error')
 '''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
try:
	s=input('Enter a string')
	al=''
	di=''
	rem=''
	for i in s:
		if(i.isalpha()):
			al+=i
		elif(i.isdigit()):
			di+=i
		else:
			rem+=i
	res1=sorted(al)
	res2=sorted(di)
	res3=sorted(rem)
	print(''.join(res1)+''.join(res2)+''.join(res3))
except:

	print('error')

