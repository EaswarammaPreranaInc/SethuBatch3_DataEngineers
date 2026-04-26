
#Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7Hint :  Use  for  loop

class iter:
    def __init__(self):
        self.pow=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.pow += 1
        if self.pow<=7:
            return 2**self.pow
        raise StopIteration
itr=iter()
for y in itr:
    print(y)



#  Find  outputs (Home  work)
import  re
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string)) # zbak
print()
print(re . findall ('[0-9]'  ,  string))  #7296
print()
print(re . findall ('[^A-Za-z0-9]'  ,  string))#.$[.%$&%]
print()
print(re . findall ('.'  ,  string))# z7.Q-$2 b[9.a%6$G&k].%
print()
print(re . findall ('[.]'  ,  string))  # ...
print()
print(re . findall ('[$]'  ,  string)) # $$
print()
print(re . findall ('[%]'  ,  string)) #%%
print()
print(re . findall ('[az-]'  ,  string))# za-


import re
string  =  input('Enter  any  string : ')#'Sankar  dayal  sarma'
pattern = input('Enter  any pattern : ')#'san'
m  =  re . match(pattern , string , re . IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m . group())# Sankar  dayal  sarma starts with san
else:
	print(string , 'does not start with' , pattern)


import  re
s1 = input('Enter first string  : ')#'HYD'
s2 = input('Enter second string  : ')#'hyd'
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)
if  m:
        print('Same  strings  after  ignoring  the  case')#Same  strings  after  ignoring  the  case
else:
        print('Different  strings')

# Write  a  regular  expression  to  validate  a  10-digit  mobile  number

# Rules:
# 1) It  should  be  a  10-digit  number

# 2) First  digit  can  be  6 , 7 , 8  or  9

# 3) Number  may  start  with  0  (or)  +91


import re
number=input("Enter mobile number : ")
pattern='(0|[+]91)[6789][0-9]{9}'
r=re.fullmatch(pattern,number)
if r:
    print("Valid")
else:
    print("invalid")


# Write  a  program  to  validate  vehicle  registration  number
# Rules:
# 1) First  2  characters  should  be  TS , ts , Ts  or  tS
# 2) There  are  29  circles  i.e.  01 , 02 , 03 , ......29
# 3) Next  two  characters  should  be  alphabets
# 4) Last  four  characters  should  be  digits
import re
veh_num=input("Enter vehicle number : ")
pattern='[Tt][Ss]([0][1-9]|[0-2][0-9])[a-zA-Z]{2}[0-9]{4}'
v=re.fullmatch(pattern,veh_num)
if v:
    print("Valid vehicle")
else:
    print("Invalid vehicle")

# Write  a  program  to  validate  date  i.e.  dd/mm/yyyy

# 1) What  is  the  valid  character  after  '0'  in  the  date ?  ---> 1  to  9
#     What  is  the  valid  character  after  '1'  in  the  date ?  --->  0  to  9
#     What  is  the  valid  character  after  '2'  in  the  date ?  ---> 0  to  9
#     What  is  the  valid  character  after  '3'  in  the  date ?  ---> 0  (or)  1

import re
date=input("Enter date(dd/mm/yyyy) : ")
valid='([0][1-9]|[12][0-9]|[3][01])[/]([0][1-9]|[1][012])[/][0-9]{4}'
d=re.fullmatch(valid,date)
if d:
    print("Valid date")
else:
    print("Not valid")


