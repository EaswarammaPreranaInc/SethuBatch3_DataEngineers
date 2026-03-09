'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set
1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO
2) Hint  1:  Same  as   prog3e  with  minor  changes
3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

n=input("enter any string:")

s=n.upper()
result=""

for i in s:
    if i in "AEIOU" and i not in result:
        result=result+i
print(result)



