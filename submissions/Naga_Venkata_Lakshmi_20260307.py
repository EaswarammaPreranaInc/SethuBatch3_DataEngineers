#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) #['15' , '36' , '48']
print(a) #15 : 36 :48

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))  #['Hyd\nis' ,'green\tcity']
print(a . split())  #['Hyd\nis' , 'green\tcity']
print(a . split('green')) #['Hyd\nis  ',  '\tcity']
print(a . split('')) #ValueError


# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))  #['Hyd' , 'is\tgreen\tcity']
print(a . split())      #['Hyd' , 'is' , 'green' , 'city']
print(a . split(' '))   #['Hyd' , 'is' , 'green' , 'city']



# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) #['Hyd' ,   'is' ,   'green' ,   'city']
print(a . split(' ')) #['Hyd' , '', '', 'is', '', '', 'green','', '' , 'city']


# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) #['www' , 'gmail' , 'com']



#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))  #15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))  #Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) #10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d)) #www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) #Type Error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))  #Sankar Dayal Sarma
g = range(5)
print('-' . join(g))  #Type Error


#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper())  #'HYD IS GREEN CITY'
print(a . lower())  #'hyd is green city'
print(a . capitalize())  #'Hyd is green city'
print(a . title())       #'Hyd Is Green City'
print(a . swapcase())    #'HYD IS gREEN cIty'
print(a)                 #'hyD is green cITy'
print('A7$a' . upper())  #'A7$A'


# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))  #True
print(a . endswith('town'))  #False
print(a . endswith('green' , 3 , 12))  #True
print(a . endswith('green' , 3 , 13))  #True
print(a . endswith(' ' , 3 , 13))      #True


#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #True
print('Rama  Rao'  . isalpha()) #True
print('Hyd4'  . isalpha())     #False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha()) #   False
print('+-$'    .  isalpha()) #  False
print('A2#'  .   isalpha())  #Falsw
print(''  .  isalpha())  #  False
print(' '  .  isalpha())  #False



# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) #True
print('92a47' . isdigit()) #False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit())    #False
print('+-$' . isdigit())    #False
print('A2#' . isdigit())    #False
print('' . isdigit()) #   False
print(' ' . isdigit()) #False
print(9247 . isdigit()) #False


# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #False
print('\n  \t' . isspace())   #True
print('\n  7\t' . isspace())  #False
print('\n' . isspace())       #True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace())       # True
print('' . isspace())  #  False
print(' ' . isspace()) #  False


 islower()  method  demo  program  (Home  work)
print('hyD' . islower()) #False
print('hyd' . islower()) #True
print('9247' . islower()) #False
print('rama  rao' . islower()) #True
print('+-$' . islower())       #False
print('hyd+-$' . islower())    # False
print('abc123' . islower())    #False
print('' . islower())          #False
print('a2#' . islower())       #False



# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))  # a : 25   b : 10.8   c : Hyd 
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a : 25   b : 10.8   c : Hyd 
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # a : 25   b : 10.8   c : Hyd 
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a : 25   b : 10.8   c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) #  x = 25  y = 10.8  z = Hyd 
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #  x = 25  y = 10.8  z = Hyd 

print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #   x = 25  y = 10.8  z = Hyd



ch = input("Enter a character:  ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit") 
elif ch.isspace():
    print("White space")  
else:
    print("Special character") 


s = input("Enter any string:  ")
rev =""

for i in range(len(s)-1,-1,-1):
    rev = rev + s[i]
print("Reversed string:", rev)    



s = input("Enter a sentence:  ")

words = s.split()

for i in range(len(words)-1, -1 , -1):
    print(words[i],end = " ")



s = input("Enter any string:  ")

chars = sorted(s)
result =""
for ch in chars:
    result = result + ch
print("Sorted string:", result)   



s = input("Enter a string: ")


first = s[0]
rest = s[1:]

rest = rest.replace(first, "*")
result = first + rest
print("Result:", result)


 
 










