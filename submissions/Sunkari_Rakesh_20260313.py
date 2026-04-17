def modes():
    l=eval(input("enter the list values"))
    mode=None
    ctr=0
    for i in set(l):
        c=l.count(i)
        if c>ctr:
            ctr=l.count(i)
            mode=i
    print(f"mode : {mode}")
#modes()

a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[0][2])
print(a[1][3])
print(a[2][1])

def matrix():
    l=eval(input("enter list of list or matrix elements"))
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],end=' ')
        print()
    
#matrix()
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)    #[10 , 20 , 30]   [40 , 50 , 60]  [70 , 80 , 90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')  # 10...20...30
                                    # 40...50...60
                                    # 70...80...9


a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)     #[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]
#for  x , y  in  a:                    errror
#	print(x , y ,	sep = '...')          error
a = [[]]
print(a[0])
for i in a:
     print(i)

def square():
     l=[i*i for i in range(1,int(input("Enter the number of you want"))+1)]
     print(l)
#square()

def firstChar():
     l=[i[0].upper() for i in eval((input("Enter the list of strings")))]
     print(l)
#firstChar()

def words():
     l=[[i.upper(),len(i)] for i in eval((input("Enter the list of strings")))]
     print(l)
#words()
def addList():
    l1=eval(input("enter 1st values : "))
    l2=eval(input("enter 2st values : "))
    l3=[l1[i]+l2[i] for i in range(min(len(l1),len(l2)))]
    print(l3)
#addList()
def addZeros():
    l1=eval(input("enter no of lists : "))
    l2=eval(input("enter no of zeros in list: "))
    l3=[]
    for i in range(l1):
         row=[]
         for j in range(l2):
             row.append(0)
         l3.append(row)
    print(l3)
#addZeros()
'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''

def comprehension():
     s1=input("enter 1st the string : ")
     s2=input("enter 2nd  string : ")
     l=[i+j for i in s1 for j in s2]
     print(l)    
#comprehension()
def comprehension2():
     s1=eval(input("enter 1st the string : "))
    
     l=[s1[i][j] for i in range(len(s1)) for j in range(len(s1[i]))]
     print(l)    
#comprehension2()


a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)                           
'''[[10, 20], [10, 20],
 [30, 40, 50], [30, 40, 50], [30, 40, 50],
 [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]'''


 # Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)  #[[],[0],[0,1],[0,1,2],[0,1,2,3]]


#Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
li=[i for i in range(1,21) if i%2==0]
print(li)

li2=[i for i in range(0,21,2)]
print(li2)

li3=[i**2 for i in range(1,21) if (i**2)%2==0]
print(li3)