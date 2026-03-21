'''a=[10,20,30,40]
b=[11,12,13,14]
#a+=b
#print(a,id(a))

a=a+b
print(a,id(a))
'''

'''a=(10,20,30,40)
b=(11,22,33,44)
a+=b
print(a,id(a))

#a=a+b
#print(a,id(a))'''


'''a=(10,[20,30,49],33,45)
#a[1][0]=70
#print(a)


a[1]=[22,33,44]
print(a)'''




'''a=[10,(20,30,40),35,45]
a[0]=70
print(a)'''


'''tpl=[10,20,30]
a,*b,c,d=tpl
print(a)
print(b)
print(c)
print(d)'''


'''x=25,10.8,'hyd',True
a,b,_,d=x
print(a)
print(b)
print(_)
print(d)'''


'''n=int(input("enter a number :"))
a=0
b=1
count=1
while count<n:
    print(a)
    c=a+b
    a=b
    b=c
    count+=1'''

'''
Most   tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Hint: Do  not  sort  the  lists

1) b = ['S' , 'A' , 'Z' , 'K'
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

'''a=input("enter a list of strings :").split(",")
b=[]
c=[]
for i in a:
    if i[0] not in b:
        b.append(i[0])
        c.append([i])
    else:
        index=b.index(i[0])
        c[index].append(i)
print(c)
'''

a=eval(input("enter a list:"))
b=[i[0] for i in a]
b1=[]
for x in b:
    if x not in b1:
        b1.append(x)
print(b1)

c=[]
for i in b1:
    d=[j for j in a if j[0]==i]
    c.append(d)
print(c)

#without using list comprehension
'''c=[]
for i in b1:
    d=[]
    for j in a:
        if j[0]==i:
            d.append(j)
    c.append(d)'''


    

















