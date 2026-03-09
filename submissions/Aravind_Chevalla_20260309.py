'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

a=input("Enter mixed case String:")
b="A,E,I,O,U"
c=a.upper()
d=""
for i in range(len(c)):
        if c[i]in b:
          if c[i] not in d:
              d+=c[i]
print("Distinct vowels= ",d)