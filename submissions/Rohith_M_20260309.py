'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
#----------------------------------------
a= input("Enter a string: ")#Rama rAo
x= "AEIOU"
b= a.upper()
c= ""
for ch in b :
    if ch in x:
        if ch not in c:
            c+= ch
print("Distinct vowels: ", c)