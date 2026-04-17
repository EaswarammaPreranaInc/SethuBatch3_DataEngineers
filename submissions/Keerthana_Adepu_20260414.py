#1
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
from rational import rat
a = rat()
b = rat()
c = rat()

a.get()
b.get()

c.add(a , b)
print('Sum:', c)

c.sub(a , b)
print('Difference:', c)

c.mul(a , b)
print('Product:', c)

c.div(a , b)
if b.nr != 0:
    print('Division:', c)
else:
    print('Division is not permitted')



#2
'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from rational import rat

a = [rat() , rat() , rat() , rat() , rat() , rat()]

for i in range(len(a)):
    if i <= 1:
        a[i].get()
    else:
        break

a[2].add(a[0] , a[1])
a[3].sub(a[0] , a[1])
a[4].mul(a[0] , a[1])
a[5].div(a[0] , a[1])

print('Sum:', a[2])
print('Difference:', a[3])
print('Product:', a[4])

if a[1].nr != 0:
    print('Division:', a[5])
else:
    print('Division is not permitted')

