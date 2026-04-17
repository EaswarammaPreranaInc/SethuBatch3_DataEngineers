'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

a = input('Enter any mixed case string : ')
a = a.upper()
b = ''
v = ['A', 'E', 'I', 'O', 'U']

for ch in a:
    if ch in v and ch not in b:
        b += ch
print(b)