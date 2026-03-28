
# Find outputs  (Home  work)
# print( 'green'   in   'Hyd  is  green  city')#True
# print('day'   in   'Sankar  dayal  sarma')#True
# print('Green'   in   'Hyd  is  green  city')#False
# print('d  is'   in   'Hyd  is  green  city')#True
# print('dis'   in   'Hyd  is  green  city')#False
# print('iniv'   in   'Srinivas')#True
# print('iniv'   not   in   'Srinivas')#False


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
# a = 'Rama Rao'
# print(a [ : 7 : 2]) #  a[0 : 7 : 2]  --->  String  from  indexes  0  to  6  in  steps  of  2  i.e. Rm<space>a
# print(a [ : 7])  #  a[0 : 7 : 1]  --->  String  from  indexes  0  to  6  in  steps  of  1  i.e. Rama<space>Ra
# print(a [2 : 4])   #  a[2 : 4 : 1]  --->  String  from  indexes  2  to  3  in  steps  of  1  i.e. ma
# print(a [2 : ])  #  a[2 : 8 : 1]  --->  String  from  indexes  2  to  7  in  steps  of  1  i.e. ma  Rao
# print(a [ : 4 ]) #  a[0 : 4 : 1]  --->  String  from  indexes  0  to  3  in  steps  of  1  i.e. Rama
# print(a [ : : 2])  #  a[0 : 8 : 2]  --->  String  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
# print(a [-6 : -1])  #  a[-6 : -1 : 1]   --->  String  from  indexes  -6  to  -2  in  steps  of  1  i.e. ma<space>Ra
# print(a [-6 : ])  #  a[-6 : 8 : 1]  --->  String  from  indexes   -6  to  7  in  steps  of  1  i.e. ma<space>Rao
# print(a [: -4 : -1])  #  a[-1 : -4 : -1]   --->  String  from  indexes  -1  to  -3  in  steps  of  -1   i.e.  oaR
# print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  String  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
# print(a [-3 : ])  #  a[-3 : 8 : 1]  --->  String  from  indexes  -3  to  7  in  steps  of  1  i.e. Rao
# print(a [ : : ])  #  a[0 : 8 : 1]  --->  String  from  indexes  0  to  7  in  steps  of  1  i.e. Rama Rao
# print(a [ : ]) #  a[0 : 8 : 1]  --->  String  from  indexes  0  to  7  in  steps  of  1  i.e. Rama Rao
# print(a [ : : -1])  # a[-1 : -9 : -1]  --->  String  from  indexes  -1  to  -8  in  steps  of  -1  i.e.  oaR<space>amaR
# print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
# print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  String  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
# print(a [2 : 8])  #  a[2 : 8  : 1]  -->  String  from  indexes  2  to  7  in  steps  of  1  i.e. ma<space>Rao
# print(a [2 : 8 : -1]) #  String  from  indexes  2  to  9  in  steps  of  -1   i.e.  Empty  string
# print(a [ : -6 : -1])  #  a[-1 : -6 : -1]  --->  String  from  indexes   -1   to  -5   in  steps  of  -1   i.e.  oaR<space>a
# print(a [2 : -3])  #  a[2 : -3 : 1]  --->  String  from  indexes  2  to   -4   in  steps  of  1  i.e. ma<space>
# print(a [1 : 6 : 2])  #   String  from  indexes  1  to  5  in  steps  of  2  i.e. aaR
# print(a [ : -5 : -5])  #  a[-1 : -5 : -5]  --->  String  from  indexes  -1  to  -4   in  steps  of  -5    i.e. o
# print(a [2 : -5])  #  a[2 : -5 : 1]  --->  String  from  indexes  2  to  -6  in  steps  of  1  i.e. m
# print(a [2 : -5 : 2])  #  String  from  indexes  2  to  -6  in  steps  of  2  i.e. m
# print(a [ : 0 : -1])  #  a[-1 : 0 : -1]  --->  String  from  indexes  -1   to   1  in  steps  of  -1   i.e.  oaR<space>ama
# print(a [-5 : 0 : -2])  #   String  from  indexes  -5  to  1   in  steps  of  -2  i.e.aa 


'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice
'''
# a = input('Enter First String : ')
# b = input('Enter Second String : ')

# print('Result : ',b[0:2]+a[2:],a[0:2]+b[2:],sep = " ")

'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''
# x = input('Enter any string : ')
# if len(x)<4:
#     print('Result : ',' ')
# else:
#     print('Result : ',x[0:2]+x[-2:])

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
# x = input('Enter any string : ')
# print('String from left to right : ')
# for i in range(len(x)):
#       print(f'Character at index {i} : {x[i]}')
# print('String from right to left : ')
# for i in range(-1,-len(x)-1,-1):
#     print(f'Character at index {i} : {x[i]}')


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
# x = input('Enter any string : ')
# even = ""
# odd = ""
# for i in range(0,len(x),1):
#     if i%2 == 0:
#         even+=x[i]
#     else:
#            odd+=x[i]
# print('string at even indexes : ',even)
# print('string at odd indexes : ',odd)


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
# try:
# 	a = input('Enter  any  string  with  alternate  character  and  digit :  ')
# 	s = ''
# 	for  i  in   range(0 , len(a) , 2):
# 			s += a[i] * int(a[i + 1])
# 	print('Result :  ' ,  s)
# except:
# 	print('String   should  have  alternate  character  and  digit')

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
# x = input('Enter first string : ')
# y = input('Enter second string : ')
# new_string = ""
# len_new_string = x+y
# print(len_new_string)

