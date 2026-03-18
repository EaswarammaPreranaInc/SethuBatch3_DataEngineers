'''
Most  tricky  program
Input: List of strings
       Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar']
Output: Nested list
        i.e. [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Hint: Do not sort the lists

1) b = ['S' , 'A' , 'Z' , 'K']

2) c = []

3) Iteartion 1 : d = ['Swathi' , 'Srinivas'] 
                 c =  [['Swathi' , 'Srinivas']]

4) Iteartion 2 : d = ['Anand' , 'Amar']
                 c = [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion 3 : d = ['Zebra']
                 c = [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion 4 : d = ['King']
                 c = [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
'''

strings = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']

unq = []
for word in strings:
    fc = word[0]
    if fc not in unq:
        unq.append(fc)

flist = []

for char in unq:

    group = []
    
    for word in strings:
        if word.startswith(char):
            group.append(word)

    flist.append(group)

print(flist)