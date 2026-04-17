#Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
s=input("Enter string : ")
firstchar=s[0]
s=s[0]+s[1:].replace(firstchar,'*')
print(s)

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))  # ['15','35','48']
print(a)  # '15:36:48'

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis', 'green\tcity']
print(a . split()) # ['Hyd','is','green','city']
print(a . split('green'))# ['Hyd\nis','\tcity']
print(a . split('')) # error 

# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # [Hyd','is','green','city']
print(a . split()) # [Hyd','is','green','city']
print(a . split(' ')) # ['Hyd	is	green	city']

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # [Hyd','is','green','city']
print(a . split(' ')) # ['Hyd',' ',' ','is',' ',' ','green',' ',' ','city']
    
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) # ['www','gmail','com']

'''Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum'''
n=input("Enter str : ")
l=n.split('+')
sum=0
for x in l:
    sum+=int(x)
print(sum)

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))   # '15:36:48'
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) #'Hyd is green city'
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # '10,20,15,25,52'
d = ['www' , 'gmail', 'com']
print('.' . join(d)) # 'www.gmail.com'
e = [15 , 36 , 48]
#print(':' . join(e)) # error, bcz join() takes list of strings not integers
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) #'SankarDayalSarma'
g = range(5)
#print('-' . join(g)) # error bcz range obj contains integer values but not strings

#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) # 'HYD IS GREEN CITY'
print(a . lower()) # 'hyd is green city'
print(a . capitalize()) #'Hyd is green city'
print(a . title()) #'Hyd Is Green City'
print(a . swapcase()) # HYd Is GReEN CitY'
print(a) # 'hyD  iS  grEen  cITy'
print('A7$a' . upper()) #'A7$A'

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) # True
print(a . endswith('town')) # False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13)) # False
print(a . endswith(' ' , 3 , 13)) # True

'''Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters'''

s=input()
c=s.endswith('ing')
if len(s)<3 :
    print(s)
elif c:
    s+='ly'
    print(s)
else:
    s+='ing'
    print(s)

#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  # True
print('Rama  Rao'  . isalpha()) # False
print('Hyd4'  . isalpha()) # False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha()) # False
print('+-$'    .  isalpha()) # False
print('A2#'  .   isalpha()) # False
print(''  .  isalpha())  #  False
print(' '  .  isalpha()) # False

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

# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) # False
print('\n  \t' . isspace()) # True
print('\n  7\t' . isspace()) # False
print('\n' . isspace()) # True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace()) # True
print('' . isspace())  #  False
print(' ' . isspace()) # True

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

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a : 25   b : 10.8   c : 'Hyd'
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a : 25   b : 10.8   c : 'Hyd'
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # a : 'Hyd''   b : 10.8   c : 25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a : 'Hyd'   b : 'Hyd'   c : 'Hyd'
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # a  :  25  	  b  :  10.8  	  c  :  'Hyd' 
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  'Hyd'  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  25  	  b  :  25  	  c  :  25

# Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character
ui=input()
if ui.isalnum():
    if ui.isalpha():
        if ui.isupper():
            
            print("Aplhabet character")
            print("Upper case alphabet")
            print("Alphanumeric")
        else:
            print("Alphanumeric")
            print("Aplhabet character")
            print("lower case alphabet")
    else:
        if ui.isdigit():
            print("Alphanumeric")
            print("Digit")
elif ui.isspace():
    print("Whitespace")
else:
    print("Special character")

# Write  a  program  to  reverse  a  string  without  slice
s=input()
n=''
for i in range(1,len(s)+1):
    n+=s[-i]
print(n)

# Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
s=input()
n=s.split()
r=''
for i in range(1,len(n)+1):
    r+=n[-i]+' ' 
print(r)

# Write  a  program  to  reverse  each  word  of  the  sentence
s=input()
n=s.split()
r=''
for x in n:
     r+=x[::-1]+' '
print(r)

# Write  a  program  to  sort  string  in  alphabetical  order
s=input()
n=''
ch=list(s)
b=sorted(ch)
for x in b:
    n+=x
    
print(n)

# Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
s=input()
alp=''
dig=''
al=''
di=''
for ch in s:
    if ch.isalpha():
        alp+=ch
    else:
        dig+=ch
for a in sorted(alp):
    al+=a
for d in sorted(dig):
    di+=d
print(a+d)














