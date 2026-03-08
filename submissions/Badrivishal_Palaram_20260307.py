# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')#True
print('day'   in   'Sankar  dayal  sarma')#True
print('Green'   in   'Hyd  is  green  city')#False
print('d  is'   in   'Hyd  is  green  city')#True
print('dis'   in   'Hyd  is  green  city')#True
print('iniv'   in   'Srinivas')#True
print('iniv'   not   in   'Srinivas')#False

'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
Code                 
 print(a[:7:2])#RmaR
 print(a[:7])#Rama Ram
 print(a[2:4])#ma
 print(a[2:])#ma Rao
 print(a[:4])#Rama  
 print(a[::2])#RmaR            
 print(a[-6:-1])#ma Ra           
 print(a[-6:])#ma Rao          
 print(a[:-4:-1])#oar             
 print(a[-3:-1])#Ra             
 print(a[-3:])#Rao             
 print(a[::])#Rama Rao        
 print(a[:])#Rama Rao        
 print(a[::-1])#oaR amaR        
 print(a[::-2])#oRmR         
print(a[-2::-2])#a a             
 print(a[2:8])#ma Rao          
 print(a[2:8:-1])#(empty string) 
 print(a[:-6:-1])#oaR a          
 print(a[2:-3])#ma              
 print(a[1:6:2])#aaR             
 print(a[:-5:-5])#o              
 print(a[2:-5])#m               
 print(a[2:-5:2])#m           
 print(a[:0:-1])#oaR ama         
 print(a[-5:0:-2])#aa             




'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice
'''
x=input("enter first input:")
y=input("enter second input:")

a= y[0:2]+ x[2:]
b= x[0:2]+ y[2:]

print(a,b)



'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''

x=input("enter first input:")
y=input("enter second input:")

a= y[0:2]+ x[2:]
b= x[0:2]+ y[2:]

print(a,b)


'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		                  V      A     M      S     I
			        	 -5     -4    -3     -2    -1

What  are  the  outputs ?  ---> 
 Character  at  index  0  :  V
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
x=input("enter the string:")

for i in range(0,len(x)):
 print("character at index:",i,x[i])
for i in range(-1,-len(x),-1):
 print("character at index:",i,x[i])

		



'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

		 					 0      1      2      3     4     5     6      7
Let  input  be                                           R      a      m      a           R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' = 'Rm a'

1) What  action  to  be  made  when  index  is  even ?  ---> Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  --->  Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop
'''
x=input("enter a string:")

x=input("enter a string:")
even=""
odd=""

for i in range(0,len(x)):
	if i%2==0:
		even=even+x[i]
	else:
		odd=odd+x[i]

print("even indexed characters:",even)
print("odd indexed characters:",odd)





'''
Let  input  be    A   4   B   3   C   2   $   5
                  0   1   2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  ---> 'AAAA'

2)  i        a[i]       a[i + 1]          out
   -------------------------------------------------------
                                               ''
        0         'A'          '4'	       '' + 'A' * 4 = 'AAAA'
	2         'B'          '3'             'AAAA' +  'B' * 3  = 'AAAABBB' 
	4         'C'          '2'             'AAAABBB' +  'C' * 2  = 'AAAABBBCC' 
	6         '$'          '5'             'AAAABBBCC' +  '$' * 5  = 'AAAABBBCC$$$$$' 
   -------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  --->  a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
'''

a=input("enter any string:")
b=""
for i in range(0,len(a),2):
	b=b + a[i]*int(a[i+1])
print(b)



'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  ---> HVYADMSI

          0     1    2
a  --->   H     Y    D

           0    1    2    3    4
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
x=input("enter 1st string:")
y=input("enter 2nd string:")

i=0
result=""

while i<len(x) and len(y):
	result=result+x[i:i+1]+y[i:i+1]
	i+=1
	
result = result + x[i:] + y[i:]
print(result)




'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O
2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M'  = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'
3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  ---> 	Concatenate  the  character  to  out  object
4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  ---> Ignore  the  character
5) Hint:  Use  not  in   operator
'''
x=input("enter a string:")

out=""

for ch in x:
	if ch not in out:
		out=out+ch
print(out)


# len()  function  demo  program  (Home  work)
print(len('Hyd')) #3
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len('+-$'))#3
print(len(''))#0
print(len(' '))#1
print(len('A2#'))#3
print(len(3456))#error, int has no len
print('Sec'. len())#syntax error


'''
What  does  len(string)  do  ?  --->  Returns  number  of  characters  in  the  string
'''



# chr()  function  demo  program
print(chr(65))#A
print(chr(90))#Z
print(chr(97))#a
print(chr(122))#z
print(chr(48))#0
print(chr(57))#9
print(chr(36))#$
print(chr(32))#_
'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''



# ord()  function  demo  program
print(ord('A'))#65
print(ord('Z'))#90
print(ord('a'))#97
print(ord('z'))#122
print(ord('0'))#48
print(ord('9'))#57
print(ord('$'))#36
print(ord(' '))#32



'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A     4     M     3    Z    5    D     2


    i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                           ''
   0        'A'        '4'             '' + 'A' +  'E' = 'AE'
   2        'M'        '3'             'AE' + 'M' +  'P' = 'AEMP'
   4        'Z'        '5'             'AEMP' + 'Z' +  '_' = 'AEMPZ_'
   6        'D'        '2'             'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'															 
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions
'''
a = input("Enter the string: ")
out = ""
for i in range(0, len(a), 2):
    ch = a[i]
    num = int(a[i+1])
    new_char = chr(ord(ch) + num)
    out = out + ch + new_char

print(out)




'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while (index:=a.find('is',index+1))!=-1
	print(index)
print('End')


'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
j=a(index('is'))
while  j != -1:
	print(j)
	j = a . find('is' , j + 1)
print('End')
	
'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  raises   error (but  not  -1) when  string  is  not  found
Syntax :  Same  as   find()  method
'''




'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = rfind('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

'''
rfind()  method
-------------------
1) What  does  str1 . rfind(str2 , x , y)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  y - 1  downto  x i.e. right  to  left
2) What  does  str1 . rfind(str2)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  len(str1) - 1  downto  0 i.e. right  to  left
3) What  does  str1 . rfind(str2 , x)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  x  to  len(str1) - 1 i.e.  left  to  right
4) How  many  arguments  can  rfind()  method  take ?  --->  1 (or) 3  but  not  2
5) What  is  the  issue  with  two  arguments ?  ---> Method  searches  from  left  to  right  even  though  it  is  rfind()  method
6) What  does  rfind()  method  return  (+ve  (or)  -ve  index) ?  ---> +ve  index  even  though  search  is  from  right  to  left
7) What  does  rfind()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1


'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method
Hint: Use   try  and  except

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')'''


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = len(a)
try:
    while True:
        index = a.rindex('is', 0, index)
        print(index)
except ValueError:
    print('End')

'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
'''




#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))#4
print(a . count('is' , 19 , 48))#3
print(a . count('was'))#0


'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  in  str1
2) What  does  str1 . count(str2 , x , y)  do ? --->	Returns  number  of  times  str2  is  in  str1  between  indexes  x  and  y - 1
																		
'''





#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))#0
print(a . count('\t'))#3
print(a . count('\n'))#2


#isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())#False
print('\n  \t' . isspace())#True
print('\n  7\t' . isspace())#False
print('\n' . isspace())#True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace())#True
print('' . isspace())  #  False
print(' ' . isspace())#True


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character
2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  not  a  white  space
(i.e.  Alphabet, digit (or)  special  character)
		(or)
When  there  are  no  white  space  characters'''




# islower()  method  demo  program  (Home  work)
print('hyD' . islower())#False
print('hyd' . islower())#True
print('9247' . islower())False
print('rama  rao' . islower())#True
print('+-$' . islower())#False
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower())#False
print('a2#' . islower())#True


'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  ---> When  at  least  one  character  of  the  string  is  uppercase  alphabet
										(or)											 				  When  there  are  no  lowercase  alphabets  in  the  string
2) When  does  it  return  True ?  -------------> When  there  are  no  uppercase  alphabets  in  the  string
								and
				                  at  least  one  character  is  lowercase  alphabet


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)#a  :  25<tab space>b  :  10.8<tab space>c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)))#a  :  25<tab space>b  :  10.8<tab space>c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)))#a  :  Hyd<tab space>b  :  10.8<tab space>c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)))#a  :  Hyd<tab space>b  :  Hyd<tab space>c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)))#a  :  25<tab space>b  :  10.8<tab space>c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)))#a  :  Hyd<tab space>b  :  10.8<tab space>c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)))#a  :  25<tab space>b  :  25<tab space>c  :  25

'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet
2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet
3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character
4) What  is  the  output  if  input  is  '$' ?  ---> Special  character
5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space
6) What  is  the  output  if  input  is  <tab>  key ?  ---> White  space
7) What  is  the  output  if  input   is   <enter>   key ?  --->White  space
8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods
9) Hint2:  Use  nested  if  and   elif

x=input("enter any input:")

if x.isdigit():
	print("digit")
elif x.isalpha():
	print("alpha numeric character")
	if x.isupper():
		print("Upper class alphabet")
	else:
		print("lower case alphabet")
elif x.isspace():
	print("Space")
else:
	print("special character")

	
'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  --->  dyH

2)   H       y      d
     -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1        'd'             '' + 'd' = 'd'								
     2       'y'             'd' + 'y' = 'dy'								
     3       'H'            'dy' + 'H' = 'dyH'								
  ---------------------------------------------
'''

x=input("enter a string:")

y=""

for i in range(1,len(a)+1)
	b=b+a[-i]
print(b)



'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
    1        'city'        '' + 'city' + ' ' = 'city '							  
    2        'green'     'city ' + 'green' + ' ' = 'city green '							  
    3        'is'            'city green ' + 'is' + ' ' = 'city green is '							  
    4        'Hyd'        'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '							  
   -------------------------------------------------------
'''
a = input("Enter a sentence: ")

b = a.split()
c = ""

for i in range(1, len(b) + 1):
    c = c + b[-i] + " "

print(c)


'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
x=str(input("enter any string"))
y=" "
for i in range(0,len(x)+1):
	y=x[::-1]
print(y)




'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
x=input("enter any string:")

y=list(x)

y.sort()

z=''

for ch in y:
	z=z+ch
print(z)	



'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'

x=input("enter string with nums and alphabets:")

y=""
z=""

for ch in x:
	if ch.isalpha():
		y=y+ch
	elif ch.isnumeric():
		z=z+ch
y="".join(sort(y))
z="".join(sort(z))

'''
