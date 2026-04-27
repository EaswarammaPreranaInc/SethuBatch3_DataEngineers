import  re
cred=input("enter the credit card number : ")
res=re.fullmatch('[4-6][0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}',cred)
if res:
        print("valid credit card: ",cred)
        exit()
else:
        print("invalid credit card: ",cred)
        exit()

add=input("  Address  format :  streetname , city ,  State - PIN code\nenter the address : ")
res=re.fullmatch('[a-zA-Z ]*[,][a-zA-Z ]*[,][a-zA-Z ]*[-][0-9]{6}',add)

if res:
        print("valid address: ",add)
        exit()
else:
        print("invalid address: ",add)
        exit()
d=input("enter the date (dd/mm/yyyy) : ")
res=re.fullmatch('([0]?[1-9]|1[0-9]|[2][0-9]|[3][0-1])[/](0?[1-9]|1[0-2])[/][1-9][0-9]{3}',d)
if res:
        print("valid date: ",d)
        exit()
else:
        print("invalid date: ",d)
        exit()

pn=input("enter vechicle number : ")
res=re.fullmatch('(TS|ts|Ts|tS)(0[1-9]|[1-2][0-9])[A-Za-z]{2}[0-9]{4}',pn )
if res:
        print("valid vechicle number : ",pn)
        exit()
else:
        print("invalid vechicle number : ",pn)
        exit()
        
n=input("enter the phone number")
res=re.fullmatch('(0|[+]91)?[6789][0-9]{9}',n)
if res:
        print(f"{n} number is valid")
        exit()
else:
         print(f"{n} number is not valid")
         exit()
        
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string))# ['a','b','k']
print()
print(re . findall ('[0-9]'  ,  string)) #['9','7','2','6']
print()
print(re . findall ('[^A-Za-z0-9]'  ,  string)) #['.','-','$','[','$','&','.','%']
print()
print(re . findall ('.'  ,  string)) #['z','7','.','Q','-','$','2',' ','b','[','9','.','a','%','6','$','G','&','k','.','%']
print()
print(re . findall ('[.]'  ,  string)) #['.','.','.']
print()
print(re . findall ('[$]'  ,  string))  #['$','$']
print()
print(re . findall ('[%]'  ,  string))   #['%','%']
print()
print(re . findall ('[az-]'  ,  string)) #['a','z','-']


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
	print(string  ,  'starts  with ' , m . group())
else:
	print(string , 'does not start with' , pattern)
'''
Sankar  dayal  sarma   starts  with   San
Hyderabad  does not start with  pattern Sec

'''

'''  (Home   work)
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  ---> same string after ignoring the case

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  ---> different strings
'''
import  re
s1 = input('Enter first string  : ')
s2 = input('Enter second string  : ')
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)
if  m:
        print('Same  strings  after  ignoring  the  case')
else:
        print('Different  strings')