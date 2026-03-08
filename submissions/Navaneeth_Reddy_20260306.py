# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') #True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') # False

#-----------------------------------------------------------------------------------------------------------------
'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) # Rm a , string from index 0 to 6 in steps of 2
print(a [ : 7]) # Rama Ra, string from index 0 to 6 in steps of 1
print(a [2 : 4]) # ma, string from index 2 to 3 in steps of 1
print(a [2 : ]) # ma Rao , string from index 2 to 7 in steps of 1
print(a [ : 4 ]) # Rama ,string from index 0 to 3 in steps of 1
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) # ma Ra , string from index -6 to -2 in steps of 1
print(a [-6 : ]) # ma Rao
print(a [: -4 : -1]) # oaR
print(a [-3 : -1]) # Ra ,string from index -3 to -2 in steps of 1
print(a [-3 : ]) # Rao
print(a [ : : ]) # Rama Rao , default start =0 , default stop = 8 , default step is 1
print(a [ : ]) # Rama Rao , default start =0 , default stop = 8 , default step is 1
print(a [ : : -1]) #oaR amaR , default start is -1, default stop is -8 and step value is -1
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) # a mR, string of indexes -2, -4, -6, -8 because start is -2 with step value of -2
print(a [2 : 8]) # ma Rao
print(a [2 : 8 : -1]) #Empty String, negative step for postive indexes
print(a [ : -6 : -1]) # oaR a, 
print(a [2 : -3]) # ma
print(a [1 : 6 : 2]) # aaR
print(a [ : -5 : -5]) #o
print(a [2 : -5]) # m
print(a [2 : -5 : 2]) # m
print(a [ : 0 : -1]) # oaR ama
print(a [-5 : 0 : -2]) #aa

#--------------------------------------------------------------------------
'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice
'''
st1 = input("Enter the 1st string : ")
st2 = input("Enter the 2nd string : ")

nst1 = st2[:2] + st1[2:]
nst2 = st1[:2] + st2[2:]

res = nst1 +" " + nst2
print("Output : ", res)

'''
Output :
Enter the 1st string : JAVA
Enter the 2nd string : PYTHON
Output :  PYVA JATHON
Enter the 1st string : HYD
Enter the 2nd string : SEC
Output :  SED HYC
'''
#------------------------------------------------------------------
'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''

st1 = input("Enter the string : ")

if len(st1) < 4:
    print("Nothing")
else :
    nst = st1[:2]+st1[-2:]
    print(nst)

'''
Output :
Enter the string : HYDERABAD
HYAD
Enter the string : HYD
Nothing
'''
#---------------------------------------------------------------------
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

a = input("Enter the string : ")

print("String from Left to Right")
for i in range(len(a)) :
    print(f'Character at index {i} : {a[i]}')
print("String from Right to Left")
for j in range(-1, -len(a)-1, -1):
    print(f'Character at index {j} : {a[j]}')
    
'''
Output :
Enter the string : HY12$
String from Left to Right
Character at index 0 : H
Character at index 1 : Y
Character at index 2 : 1
Character at index 3 : 2
Character at index 4 : $
String from Right to Left
Character at index -1 : $
Character at index -2 : 2
Character at index -3 : 1
Character at index -4 : Y
Character at index -5 : H
'''
#----------------------------------------------------------
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
b = input("Enter the string : ")

even = ""
odd = ""
for i in range(len(b)):
    if i%2 == 0:
        even = even + b[i]
    else :
        odd = odd + b[i]
        
print("String at even indexes : ",even)
print("String at odd indexes : ", odd)
'''
Output :
Enter the string : Rama Rao
String at even indexes :  Rm a
String at odd indexes :  aaRo
'''
#-----------------------------------------------------------------------------
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
a1 = input("Enter the 1st string : ")
a2 = input("Enter the 2nd string : ")

ot = ""

for i in range(min(len(a1), len(a2))) :
    ot = ot + a1[i] + a2[i]

if len(a1) > len(a2) :
    ot = ot + a1[len(a2):]
elif len(a2) > len(a1):
    ot = ot + a2[len(a1):]

print("Result : ",ot)

'''
Output :
Enter the 1st string : HYDE
Enter the 2nd string : SECUN   
Result :  HSYEDCEUN
Enter the 1st string : HYDE 
Enter the 2nd string : SEC 
Result :  HSYEDCE
'''
#------------------------------------------------------------------------------------
'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M'  = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'



3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  ---> 	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  ---> Ignore  the  character

5) Hint:  Use  not  in   operator
'''
b = input("Enter the string : ")
 
out =" "
 
for x in b :
     if x not in b :
         out = out + ""

print("String without any duplicates : ", out)

'''
Output :
Enter the string : RAMA RAO
String without any duplicates : RAM O
'''
#-----------------------------------------------------------------------
# len()  function  demo  program  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('+-$')) #3
print(len('')) #0
print(len(' ')) #1
print(len('A2#')) #3
print(len(3456)) #Error, because we cannot find length of non sequence object
print('Sec'. len()) # Error, because it is function and length function cannot be called like this
#-----------------------------------------------
# chr()  function  demo  program
print(chr(65))  #  A
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z
print(chr(48)) # 0
print(chr(57)) # 9
print(chr(36)) # $
print(chr(32)) # <space>
#----------------------------------------------------------
# ord()  function  demo  program
print(ord('A')) # 65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) # 122
print(ord('0')) # 48
print(ord('9')) # 57
print(ord('$')) # 36
print(ord(' ')) # 32

#--------------------------------------------------------------
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

while (index := a.find('is', 0 if 'index' not in locals() else index + 1)) != -1:
    print(index)

print('End')
#-----------------------------------------------------------------------

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.index('is')
    while True:
        print(index)
        index = a.index('is', index + 1)
except ValueError:
    pass

print('End')

#-----------------------------------
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = a.rfind('is')

while index != -1:
    print(index)
    index = a.rfind('is', 0, index)

print('End')

#----------------------------------------------------------------

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.rindex('is')
    
    while True:
        print(index)
        index = a.rindex('is', 0, index)

except ValueError:
    pass

print('End')

#------------------------------------------------------------------

#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) # 4
print(a . count('is' , 19 , 48)) # 3
print(a . count('was')) # 0

#----------------------------------------------------------------------
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) # 3
print(a . count('\t')) #3
print(a . count('\n')) # 3










