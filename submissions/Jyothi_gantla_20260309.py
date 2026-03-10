'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

s = input("Enter a string: ").upper()

a = "AEIOU"
b= ""

for ch in s:
    if ch in a and ch not in b:
        b+= ch

print(b)
