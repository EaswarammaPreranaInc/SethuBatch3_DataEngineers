
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'

a=input("Enter the input in uppercase :").upper()
b="AEIOU"
c=""
d=""
for ch in a:
    if ch in b:
        c+=ch
for i in c:
    if i not in d:
        d+=i
print(d)