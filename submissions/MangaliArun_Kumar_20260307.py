# Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

str = input("Enter string: ")
first = str[0]
rest = str[1:]
rest = rest.replace(first, '*')
print(first + rest)

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) # ['15','36','48']
print(a) # 15:36:48

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis' , 'green\tcity']
print(a . split()) # ['Hyd','is','green','city']
print(a . split('green')) # ['Hyd\nis','\tcity']
#print(a . split('')) # Error

# Find  outputs  (Home  work)
a = 'Hyd    is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd','is','green','city']
print(a . split()) # ['Hyd','is','green','city']
print(a . split(' ')) # ['Hyd'  'is'    'green' 'city']

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # ['Hyd','is','green','city']
print(a . split(' ')) # ['Hyd','','','is','','','green','','','city']

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) # ['www','gamil','com']

#Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols

a = (input("Enter expression : "))
newa = a.split("+")
ttl = 0
for i in range(len(newa)):
    ttl += int(newa[i])
print("sum : ",ttl)

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) # [15:36:48]
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) # [Hyd is green city]
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # [10,20,15,25,52]
d = ['www' , 'gmail', 'com']
print('.' . join(d)) # [www.gmail.com]
e = [15 , 36 , 48]
#print(':' . join(e)) # Error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # [SankarDayalSarma]
g = range(5)
print('-' . join(g)) # 0-1-2-3-4

#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) # HYd IS GREEN CITY
print(a . lower()) # hyd is green city
print(a . capitalize()) # Hyd is green city
print(a . title()) # Hyd Is Green City
print(a . swapcase()) # HYd Is GReEN City
print(a) # hyD iS grEen cITY
print('A7$a' . upper()) # Error

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) # True
print(a . endswith('town')) # False
print(a . endswith('green' , 3 , 12)) # False
print(a . endswith('green' , 3 , 13)) # True
print(a . endswith(' ' , 3 , 13)) # False

#Write  a  program  to  append  'ing'  to  input  string. Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'. Leave  the  string  unchanged  if  string  has  lessthan  three  characters
str = input("Enter a string : ")
if len(str)<3:
    print(str)
else:
    if str.endswith("ing"):
        str += "ly"
    else:
        str += "ing"
    print(str)
    
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha()) # True
print('Rama  Rao'  . isalpha()) # True
print('Hyd4'  . isalpha()) # False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha()) # False
print('+-$'    .  isalpha()) # False
print('A2#'  .   isalpha()) # False
print(''  .  isalpha())  #  False
print(' '  .  isalpha()) # False

# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) # True
print('92a47' . isdigit()) # True
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit()) # False
print('+-$' . isdigit()) # False
print('A2#' . isdigit()) # False
print('' . isdigit()) #   False
print(' ' . isdigit()) # False
print(9247 . isdigit()) # False

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
print('hyd+-$' . islower()) # False
print('abc123' . islower()) # False
print('' . islower()) # False
print('a2#' . islower()) # False

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a:25    b:10.8  c:Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a:25    b:10.8  c:Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # a:Hyd  b:10.8  c:25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a:25   a:25    a:25
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # a:25    b:10.8  c:Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a:Hyd  b:10.8  c:25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a:25   a:25    a:25

# Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

ch = input("Enter any character : ")
if ch.isalnum():
    print("Alpha numeric character")
    if ch.isalpha():
        print("Alphabet character")
        if ch.isupper():
            print("Upper case character")
        else:
            print("Lower case character")
    else:
        print("Digit character")
elif ch.issapce() or ch == "":
    print("White space Character")
else:
    print("special character")

# Write  a  program  to  reverse  a  string  without  slice

a  = input("Enter any string : ")
b = ""
for i in range(1,len(a)+1):
    b += a[-i]
print("Reverse string: ",b)

# Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

a  = input("Enter any sentence : ")
b = a.split()
c = ""
for i in range(1,len(b)+1):
    c += b[-i] + " "
print("Reverse order of words: ",c)


# Write  a  program  to  reverse  each  word  of  the  sentence

a = input("Enter any sentence : ")
b = a.split()
c = ""
for x in b:
    c += x[::-1]+" "
print(c)

#Write  a  program  to  sort  string  in  alphabetical  order

a  = input("Enter any string : ")
b = sorted(a)
c = "".join(b)
print("Sorted string: ",c)


#Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

a  = input("Enter any string : ")
b = sorted(a)
alpha = digit = ""
for ch in b:
    if ch.isalpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch
print("Result : ",alpha + digit)

