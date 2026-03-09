'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

x = input('Enter any mixed case string : ')  # Enter any mixed case string : RamA raO

x = x.upper()

v = ''
for ch in x:
    if ch in 'AEIOU' and ch not in v:
        v += ch

print('Distinct Vowels :', v)  # Distinct Vowels : AO