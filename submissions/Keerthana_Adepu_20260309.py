#Programming Homework

'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
'''
Sample Output:

Enter any mixed case string: RamA raO
Distinct Vowels: AO
Press any key to continue...
'''

a = input('Enter any mixed case string:')
b = a.upper()
v = [65 , 69 , 73 , 79 , 85]
out = ''

for i in range(len(b)):
    if ord(b[i]) in v:
        if b[i] not in out:
            out = out + b[i]
print(out)

