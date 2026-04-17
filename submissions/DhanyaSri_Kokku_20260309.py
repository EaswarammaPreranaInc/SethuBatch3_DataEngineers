'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
# Code :
s = input("Enter any mixed case string :  ")
vowels = "AEIOU"
s = s.upper()
res = ''
for ch in s:
    if ch in vowels and ch not in res:
        res+=ch
print("Distinct vowels  :  ",res)

''' Output:
Enter any mixed case string :  RamA raO
Distinct vowels  :   AO
'''