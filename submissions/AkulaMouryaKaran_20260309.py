'''
1) Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set
    Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO
'''
a = input('Enter any mixed case string : ')
a = a.upper()
out = ''
for x in a:
    if x in 'AEIOU' and x not in out:
        out += x
print('Distinct Vowels :', out)