Name-Dhruva Gupta
Roll Number-D238

1)
# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city’) #True
print('day'   in   'Sankar  dayal  sarma’) #True
print('Green'   in   'Hyd  is  green  city’) #False
print('d  is'   in   'Hyd  is  green  city’) #True
print('dis'   in   'Hyd  is  green  city’) #False
print('iniv'   in   ‘Srinivas') #True
print('iniv'   not   in   ‘Srinivas') #False

2)
'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) #Rm a
print(a [ : 7]) #Rama Ra
print(a [2 : 4]) #ma
print(a [2 : ]) #ma Rao
print(a [ : 4 ]) #Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) #ma Ra
print(a [-6 : ]) #ma Rao
print(a [: -4 : -1]) # Ra
print(a [-3 : -1]) #Ra
print(a [-3 : ]) #Rao
print(a [ : : ]) #Full String
print(a [ : ]) #Full String
print(a [ : : -1]) #Full String in Reverse
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])  a mR
print(a [2 : 8]) #ma Rao
print(a [2 : 8 : -1]) #Empty String
print(a [ : -6 : -1]) #oaR a
print(a [2 : -3])  #Empty String
print(a [1 : 6 : 2]) #aaR
print(a [ : -5 : -5])#Empty String
print(a [2 : -5]) #Empty String
print(a [2 : -5 : 2]) #Empty String
print(a [ : 0 : -1]) #Empty String
print(a [-5 : 0 : -2]) #Empty String

3)
# len()  function  demo  program  (Home  work)
print(len('Hyd'))   #3
print(len('Rama Rao’)) #8
print(len(‘9247')) #4
print(len(‘+-$')) #3
print(len(‘')) #0
print(len(' ‘)) #1
print(len(‘A2#')) #3
print(len(3456)) #Error
print('Sec'. len()) ##error


4)
# chr()  function  demo  program
print(chr(65))  #   A
print(chr(90)) # Z
print(chr(97)) #a
print(chr(122)) #z
print(chr(48)) #0
print(chr(57)) #9
print(chr(36)) #$
print(chr(32)) # space

5)
# ord()  function  demo  program
print(ord(‘A')) #65
print(ord(‘Z')) #90
print(ord(‘a')) #97
print(ord(‘z')) #122
print(ord(‘0')) #48
print(ord(‘9')) #57
print(ord(‘$')) #36
print(ord(' ‘)) #32

6)
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ‘)) #3
print(a . count(‘\t')) #3
print(a . count(‘\n')) #3

7)
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(‘:')) #[’15’,’36’,’48’]
print(a) #15:36:48

8)
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ‘)) #['Hyd\nis', 'green\tcity']
print(a . split()) #['Hyd', 'is', 'green', 'city']
print(a . split(‘green')) ['Hyd\nis ', '\tcity']
print(a . split(‘')) #Empty string not allowed

9)
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split(‘\t')) #[‘Hyd’,’is’,’green’,’city’]
print(a . split()) #[‘Hyd’,’is’,’green’,’city’]
print(a . split(' ‘)) [‘Hyd\tis\tgreen\tcity']

10)
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) #[‘Hyd’,’is’,’green’,’city’]
print(a . split(' ‘)) #[‘Hyd’,’is’,’green’,’city’]

11)
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split(‘.')) #[‘www’,’gmail’,’com’]

12)
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) #15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) #Hyd id green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) #10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d)) #www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) #Elements need to be string
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) #SankarDayalSarma
g = range(5)
print('-' . join(g)) #Error

13)
#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper()) #HYD  IS  GREEN  CITY
print(a . lower()) #hyd  is  green  city
print(a . capitalize()) #Hyd  is  green  city
print(a . title()) #Hyd  Is  Green  City
print(a . swapcase()) #HYd  Is  GReEN  CitY
print(a) #hyD  iS  grEen  cITy
print('A7$a' . upper()) #A7$A

14)
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith(‘city')) #True
print(a . endswith(‘town')) #False
print(a . endswith('green' , 3 , 12)) #True
print(a . endswith('green' , 3 , 13)) #False
print(a . endswith(' ' , 3 , 13)) #True

15)
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha()) #True
print('Rama  Rao'  . isalpha()) #False
print('Hyd4'  . isalpha()) #False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha()) #False
print('+-$'    .  isalpha()) #False
print('A2#'  .   isalpha()) #False
print(''  .  isalpha())  #  False
print(' '  .  isalpha()) #False

16)
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) #True
print('92a47' . isdigit()) #False
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit()) #False
print('+-$' . isdigit()) #False
print('A2#' . isdigit()) #False
print('' . isdigit()) #   False
print(' ' . isdigit()) #False
print(9247 . isdigit()) #Error

17)
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) #False
print('\n  \t' . isspace()) #True
print('\n  7\t' . isspace()) #False
print('\n' . isspace()) #True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace()) #True
print('' . isspace())  #  False
print(' ' . isspace()) #True

18)
# islower()  method  demo  program  (Home  work)
print('hyD' . islower()) #False
print('hyd' . islower()) #True
print('9247' . islower()) #False
print('rama  rao' . islower()) #True
print('+-$' . islower()) #False
print('hyd+-$' . islower()) #True
print('abc123' . islower()) #True
print('' . islower()) #False
print('a2#' . islower()) #True

19)
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))

20)
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) #a:25		b:10.8		c:Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) #a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) #a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) #a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) #a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #a  :  25  	  b  :  25  	  c  :  25

21)
s=input("Give the input: ")
if len(s)<4:
    print(" ")
print(s[0:2]+s[-2:])

22)
s="Vamsi"
for i in range(0,len(s)):
    print(f"Character at index {i} : {s[i]} ")
print("---------------------------------------------")
for i in range(-1,-len(s)-1,-1):
    print(f"Character at index {i} : {s[i]} ")

23)
s="Rama Rao"
even=""
odd=""
for i in range(0,len(s)):
    if(i%2==0):
        even=even+s[i]
    else:
        odd=odd+s[i]
print(even)
print(odd)

24)
s1="HYD"
s2="VAMSI" #5-3=2
ans=""
i=0 
while i<len(s1):
    ans=ans+(s1[i]+s2[i])
    i=i+1
ans=ans+(s2[-2:])
print(ans)

25)
s=input("Enter the input: ")
ans=""
try:
    for i in range(0,len(s)):
        if(i%2==0):
            ans=ans+(s[i]+chr(ord(s[i])+int(s[i+1])))
except Exception:
    print("Check Inputs")
print(ans)

26)
s = "babble"
i = s.find("b")
s = s[:i+1] + s[i+1:].replace("b", "*")
print(s)

s = "9876543210"
print(s[:3] + "*"*6 + s[len(s)-1])

27)
s=input("Enter the input: ")
if(s.isalnum()):
    if(s.isalpha()):
        if(s==s.upper()):
            print("Alphanumeric  character , Alphabet character , Upper case  alphabet")
if(s.isalnum()):
    if(s.isalpha()):
        if(s==s.lower()):
            print("Alphanumeric  character , Alphabet character , lower case  alphabet")
if(s.isalnum()):
    if(s.isdigit()):
        print("Alphanumeric  character , digit  character")
if(s.isspace()):
    print("White  space")

28)
s="Hyd  is  green  city"
ans=""
b=s.split()
print(b)
print(ans)

29)
s="Z9K3PA7D51"
a=""
b=""
for i in range(0,len(s)):
    if(ord(s[i])>=65 and ord(s[i])<=97):
        a=a+s[i]
    else:
        b=b+s[i]
c=sorted(a)
d=sorted(b)
e=c+d
for i in e:
    print(i,end="")

30)
s=input("Enter the String ")
ans=s
if len(s)<3:
    print("Enter more characters: ")
if s.endswith('ing'):
    ans=ans+'ly'
else:
    ans=ans+'ing'
print(ans)

31)
s="Hyd  is  green  city"
ans=""
b=s.split()
for i in range(len(b)-1,-1,-1):
    ans=ans+" "+b[i]
print(ans)

32)
s=input("Enter the input: ")
ans=""
for i in range(1,len(s)+1):
    ans=ans+s[-i]
print(ans)

33)
s = "RAJESH"
a = list(s)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

for i in a:
    print(i, end="")

34)
s="23 + 456 + 7 + 8912"
b=s.split('+')
sum=0
for i in b:
    sum=sum+int(i)
print(sum)
