##1.Most   tricky  program
##Input :   List  of  strings
##              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
##Output :  Nested  list
##		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
##
##Hint: Do  not  sort  the  lists
##
##1) b = ['S' , 'A' , 'Z' , 'K']
##
##2) c = []
##
##3) Iteartion  1 :  d  = ['Swathi' , 'Srinivas'] 
##                           c =  [['Swathi' , 'Srinivas']]
##
##4) Iteartion  2 :  d  =  ['Anand' , 'Amar']
##                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]
##
##5) Iteartion  3 :  d  =  ['Zebra']
##                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]
##
##6) Iteartion  4 :  d  =  ['King']
##                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]




s = eval(input('Enter List of strings : '))
f = []
for i in s:
    if i[0] not in f:
        f.append(i[0])
new = []
for i in f:
    temp = []
    for j in s:
        if j.startswith(i):
            temp.append(j)
    new.append(temp)
print(new)




















