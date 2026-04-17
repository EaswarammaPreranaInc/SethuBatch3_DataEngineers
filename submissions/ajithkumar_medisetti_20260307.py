'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
#Program:
s = input("Enter a string: ")

first = s[0]                
rest = s[1:].replace(first,'*')   
result = first + rest
print("Result:",result)   
  
#Output:
Enter a string: babble
Result: ba**le

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))# ['15', '36', '48']
print(a) # 15:36:48

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))   #Hyd\nis green\tcity
print(a . split())      #['Hyd', 'is', 'green', 'city']
print(a . split('green'))   #['Hyd\nis ', '\tcity']
print(a . split(''))        #Error due to empty separator



# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))     #['Hyd', 'is', 'green', 'city']
print(a . split())         #['Hyd', 'is', 'green', 'city']
print(a . split(' '))      #['Hyd\nis', 'green\tcity']


# Find  outputs (Home  work)
a = 'Hyd   is   green   city'   # There are 3 spaces between the words
print(a.split())     # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))  # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']


# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))  # ['www', 'gmail', 'com']

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''
#Program:
exp = input("Enter expression: ")   
parts = exp.split('+')              
total = 0
for i in parts:
    total += int(i.strip())  
print("Sum =", total)

#Output:
Enter expression : 10 + 20 + 30
Sum = 60

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':'.join(a))        # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' '.join(b))        # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(','.join(c))        # order may vary (set is unordered) e.g. 10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.'.join(d))        # www.gmail.com
e = [15 , 36 , 48]
print(':'.join(e))        # Error: sequence item 0: expected str instance, int found
f = ['Sankar' , 'Dayal' , 'Sarma']
print(''.join(f))         # SankarDayalSarma
g = range(5)
print('-'.join(g))        # Error: sequence item 0: expected str instance, int found

#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a.upper())       # HYD  IS  GREEN  CITY
print(a.lower())       # hyd  is  green  city
print(a.capitalize())  # Hyd  is  green  city
print(a.title())       # Hyd  Is  Green  City
print(a.swapcase())    # HYd  Is  GReEN  CitY
print(a)               # hyD  iS  grEen  cITy
print('A7$a'.upper())  # A7$A

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a.endswith('city'))         # True  
print(a.endswith('town'))         # False 
print(a.endswith('green', 3, 12)) # False 
print(a.endswith('green', 3, 13)) # True  
print(a.endswith(' ', 3, 13))     # False 

'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself

4) Hint:  Use  endswith()  method
'''
#Program:

s = input("Please enter a string: ") 
if len(s) < 3:
    result = s                
elif s.endswith('ing'):
    result = s + 'ly'         
else:
    result = s + 'ing'      
print(result)

#Output:
Please enter a string:play
playing

#  isalpha()  method  demo  program (Home  work)
print('Hyd'.isalpha())        # True 
print('Rama  Rao'.isalpha())  # False
print('Hyd4'.isalpha())       # False
print('Hyd$'.isalpha())       # False
print('9247'.isalpha())       # False
print('+-$'.isalpha())        # False
print('A2#'.isalpha())        # False
print(''.isalpha())           # False
print(' '.isalpha())          # False


# isdigit()  method  demo  program  (Home  work)
print('9247'.isdigit())       # True
print('92a47'.isdigit())      # False
print('92$47'.isdigit())      # False
print('Hyd'.isdigit())        # False
print('+-$'.isdigit())        # False
print('A2#'.isdigit())        # False
print(''.isdigit())           # False
print(' '.isdigit())          # False
print(9247.isdigit())         # Error

# isspace()  method  demo  program  (Home  work)
print('\n  A\t'.isspace())   # False
print('\n  \t'.isspace())    # True 
print('\n  7\t'.isspace())   # False
print('\n'.isspace())        # True 
print('\n  $\t'.isspace())   # False
print('\t'.isspace())        # True 
print(''.isspace())          # False
print(' '.isspace())         # True 

# islower()  method  demo  program  (Home  work)
print('hyD'.islower())       # False
print('hyd'.islower())       # True 
print('9247'.islower())      # False
print('rama  rao'.islower()) # True 
print('+-$'.islower())       # False
print('hyd+-$'.islower())    # True 
print('abc123'.islower())    # True 
print(''.islower())          # False
print('a2#'.islower())       # True 


# Find  outputs  (Home  work)
a, b, c = 25, 10.8, 'Hyd'

print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '.format(a, b, c))  # a  :  25  	  b  :  10.8 	  c  :  Hyd

print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  '.format(a, b, c))  # a  :  25  	  b  :  10.8 	  c  :  Hyd

print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  '.format(a, b, c))  # a  :  Hyd  	  b  :  10.8 	  c  :  25

print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  '.format(a, b, c))  # a  :  Hyd  	  b  :  Hyd 	  c  :  Hyd

print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(x=a, y=b, z=c))  # a  :  25  	  b  :  10.8 	  c  :  Hyd

print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(z=a, y=b, x=c))  # a  :  Hyd  	  b  :  10.8 	  c  :  25

print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  '.format(z=a, y=b, x=c))  # a  :  25  	  b  :  25 	  c  :  25

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
#Program:

ch = input("Enter any character : ")
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

#Output:
Enter any character : A
Alphanumeric character
Alphabet character
Upper case alphabet

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
# Program:

a = input("Enter a string: ")

b = ""

for i in range(1, len(a)+1):
    b = b + a[-i]

print(b)

#Output:
Enter a string: Hyd
dyH

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
#Program:

s = input("Enter a sentence: ")    
words = s.split()                  
rev_sentence = ''              
for i in range(1, len(words)+1):
    rev_sentence += words[-i] + ' '
rev_sentence = rev_sentence.rstrip()
print("Reversed sentence:", rev_sentence)

#Output:
Enter a sentence: Hyd  is  green  city
Reversed sentence: city   green   is   Hyd


'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
# Program:

s = input("Enter a sentence: ")
words = s.split()              
rev_words = []
for word in words:
    rev_words.append(word[::-1])
rev_sentence = ' '.join(rev_words)
print("Reversed words sentence:", rev_sentence)

#output:
Enter a sentence:  Hyd  is  green  city
Reversed words sentence: dyH si neerg ytic

'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
# Program:

s = input("Enter a string : ")      
sorted_chars = sorted(s)           
sorted_string = ''.join(sorted_chars)
print("Sorted string :", sorted_string)

#Output:
Enter a string : RAJESH
Sorted string : AEHJRS

'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
#Program:

s = input("Enter string with alphabets and digits : ")   
sorted_chars = sorted(s)        
alpha = ''
digit = ''
for ch in sorted_chars:
    if ch.isalpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch
result = alpha + digit
print("Result :", result)

#Output:
Enter string with alphabets and digits :  Z9K3PA7D51
Result : ADKPZ13579