text=input("Enter any string: ")
first_char=text[0]
string=text[1:]
modified_str=string.replace(first_char,'*')
result=first_char+modified_str
print(f"Result: {result}")


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))    #['15', '36', '48']
print(a)                         #15:36:48


# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'	#['Hyd\nis', 'green\tcity']
print(a . split(' '))		#['Hyd', 'is', 'green','city']
print(a . split())		#['Hyd\nis ','\tcity']
print(a . split('green'))
print(a . split(''))		



# Find  outputs  (Home  work)
a = 'Hyd	is	green	city'   #There  is  tab  between  the  words
print(a . split('\t'))        #['Hyd', 'is', 'green', 'city']                          
print(a . split())		#['Hyd','is','green','city']
print(a . split(' '))		#['Hyd\tis\tgreen\tcity']


# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())		#['Hyd','is','green','city']
print(a . split(' ')           #['Hyd','','''is','','''green','','''city']
          


# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))     #['www','gmail','com']


parts=input("Enter the expression: ").split("+")
numbers=[int(i.strip()) for i in parts]
total_sum=sum(numbers)
print(f"sum of the expression is {total_sum}")



#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))			#[15:36:48]
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))			#Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))			#10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))			#www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))			#error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))			#SankarDayalSarma
g = range(5)
print('-' . join(g))			#error


#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper())		#HYD IS GREEN CITY
print(a . lower())		#hyd is green city
print(a . capitalize())		#Hyd is green city
print(a . title())		#Hyd Is Green City
print(a . swapcase())		#HYd Is GReEN CitY
print(a)			#hyD iS grEen cITy
print('A7$a' . upper())		#A7$A



# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))		#True
print(a . endswith('town'))		#False
print(a . endswith('green' , 3 , 12))	#True
print(a . endswith('green' , 3 , 13))	#False
print(a . endswith(' ' , 3 , 13))	#True


user_string=input("please enter string: ")
if len(user_string)<3:
    result=user_string
elif user_string.endswith('ing'):
    result=user_string+'ly'
else:
    result=user_string+'ing'
print(result)    


#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())	#True
print('Rama  Rao'  . isalpha())	#False
print('Hyd4'  . isalpha())	#False
print('Hyd$'  . isalpha())      #False
print('9247'  .  isalpha())	#False
print('+-$'    .  isalpha())	#False
print('A2#'  .   isalpha())	#False
print(''  .  isalpha())         #False
print(' '  .  isalpha())	#False



# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())	#True
print('92a47' . isdigit())	#False
print('92$47' . isdigit())      #False
print('Hyd' . isdigit())	#False
print('+-$' . isdigit())	#False
print('A2#' . isdigit())	#False
print('' . isdigit())		#False
print(' ' . isdigit())		#False
print(9247 . isdigit())		#error int object has no attribute like isdigit()


# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())	#False
print('\n  \t' . isspace())	#True
print('\n  7\t' . isspace())	#False
print('\n' . isspace())		#True
print('\n  $\t' . isspace())    #False
print('\t' . isspace())		#True
print('' . isspace())  		#False
print(' ' . isspace())		#True



# islower()  method  demo  program  (Home  work)
print('hyD' . islower())	#False
print('hyd' . islower())	#True
print('9247' . islower())	#False
print('rama  rao' . islower())	#True
print('+-$' . islower())	#False
print('hyd+-$' . islower())	#True
print('abc123' . islower())	#True
print('' . islower())		#False
print('a2#' . islower())	#True


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))	#a:25  b:10.8   c:Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))	#a:25  b:10.8   c:Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))	#a:Hyd b:10.8   c:25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))	#a:Hyd b:Hyd    c:Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))   #a:25  b:10.8  c:Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))   #a:Hyd  b:10.8  c:25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))   #a:25   b:25    b:25


char=input("Enter a character: ")
if char.isspace():
    print("output: White space")
elif char.isalnum():
    if char .isalpha():
        case="Upper case"if char.isupper()else "Lower case"
        print(f"output: Alphanumeric character, Alphabet character,{case} alphabet")
    else:
        print("output: Alphanumeric character,Digit character")
else:
    print("output: special character")


text=input("Enter a string: ")
reversed_text=""
for i in range(len(text)-1,-1,-1):
    reversed_text+=text[i]
print(f"Reversed_text:{reversed_text}")    


sentence=input("Enter a sentence: ")
words=sentence.split()
result=""
for i in range(len(words)-1,-1,-1):
    result+=words[i]+" "
print(result.strip())    


text=input("Enter a string: ")
sorted_text="".join(sorted(text))
print(f"output: {sorted_text}")


user_input=input("Enter string with alphabets and digits: ")
alphas=[]
digits=[]
for char in user_input:
    if char.isalpha():
        alphas.append(char)
    elif char.isdigit():
        digits.append(char)
alphas.sort()
digits.sort()
result="".join(alphas)+"".join(digits)
print(f"sorted output: {result}")



