'''
Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import   Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''
from  Rational_Program import rat

a=rat()
b=rat()
c=rat()

c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)


'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5] '''

a=[0]*5
for i in range(3):
    a[i]=rat()

a[2]=a+b
a[3]=a-b
a[4]=a*b
print('Sum :  ' , a[2])
print('Difference :  ' , a[3])
print('Product :  ' ,  a[4])


