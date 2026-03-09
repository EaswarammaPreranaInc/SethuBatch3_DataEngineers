'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''


a=input('Enter any mixed case string : ')
a=a.upper()
v='AEIOU'
result=''
for i in a:
    if i in v and i not in result:
        result = result+i
print('Distinct Vowels : ',result)