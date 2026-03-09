
'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

cha = input("Enter Alphabets:")
empty=''
voewl=''
for i in cha:
    if (i == 'A' ):
        if i not in voewl:
            voewl+=i
    elif (i== 'E' ):
        if i not in voewl:
            voewl+=i
    elif i=='I':
        if i not in voewl:
            voewl+=i
    elif i== 'U':
        if i not in voewl:
            voewl+=i
    elif (i== 'O'):
        if i not in voewl:
            voewl+=i
     
        
print(voewl)


'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''


'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''

alpha = input("Enter Alphabets and digits alternate :")
empty =''
digits =''

for i in range(0,len(alpha),2):
	empty+=alpha[i]
for i in range(1,len(alpha),2):
    digits +=alpha[i]
result = empty+digits
print(result)



















