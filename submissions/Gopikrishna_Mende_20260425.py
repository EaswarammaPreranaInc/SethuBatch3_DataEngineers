'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
def power_of_two():
    for i in range(8):
        yield 2 ** i
for value in power_of_two():
    print(value)

# ===============================================================

#  Find  outputs (Home  work)
import  re
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string))  # ['z', 'b', 'a', 'k']
print() # space
print(re . findall ('[0-9]'  ,  string))   # [7,2,9,6]
print() # space
print(re . findall ('[^A-Za-z0-9]'  ,  string)) #['.', '-', '$', ' ', '[', '.', '%', '$', '&', '.', '%']
print() # space
print(re . findall ('.'  ,  string)) # ['z', '7', '.', 'Q', '-', '$', '2', ' ', 'b', '[', '9', '.', 'a', '%', '6', '$', 'G', '&', 'k', '.', '%']
print() # space
print(re . findall ('[.]'  ,  string))  # ['.' ,' .' , '.']
print() # space
print(re . findall ('[$]'  ,  string))  #[$,$]
print() #space
print(re . findall ('[%]'  ,  string))  # [% , %]
print() # space
print(re . findall ('[az-]'  ,  string)) # ['z','-','a']

# ============================================================

''' (Home  work)
1) 1st  string --->  'Sankar  dayal  sarma'
    2nd  string ---> 'san'
    What  are  the  outputs ?  --->

2) 1st  string  ---> 'Hyderabad'
    2nd  string  --->  'Sec'
    What  are  the  outputs ?  --->
'''
import re
string  =  input('Enter  any  string : ')  #  'Sankar  dayal  sarma'
pattern = input('Enter  any pattern : ')
m  =  re . match(pattern , string , re . IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m . group()) # san
else:
	print(string , 'does not start with' , pattern)


# ========================================

'''  (Home   work)
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  ---> same o/p

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  ---> different o/p
'''
import  re
s1 = input('Enter first string  : ')
s2 = input('Enter second string  : ')
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)
if  m:
        print('Same  strings  after  ignoring  the  case')
else:
        print('Different  strings')

# ===================================================

'''
Write  a  regular  expression  to  validate  a  10-digit  mobile  number

Rules:
1) It  should  be  a  10-digit  number

2) First  digit  can  be  6 , 7 , 8  or  9

3) Number  may  start  with  0  (or)  +91


Which  of  the  following  are  valid
----------------------------------------
a) 5948250500  --->  Invalid  becoz  first  character  '5'  is  not  between  '6'  and  '9'
b) 994825050 --->  Invalid  becoz  length  of  the  string  is  not  10
c) 9948-250500  ---> Invalid  due  to  '-'
d) 9948250500  --->  Valid
e) 09948250500  ---> Valid  becoz  number  may  start  with  '0'
f) +919948250500 ---> Valid  becoz  number  may  start  with  +91
g) 919948250500  --->  Inavlid  becoz  length  of  the   string  is  not  10

What  is  the  regular  expression  for  the  above  rules ?  --->  (0|[+]91)?[6789][0-9]{9}

2) Which  function  should  be  used ?  --->  fullmatch()  function
'''


import re

pattern = r"(0|\+91)?[6-9][0-9]{9}"

numbers = input("Enter numbers separated by space: ").split()

for num in numbers:
    if re.fullmatch(pattern, num):
        print(num, "→ Valid")
    else:
        print(num, "→ Invalid")

# =======================================================
'''
Write  a  program  to  validate  vehicle  registration  number

Rules:
1) First  2  characters  should  be  TS , ts , Ts  or  tS

2) There  are  29  circles  i.e.  01 , 02 , 03 , ......29

3) Next  two  characters  should  be  alphabets

4) Last  four  characters  should  be  digits


Which  of  the  following  is  valid
--------------------------------------
a) TS30AB1234 ---> Invalid  becoz  circle  30  does  not  exist
b) AP15CD1234  --->  Invalid  becoz  first  2  characters  can  not  be  AP
c) Ts15E1234 --->  Invalid  due  to  single  character  'E'
d) tS15FG123 --->  Invalid  due  to  3 - digit  number  123
e) ts9KP1234 --->  Invalid  due  to  single  digit  9
f) tS10LW1234  --->  Valid
g) 15XY1234  --->  Invalid  becoz  TS   is  missing
h) Ts00PQ1234  ---> Invalid  becoz  circle  00  does  not  exist
i) TS20RS1234 --->  Valid
j) Ts25TR1234 --->   Valid

What  is  the  regular  expression  for  the  above  rules ?  --->
'''
import re

pattern =  r"[Tt][Ss](0[1-9]|1[0-9]|2[0-9])[A-Za-z]{2}[0-9]{4}"

numbers = input("Enter numbers separated by space: ").split()

for num in numbers:
    if re.fullmatch(pattern, num):
        print(num, "→ Valid")
    else:
        print(num, "→ Invalid")

# ======================================================

'''
Write  a  program  to  validate  credit card  number

Rules:
1) It  must  start  with  4 , 5  (or) 6
2) It  must  be  a  16 digit  number
3) It  should  have  digits  from  0  to  9
4) It  may  have  digits  in  a  group  of  4  separated  by  one  hyphen
5) It  should  not  have  any  other  separator  like  _ ,  / , etc
'''

import re

pattern = r"[456]\d{15}|[456]\d{3}(-\d{4}){3}"

numbers = input("Enter numbers separated by space: ").split()

for num in numbers:
    if re.fullmatch(pattern, num):
        print(num, "→ Valid")
    else:
        print(num, "→ Invalid")