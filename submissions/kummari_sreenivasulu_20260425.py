'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''

class g1:
    def __init__(self,b=0):
        self.x=2
        self.b=b
    def __iter__(self):
        return self
    def __next__ (self):
        if self.b <7:
            value = self.x ** self.b
            self.b += 1
            return value
        else:    
            raise StopIteration
        
a = g1()
for i in a:
    print(i)


#  Find  outputs (Home  work)
import  re
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string))  
print() --> ['z', 'b', 'a', 'k']
print(re . findall ('[0-9]'  ,  string))  
print() --> ['7', '2', '9', '6']
print(re . findall ('[^A-Za-z0-9]'  ,  string))
print() --> ['.', '-', '$', ' ', '[', '.', '%', '$', '&', '.', '%']
print(re . findall ('.'  ,  string))
print() --> ['z', '7', '.', 'Q', '-', '$', '2', ' ', 'b', '[', '9', '.', 'a', '%', '6', '$', 'G', '&', 'k', '.', '%']
print(re . findall ('[.]'  ,  string))  
print() --> ['.', '.', '.']
print(re . findall ('[$]'  ,  string)) 
print() --> ['$','$']
print(re . findall ('[%]'  ,  string)) 
print() --> ['%', '%']
print(re . findall ('[az-]'  ,  string))
print() --> ['z', '-', 'a']






''' (Home  work)
1) 1st  string --->  'Sankar  dayal  sarma'
    2nd  string ---> 'san'
    What  are  the  outputs ?  ---> 'san' starts with san
				     'san', does not starts with san

2) 1st  string  ---> 'Hyderabad'
    2nd  string  --->  'Sec'
    What  are  the  outputs ?  ---> 'sec' does not starts with sec
				     'sec', does not end with sec
'''
import re
string  =  input('Enter  any  string : ')
pattern = input('Enter  any pattern : ')
m  =  re . match(pattern , string , re . IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m . group())
else:
	print(string , 'does not start with' , pattern)





'''  (Home   work)
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  ---> hyd

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  ---> None
'''
import  re
s1 = input('Enter first string  : ')
s2 = input('Enter second string  : ')
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)
if  m:
        print('Same  strings  after  ignoring  the  case')
else:
        print('Different  strings')

import re

pattern = r"(0|\+91)?[6-9][0-9]{9}"

numbers =[
    "5948250500",
    "994825050",
    "9948-250500",
    "9948250500",
    "09948250500",
    "+919948250500",
    "919948250500"
]

for num in numbers:
    if re.fullmatch(pattern, num):
        print(num, "Valid")
    else:
        print(num, "Invalid")



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

import re

pattern = r"(?i)TS(0[1-9]|1[0-9]|2[0-9])[A-Z]{2}[0-9]{4}"

tests = [
    "TS30AB1234",
    "AP15CD1234",
    "Ts15E1234",
    "tS15FG123",
    "ts9KP1234",
    "tS10LW1234",
    "15XY1234",
    "Ts00PQ1234",
    "TS20RS1234",
    "Ts25TR1234"
]
for t in tests:
	if re.fullmatch(pattern, t):
		print(t, "Valid")
	else:
		print('Invalid')




'''
Write  a  program  to  validate  date  i.e.  dd/mm/yyyy

1) What  is  the  valid  character  after  '0'  in  the  date ?  ---> 1  to  9
    What  is  the  valid  character  after  '1'  in  the  date ?  --->  0  to  9
    What  is  the  valid  character  after  '2'  in  the  date ?  ---> 0  to  9
    What  is  the  valid  character  after  '3'  in  the  date ?  ---> 0  (or)  1

2) Is  0  mandatory  for  single  digit  date ?  ---> No  and  it  is  optional

3) What  is  the  valid  character  after  '0'  in  the  month ?  --->  1  to  9
    What  is  the  valid  character  after  '1'  in  the  month ?  --->  0  to  2

4) Is  0  mandatory  for  single  digit  month ?  --->   No  and  it  is  optional

5) Which  of  the  following  are  valid ?
     a) 00/05/2025  --->  Invalid  due  to  date  00
     b) 0/12/2025  ---> Invalid  due  to  date  0
     c) 32/8/2025  ---> Invalid  due  to  date  32
     d) 07/13/2025  --->  Invalid  due  to  month  13
     e) 15/00/2025  --->	 Invalid  due  to  month  00
     f) 25/12/25  ---> Invalid  due  to  year  25
	 g) 15-8-1947  ---> Invalid  due  to  -
    h) 15.8.1947  ---> Invalid  due  to  '.'
'''

import re

pattern = r"(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/[0-9]{4}"

dates = [
    "00/05/2025",
    "0/12/2025",
    "32/8/2025",
    "07/13/2025",
    "15/00/2025",
    "25/12/25",
    "15-8-1947",
    "15.8.1947",
    "15/8/1947",
    "07/05/2025"
]

for d in dates:
	if re.fullmatch(pattern,d):
		print(d,'Valid')
	else:
		print(d,'Invalid')



'''
Write  a  program  to validate  address

Address  format :  streetname , city ,  State - PIN code
Eg:  Khairtabad , Hyderabad , Telangana - 500004

Rules:
1) street name  should  have  alphabets  (or)  spaces
2) ,  is   mandatory  between  street  name  and  city
3) City  name  should  have  alphabets  (or)  spaces
4) ,  is   mandatory  between  city  and  state
5) State  name  should  have  alphabets  (or)  spaces
6) -  is  mandatory  between  state  and  pincode
7) Pincode should  be  a  six-digit  number
'''

import re

pattern = r"[A-Za-z ]+,[ ]*[A-Za-z ]+,[ ]*[A-Za-z ]+[ ]*-[ ]*\d{6}"

addresses = [
    "Khairtabad, Hyderabad, Telangana - 500004",
    "Ameerpet,Hyderabad,Telangana-500016",
    "123Street, Hyderabad, Telangana - 500004",
    "Khairtabad Hyderabad Telangana - 500004",
    "Khairtabad, Hyderabad, Telangana - 50004"
]

for addr in addresses:
    print(addr, "Valid" if re.fullmatch(pattern, addr) else "Invalid")




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

pattern = r"((4|5|6)\d{15})|((4|5|6)\d{3}(-\d{4}){3})"

cards = [
    "4123456789123456",
    "5123-4567-8912-3456",
    "61234-567-8912-3456",
    "7123456789123456",
    "4123_4567_8912_3456",
    "412345678912345"
]

for c in cards:
    print(c, "Valid" if re.fullmatch(pattern, c) else "Invalid")

