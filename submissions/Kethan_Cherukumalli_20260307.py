'''
Write a program to replace every occurance of first character in the string with '*' except first character

Let input be 'babble'
What is the output? ---> ba**le

Hint: Use replace() method
'''
s = input("Enter any string : ")

char = s[0]

result = char + s[1:].replace(char, '*')

print("Result : ", result)


---------------------------------------------------

# Find outputs (Homework)
a = '15:36:48'
print(a . split(':')) #['15', '36', '48']
print(a) #15:36:48




---------------------------------------------------


# Find outputs (Homework)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) #['Hyd\nis', 'green\tcity']
print(a . split()) #['Hyd', 'is', 'green', 'city']
print(a . split('green')) #['Hyd\nis ', '\tcity']
print(a . split('')) #Error as no delimeter declared to be used for seperation




---------------------------------------------------


# Find outputs (Homework)
a = 'Hyd   is   green   city' # There is tab between the words
print(a . split('\t')) #['Hyd   is   green   city']
print(a . split()) #['Hyd', 'is', 'green', 'city']
print(a . split(' ')) #['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']




---------------------------------------------------


# Find outputs (Homework)
a = 'Hyd is green city'  # There are 3 spaces between the words
print(a . split()) #['Hyd', 'is', 'green', 'city']
print(a . split(' ')) #['Hyd', 'is', 'green', 'city']




---------------------------------------------------


# Find outputs (Homework)
a = 'www.gmail.com'
print(a . split('.')) #['www', 'gmail', 'com']




---------------------------------------------------


'''
Write a program to evaluate an expression which contains only + symbols
Let input be 23 + 456 + 7 + 8912

Print the sum

Hint: Use split() method
'''
expr = input("Enter any addition expression (e.g., 23 + 456 + 7): ")

parts = expr.split('+')

total_sum = 0

for num_str in parts:
    total_sum += int(num_str.strip())

print("Result of evaluation :", total_sum)




---------------------------------------------------


#  Find outputs (Homework)
a = ['15' , '36' , '48']
print(':' . join(a)) #15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) #Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) #10 , 20 , 15 , 25 , 52
d = ['www' , 'gmail', 'com']
print('.' . join(d)) #www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) #Error as only sequence objects i.e strings can be joined via join() method but not non-sequence objects i.e. int objects 15, 36 and 48
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) #SankarDayalSarma
g = range(5)
print('-' . join(g)) ##Error as only sequence objects i.e strings can be joined via join() method but not range() object i.e. range(5)




---------------------------------------------------


#  Case conversion methods (Homework)
a = 'hyD iS grEen cITy'
print(a . upper()) #HYD IS GREEN CITY
print(a . lower()) #hyd is green city
print(a . capitalize()) #Hyd is green city
print(a . title()) #Hyd Is Green City
print(a . swapcase()) #HYd Is GReEN CitY
print(a) #hyD iS grEen cITy
print('A7$a' . upper()) #A7$A




---------------------------------------------------


# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) #True
print(a . endswith('town')) #False
print(a . endswith('green' , 3 , 12)) #True
print(a . endswith('green' , 3 , 13)) #False
print(a . endswith(' ' , 3 , 13)) #True




---------------------------------------------------


'''
Write a program to append 'ing' to input string.
Append 'ly' to the string if the string already ends with 'ing'.
Leave the string unchanged if string has lessthan three characters

1) What is the output if input is 'interest'? ---> interesting

2) What is the output if input is 'interesting'? ---> interestingly

3) What is the output if input is Hi? ---> Hi (itself)

4) Hint: Use endswith() method
'''
s = input("Please enter string : ")

if len(s) < 3:
    result = s
elif s.endswith('ing'):
    result = s + 'ly'
else:
    result = s + 'ing'

print(result)



---------------------------------------------------


# isalpha() method demo program (Homework)
print('Hyd' . isalpha()) #True
print('Rama Rao' . isalpha()) #False
print('Hyd4' . isalpha()) #False
print('Hyd$' . isalpha()) #False
print('9247' . isalpha()) #False
print('+-$' . isalpha()) #False
print('A2#' . isalpha()) #False
print('' . isalpha()) #False
print(' ' . isalpha()) #False



---------------------------------------------------


# isdigit() method demo program (Homework)
print('9247' . isdigit()) #True
print('92a47' . isdigit()) #False
print('92$47' . isdigit()) #False
print('Hyd' . isdigit()) #False
print('+-$' . isdigit()) #False
print('A2#' . isdigit()) #False
print('' . isdigit()) #False
print(' ' . isdigit()) #False
print(9247 . isdigit()) #Error as 'int' object has no attribute 'isdigit'



---------------------------------------------------


# isspace() method demo program (Homework)
print('\n  A\t' . isspace()) #False
print('\n  \t' . isspace()) #True
print('\n  7\t' . isspace()) #False
print('\n' . isspace()) #True
print('\n  $\t' . isspace()) #False
print('\t' . isspace()) #True
print('' . isspace()) #False
print(' ' . isspace()) #True



---------------------------------------------------


# islower() method demo program (Homework)
print('hyD' . islower()) #False
print('hyd' . islower()) #True
print('9247' . islower()) #False
print('rama rao' . islower()) #True
print('+-$' . islower()) #False
print('hyd+-$' . islower()) #True
print('abc123' . islower()) #True
print('' . islower()) #False
print('a2#' . islower()) #True



---------------------------------------------------


# Find outputs (Homework)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) #a  :  25<tab>b  :  10.8<tab>c  :  Hyd  
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) #a  :  25<tab>b  :  10.8<tab>c  :  Hyd  
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) #a  :  Hyd<tab>b  :  10.8<tab>c  :  25 
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) #a  :  Hyd<tab>b  :  Hyd<tab>c  :  Hyd  
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) #a  :  25<tab>b  :  10.8<tab>c  :  Hyd  
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #a  :  Hyd<tab>b  :  10.8<tab>c  :  25 
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #a  :  25<tab>b  :  25<tab>c  :  25  



---------------------------------------------------


'''
Write a program to determine user input is alphabet , digit , white space or special character

1) What are the three outputs if input is 'A'? ---> Alphanumeric character , Alphabet character , Upper case alphabet

2) What are the three outputs if input is 'a'? ---> Alphanumeric character , Alphabet character , lower case alphabet

3) What are the two outputs if input is '7'? ---> Alphanumeric character , digit character

4) What is the output if input is '$'? ---> Special character

5) What is the output if input is <spacebar>? ---> White space

6) What is the output if input is <tab> key? ---> White space

7) What is the output if input is <enter> key? ---> White space

8) Hint1: Use isalnum() , isalpha() , isupper() , islower() , isdigit() and isspace() methods

9) Hint2: Use nested if and elif
'''
ch = input("Enter any character : ")

if ch.isalnum():
    print("Alpha Numeric Character")
    
    if ch.isalpha():
        print("Alphabet Character")
        
        if ch.isupper():
            print("Upper case Alphabet")
        else:
            print("lower case alphabet")
            
    elif ch.isdigit():
        print("digit character")

elif ch.isspace():
    print("White space")

else:
    print("Special character")



---------------------------------------------------


'''
Write a program to reverse a string without slice

1)  Let input be  Hyd
    What is the output ? ---> dyH

2)  H   y   d
   -3  -2  -1

i       a[-i]          b
------------------------------------------
                       ''
1       'd'            '' + 'd' = 'd'
2       'y'            'd' + 'y' = 'dy'
3       'H'            'dy' + 'H' = 'dyH'
------------------------------------------
'''
s = input("Enter any string : ")
rs = ""

for i in range(1, len(s) + 1):
    char = s[-i]
    rs += char

print("Reverse String : ", rs)



---------------------------------------------------


'''
Write a program to reverse order of words in the sentence without slice

1)  Let input be Hyd is green city
    What is the output? ---> city green is Hyd

2) What is the result of input . split()? ---> ['Hyd' , 'is' , 'green' , 'city'] ---> Assume that it is 'b'

3) i        b[-i]           c
   ------------------------------------------------------------------------------
                           ''
    1        'city'        '' + 'city' + ' ' = 'city '
    2        'green'       'city ' + 'green' + ' ' = 'city green '
    3        'is'          'city green ' + 'is' + ' ' = 'city green is '
    4        'Hyd'         'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '
   ------------------------------------------------------------------------------
'''
s = input("Enter any sentence: ")
b = s.split()
c = ""

for i in range(1, len(b) + 1):
    word = b[-i]
    c = c + word + " "

print("Reverse order of words: ", c.strip())


---------------------------------------------------


'''
Write a program to reverse each word of the sentence

1)  Let input be Hyd is green city
    What is the output? ---> dyH si neerg ytic

2) Hint: Use for each loop and also slice
'''
s = input("Enter any sentence: ")

words = s.split()

revw = []
for word in words:
    revw.append(word[::-1])

result = " ".join(revw)

print(result)



---------------------------------------------------


'''
Write a program to sort string in alphabetical order

Let input be RAJESH
What is the output ? ---> AEHJRS
'''
s = input("Enter any string: ")

charl = sorted(s)

sortstr = "".join(charl)

print("Sorted string: ", sortstr)



---------------------------------------------------


'''
Write a program to sort string such that alphabets in alphabetical order and digits in ascending order

Let input be Z9K3PA7D51
What is the output ? ---> ADKPZ13579

1) What is the result after input is sorted? ---> '13579ADKPZ'

2)  alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9' = '13579'

3) What is the result after alpha and digit are concatenated? ---> 'ADKPZ13579'
'''
s = input("Enter string with alphabets and digits : ")

alpha = ""
digit = ""

for char in s:
    if char.isalpha():
        alpha += char
    elif char.isdigit():
        digit += char

sortalpha = "".join(sorted(alpha))
sortdigit = "".join(sorted(digit))

result = sortalpha + sortdigit

print("Result : ", result)