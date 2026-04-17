'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
x=(input("enter the string:")).upper()
result=""
vowels='aeiouAEIOU'
for i in range(len(x)):
    if x[i] in vowels and x[i] not in result:
       result+=x[i]
print("distinct vowels:",result )

