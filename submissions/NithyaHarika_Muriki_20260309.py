'''Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
a = input("Enter string:")
l =['A','E','I','O','U']
b = ""
for x in a:
    if x in l:
        b=b+x

print(b)