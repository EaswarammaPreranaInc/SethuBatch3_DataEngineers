'''# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') #True
print('day'   in   'Sankar  dayal  sarma') #True
print('Green'   in   'Hyd  is  green  city') # False due to python is case sensitive.
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city')# False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') #False
'''

'''
1) What  does  in  and  not  in  operators  do ?  --->  Searches  for  a  string  in  another  string

2) What  does  str1  in  str2  do ? --->  Returns  True  if  str1  is  in  str2  and  False  otherwise

3) What  does  str1  not  in  str2  do ? --->  Returns  True  if  str1  is  not  in  str2  and  False  otherwise

4) not  in  operator  is  quite  opposite  to  in  operator
'''





'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) #Rm a
print(a [ : 7]) #Rama Ra
print(a [2 : 4]) #ma<space>
print(a [2 : ]) #ma Rao
print(a [ : 4 ]) #Ram
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) #ma Ra
print(a [-6 : ]) #ma Rao
print(a [: -4 : -1]) #oar
print(a [-3 : -1])#Ra
print(a [-3 : ]) #Rao
print(a [ : : ])#Rama Rao
print(a [ : ]) #Rama Rao
print(a [ : : -1])#oaR amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) #a mR
print(a [2 : 8])#ma Rao
print(a [2 : 8 : -1])#oaR ama
print(a [ : -6 : -1])#oaR a
print(a [2 : -3])#ma<space>
print(a [1 : 6 : 2])#aa R
print(a [ : -5 : -5])#o
print(a [2 : -5])#m
print(a [2 : -5 : 2])#m
print(a [ : 0 : -1])#oaR ama
print(a [-5 : 0 : -2])#aa







'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice
'''
# x=input("Enter first string : ")
# y=input("Enter second string: ")

# if len(x) and len(y)>2 :
#     z=x[0:2]+y[2:]
#     a=y[0:2]+x[2:]
#     print(F'Result :{z}\n{a}')
# else:
#     print("Enter strings length greater than 2")



'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''
# x=input("Enter first string : ")
# if len(x)>4:
#     y=x[:2]+x[-2:]
#     print(F'Result: {y}')
# else:
#     print("Nothing")



'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

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
'''


'''x=input("Enter the string: ")

for i in range(len(x)):
    print("string from left to right")
    print(F'Character at index{i} : {x[i]}')
for y in range(len(x)-1,-1,-1):
    print("String from right to left :")
    print(F'Character at index{y} : {x[y]}')'''


'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' = 'Rm a'

1) What  action  to  be  made  when  index  is  even ?  ---> Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  --->  Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop
'''


# x= input("Enter the input : ")
# even=""
# odd=""
# for i in range(len(x)):
#     if i%2==0:
#         even+=x[i]
#     else:
#         odd+=x[i]
# print(F'Even indexes : {even}')
# print(F'Odd indexes : {odd}')







'''
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
'''


# x=input("Enter a string : ")
# out=" "
# try:
#     for i in range(0,len(x),2):
#         out+= x[i]*eval(x[i+1])
#     print(out)
# except NameError:
#     print("string should have alternate character and digit ")




'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

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
'''

# x=input("Enter first string : ")
# y=input("Enter second string : ")
# c=""
# d=0
# while d<len(x) and d<len(y) :
#     c = c+x[d]+y[d]
#     d+=1

# c=c+x[d:]+y[d:]
# print(c)   



'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M'  = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'



3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  ---> 	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  ---> Ignore  the  character

5) Hint:  Use  not  in   operator
'''

'''x=input("Enter the string : ")
y=""
for i in range(len(x)):
    if x[i] not in y:
        y+=x[i] 
print(y)'''



# len()  function  demo  program  (Home  work)
# print(len('Hyd'))  # 3
# print(len('Rama Rao')) # 8
# print(len('9247'))#4
# print(len('+-$'))#3
# print(len(''))#0
# print(len(' '))#1
# print(len('A2#'))#3
# # print(len(3456))# Error no length for int 
# # print('Sec'. len())# Error syntax is wrong 


'''
What  does  len(string)  do  ?  --->  Returns  number  of  characters  in  the  string
'''

# chr()  function  demo  program
# print(chr(65))  #   A
# print(chr(90)) # B
# print(chr(97))#a
# print(chr(122))#z
# print(chr(48))#0
# print(chr(57))#
# print(chr(36))#9
# print(chr(32))#$





'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''



# ord()  function  demo  program
# print(ord('A'))#65
# print(ord('Z'))#90
# print(ord('a'))#97
# print(ord('z'))#122
# print(ord('0'))#48
# print(ord('9'))#57
# print(ord('$'))#36
# print(ord(' '))#32




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
'''




'''
Let  input  be  A4M3Z5D2

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
'''


# try:
#     x=input("Enter a string with alternate character and digit : ")
#     out=""
#     for i in range(0,len(x),2):
#         out=out+x[i]+chr(ord(x[i])+int(x[i+1]))
#     print(out)
# except ValueError :
#     print("Enter a string with alternate character and digit")

# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

# index = -1
# while (index := a.find('is', index + 1)) != -1:
#     print(index)

# print('End')

# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

# index = a.rfind('is')

# while index != -1:
#     print(index)
#     index = a.rfind('is', 0, index)

# print('End')

# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

# try:
#     index = a.rindex('is')

#     while True:
#         print(index)
#         index = a.rindex('is', 0, index)

# except ValueError:
#     print("End")

# a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

# print(a.count('is'))
# print(a.count('is',19,48))
# print(a.count('was'))

# a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'

# print(a.count(' '))
# print(a.count('\t'))
# print(a.count('\n'))


