'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

a=input("Enter any mixed case string: ")
a=a.upper()
ans=set()
for i in a:
    if(i=='A' or i=='E' or i=="O" or i=='U' or i=='I'):
        ans.add(i)
print("Distinct vowels ",*ans)