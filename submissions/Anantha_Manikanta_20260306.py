'''
1) Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')  # True
print('day'   in   'Sankar  dayal  sarma')  # True
print('Green'   in   'Hyd  is  green  city')  # False
print('d  is'   in   'Hyd  is  green  city')  # True
print('dis'   in   'Hyd  is  green  city')  # False
print('iniv'   in   'Srinivas')  # True
print('iniv'   not   in   'Srinivas')  # False
'''

'''
2)(Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1

a = 'Rama Rao'
print(a [ : 7 : 2])  # Rm a
print(a [ : 7])  # Rama Ra
print(a [2 : 4]) # ma
print(a [2 : ])  # ma Rao
print(a [ : 4 ]) # Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1])  # ma Ra
print(a [-6 : ])  # ma Rao
print(a [: -4 : -1]) # oaR
print(a [-3 : -1]) # Ra
print(a [-3 : ])  # Rao
print(a [ : : ])  # Rama Rao
print(a [ : ])  # Rama Rao
print(a [ : : -1])  # oaR amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])  # a mR
print(a [2 : 8])  # ma Rao
print(a [2 : 8 : -1])  # ''
print(a [ : -6 : -1])  # oaR
print(a [2 : -3])  # ma
print(a [1 : 6 : 2]) # aaR
print(a [ : -5 : -5])  # o
print(a [2 : -5])  # m
print(a [2 : -5 : 2]) # m
print(a [ : 0 : -1])  # oaR ama
print(a [-5 : 0 : -2]) # aa
'''

'''
3) Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters
Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon
'''
a = input('Enter first string: ')
b = input('Enter second string: ')
result = b[:2] + a[2:] + ' ' + a[:2] + b[2:]
print('Result  :  ', result)

'''
4) Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters
1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON
2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''
s = input('Enter any string : ')
if len(s) < 4:
    print('Result : ')
else:
    print('Result : ', s[:2] + s[-2:])

'''
5) Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     	          0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 
What  are  the  outputs ?
'''
s = input('Enter the string: ')
print('String from left to right :')
for i in range(len(s)):
    print('Character at index', i, ':', s[i])
print('String from right to left:')
for i in range(-1, -len(s)-1, -1):
    print('Character at index', i, ':', s[i])
'''
6) Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
		      0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o
odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' = 'Rm a'
'''
s = input('Enter any string : ')
even = ''
odd = ''
for i in range(len(s)):
    if i % 2 == 0:
        even = even + s[i]
    else:
        odd = odd + s[i]
print('String at even indexes :', even)
print('String at odd indexes  :', odd)

'''
7) Let  input  be    A   4   B   3   C   2   $   5
                     0   1    2   3   4   5   6   7
'''
a = input('Enter any string with alternate character and digit : ')
if len(a) % 2 != 0:
    print('String should have alternate character and digit')
else:
    out = ''
    for i in range(0, len(a), 2):
        out = out + a[i] * int(a[i+1])
    print('Result :', out)
'''
8) Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  ---> HVYADMSI

Hint:  Use  single  while  loop  and  slice
'''
a = input('Enter first string : ')
b = input('Enter second string : ')
c = ''
i = 0
while i < len(a) and i < len(b):
    c = c + a[i] + b[i]
    i += 1
c = c + a[i:] + b[i:]
print('Result :', c)
'''
9) Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
'''
s = input('Enter any string : ')
out = ''
for ch in s:
    if ch not in out:
        out = out + ch
print('String without duplicates :', out)
'''
10) len()  function  demo  program  (Home  work)

print(len('Hyd'))  # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('+-$')) # 3
print(len(''))  # 0
print(len(' ')) # 1
print(len('A2#')) # 3
print(len(3456)) # 4
print('Sec'. len()) # Error because there should not be a space after (.)
'''
11) chr()  function  demo  program
print(chr(65))  # A
print(chr(90))  # Z
print(chr(97))  # a
print(chr(122)) # z
print(chr(48))  # 0
print(chr(57))  # 9
print(chr(36))  # $
print(chr(32))  # ' '
'''
'''
12) ord()  function  demo  program
print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32
'''
'''
13) Let  input  be  A4M3Z5D2
What  is  the  output ?  --->  AEMPZ_DF
 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2
'''
a = input('Enter any string with alternate character and digit : ')
if len(a) % 2 != 0:
    print('Pls enter string with alternate char and digit')
else:
    out = ''
    for i in range(0, len(a), 2):
        ch = a[i]
        num = int(a[i+1])
        out = out + ch + chr(ord(ch) + num)
    print('Result :', out)
'''
14) Modify  following  program  with  walrus  operator
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')

''' 
15) Modify  the  following  program  with  index()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
try:
    while True:
        index = a.index('is', index + 1)
        print(index)
except ValueError:
    pass
print('End')

'''
16) Modify  following  program  with  rfind()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a.rfind('is')
while index != -1:
    print(index)
    index = a.rfind('is', 0, index)
print('End')
'''
17) Modify  following  program  with  rindex()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = len(a)
try:
    while True:
        index = a.rindex('is', 0, index)
        print(index)
except ValueError:
    pass
print('End')

'''
18) count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))  # 4
print(a . count('is' , 19 , 48))  # 3
print(a . count('was')) # 0
'''
'''
19)Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))   # 3
print(a . count('\t'))  # 3
print(a . count('\n'))  # 3
'''