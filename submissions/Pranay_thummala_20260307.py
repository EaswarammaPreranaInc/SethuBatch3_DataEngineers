s = input("Enter a string: ")
a=s[0]
b=s[1:].replace(a,'*')
res = a+b
print(res)


a = '15:36:48'
print(a.split(':')) #['15', '36', '48']
print(a)        #15:36:48



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



a = 'Hyd   is   green   city'   # There are 3 spaces between the words
print(a.split())     # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))  # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']




a = 'www.gmail.com'
print(a.split('.'))   # ['www', 'gmail', 'com']



# Program to evaluate an expression containing only + symbols with an example be 23 + 456 + 7 + 8912
exp = input("Enter expression: ")   
parts = exp.split('+')              
total = 0
for i in parts:
    total += int(i.strip())  
print("Sum =", total)



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




a = 'hyD  iS  grEen  cITy'
print(a.upper())       # HYD  IS  GREEN  CITY
print(a.lower())       # hyd  is  green  city
print(a.capitalize())  # Hyd  is  green  city
print(a.title())       # Hyd  Is  Green  City
print(a.swapcase())    # HYd  Is  GReEN  CitY
print(a)               # hyD  iS  grEen  cITy
print('A7$a'.upper())  # A7$A




a = 'Hyd is green city'

print(a.endswith('city'))         # True  
print(a.endswith('town'))         # False 
print(a.endswith('green', 3, 12)) # False 
print(a.endswith('green', 3, 13)) # True  
print(a.endswith(' ', 3, 13))     # False 



# Program to append 'ing' or 'ly' based on conditions
s = input("Enter a string: ") 
if len(s) < 3:
    result = s                
elif s.endswith('ing'):
    result = s + 'ly'         
else:
    result = s + 'ing'      
print(result)



print('Hyd'.isalpha())        # True 
print('Rama  Rao'.isalpha())  # False
print('Hyd4'.isalpha())       # False
print('Hyd$'.isalpha())       # False
print('9247'.isalpha())       # False
print('+-$'.isalpha())        # False
print('A2#'.isalpha())        # False
print(''.isalpha())           # False
print(' '.isalpha())          # False




print('9247'.isdigit())       # True
print('92a47'.isdigit())      # False
print('92$47'.isdigit())      # False
print('Hyd'.isdigit())        # False
print('+-$'.isdigit())        # False
print('A2#'.isdigit())        # False
print(''.isdigit())           # False
print(' '.isdigit())          # False
# print(9247.isdigit())         # Error



print('\n  A\t'.isspace())   # False
print('\n  \t'.isspace())    # True 
print('\n  7\t'.isspace())   # False
print('\n'.isspace())        # True 
print('\n  $\t'.isspace())   # False
print('\t'.isspace())        # True 
print(''.isspace())          # False
print(' '.isspace())         # True 




print('hyD'.islower())       # False
print('hyd'.islower())       # True 
print('9247'.islower())      # False
print('rama  rao'.islower()) # True 
print('+-$'.islower())       # False
print('hyd+-$'.islower())    # True 
print('abc123'.islower())    # True 
print(''.islower())          # False
print('a2#'.islower())       # True 



a, b, c = 25, 10.8, 'Hyd'

print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '.format(a, b, c))  # a  :  25  	  b  :  10.8 	  c  :  Hyd

print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  '.format(a, b, c))  # a  :  25  	  b  :  10.8 	  c  :  Hyd

print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  '.format(a, b, c))  # a  :  Hyd  	  b  :  10.8 	  c  :  25

print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  '.format(a, b, c))  # a  :  Hyd  	  b  :  Hyd 	  c  :  Hyd

print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(x=a, y=b, z=c))  # a  :  25  	  b  :  10.8 	  c  :  Hyd

print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(z=a, y=b, x=c))  # a  :  Hyd  	  b  :  10.8 	  c  :  25

print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  '.format(z=a, y=b, x=c))  # a  :  25  	  b  :  25 	  c  :  25




# Program to determine the type of user input character
ch = input("Enter a single character: ")
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




# Program to reverse a string without using slice
s = input("Enter a string: ")
rev = ''                       
for i in range(1, len(s)+1):
    rev += s[-i]                
print("Reversed string:", rev)




# Program to reverse the order of words in a sentence
s = input("Enter a sentence: ")    
words = s.split()                  
rev_sentence = ''              
for i in range(1, len(words)+1):
    rev_sentence += words[-i] + ' '
rev_sentence = rev_sentence.rstrip()
print("Reversed sentence:", rev_sentence)



# Program to reverse each word in a sentence
s = input("Enter a sentence: ")
words = s.split()              
rev_words = []
for word in words:
    rev_words.append(word[::-1])
rev_sentence = ' '.join(rev_words)
print("Reversed words sentence:", rev_sentence)



# Program to sort string alphabetically
s = input("Enter a string: ")      
sorted_chars = sorted(s)           
sorted_string = ''.join(sorted_chars)
print("Sorted string:", sorted_string)




s = input("Enter a string: ")   
sorted_chars = sorted(s)        
alpha = ''
digit = ''
for ch in sorted_chars:
    if ch.isalpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch
result = alpha + digit
print("Sorted string:", result)