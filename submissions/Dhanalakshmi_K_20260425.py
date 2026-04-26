'''
Repeat  prog6a  with  next()  function.

Reuse  class  c1  defined  in  prog6a  but   do  not  rewrite  class  c1  again
'''
import re
import prog6a
identifier = input("Enter any Identifier: ")
matches = iter([re.fullmatch('[a-k][0369][A-Za-z0-9#]*', identifier)])
try:
    # Use next() to get the match object
    m = next(matches)
    if m:
        print("Valid")
    else:
        print("Invalid")
except StopIteration:
    print("Invalid")


'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
class c1:
    def __init__(self):
        self.n=0

    def __iter__(self):
        print('__iter__ method')
        return self   

    def __next__(self):
        if self.n <= 7:
            value = 2**self.n
            self.n += 1
            return value
        else:
            raise StopIteration
itr = c1()
for value in itr:
    print(value)
print('End')


#  Find  outputs (Home  work)
import  re
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string))  #['z','b','a','k']
print()
print(re . findall ('[0-9]'  ,  string))  #[7,2,9,6]
print()
print(re . findall ('[^A-Za-z0-9]'  ,  string))
print()
print(re . findall ('.'  ,  string))#['z','7','.','Q','-','$','2',' ','b','[','9','.','a','%','6','$','G','&','k','.','%']
print()
print(re . findall ('[.]'  ,  string)) #['.','.','.']
print()
print(re . findall ('[$]'  ,  string)) #['$','$']
print()
print(re . findall ('[%]'  ,  string)) #['%','%']
print()
print(re . findall ('[az-]'  ,  string))#['z','-','a']


''' (Home  work)
1) 1st  string --->  'Sankar  dayal  sarma'
    2nd  string ---> 'san'
    What  are  the  outputs ?  --->Sankar  dayal  sarma starts with San

2) 1st  string  ---> 'Hyderabad'
    2nd  string  --->  'Sec'
    What  are  the  outputs ?  --->Hyderabad does not start with Sec
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
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  --->Same  strings  after  ignoring  the  case

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  --->Different  strings
'''
import  re
s1 = input('Enter first string  : ')
s2 = input('Enter second string  : ')
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)
if  m:
        print('Same  strings  after  ignoring  the  case')
else:
        print('Different  strings')


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

pattern = r'(0|\+91)?[6789][0-9]{9}'

mobile_number = input("Enter mobile number: ")

if re.fullmatch(pattern, mobile_number):
    print(f"{mobile_number} ---> Valid")
else:
    if mobile_number and mobile_number[0] not in '06789+':
        print(f"{mobile_number} ---> Invalid becoz first character '{mobile_number[0]}' is not between '6' and '9'")
    elif mobile_number and mobile_number[0] == '0' and len(mobile_number) != 11:
        print(f"{mobile_number} ---> Invalid becoz length of the string is not 11")
    elif mobile_number and mobile_number[0] == '+':
        if len(mobile_number) != 13:
            print(f"{mobile_number} ---> Invalid becoz length of the string is not 13")
        else:
            print(f"{mobile_number} ---> Invalid")
    elif len(mobile_number) != 10:
        print(f"{mobile_number} ---> Invalid becoz length of the string is not 10")
    else:
        print(f"{mobile_number} ---> Invalid due to special characters")



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

What  is  the  regular  expression  for  the  above  rules ?  --->^[TtsS]{2}[0-2][0-9][A-Z][A-Z][0-9]{4}$
'''
import re
pattern = r'(?i)^TS(0[1-9]|1[0-9]|2[0-9])[A-Z]{2}[0-9]{4}$'
def validate_registration(reg_num: str) :
    return bool(re.match(pattern, reg_num))
reg_num = input("Enter a vehicle number: ")
if validate_registration(reg_num):
    print("Valid vehicle registration number.")
else:
    print("Invalid vehicle registration number.")



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
     e) 15/00/2025  --->	Invalid  due  to  month  00
     f) 25/12/25  ---> Invalid  due  to  year  25
	 g) 15-8-1947  ---> Invalid  due  to  -
    h) 15.8.1947  ---> Invalid  due  to  '.'
'''
import re
from datetime import datetime

# Regex pattern for dd/mm/yyyy with optional leading zeros
pattern = r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/([0-9]{4})$'

def validate_date(date: str) -> str:
    # Check separator
    if "-" in date:
        return f"{date} ---> Invalid due to '-'"
    if "." in date:
        return f"{date} ---> Invalid due to '.'"

    match = re.match(pattern, date)
    if not match:
        return f"{date} ---> Invalid format or range"

    day, month, year = map(int, date.split("/"))

    # Specific invalid cases
    if day == 0:
        return f"{date} ---> Invalid due to date 00"
    if month == 0:
        return f"{date} ---> Invalid due to month 00"
    if year < 1000 or year > 9999:
        return f"{date} ---> Invalid due to year {year}"

    try:
        datetime.strptime(date, "%d/%m/%Y")
        return f"{date} ---> Valid"
    except ValueError:
        return f"{date} ---> Invalid due to calendar rules"

# Interactive input
user_date = input("Enter a date in dd/mm/yyyy format: ")
print(validate_date(user_date))



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

pattern = r'^[A-Za-z ]+,\s*[A-Za-z ]+,\s*[A-Za-z ]+\s*-\s*[0-9]{6}$'

def validate_address(address: str) -> bool:
    return bool(re.match(pattern, address))

address = input("Enter an address (street, city, state - pincode): ")

if validate_address(address):
    print("Valid address format")
else:
    print("Invalid address format")



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

pattern = r'^[4-6][0-9]{15}$|^[4-6][0-9]{3}(-[0-9]{4}){3}$'

def validate_credit_card(card_num: str) -> bool:
    return bool(re.match(pattern, card_num))

card_num = input("Enter a credit card number: ")

if validate_credit_card(card_num):
    print("Valid credit card number")
else:
    print("Invalid credit card number")