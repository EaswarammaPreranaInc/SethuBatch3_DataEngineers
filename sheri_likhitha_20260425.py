def powers_of_two():
    for i in range(8):   # 0 to 7
        yield 2 ** i

# Using the iterator
for value in powers_of_two():
    print(value)




#  Find  outputs (Home  work)
import  re
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string))	#['z','b','a','k']  
print()
print(re . findall ('[0-9]'  ,  string)) 	#['7','2','9','6'] 
print()
print(re . findall ('[^A-Za-z0-9]'  ,  string))	#except letters and digits it matches with other objects
print()
print(re . findall ('.'  ,  string))	#matches any character except new line
print()
print(re . findall ('[.]'  ,  string))	#matches only the dot character  
print()
print(re . findall ('[$]'  ,  string))	#matches only $  
print()
print(re . findall ('[%]'  ,  string))	#matches only % 
print()
print(re . findall ('[az-]'  ,  string)) #finds the characters in string







''' (Home  work)
1) 1st  string --->  'Sankar  dayal  sarma'
    2nd  string ---> 'san'
    What  are  the  outputs ?  --->

2) 1st  string  ---> 'Hyderabad'
    2nd  string  --->  'Sec'
    What  are  the  outputs ?  --->
'''
import re
string  =  input('Enter  any  string : ')
pattern = input('Enter  any pattern : ')
m  =  re . match(pattern , string , re . IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m . group())	#sankar dayal sarma starts with san
else:
	print(string , 'does not start with' , pattern)	#hyderabad does not start with sec







'''  (Home   work)
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  --->

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  --->
'''
import  re
s1 = input('Enter first string  : ')
s2 = input('Enter second string  : ')
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)
if  m:
        print('Same  strings  after  ignoring  the  case')	#exectes this lline for first input
else:
        print('Different  strings') 	#executes for second line





import re

# Read input from user
mobile = input("Enter mobile number: ")

# Regular expression
pattern = r'(0|\+91)?[6-9]\d{9}'

# Validate using fullmatch
m = re.fullmatch(pattern, mobile)

if m:
    print("Valid mobile number")
else:
    print("Invalid mobile number")





import re

date = input("Enter date (dd/mm/yyyy): ")

pattern = r'(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/[0-9]{4}'

m = re.fullmatch(pattern, date)

if m:
    print("Valid date")
else:
    print("Invalid date")




import re

address = input("Enter address: ")

pattern = r'[A-Za-z ]+,\s*[A-Za-z ]+,\s*[A-Za-z ]+\s*-\s*[0-9]{6}'

m = re.fullmatch(pattern, address)

if m:
    print("Valid address")
else:
    print("Invalid address")





import re

card = input("Enter credit card number: ")

pattern = r'([456][0-9]{15})|([456][0-9]{3}(-[0-9]{4}){3})'

m = re.fullmatch(pattern, card)

if m:
    print("Valid credit card number")
else:
    print("Invalid credit card number") 