'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

s=input('Enter any mixed case string: ')
vowel_string='AEIOU'
s=s.upper()
distinct_vowels=""
for x in s:
    if x in vowel_string and x not in distinct_vowels:
        distinct_vowels=distinct_vowels+x 
print(distinct_vowels)

output:
Enter any mixed case string: RamA raO
AO