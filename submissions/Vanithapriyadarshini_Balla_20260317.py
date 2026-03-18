'''Most   tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Hint: Do  not  sort  the  lists

l=eval(input("Enter list of strings : "))
b=[]
c=[]
for x in l:
    if x[0] not in b:
        b.append(x[0])
for i in b:
    d=[]
    for x in l:
        if x.startswith(i):
           d.append(x)
    c.append(d)
        
print(c)'''


l=eval(input("Enter list of strings : "))
b=[]
[b.append(x[0]) for x in l if x[0] not in b]
c=[[x for x in l if x.startswith(i)] for i in b]
print(c)
