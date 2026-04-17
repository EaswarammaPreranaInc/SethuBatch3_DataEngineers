'''
Most   tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
'''

a=eval(input('Enter list of strings: '))  #['Swathi','Anand','Srinivas','Zebra','King','Amar']
b=[]
c=[]
for x in a:
    if x[0] not in b:
        b.append(x[0])
for y in b:
    d=[]
    for z in a:
        if z[0]==y:
            d.append(z)            
    c.append(d)
print(c)  #[['Swathi','Srinivas'],['Anand','Amar'],['Zebra'],['King']]