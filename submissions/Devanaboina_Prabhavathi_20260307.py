Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''

s = input("Enter string: ")
first = s[0]        
rest = s[1:]          
rest = rest.replace(first, '*')

result = first + rest
print(result)


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) 
print(a) # ['15' '36' '48']
15:36:48

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split('Hyd ')) # Hyd
print(a . split('is')) # is
print(a . split('green')) # green
print(a . split('city')) # city

# Find  outputs  (Home  work)
a = 'Hyd  is   green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd', 'is', 'green', 'city']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd\tis\tgreen\tcity']

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # 'Hyd' 'is' 'green' 'city'
print(a . split(' ') # ['Hyd','','','is','', '','green','','','city']

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#['www','gmail','com']


'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''
a = input("Enter expression: ")
parts = a.split('+')   # split numbers using +

total = 0
for x in parts:
    total = total + int(x)
print("Sum =", total)


#  Find  outputs  (Home  work)
a = ['15' , '36' , '48'] 
print(':' . join(a)) #15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) # Hyd  is  green  city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) 10, 20, 15, 25, 52
d = ['www' , 'gmail', 'com']
print('.' . join(d)) #www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) # error
f = ['Sankar' , 'Dayal' , 'Sarma'] 
print('' . join(f)) # SankarDayalSarma
g = range(5)
print('-' . join(g)) # error


 #Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) # HYD IS GREEN CITY
print(a . lower()) # hyd is green city
print(a . capitalize()) #Hyd is green city
print(a . title()) # Hyd Is Green City
print(a . swapcase()) # 'HYd  Is  GReEN  CitY'
print(a)  # hyD  iS  grEen  cITy
print('A7$a' . upper()) # 'A7$a' → 'A7$A'


# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) #True
print(a . endswith('town')) # false
print(a . endswith('green' , 3 , 12)) #true
print(a . endswith('green' , 3 , 13)) #false
print(a . endswith(' ' , 3 , 13))  #true

# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) #true
print('92a47' . isdigit()) #false
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit()) #false
print('+-$' . isdigit()) # false
print('A2#' . isdigit()) # false
print('' . isdigit()) #   False
print(' ' . isdigit()) # false
print(9247 . isdigit())# false


# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) # False
print('\n  \t' . isspace()) # True
print('\n  7\t' . isspace()) # False
print('\n' . isspace())  # True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace()) # True
print('' . isspace())  #  False
print(' ' . isspace())# True

# islower()  method  demo  program  (Home  work)
print('hyD' . islower()) # False
print('hyd' . islower()) # True
print('9247' . islower()) # False
print('rama  rao' . islower()) # true
print('+-$' . islower()) # false
print('hyd+-$' . islower()) # True
print('abc123' . islower()) #True
print('' . islower()) # False
print('a2#' . islower()) # True


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
a = input("Enter a string: ")
b = ''

for i in range(1, len(a)+1):  # i = 1 to length of string
    b += a[-i]

print("Reversed string:", b)

'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''

sentence = input("Enter a sentence: ")
reversed_words = []

for word in sentence.split():
    reversed_words.append(word[::-1])

result = ' '.join(reversed_words)
print("Reversed words:", result)


'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''

s = input("Enter a string: ")

# Sort characters and join them back
sorted_s = ''.join(sorted(s))

print("Sorted string:", sorted_s)

