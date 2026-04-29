#1
'''
Repeat  prog6a  with  next()  function.

Reuse  class  c1  defined  in  prog6a  but   do  not  rewrite  class  c1  again
'''

class c1:
    def __init__(self):
        self.x=-1
    def __iter__(self):
        return self
    def __next__(self):
         self.x+=1
         if self.x==8:
             raise StopIteration
         return pow(2,self.x)
a=c1()
while True:
    try:
        print(next(a))
    except StopIteration:
        break

#2
'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''

import time 
class itr:
    def __init__(self):
        self.x = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.x > 7:
            raise StopIteration
        val =2** self.x
        self.x+=1
        return val
a = itr()
for x in a:
    print(x) 
    time.sleep(1)      


#3
#  Find  outputs (Home  work)
import  re
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string))  # ['z', 'b', 'a', 'k']
print()
print(re . findall ('[0-9]'  ,  string))  # ['7', '2', '9', '6']
print()
print(re . findall ('[^A-Za-z0-9]'  ,  string)) # ['.', '-', '$', ' ', '[', '.', '%', '$', '&', '.', '%']
print()
print(re . findall ('.'  ,  string)) # ['z', '7', '.', 'Q', '-', '$', '2', ' ', 'b', '[', '9', '.', 'a', '%', '6', '$', 'G', '&', 'k', '.', '%']
print()
print(re . findall ('[.]'  ,  string))  # ['.', '.', '.']
print()
print(re . findall ('[$]'  ,  string)) # ['$', '$']
print()
print(re . findall ('[%]'  ,  string)) # ['%', '%']
print()
print(re . findall ('[az-]'  ,  string)) # ['z', '-', 'a']



#4
''' (Home  work)
1) 1st  string --->  'Sankar  dayal  sarma'
    2nd  string ---> 'san'
    What  are  the  outputs ?  --->  Sankar  dayal  sarma starts  with  San

2) 1st  string  ---> 'Hyderabad'
    2nd  string  --->  'Sec'
    What  are  the  outputs ?  --->  Hyderabad does not start with Sec
'''
import re
string  =  input('Enter  any  string : ')
pattern = input('Enter  any pattern : ')
m  =  re . match(pattern , string , re . IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m . group())
else:
	print(string , 'does not start with' , pattern)




#5 
'''  (Home   work)
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  ---> Same  strings  after  ignoring  the  case

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  ---> Different  strings
'''
import  re
s1 = input('Enter first string  : ')
s2 = input('Enter second string  : ')
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)
if  m:
        print('Same  strings  after  ignoring  the  case')
else:
        print('Different  strings')


#6
'''
Write  a  regular  expression  to  validate  a  10-digit  mobile  number

Rules:
1) It  should  be  a  10-digit  number

2) First  digit  can  be  6 , 7 , 8  or  9

3) Number  may  start  with  0  (or)  +91
'''
import re 
num = input("Enter 10 digit number :")
m = re.fullmatch ('(0|[+]91)?[6789][0-9]{9}',num)

if m:
    print("valid")
else:
    print("Not valid")    


#7
'''
Write  a  program  to  validate  vehicle  registration  number

Rules:
1) First  2  characters  should  be  TS , ts , Ts  or  tS

2) There  are  29  circles  i.e.  01 , 02 , 03 , ......29

3) Next  two  characters  should  be  alphabets

4) Last  four  characters  should  be  digits


What  is  the  regular  expression  for  the  above  rules ? 
'''
import re 
num = input("Enter vehicle number :")
m = re.fullmatch ('[Tt][Ss](0[1-9]|1[0-9]|2[0-9])[A-Za-z]{2}[0-9]{4}',num)

if m:
    print("valid")
else:
    print("Not valid") 



#8
'''
Write  a  program  to  validate  date  i.e.  dd/mm/yyyy
'''


import re 
date = input("Enter date  :")
m = re.fullmatch ('(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/[0-9]{4}$',date)

if m:
    print("valid")
else:
    print("Not valid")  
    
      
#9
'''
Write  a  program  to validate  address

Address  format :  streetname , city ,  State - PIN code
Eg:  Khairtabad , Hyderabad , Telangana - 500004
'''


import re 
Address = input("Enter Address  :")
m = re.fullmatch ('^[A-Za-z ]+,[A-Za-z ]+,[A-Za-z ]+-[0-9]{6}$',Address)

if m:
    print("valid Adress")
else:
    print("Invalid Adress")  
    
      
#10
'''
Write  a  program  to  validate  credit card  number
import re
'''

card = input("Enter card number: ")

pattern = r'^(?:[4-6]\d{15}|[4-6]\d{3}(?:-\d{4}){3})$'

if re.fullmatch(pattern, card):
    print("Valid card")
else:
    print("Invalid card")