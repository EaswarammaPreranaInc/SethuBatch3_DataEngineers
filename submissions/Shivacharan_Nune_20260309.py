'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
#--------------------------------------------------------------------------------
n=input("enter a string :")
s="AEIOU"
n=n.upper()
k=""
for i in n:
    if i in s and i not in k:
       k=k+i
print(k)