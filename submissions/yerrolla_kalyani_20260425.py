'''
Repeat  prog6a  with  next()  function.
Reuse  class  c1  defined  in  prog6a  but   do  not  rewrite  class  c1  again
'''
import yerrolla_kalyani_20260425  as prog6a
from yerrolla_kalyani_20260425 import a ,c1
for x in a:
    print(x)

'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7
Hint :  Use  for  loop
'''
class pow_of_base:
    def __init__(self,base,limit):
           self.base=base
           self.limit=limit
           self.current=0
    def __iter__(self):
           print("__iter__ method")
           return self
    def __next__(self):
        if self.current<=self.limit:
            result=self.base**self.current
            self.current+=1
            return result
        raise  StopIteration
#end of iterator (finate iterator )
a=pow_of_base(2,7)
for x in a:
      print(x)

           
           

#  Find  outputs (Home  work)
import  re
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string))  #['z','b','a','k']
print()#nothig is printed 
print(re . findall ('[0-9]'  ,  string))  #[7,2,9,6]
print()#nothig is printed 
print(re . findall ('[^A-Za-z0-9]'  ,  string))#['.','-','$',' ','[','.','%','$','&','.','%']
print()#nothig is printed 
print(re . findall ('.'  ,  string))#['z',7,'Q','-','$',2,' ','b','[',9,'a','%',6,'$','G','&','k','%']
print()#nothig is printed 
print(re . findall ('[.]'  ,  string))  #['.','.','.']
print()#nothig is printed 
print(re . findall ('[$]'  ,  string)) #['$','$']
print()#nothig is printed 
print(re . findall ('[%]'  ,  string)) #['%','%']
print()#nothig is printed 
print(re . findall ('[az-]'  ,  string))#['z','-','a']



''' (Home  work)
1) 1st  string --->  'Sankar  dayal  sarma'
    2nd  string ---> 'san'
    What  are  the  outputs ?  --->Sankar  dayal  sarma <space> starts  with <space> 3

2) 1st  string  ---> 'Hyderabad'
    2nd  string  --->  'Sec'
    What  are  the  outputs ?  --->Sankar  dayal  sarma <space> does not start with <space> Sec
'''
import re
string  =  input('Enter  any  string : ')#Sankar  dayal  sarma
pattern = input('Enter  any pattern : ')#san
m  =  re . match(pattern , string , re . IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m . group())#Sankar  dayal  sarma <space> starts  with <space> 3
else:
	print(string , 'does not start with' , pattern)



'''  (Home   work)
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  --->Same  strings  after  ignoring  the  case

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  --->Different  strings
'''
import  re
s1 = input('Enter first string  : ')#'HYD'
s2 = input('Enter second string  : ')# 'hyd' 
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)#matcht object 
if  m:
        print('Same  strings  after  ignoring  the  case')#Same  strings  after  ignoring  the  case
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
mobile_number=input("Enter mobile number:")
r=re.fullmatch("(0|[+]91)?[6789][0-9]{9}",mobile_number)
if r:
    print("valid mobile number")
else:
    print("invalid number")



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
What  is  the  regular  expression  for  the  above  rules ?  --->'''
import re
vehicle_registration_number=input("Enter the vehicle_registration_number:")
r=re.fullmatch('(Ts|TS|tS|ts)(0[1-2]|1[0-9]|2[0-9])[A-Z]{2}[0-9]{4}',vehicle_registration_number)#even this will work r = re.fullmatch(r'[Tt][Ss](0[1-9]|1[0-9]|2[0-9])[A-Z]{2}[0-9]{4}', vehicle_registration_number)
if r:
    print("valid ")
else:
    print("invalid")
   
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

import re
date = input("Enter date (dd/mm/yyyy): ")
r=  re.fullmatch('(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/[0-9]{4}',date)
if r:
    print("Valid date")
else:
    print("Invalid date")




''''''
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
for i in range(5):
    address = input("Enter address: ")
    r=re.fullmatch('[A-Za-z ]+,[ ]*[A-Za-z ]+,[ ]*[A-Za-z ]+[ ]*-[ ]*[0-9]{6}',address)
    if r:
        print("Valid address")
    else:
        print("Invalid address")



'''
Write  a  program  to  validate  credit card  number

Rules:
1) It  must  start  with  4 , 5  (or) 6
2) It  must  be  a  16 digit  number
3) It  should  have  digits  from  0  to  9
4) It  may  have  digits  in  a  group  of  4  separated  by  one  hyphen
5) It  should  not  have  any  other  separator  like  _ ,  / , etc
# '''
import re
card_number = input("Enter credit card number: ")
m = re.fullmatch('[456][0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}',card_number)
if m:
    print("Valid card number")
else:
    print("Invalid card number")