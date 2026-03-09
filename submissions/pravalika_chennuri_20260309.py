'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
a = input("enter a string : ")
output = ""
for i in a.upper():
    if i not in output and (i == 'A' or i == 'E' or i== 'I' or i == 'O' or i == 'U'):
        output += i
print("DISTINCT VOWELS : ", output)