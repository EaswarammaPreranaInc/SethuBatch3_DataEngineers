#Programming Homework
'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''



a = input('Enter any mixed case string:')
b = a.upper()
v = 'AEIOU'
out = ''

for i in range(len(b)):
    if b[i] not in out and b[i] in v :
        out =out + b[i]
print(out)      
