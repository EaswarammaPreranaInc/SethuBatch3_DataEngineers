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
input=eval(input("Enter the list :"))#['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
b=[]#empty list to store first characters of the each string in input ,only store uniqe elements.
c=[]#empty list to store each name that start with a specific character of b in list input 
d=[]#empty list to store all nested list of unique lists that start with a specific character
for x in input:#each element of the list input['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
   if  x[:1]  not in b:# if first character of x not in b
       b.append(x[:1])#append x[:1]to b
print(b)#list b of uniqe characters 
for x in b:#iterating to through the list b
    for y in input:#iterating to through the list input
        if y[:1]==x:#if first character of y==x 
           c. append(y)#append y to c
    d.append((c))#append list c to list d
    c=[]#intializing list c with zero elements
print(d)#print the nested list [['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]


       

