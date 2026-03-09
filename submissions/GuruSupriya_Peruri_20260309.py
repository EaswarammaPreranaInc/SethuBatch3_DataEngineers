'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
st=input('Enter any String : ')
st=st.upper()
out=''
for i in st:
    if (i in 'AEIOU') and (i not in out):
        out+=i
print('Result :',out)
