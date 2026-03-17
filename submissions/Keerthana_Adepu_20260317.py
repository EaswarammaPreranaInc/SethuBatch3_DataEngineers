#1
'''
Most   tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Hint: Do  not  sort  the  lists

1) b = ['S' , 'A' , 'Z' , 'K']

2) c = []

3) Iteartion  1 :  d  = ['Swathi' , 'Srinivas'] 
                           c =  [['Swathi' , 'Srinivas']]

4) Iteartion  2 :  d  =  ['Anand' , 'Amar']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion  3 :  d  =  ['Zebra']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion  4 :  d  =  ['King']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
'''
'''
Sample Output:

Enter list of strings: ['Swati' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar']

[['Swati' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Press any key to continue...
'''

a = eval(input('Enter list of strings:'))
b = []

for i in range(len(a)):
    if a[i][0] not in b:
        b.append(a[i][0])

c = [[a[j] for j in range(len(a)) if a[j].startswith(b[i])] for i in range(len(b))]

print(c)
