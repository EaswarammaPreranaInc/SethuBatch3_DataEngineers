# --------------------------------------------
# Replace every occurrence of first character
# --------------------------------------------
x = input("Enter a string: ")
z = x[0] + x[1:].replace(x[0], '*')
print(z)
# Example:
# Input : babble
# Output: ba**le




# --------------------------------------------
# split() method outputs
# --------------------------------------------
a = '15:36:48'
print(a.split(':')) # ['15','36','48']
print(a) # 15:36:48


a = 'Hyd\nis green\tcity'
print(a.split(' ')) # ['Hyd\nis','green\tcity']
print(a.split()) # ['Hyd','is','green','city']
print(a.split('green')) # ['Hyd\nis ','\tcity']
# print(a.split('')) # Error (delimiter cannot be empty)


a = 'Hyd\tis\tgreen\tcity'
print(a.split('\t')) # ['Hyd','is','green','city']
print(a.split()) # ['Hyd','is','green','city']
print(a.split(' ')) # ['Hyd\tis\tgreen\tcity']


a = 'Hyd is green city'
print(a.split()) # ['Hyd','is','green','city']
print(a.split(' ')) # ['Hyd','','','is','','','green','','','city']


a = 'www.gmail.com'
print(a.split('.')) # ['www','gmail','com']




# --------------------------------------------
# Evaluate expression containing +
# --------------------------------------------
x = input("Enter expression with + symbols: ")
y = x.split('+')
z = []
for i in y:
    z.append(int(i))
print(sum(z))
# Example:
# Input : 23+456+7+8912
# Output: 9398




# --------------------------------------------
# join() method demo
# --------------------------------------------
a = ['15','36','48']
print(':'.join(a)) # 15:36:48


b = ('Hyd','is','green','city')
print(' '.join(b)) # Hyd is green city


c = {'10','20','15','25','52'}
print(','.join(c)) # order may change (set)


d = ['www','gmail','com']
print('.'.join(d)) # www.gmail.com


# e = [15,36,48]
# print(':'.join(e)) # Error


f = ['Sankar','Dayal','Sarma']
print(''.join(f)) # SankarDayalSarma


# g = range(5)
# print('-'.join(g)) # Error




# --------------------------------------------
# Case conversion methods
# --------------------------------------------
a = 'hyD iS grEen cITy'
print(a.upper()) # HYD IS GREEN CITY
print(a.lower()) # hyd is green city
print(a.capitalize()) # Hyd is green city
print(a.title()) # Hyd Is Green City
print(a.swapcase()) # HYd Is GReEN CitY
print(a) # hyD iS grEen cITy
print('A7$a'.upper()) # A7$A




# --------------------------------------------
# endswith() method
# --------------------------------------------
a = 'Hyd is green city'
print(a.endswith('city')) # True
print(a.endswith('town')) # False
print(a.endswith('green',3,12)) # True
print(a.endswith('green',3,13)) # False
print(a.endswith(' ',3,13)) # True




# --------------------------------------------
# Append ing / ly
# --------------------------------------------
x = input("Enter a string: ")


if len(x) < 3:
    print(x)
else:
    if x.endswith('ing'):
        x += 'ly'
    else:
        x += 'ing'
    print(x)


# Example outputs
# interest → interesting
# interesting → interestingly
# Hi → Hi




# --------------------------------------------
# isalpha()
# --------------------------------------------
print('Hyd'.isalpha()) # True
print('Rama Rao'.isalpha()) # False
print('Hyd4'.isalpha()) # False
print('Hyd$'.isalpha()) # False
print('9247'.isalpha()) # False
print('+-$'.isalpha()) # False
print('A2#'.isalpha()) # False
print(''.isalpha()) # False
print(' '.isalpha()) # False




# --------------------------------------------
# isdigit()
# --------------------------------------------
print('9247'.isdigit()) # True
print('92a47'.isdigit()) # False
print('92$47'.isdigit()) # False
print('Hyd'.isdigit()) # False
print('+-$'.isdigit()) # False
print('A2#'.isdigit()) # False
print(''.isdigit()) # False
print(' '.isdigit()) # False
# print(9247.isdigit()) # Error




# --------------------------------------------
# isspace()
# --------------------------------------------
print('\n A\t'.isspace()) # False
print('\n \t'.isspace()) # True
print('\n 7\t'.isspace()) # False
print('\n'.isspace()) # True
print('\n $\t'.isspace()) # False
print('\t'.isspace()) # True
print(''.isspace()) # False
print(' '.isspace()) # True




# --------------------------------------------
# islower()
# --------------------------------------------
print('hyD'.islower()) # False
print('hyd'.islower()) # True
print('9247'.islower()) # False
print('rama rao'.islower()) # True
print('+-$'.islower()) # False
print('hyd+-$'.islower()) # True
print('abc123'.islower()) # True
print(''.islower()) # False
print('a2#'.islower()) # True




# --------------------------------------------
# format() method
# --------------------------------------------
a , b , c = 25 , 10.8 , 'Hyd'


print('a : {} \t b : {} \t c : {}'.format(a,b,c))
# a : 25 b : 10.8 c : Hyd


print('a : {0} \t b : {1} \t c : {2}'.format(a,b,c))
# a : 25 b : 10.8 c : Hyd


print('a : {2} \t b : {1} \t c : {0}'.format(a,b,c))
# a : Hyd b : 10.8 c : 25


print('a : {2} \t b : {2} \t c : {2}'.format(a,b,c))
# a : Hyd b : Hyd c : Hyd




# --------------------------------------------
# Identify character type
# --------------------------------------------
a = input("Enter a character: ")


if a.isalnum():
    print("Alphanumeric character")


    if a.isalpha():
        print("Alphabet character")


        if a.islower():
            print("Lower case alphabet")


        if a.isupper():
            print("Upper case alphabet")


    if a.isdigit():
        print("Digit character")


elif a.isspace():
    print("White space")


else:
    print("Special character")




# --------------------------------------------
# Reverse string without slice
# --------------------------------------------
a = input("Enter a string: ")
z = ''


for i in range(1,len(a)+1):
    z += a[-i]


print("Reverse string:",z)
# Example
# Input : Hyd
# Output: dyH




# --------------------------------------------
# Reverse order of words
# --------------------------------------------
a = input("Enter a sentence: ")
b = a.split()
c = ''


for i in range(1,len(b)+1):
    c += b[-i] + ' '


print("Reverse order of words:",c)
# Example
# Input : Hyd is green city
# Output: city green is Hyd




# --------------------------------------------
# Sort string
# --------------------------------------------
a = input("Enter a string: ")
b = sorted(a)
c = ''


for i in b:
    c += i


print("Sorted string:",c)




# --------------------------------------------
# Sort alphabets and digits separately
# --------------------------------------------
a = input("Enter string with alphabets and digits: ")


alpha = ''
digit = ''


for i in a:
    if i.isalpha():
        alpha += i
    elif i.isdigit():
        digit += i


alpha = ''.join(sorted(alpha))
digit = ''.join(sorted(digit))


print("Result:",alpha + digit)
# Example
# Input : Z9K3PA7D51
# Output: ADKPZ13579