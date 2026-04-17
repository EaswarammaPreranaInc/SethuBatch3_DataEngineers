# 1 . Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # output : True
print('day'   in   'Sankar  dayal  sarma') # output : True
print('Green'   in   'Hyd  is  green  city') # output : False
print('d  is'   in   'Hyd  is  green  city') # output : True
print('dis'   in   'Hyd  is  green  city') # ouput : False
print('iniv'   in   'Srinivas')  # output : True
print('iniv'   not   in   'Srinivas') # output : False


'''
1) What  does  in  and  not  in  operators  do ?  --->  Searches  for  a  string  in  another  string

2) What  does  str1  in  str2  do ? --->  Returns  True  if  str1  is  in  str2  and  False  otherwise

3) What  does  str1  not  in  str2  do ? --->  Returns  True  if  str1  is  not  in  str2  and  False  otherwise

4) not  in  operator  is  quite  opposite  to  in  operator


# 2 . '''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) # output : Rm a
print(a [ : 7]) # output : Rama Ra
print(a [2 : 4]) # output : ma
print(a [2 : ]) # output : ma Rao
print(a [ : 4 ]) # output : Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) # output : ma Ra
print(a [-6 : ]) # output : ma Rao
print(a [: -4 : -1]) # output : oaR
print(a [-3 : -1]) # output : Ra
print(a [-3 : ]) # output : Rao
print(a [ : : ]) # output : Rama Rao
print(a [ : ]) # output : Rama Rao
print(a [ : : -1]) # output : oaR amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])  # output : a aR
print(a [2 : 8])# output : ma Rao
print(a [2 : 8 : -1]) # output : 
print(a [ : -6 : -1]) # output : oaR
print(a [2 : -3]) # output : ma
print(a [1 : 6 : 2]) # output : aaR
print(a [ : -5 : -5]) # output : o
print(a [2 : -5])  # output : m
print(a [2 : -5 : 2]) # output : m 
print(a [ : 0 : -1])  # output : oaR ama
print(a [-5 : 0 : -2]) # output : aa

# 3 .Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice

# output : a = input("Enter first string: ")
b = input("Enter second string: ")

result = b[:2] + a[2:] + " " + a[:2] + b[2:]

print("Result:", result)


# 4 . Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing

# output : s = input("Enter a string: ")

if len(s) < 4:
    print("")
else:
    result = s[:2] + s[-2:]
    print(result)


# 5 . Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                 Character  at  index  1  :  A
								                 Character  at  index  2  :  M
							                     Character  at  index  3  :  S
								                 Character  at  index  4  :  I

								                 Character  at  index  -1  :  I
								                 Character  at  index  -2  :  S
								                 Character  at  index  -3  :  M
								                 Character  at  index  -4  :  A
								                 Character  at  index  -5  :  V

Hint:  Use  two  for  loops

# output : s = input("Enter a string: ")

# Forward direction
for i in range(len(s)):
    print("Character at index", i, ":", s[i])

# Reverse direction
for i in range(1, len(s)+1):
    print("Character at index", -i, ":", s[-i])


# 6 . '''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' = 'Rm a'

1) What  action  to  be  made  when  index  is  even ?  ---> Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  --->  Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop

# output : s = input("Enter a string: ")

even = ''
odd = ''

for i in range(len(s)):
    if i % 2 == 0:
        even = even + s[i]
    else:
        odd = odd + s[i]

print("Even index characters:", even)
print("Odd index characters:", odd)


# 7 . '''
Let  input  be    A   4   B   3   C   2   $   5
                         0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  ---> 'AAAA'

2)  i        a[i]       a[i + 1]          out
   -------------------------------------------------------
                                               ''
    0         'A'          '4'			   '' + 'A' * 4 = 'AAAA'
	2         'B'          '3'             'AAAA' +  'B' * 3  = 'AAAABBB' 
	4         'C'          '2'             'AAAABBB' +  'C' * 2  = 'AAAABBBCC' 
	6         '$'          '5'             'AAAABBBCC' +  '$' * 5  = 'AAAABBBCC$$$$$' 
   -------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  --->  a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string


# output : 
s = input("Enter the string: ")

out = ''

for i in range(0, len(s), 2):
    out = out + s[i] * int(s[i+1])

print(out)


# 8 . Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  ---> HVYADMSI

             0     1    2
a  --->   H     Y    D

              0    1     2     3    4
b  --->    V    A    M    S    I


i       a[i]        b[i]          c
--------------------------------------------------------
                                    ''
0       'H'        'V'         '' + 'H' + 'V = 'HV'									
1       'Y'        'A'         'HV' + 'Y' + 'A = 'HVYA'									
2       'D'        'M'        'HVYA' + 'D' + 'M = 'HVYADM'									
--------------------------------------------------------

Concatenate  remainging  characters   of  the  other  string  to  object  'c'
What  is  the  final  result ?  --->  'HVYADMSI'

Hint:  Use  single  while  loop  and  slice

# output : a = input("Enter first string: ")
b = input("Enter second string: ")

c = ''
i = 0

while i < len(a) and i < len(b):
    c = c + a[i] + b[i]
    i += 1

c = c + a[i:] + b[i:]

print("Result:", c)



# 9 . Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M'  = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'



3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  ---> 	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  ---> Ignore  the  character

5) Hint:  Use  not  in   operator

# output : s = input("Enter a string: ")

out = ''

for ch in s:
    if ch not in out:
        out = out + ch

print("Result:", out)


# 10 . # len()  function  demo  program  (Home  work)
print(len('Hyd')) # output : 3 
print(len('Rama Rao')) # output : 8
print(len('9247')) # output : 4
print(len('+-$')) # output : 3
print(len('')) # output : 0
print(len(' ')) # output : 1
print(len('A2#')) # output : 3
print(len(3456))  # output : TypeError: object of type 'int' has no len()
print('Sec'. len()) # output : 3

'''
What  does  len(string)  do  ?  --->  Returns  number  of  characters  in  the  string


# 11 . # chr()  function  demo  program
print(chr(65))  #   A
print(chr(90)) # output : Z
print(chr(97)) # output : a
print(chr(122)) # output : z
print(chr(48)) # output : 0
print(chr(57)) # output : 9
print(chr(36))  # output : $
print(chr(32)) # output : space


'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character


# 12 . # ord()  function  demo  program
print(ord('A')) # output : 65
print(ord('Z')) # output : 90
print(ord('a')) # output : 97
print(ord('z')) # output : 122
print(ord('0'))  # output : 48
print(ord('9'))   # output : 57
print(ord('$')) # output : 36
print(ord(' ')) # output : 32

'''
ord()  function
------------------
1) What  does  ord()  function  do ?  --->  Converts  character  to  unicode  value

2) How  many  unicode  values  exist ?  --->  512

3) What  is  the  range  of  unicode  values ?  ---> 0  to  511

4) What  are  the  unicode  values  of  'A'  -  'Z' ?  --->  65  to  90
     What  are  the  unicode  values  of  'a'  -  'z' ?  --->  97  to  122
     What  are  the  unicode  values  of  '0'  -  '9' ?  ---> 48  to  57

5) What  is  another  name  of  unicode ?  ---> Extended  Ascii

Note:  chr()  and  ord()  are  quite  opposite  functions


# 13 . Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


    i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                           ''
   0        'A'        '4'             '' + 'A' +  'E' = 'AE'
   2        'M'        '3'             'AE' + 'M' +  'P' = 'AEMP'
   4        'Z'        '5'             'AEMP' + 'Z' +  '' = 'AEMPZ'
   6        'D'        '2'             'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'															 
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions


# output : s = input("Enter the string: ")

out = ''
i = 0

while i < len(s):
    ch = s[i]           
    n = int(s[i+1])      

    next_ch = chr(ord(ch) + n)   

    if next_ch > 'Z':     
        next_ch = '_'

    out = out + ch + next_ch
    i += 2

print(out)


# 14 . Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

# output : a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)

print('End')



# 15 . ''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  raises   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method

#output : a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.index('is')
    while True:
        print(index)
        index = a.index('is', index + 1)
except ValueError:
    pass

print('End')


# 16 . #  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))
print(a . count('\t'))
print(a . count('\n'))

# output : 3
           3
           3


# 17 . #  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))
print(a . count('is' , 19 , 48))
print(a . count('was'))


'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->
							Returns  number  of  times  str2  is  in  str1  between  indexes  x  and  y - 1

# output : 4
           2
           0


# 18 .   (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found

# output : a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.rindex('is')
    while True:
        print(index)
        index = a.rindex('is', 0, index)
except ValueError:
    pass

print('End')

output : 42
23
4
End