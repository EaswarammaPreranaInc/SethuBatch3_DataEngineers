# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)                #(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))          # <class 'tuple'>
#a[3] = 'Sec'            # Error
#a[3 : 6] = 60 , 70 , 80 # error

a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a))      # (1 , 2 , 3) address of a
a += b
print(a , id(a))      # (1 , 2 , 3,4 , 5 , 6) new address of a

#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) 
a = a + b
print(a , id(a))

a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)      #(10 , [70 , 30 , 40] , 50 , 60)
#a[1] = [80 , 90 , 100] # error


a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)         # (25,10.8,'Hyd',True)
print(type(x))   # <class 'tuple'>


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)         #25
print(b)         # 10.8
print(c)         # hyd
print(d)         #True
#p , q , r =  x  # error
#a , b , c , d  , e =x  # error

tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl
print(a)    # 25
print(b)    # 10.8
print(c)    #['Hyd',True] 
print(type(c)) # <class 'tuple'>

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35
print(a)
print(id(a))
a=a[:2]+(35,)+a[3:]
print(a)
print(id(a))


a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)  # error
#del  a[2]       # error
#a . pop(2)      #error
print(a)
print(id(a))
a=a[:2]+a[3:]
print(a)
print(id(a))

a= ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[1][2])
print(a[2][1])
print(a[2][3])


a = set()
a . add(True)
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a) #{True,25,10.8,1,'Hyd'}
#a . add([10,20,30]) # errp
'''Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  ---> [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
def common():
    s=eval(input("enter list 1 values"))
    s2=eval(input("enter list 2 values"))
    s=set(s)
    s2=set(s2)
    res=list(s.intersection(s2))
    print(f"common elements between the 2 list : {res}")
#common()

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''

def removeDuplicate():
    s=eval(input("enter list values"))
    s=set(s)
    print(f"res : {list(s)}")
#removeDuplicate()

'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''
def stringdulicates():
    s=input("enter the string values")
    s=set(s)
    s=list(s)
    print(f"without duplicate values : {''.join(s)}")
#stringdulicates()
s = {20 , 10 , 20 , 10}
print(s)  #{10,20}
x , y = s
print(x)  #10
print(y)  #20

#program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) #{100,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) 
print(d)   #{10,20,15,18,50,12}
e = set('Rama  rAo')  
print(e)            #{'m', 'a', 'r', 'o', ' ', 'A', 'R'}
#print(set(25))   # error
print(set())       


tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))
print(s)
#s . update(25) error

a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)  #{10,20,30,40,50,60,70}
print(len(s)) # 7
#s . add(a , b , c) #error

