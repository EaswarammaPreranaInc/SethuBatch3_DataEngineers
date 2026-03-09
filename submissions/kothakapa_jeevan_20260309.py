
'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

a = 'sAenigfd'
b = 'AEIOU'
u = a.upper()
d =''
for i in range(len(u)):
    if u[i] in b:
        if u[i] not in d:
            d += u[i]
print(d)