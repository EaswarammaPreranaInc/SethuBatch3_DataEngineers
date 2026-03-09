Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method

a = 'babble'

first = a[0]
rest = a[1:].replace(first, '*')

result = first + rest
print(result)

a = "babble"

first = a[0]
rest = a[1:].replace(first, '*')

result = first + rest
print(result)

 # Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) #['15', '36', '48']
print(a) #15:36:48

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) #['Hyd\nis', 'green\tcity']
print(a . split()) #['Hyd', 'is', 'green', 'city']
print(a . split('green')) #['Hyd\nis ', '\tcity']
print(a . split('')) #error

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) #'Hyd', 'is', 'green', 'city']
print(a . split(' ')) #['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) #['www', 'gmail', 'com']

Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method

a = input("Enter expression: ")

for x in parts:
    total += int(x)

print("Sum =", total)


parts = a.split('+')#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) #15:36:48
b = ('Hyd' , 'is' , 'green' , 'city') 
print(' ' . join(b)) #Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) #52,15,10,25,20
d = ['www' , 'gmail', 'com']
print('.' . join(d)) #www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))#error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))
g = range(5)#SankarDayalSarma
print('-' . join(g)) #error

a = 'hyD  iS  grEen  cITy'

print(a.upper())       # True  
print(a.lower())       # True  
print(a.capitalize())  # True 
print(a.title())       # True  -
print(a.swapcase())    # True  
print(a)               # True  



a = 'Hyd is green city'

print(a.endswith('city'))        # True
print(a.endswith('town'))        # False
print(a.endswith('green', 3, 12))# True
print(a.endswith('green', 3, 13))# False
print(a.endswith(' ', 3, 13))    # False

print('Hyd'.isalpha())        # True
print('Rama  Rao'.isalpha())  # False
print('Hyd4'.isalpha())       # False
print('Hyd$'.isalpha())       # False
print('9247'.isalpha())       # False
print('+-$'.isalpha())        # False
print('A2#'.isalpha())        # False
print(''.isalpha())           # False
print(' '.isalpha())          # False

print('Hyd'.isalpha())        # True
print('Rama  Rao'.isalpha())  # False
print('Hyd4'.isalpha())       # False
print('Hyd$'.isalpha())       # False
print('9247'.isalpha())       # False
print('+-$'.isalpha())        # False
print('A2#'.isalpha())        # False
print(''.isalpha())           # False
print(' '.isalpha())          # False

# isspace() method demo program (Home work)

print('\n  A\t'.isspace())   # False
print('\n  \t'.isspace())    # True
print('\n  7\t'.isspace())   # False
print('\n'.isspace())        # True
print('\n  $\t'.isspace())   # False
print('\t'.isspace())        # True
print(''.isspace())          # False
print(' '.isspace())         # True

# islower() method demo program (Home work)

print('hyD'.islower())  # False
print('hyd'.islower())    # True
print('9247'.islower())      # False
print('rama  rao'.islower()) # True
print('+-$'.islower())       # False
print('hyd+-$'.islower())    # True
print('abc123'.islower())    # True
print(''.islower())          # False
print('a2#'.islower())       # True


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

a = input("Enter a character: ")

if a.isalnum():
    print("Alphanumeric character")
    
    if a.isalpha():
        print("Alphabet character")
        
        if a.isupper():
            print("Upper case alphabet")
        elif a.islower():
            print("Lower case alphabet")
    
    elif a.isdigit():
        print("Digit character")

elif a.isspace():
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

a = input("Enter a string: ")  
b = '' 
for i in range(1, len(a)+1):
    b = b + a[-i]  

print("Reversed string:", b)


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

a = input("Enter a sentence: ")  
b = a.split()                     
c = ''                             

for i in range(1, len(b)+1):
    c = c + b[-i] + ' '  

c = c.rstrip()  
print("Reversed sentence:", c)

'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice


'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice


Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS


string = input("Enter a string: ")
sorted_chars = sorted(string)
sorted_string = ''.join(sorted_chars)
print("Sorted string:", sorted_string)

'
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'


string = input("Enter a string with letters and digits: ")
letters = ''.join(sorted([c for c in string if c.isalpha()]))
digits  = ''.join(sorted([c for c in string if c.isdigit()]))
result = letters + digits

print("Sorted string (letters first, digits after):", result)



