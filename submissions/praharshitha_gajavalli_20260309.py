'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'

Sample output:
Enter any mixed case string : RamA raO
Distinct Vowels : AO
Press any key to continue . . .
'''

s = input('Enter any mixed case string: ')
s = s.upper()        # convert string to uppercase
vowels = 'AEIOU'
result = ''
for ch in s:
    if ch in vowels and ch not in result:
        result += ch
print('Distinct Vowels :', result)