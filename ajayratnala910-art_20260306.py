# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') # False


# Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) # Rm a
print(a [ : 7]) # Rama Ra
print(a [2 : 4]) # ma 
print(a [2 : ]) # ma Rao
print(a [ : 4 ]) # Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) # ma Ra 
print(a [-6 : ]) # ma Ra 
print(a [: -4 : -1]) # oaR 
print(a [-3 : -1]) # Ra
print(a [-3 : ]) # Rao
print(a [ : : ]) # Rama Rao
print(a [ : ]) # Rama Rao
print(a [ : : -1]) # oaR amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) # a mR
print(a [2 : 8]) # ma Rao
print(a [2 : 8 : -1]) # 
print(a [ : -6 : -1]) # oaR a
print(a [2 : -3]) # ma 
print(a [1 : 6 : 2]) # aaR
print(a [ : -5 : -5])# o
print(a [2 : -5]) # m
print(a [2 : -5 : 2]) # m
print(a [ : 0 : -1]) # oaR ama
print(a [-5 : 0 : -2]) # aa


Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
program:
a = input("enter str1: ");
b = input("enter str2: ");
if len(a) < 2 or len(b) < 2:
    print("enter str with atleast two characters");
else:
    c = b[0:2]+a[2:];
    d = a[0:2]+b[2:];
    print(c,d, sep=' ');


Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

 a = input("enter the str1: ");
 n = len(a);
 if len(a)<4:
     print('');
 else:
     print(a[0:2],a[n-2:n], sep=' ');

# Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

a = input("enter the str1: ");
n = len(a);
for i in range(n):
    print(a[i], end = '');
print();
for i in range(-1,-n-1,-1):
	print(a[i], end='')

# Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
a = input("enter the str1: ");
b=[]
c=[]
n =len(a);
for i in range(n):
    if i%2==0:
        b.append(a[i]);
    else:
        c.append(a[i]);
print(b,c);


a = input("Enter string: ")
out = ""

for i in range(0, len(a), 2):
    out += a[i] * int(a[i+1])

print(out)




a = input("Enter first string: ")   # HYD
b = input("Enter second string: ")  # VAMSI

c = ""
i = 0
n = min(len(a), len(b))
while i < n:
    c += a[i] + b[i]
    i += 1
c += a[i:] + b[i:]
print(c)



s = input("Enter a string: ")  # RAMA RAO
out = ""
for char in s:
    if char not in out:
        out += char
print(out)



print(len('Hyd'))        # 3     'H','y','d'
print(len('Rama Rao'))   # 8     includes space
print(len('9247'))       # 4
print(len('+-$'))        # 3
print(len(''))           # 0     empty string
print(len(' '))          # 1     space counts as a character
print(len('A2#'))        # 3
print(len(3456))        # Error: int has no len()
print('Sec'. len())     # Error: wrong syntax, should be len('Sec')
print(len('Sec'))        # 3



print(chr(65))   # A   Unicode 65
print(chr(90))   # Z   Unicode 90
print(chr(97))   # a   Unicode 97
print(chr(122))  # z   Unicode 122
print(chr(48))   # 0   Unicode 48
print(chr(57))   # 9   Unicode 57
print(chr(36))   # $   Unicode 36
print(chr(32))   # space Unicode 32



print(ord('A'))  # 65  Unicode of 'A'
print(ord('Z'))  # 90  Unicode of 'Z'
print(ord('a'))  # 97  Unicode of 'a'
print(ord('z'))  # 122 Unicode of 'z'
print(ord('0'))  # 48  Unicode of '0'
print(ord('9'))  # 57   Unicode of '9'
print(ord('$'))  # 36  Unicode of '$'
print(ord(' '))  # 32   Unicode of space



s = input("Enter string: ")  # A4M3Z5D2
out = ""
for i in range(0, len(s), 2):
    char = s[i]
    num = int(s[i+1])
    out += char + chr(ord(char) + num)
print(out)



a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = 0
while (index := a.find('is', index)) != -1:
    print(index)
    index += 1   
print('End')



a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = 0
while True:
    try:
        index = a.index('is', index)
        print(index)
        index += 1                  
    except ValueError:
        break
print('End')



a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = len(a)
while True:
    index = a.rfind('is', 0, index)   
    if index == -1:
        break
    print(index)



a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = len(a)

while True:
    try:
        index = a.rindex('is', 0, index)
        print(index)
        index -= 1   
    except ValueError:
        break

print('End')




a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a.count('is'))          
print(a.count('is', 19, 48))  
print(a.count('was'))