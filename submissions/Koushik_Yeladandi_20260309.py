Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   programe 3 with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'



#Program:
vowels = ("AEIOUaeiou")
a=eval(input('Enter any mixed case string :'))
c=''
for i in a:
    if i in vowels:
        i=i.upper()
        if i not in c:
            c=c+i
print('Distinct vowels :', c)