'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

a = input('Enter any mixed case String : ')

a = a.upper()

out = ''

for x in a:
    if (x in 'AEIOU') and (x not in out):
        out = out + x
        
print('Distinct vowels : ',out)

'''
Output :
Enter any mixed case String : 'Rama Rao'
Distinct vowels :  AO

PS D:\SSSSDP\Homeworks> py o1.py
Enter any mixed case String : navAnEetH
Distinct vowels :  AE
'''
